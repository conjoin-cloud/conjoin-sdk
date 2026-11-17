package conjoin_test

import (
	"context"
	"errors"
	"fmt"
	"net/http"
	"strings"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

func TestErrorsNeverCarryTheKey(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusUnauthorized}, behaviour{kind: dropBeforeStore})
	client := server.client(t, conjoin.WithMaxRetries(0))

	authError := readCustomer(context.Background(), client)
	networkError := readCustomer(context.Background(), client)
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
