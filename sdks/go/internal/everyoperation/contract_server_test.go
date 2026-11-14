package everyoperation

import (
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"net/url"
	"sync"
	"testing"
)

const maxContractBodyBytes = 4 << 20

type recordedRequest struct {
	operation  *documentOperation
	pathParams map[string]string
	header     http.Header
	query      url.Values
	body       []byte
}

type contractServer struct {
	server     *httptest.Server
	transport  *http.Transport
	operations []*documentOperation
	mu         sync.Mutex
	requests   []recordedRequest
	unmatched  []string
}

func startContractServer(t *testing.T, doc *openAPIDocument) *contractServer {
	t.Helper()
	s := &contractServer{operations: doc.operations, transport: &http.Transport{}}
	s.server = httptest.NewServer(http.HandlerFunc(s.handle))
	t.Cleanup(func() {
		s.transport.CloseIdleConnections()
		s.server.Close()
	})
	return s
}

func (s *contractServer) match(method, escapedPath string) (*documentOperation, map[string]string) {
	var best *documentOperation
	var bestParams map[string]string
	for _, candidate := range s.operations {
		if candidate.method != method {
			continue
		}
		groups := candidate.route.FindStringSubmatch(escapedPath)
		if groups == nil || (best != nil && len(candidate.paramNames) >= len(best.paramNames)) {
			continue
		}
		params := map[string]string{}
		valid := true
		for index, name := range candidate.paramNames {
			value, err := url.PathUnescape(groups[index+1])
			valid = valid && err == nil
			params[name] = value
		}
		if valid {
			best, bestParams = candidate, params
		}
	}
	return best, bestParams
}

func (s *contractServer) handle(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(io.LimitReader(r.Body, maxContractBodyBytes))
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	operation, params := s.match(r.Method, r.URL.EscapedPath())
	s.mu.Lock()
	if operation == nil {
		s.unmatched = append(s.unmatched, r.Method+" "+r.URL.EscapedPath())
		s.mu.Unlock()
		w.WriteHeader(http.StatusNotFound)
		return
	}
	s.requests = append(s.requests, recordedRequest{operation: operation, pathParams: params, header: r.Header.Clone(), query: r.URL.Query(), body: body})
	s.mu.Unlock()

	if operation.successBody == nil {
		w.WriteHeader(operation.successCode)
		return
	}
	encoded, err := json.Marshal(operation.successBody)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(operation.successCode)
	_, _ = w.Write(encoded)
}

func (s *contractServer) take() ([]recordedRequest, []string) {
	s.mu.Lock()
	defer s.mu.Unlock()
	requests, unmatched := s.requests, s.unmatched
	s.requests, s.unmatched = nil, nil
	return requests, unmatched
}
