package conjoin_test

import (
	"context"
	"io"
	"net/http"
	"strings"
	"sync"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type recordingTransport struct {
	mu    sync.Mutex
	hosts []string
}

func (r *recordingTransport) RoundTrip(request *http.Request) (*http.Response, error) {
	r.mu.Lock()
	r.hosts = append(r.hosts, request.URL.Scheme+"://"+request.URL.Host)
	r.mu.Unlock()
	if request.Body != nil {
		_ = request.Body.Close()
	}
	return &http.Response{
		StatusCode: http.StatusOK,
		Header:     http.Header{"Content-Type": []string{"application/json"}},
		Body:       io.NopCloser(strings.NewReader(`{"response":{"type":"SUCCESS","code":200,"message":"Success"},"data":{}}`)),
		Request:    request,
	}, nil
}

func TestTheKeyPrefixPicksTheRegionalAddress(t *testing.T) {
	cases := map[string]string{
		"cak_gh_live_harbourledger":    "https://api.gh.conjoin.cloud",
		"cak_eu_test_harbourledger":    "https://api.eu.conjoin.cloud",
		"cpk_gh_test_harbourledger":    "https://api.gh.conjoin.cloud",
		"cpk_eu_live_harbourledger":    "https://api.eu.conjoin.cloud",
		"cak_live_harbourledger":       "https://api.conjoin.cloud",
		"cak_us_live_harbourledger":    "https://api.conjoin.cloud",
		"cak_gh_staging_harbourledger": "https://api.conjoin.cloud",
		"sk_eu_live_harbourledger":     "https://api.conjoin.cloud",
		"cak_eu":                       "https://api.conjoin.cloud",
	}
	for key, want := range cases {
		transport := &recordingTransport{}
		keyOption := conjoin.WithAPIKey(key)
		if strings.HasPrefix(key, "cpk_") {
			keyOption = conjoin.WithPublishableKey(key)
		}
		client, err := conjoin.NewClient(keyOption, conjoin.WithHTTPClient(&http.Client{Transport: transport}))
		if err != nil {
			t.Fatalf("the key %s gave %v", key, err)
		}
		var out any
		if err := client.Do(context.Background(), conjoin.Operation{Method: http.MethodGet, Path: "cloud/client/settings/"}, &out); err != nil {
			t.Fatalf("the call with %s failed: %v", key, err)
		}
		if client.BaseURL() != want || len(transport.hosts) != 1 || transport.hosts[0] != want {
			t.Fatalf("the key %s sent the call to %v, want %s", key, transport.hosts, want)
		}
	}
}
