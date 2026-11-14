package conjoin_test

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/http/httptest"
	"net/url"
	"sync"
	"testing"
	"time"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

const (
	testAPIKey          = "cak_test_harbourledgertransport"
	customersPath       = "/v1/billing/customers/"
	maxTestBodyBytes    = 1 << 20
	callerRequestID     = "cnj_req_0198f0f7-5d0b-7b4a-8d5a-cf5693f0b2c1"
	requestIDExpression = `^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`
)

type behaviourKind int

const (
	answer behaviourKind = iota
	dropBeforeStore
	dropAfterStore
	slowAnswer
	slowAfterStore
	statusAnswer
)

type behaviour struct {
	kind   behaviourKind
	delay  time.Duration
	status int
	header map[string]string
	body   any
}

type receivedAttempt struct {
	method     string
	path       string
	query      url.Values
	header     http.Header
	body       string
	receivedAt time.Time
}

type storedCustomer struct {
	CustomerID string `json:"customer_id"`
	Email      string `json:"email"`
}

type keyedCustomer struct {
	body     string
	customer storedCustomer
}

type unreliableServer struct {
	server     *httptest.Server
	transport  *http.Transport
	mu         sync.Mutex
	attempts   []receivedAttempt
	behaviours []behaviour
	customers  []storedCustomer
	byKey      map[string]keyedCustomer
	pages      func(cursor string) ([]string, string)
}

func startUnreliableServer(t *testing.T) *unreliableServer {
	t.Helper()
	s := &unreliableServer{byKey: map[string]keyedCustomer{}, transport: &http.Transport{DisableKeepAlives: true}}
	s.server = httptest.NewServer(http.HandlerFunc(s.handle))
	t.Cleanup(func() {
		s.transport.CloseIdleConnections()
		s.server.CloseClientConnections()
		s.server.Close()
	})
	return s
}

func (s *unreliableServer) client(t *testing.T, opts ...conjoin.ClientOption) *conjoin.Client {
	t.Helper()
	base := []conjoin.ClientOption{
		conjoin.WithAPIKey(testAPIKey),
		conjoin.WithBaseURL(s.server.URL),
		conjoin.WithHTTPClient(&http.Client{Transport: s.transport}),
		conjoin.WithTimeout(2 * time.Second),
		conjoin.WithRetryBackoff(time.Millisecond),
		conjoin.WithMaxRetryDelay(50 * time.Millisecond),
	}
	client, err := conjoin.NewClient(append(base, opts...)...)
	if err != nil {
		t.Fatalf("the client did not start: %v", err)
	}
	return client
}

func (s *unreliableServer) queue(next ...behaviour) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.behaviours = append(s.behaviours, next...)
}

func (s *unreliableServer) servePages(source func(cursor string) ([]string, string)) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.pages = source
}

func (s *unreliableServer) recorded() []receivedAttempt {
	s.mu.Lock()
	defer s.mu.Unlock()
	return append([]receivedAttempt(nil), s.attempts...)
}

func (s *unreliableServer) storedCustomers() []storedCustomer {
	s.mu.Lock()
	defer s.mu.Unlock()
	return append([]storedCustomer(nil), s.customers...)
}

func (s *unreliableServer) store(attempt receivedAttempt) (int, *storedCustomer) {
	s.mu.Lock()
	defer s.mu.Unlock()
	key := attempt.header.Get("Idempotency-Key")
	if previous, found := s.byKey[key]; key != "" && found {
		if previous.body != attempt.body {
			return http.StatusUnprocessableEntity, nil
		}
		return http.StatusOK, &previous.customer
	}
	var request struct {
		Email string `json:"email"`
	}
	if err := json.Unmarshal([]byte(attempt.body), &request); err != nil {
		return http.StatusBadRequest, nil
	}
	customer := storedCustomer{CustomerID: fmt.Sprintf("cus_%d", len(s.customers)+1), Email: request.Email}
	s.customers = append(s.customers, customer)
	if key != "" {
		s.byKey[key] = keyedCustomer{body: attempt.body, customer: customer}
	}
	return http.StatusCreated, &customer
}

func successBody(status int, data any) map[string]any {
	return map[string]any{"response": map[string]any{"type": "SUCCESS", "code": status, "message": "Success"}, "data": data}
}

func writeJSON(w http.ResponseWriter, status int, body any, header map[string]string) {
	for name, value := range header {
		w.Header().Set(name, value)
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(body)
}

func dropConnection(w http.ResponseWriter) {
	hijacker, ok := w.(http.Hijacker)
	if !ok {
		panic("the test server cannot drop a connection")
	}
	connection, _, err := hijacker.Hijack()
	if err != nil {
		panic(err)
	}
	_ = connection.Close()
}

func (s *unreliableServer) answer(w http.ResponseWriter, attempt receivedAttempt) {
	if attempt.method == http.MethodPost && attempt.path == customersPath {
		status, customer := s.store(attempt)
		var data any
		if customer != nil {
			data = customer
		}
		writeJSON(w, status, successBody(status, data), nil)
		return
	}
	s.mu.Lock()
	pages := s.pages
	s.mu.Unlock()
	if pages != nil && attempt.method == http.MethodGet {
		data, next := pages(attempt.query.Get("cursor[next]"))
		body := successBody(http.StatusOK, data)
		var nextCursor any
		if next != "" {
			nextCursor = next
		}
		body["cursor"] = map[string]any{"prev": nil, "next": nextCursor}
		writeJSON(w, http.StatusOK, body, nil)
		return
	}
	writeJSON(w, http.StatusOK, successBody(http.StatusOK, map[string]string{"method": attempt.method, "path": attempt.path, "body": attempt.body}), nil)
}

func waitOrHangUp(r *http.Request, delay time.Duration) bool {
	timer := time.NewTimer(delay)
	defer timer.Stop()
	select {
	case <-r.Context().Done():
		return false
	case <-timer.C:
		return true
	}
}

func (s *unreliableServer) handle(w http.ResponseWriter, r *http.Request) {
	raw, err := io.ReadAll(io.LimitReader(r.Body, maxTestBodyBytes))
	if err != nil {
		writeJSON(w, http.StatusBadRequest, map[string]any{"data": nil}, nil)
		return
	}
	attempt := receivedAttempt{method: r.Method, path: r.URL.Path, query: r.URL.Query(), header: r.Header.Clone(), body: string(raw), receivedAt: time.Now()}

	s.mu.Lock()
	s.attempts = append(s.attempts, attempt)
	next := behaviour{kind: answer}
	if len(s.behaviours) > 0 {
		next, s.behaviours = s.behaviours[0], s.behaviours[1:]
	}
	s.mu.Unlock()

	isCreate := attempt.method == http.MethodPost && attempt.path == customersPath
	switch next.kind {
	case dropBeforeStore:
		dropConnection(w)
	case dropAfterStore:
		if isCreate {
			s.store(attempt)
		}
		dropConnection(w)
	case slowAnswer:
		if waitOrHangUp(r, next.delay) {
			s.answer(w, attempt)
		}
	case slowAfterStore:
		if isCreate {
			s.store(attempt)
		}
		if waitOrHangUp(r, next.delay) {
			s.answer(w, attempt)
		}
	case statusAnswer:
		body := next.body
		if body == nil {
			body = map[string]any{"data": nil}
		}
		writeJSON(w, next.status, body, next.header)
	default:
		s.answer(w, attempt)
	}
}
