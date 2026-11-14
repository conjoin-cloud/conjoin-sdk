package conjoin_test

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"net/http/httptest"
	"reflect"
	"strings"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

func TestNonRetryableStatusesAreNeverRetriedAndExposeTheErrorBody(t *testing.T) {
	cases := []struct {
		status   int
		sentinel error
	}{
		{400, conjoin.ErrValidation},
		{401, conjoin.ErrAuthentication},
		{403, conjoin.ErrPermissionDenied},
		{404, conjoin.ErrNotFound},
		{405, nil},
		{409, conjoin.ErrConflict},
		{422, conjoin.ErrValidation},
		{501, conjoin.ErrServer},
	}
	sentinels := []error{conjoin.ErrValidation, conjoin.ErrAuthentication, conjoin.ErrPermissionDenied, conjoin.ErrNotFound, conjoin.ErrConflict, conjoin.ErrRateLimited, conjoin.ErrServer}
	for _, tc := range cases {
		server := startUnreliableServer(t)
		server.queue(behaviour{kind: statusAnswer, status: tc.status, body: errorBody(tc.status)})

		err := readCustomer(context.Background(), server.client(t), http.MethodGet)
		var apiError *conjoin.APIError
		if !errors.As(err, &apiError) {
			t.Fatalf("a %d gave %v, want an API error", tc.status, err)
		}
		for _, sentinel := range sentinels {
			if errors.Is(err, sentinel) != (sentinel == tc.sentinel) {
				t.Fatalf("a %d matched %v wrongly", tc.status, sentinel)
			}
		}
		wantDetails := `[{"message":"is locked","path":"body.email"}]`
		requestID := server.recorded()[0].header.Get("Conjoin-Request-Id")
		if apiError.Status != tc.status || apiError.Code != "ledger_locked" || apiError.Param != "email" || apiError.Message != "The ledger refused it" || compactJSON(t, apiError.Details) != wantDetails || apiError.RequestID != requestID {
			t.Fatalf("a %d gave the error %+v", tc.status, apiError)
		}
		wantFields := []conjoin.FieldError{{Message: "is locked", Path: "body.email"}}
		if isValidation := tc.status == 400 || tc.status == 422; isValidation != reflect.DeepEqual(apiError.FieldErrors, wantFields) {
			t.Fatalf("a %d gave the field errors %v", tc.status, apiError.FieldErrors)
		}
		if len(server.recorded()) != 1 {
			t.Fatalf("a %d was sent %d times", tc.status, len(server.recorded()))
		}
	}
}

func compactJSON(t *testing.T, raw json.RawMessage) string {
	t.Helper()
	var value any
	if err := json.Unmarshal(raw, &value); err != nil {
		t.Fatalf("the details %q are not JSON: %v", raw, err)
	}
	compact, err := json.Marshal(value)
	if err != nil {
		t.Fatalf("the details could not be encoded: %v", err)
	}
	return string(compact)
}

func TestErrorWithoutABodyFallsBackToTheStatus(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusConflict, body: "not json"})
	err := readCustomer(context.Background(), server.client(t), http.MethodGet)
	var apiError *conjoin.APIError
	if !errors.As(err, &apiError) || apiError.Code != "conflict" || apiError.Param != "" || apiError.Details != nil || apiError.Message != "Conflict" {
		t.Fatalf("a bare 409 gave %v", err)
	}
}

func TestOversizedErrorBodyIsReadOnlyUpToTheBound(t *testing.T) {
	huge := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusBadRequest)
		chunk := []byte(strings.Repeat("x", 64<<10))
		for range 256 {
			if _, err := w.Write(chunk); err != nil {
				return
			}
		}
	}))
	t.Cleanup(huge.Close)
	client, err := conjoin.NewClient(conjoin.WithAPIKey(testAPIKey), conjoin.WithBaseURL(huge.URL))
	if err != nil {
		t.Fatalf("the client did not start: %v", err)
	}
	err = readCustomer(context.Background(), client, http.MethodGet)
	var apiError *conjoin.APIError
	if !errors.As(err, &apiError) || apiError.Status != http.StatusBadRequest || len(apiError.Message) > 1024 {
		t.Fatalf("a 16 MiB error body gave %v", err)
	}
}

func TestSuccessBodyThatIsNotJSONIsAResponseError(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusOK, body: "{"})
	err := readCustomer(context.Background(), server.client(t), http.MethodGet)
	var responseError *conjoin.ResponseError
	if !errors.As(err, &responseError) || !errors.Is(err, conjoin.ErrInvalidResponse) || responseError.RequestID == "" {
		t.Fatalf("a broken success body gave %v", err)
	}
}

func TestErrorsNeverCarryTheKey(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusUnauthorized, body: errorBody(401)}, behaviour{kind: dropBeforeStore})
	client := server.client(t, conjoin.WithMaxRetries(0))

	authError := readCustomer(context.Background(), client, http.MethodGet)
	networkError := readCustomer(context.Background(), client, http.MethodGet)
	for _, err := range []error{authError, networkError} {
		if err == nil {
			t.Fatal("a failing call returned no error")
		}
		for _, text := range []string{err.Error(), fmt.Sprintf("%+v", err), fmt.Sprintf("%#v", client), fmt.Sprint(*client)} {
			if strings.Contains(text, testAPIKey) {
				t.Fatalf("the text %q carries the API key", text)
			}
		}
	}
	if got := server.recorded()[0].header.Get("Authorization"); got != "Bearer "+testAPIKey {
		t.Fatalf("the server saw the authorization %q", got)
	}
}

func TestScopedCallNeedsItsScopeBeforeSending(t *testing.T) {
	server := startUnreliableServer(t)
	client := server.client(t)
	op := conjoin.Operation{Method: http.MethodGet, Path: "billing/customers/", Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity}}

	var out any
	if err := client.Do(context.Background(), op, &out); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("an unscoped call gave %v, want a configuration error", err)
	}
	if len(server.recorded()) != 0 {
		t.Fatal("an unscoped call reached the server")
	}

	scoped, err := client.WithScope(conjoin.Scope{BillingEntityID: "ent_ledger"})
	if err != nil {
		t.Fatalf("the scoped client did not start: %v", err)
	}
	if err := scoped.Do(context.Background(), op, &out); err != nil {
		t.Fatalf("the scoped call failed: %v", err)
	}
	if err := client.Do(context.Background(), op, &out); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("the scoped copy changed the first client: %v", err)
	}
	attempts := server.recorded()
	if len(attempts) != 1 || attempts[0].header.Get("Billing-Entity-ID") != "ent_ledger" || attempts[0].header.Get("Messaging-Profile-ID") != "" {
		t.Fatalf("the scoped call sent the headers %v", attempts)
	}
	if _, err := client.WithScope(conjoin.Scope{AuthAppID: "app ledger"}); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("a scope with a space gave %v", err)
	}
}

func TestManagedHeadersCannotBeOverriddenPerCall(t *testing.T) {
	server := startUnreliableServer(t)
	client := server.client(t, conjoin.WithBillingEntityID("ent_ledger"))
	op := conjoin.Operation{Method: http.MethodGet, Path: "billing/customers/", Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity}}
	var out any
	err := client.Do(context.Background(), op, &out,
		conjoin.WithHeader("Authorization", "Bearer cak_live_someone_else"),
		conjoin.WithHeader("Billing-Entity-ID", "ent_other"),
		conjoin.WithHeader("X-Ledger-Trace", "trace-7"))
	if err != nil {
		t.Fatalf("the call failed: %v", err)
	}
	header := server.recorded()[0].header
	if header.Get("Authorization") != "Bearer "+testAPIKey || header.Get("Billing-Entity-ID") != "ent_ledger" || header.Get("X-Ledger-Trace") != "trace-7" {
		t.Fatalf("the server saw the headers %v", header)
	}
	if err := client.Do(context.Background(), op, &out, conjoin.WithHeader("X-Ledger", "a\r\nInjected: yes")); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("a header with a line break gave %v", err)
	}
}

func TestPathParametersAreEscapedAndDotSegmentsRefused(t *testing.T) {
	server := startUnreliableServer(t)
	client := server.client(t)
	op := conjoin.Operation{Method: http.MethodGet, Path: "billing/customers/{customer_id}", PathParams: []string{"ledger/../7?#%"}}
	var out map[string]string
	if err := client.Do(context.Background(), op, &out); err != nil {
		t.Fatalf("the call failed: %v", err)
	}
	if got := server.recorded()[0].path; got != "/v1/billing/customers/ledger/../7?#%" {
		t.Fatalf("the server decoded the path %q", got)
	}
	if raw := out["path"]; raw != "/v1/billing/customers/ledger/../7?#%" {
		t.Fatalf("the echo returned %q", raw)
	}
	for _, value := range []string{"", ".", ".."} {
		op.PathParams = []string{value}
		if err := client.Do(context.Background(), op, &out); !errors.Is(err, conjoin.ErrConfiguration) {
			t.Fatalf("the path parameter %q gave %v", value, err)
		}
	}
	if len(server.recorded()) != 1 {
		t.Fatalf("the server saw %d attempts, want 1", len(server.recorded()))
	}
}
