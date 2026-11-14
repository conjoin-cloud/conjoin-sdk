package conjoin_test

import (
	"context"
	"errors"
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

func TestTheCallerBaseURLOverridesTheRegion(t *testing.T) {
	transport := &recordingTransport{}
	client, err := conjoin.NewClient(conjoin.WithAPIKey("cak_eu_live_harbourledger"), conjoin.WithBaseURL("https://ledger.example.com/"), conjoin.WithHTTPClient(&http.Client{Transport: transport}))
	if err != nil {
		t.Fatalf("the client did not start: %v", err)
	}
	var out any
	if err := client.Do(context.Background(), conjoin.Operation{Method: http.MethodGet, Path: "cloud/client/settings/"}, &out); err != nil {
		t.Fatalf("the call failed: %v", err)
	}
	if transport.hosts[0] != "https://ledger.example.com" {
		t.Fatalf("the call went to %v", transport.hosts)
	}
}

func TestTheClientNeedsExactlyOneValidKeyAndAValidAddress(t *testing.T) {
	invalid := [][]conjoin.ClientOption{
		{},
		{conjoin.WithAPIKey("cak_live_one"), conjoin.WithPublishableKey("cpk_live_two")},
		{conjoin.WithAPIKey("cak live with space")},
		{conjoin.WithAPIKey("cak_live_one"), conjoin.WithBaseURL("ftp://ledger.example.com")},
		{conjoin.WithAPIKey("cak_live_one"), conjoin.WithBaseURL("https://user:secret@ledger.example.com")},
		{conjoin.WithAPIKey("cak_live_one"), conjoin.WithBaseURL("/relative")},
		{conjoin.WithAPIKey("cak_live_one"), conjoin.WithTimeout(0)},
		{conjoin.WithAPIKey("cak_live_one"), conjoin.WithMaxRetries(-1)},
		{conjoin.WithAPIKey("cak_live_one"), conjoin.WithHTTPClient(nil)},
		{conjoin.WithAPIKey("cak_live_one"), nil},
	}
	for index, opts := range invalid {
		if client, err := conjoin.NewClient(opts...); client != nil || !errors.Is(err, conjoin.ErrConfiguration) {
			t.Fatalf("the settings at %d gave %v and %v, want a configuration error", index, client, err)
		}
	}
}

func TestBearerTokenCallsNeedATokenAndSendIt(t *testing.T) {
	server := startUnreliableServer(t)
	client := server.client(t)
	op := conjoin.Operation{Method: http.MethodGet, Path: "auth/scim/v2/{project_id}/{app_id}/Users", PathParams: []string{"prj_ledger", "app_ledger"}, Auth: conjoin.AuthBearerToken, Response: conjoin.ResponseBody}
	var out any
	if err := client.Do(context.Background(), op, &out); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("a bearer call without a token gave %v", err)
	}
	if err := client.Do(context.Background(), op, &out, conjoin.WithBearerToken("scim_ledger_directory")); err != nil {
		t.Fatalf("the bearer call failed: %v", err)
	}
	none := conjoin.Operation{Method: http.MethodGet, Path: "auth/scim/v2/Schemas", Auth: conjoin.AuthNone, Response: conjoin.ResponseBody}
	if err := client.Do(context.Background(), none, &out); err != nil {
		t.Fatalf("the public call failed: %v", err)
	}
	attempts := server.recorded()
	if len(attempts) != 2 || attempts[0].header.Get("Authorization") != "Bearer scim_ledger_directory" || attempts[1].header.Get("Authorization") != "" {
		t.Fatalf("the server saw %d attempts with the authorization %q and %q", len(attempts), attempts[0].header.Get("Authorization"), attempts[1].header.Get("Authorization"))
	}
}
