package conjoin_test

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"strings"
	"sync"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/auth"
)

const (
	stepUpAPIKey    = "cak_test_harbourledgerstepup"
	stepUpAuthApp   = "app_harbourledger"
	stepUpAccountID = "acc_harbourledger_owner"
	stepUpSessionID = "sus_harbourledger_0198f0f7"
	stepUpToken     = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
	deletedAccount  = `{"response":{"type":"SUCCESS","code":200,"message":"Success"},"data":{"account_id":"acc_harbourledger_owner","deleted":true}}`
)

type receivedRequest struct {
	method   string
	path     string
	rawQuery string
	header   http.Header
}

type headerReceiver struct {
	server   *httptest.Server
	mu       sync.Mutex
	received []receivedRequest
}

func startHeaderReceiver(t *testing.T, body string) *headerReceiver {
	t.Helper()
	receiver := &headerReceiver{}
	receiver.server = httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		receiver.mu.Lock()
		receiver.received = append(receiver.received, receivedRequest{method: r.Method, path: r.URL.Path, rawQuery: r.URL.RawQuery, header: r.Header.Clone()})
		receiver.mu.Unlock()
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(body))
	}))
	t.Cleanup(receiver.server.Close)
	return receiver
}

func (r *headerReceiver) take() []receivedRequest {
	r.mu.Lock()
	defer r.mu.Unlock()
	received := r.received
	r.received = nil
	return received
}

func stepUpAccounts(t *testing.T, receiver *headerReceiver) *auth.AccountsService {
	t.Helper()
	client, err := conjoin.NewClient(
		conjoin.WithAPIKey(stepUpAPIKey),
		conjoin.WithBaseURL(receiver.server.URL),
		conjoin.WithAuthAppID(stepUpAuthApp),
		conjoin.WithMaxRetries(0),
	)
	if err != nil {
		t.Fatalf("the client did not start: %v", err)
	}
	return auth.New(client).Accounts
}

func TestDeleteAuthAccountSendsBothStepUpHeaders(t *testing.T) {
	receiver := startHeaderReceiver(t, deletedAccount)
	headers := auth.DeleteAccountHeaders{StepUpSessionID: stepUpSessionID, StepUpToken: stepUpToken}

	if _, err := stepUpAccounts(t, receiver).Delete(context.Background(), stepUpAccountID, nil, headers); err != nil {
		t.Fatalf("the delete failed: %v", err)
	}

	received := receiver.take()
	if len(received) != 1 {
		t.Fatalf("the receiver saw %d requests, want 1", len(received))
	}
	request := received[0]
	if request.method != http.MethodDelete || request.path != "/v1/auth/accounts/"+stepUpAccountID {
		t.Fatalf("the receiver saw %s %s", request.method, request.path)
	}
	for name, want := range map[string]string{"Step-Up-Session-Id": stepUpSessionID, "Step-Up-Token": stepUpToken, "Auth-App-Id": stepUpAuthApp} {
		if got := request.header.Get(name); got != want {
			t.Fatalf("the %s header arrived as %q, want %q", name, got, want)
		}
	}
}

func TestDeleteAuthAccountKeepsTheTypedStepUpValuesOverFreeFormHeaders(t *testing.T) {
	receiver := startHeaderReceiver(t, deletedAccount)
	headers := auth.DeleteAccountHeaders{StepUpSessionID: stepUpSessionID, StepUpToken: stepUpToken}

	_, err := stepUpAccounts(t, receiver).Delete(context.Background(), stepUpAccountID, nil, headers,
		conjoin.WithHeader("step-up-token", "ffff"), conjoin.WithHeader("STEP-UP-SESSION-ID", "sus_other"))
	if err != nil {
		t.Fatalf("the delete failed: %v", err)
	}

	request := receiver.take()[0]
	if got := request.header.Values("Step-Up-Token"); len(got) != 1 || got[0] != stepUpToken {
		t.Fatalf("the Step-Up-Token header arrived as %q", got)
	}
	if got := request.header.Values("Step-Up-Session-Id"); len(got) != 1 || got[0] != stepUpSessionID {
		t.Fatalf("the Step-Up-Session-Id header arrived as %q", got)
	}
}

func TestDeleteAuthAccountDropsFreeFormStepUpHeadersWhenNoTypedValueIsGiven(t *testing.T) {
	receiver := startHeaderReceiver(t, deletedAccount)

	_, err := stepUpAccounts(t, receiver).Delete(context.Background(), stepUpAccountID, nil, auth.DeleteAccountHeaders{},
		conjoin.WithHeader("Step-Up-Token", "ffff"))
	if err != nil {
		t.Fatalf("the delete failed: %v", err)
	}

	request := receiver.take()[0]
	if request.header.Get("Step-Up-Token") != "" || request.header.Get("Step-Up-Session-Id") != "" {
		t.Fatalf("the receiver saw step-up headers %v", request.header)
	}
}

func TestDeleteAuthAccountRefusesAMalformedStepUpTokenWithoutRepeatingIt(t *testing.T) {
	cases := map[string]conjoin.Credential{
		"an uppercase token":        conjoin.Credential(strings.ToUpper(stepUpToken)),
		"a token of 257 characters": conjoin.Credential(strings.Repeat("a", 257)),
		"a token with a line break": conjoin.Credential(stepUpToken + "\r\nX-Injected: yes"),
	}
	for label, token := range cases {
		t.Run(label, func(t *testing.T) {
			receiver := startHeaderReceiver(t, deletedAccount)
			headers := auth.DeleteAccountHeaders{StepUpSessionID: stepUpSessionID, StepUpToken: token}

			_, err := stepUpAccounts(t, receiver).Delete(context.Background(), stepUpAccountID, nil, headers)

			if !errors.Is(err, conjoin.ErrConfiguration) {
				t.Fatalf("the delete gave %v, want a configuration error", err)
			}
			if !strings.Contains(err.Error(), "StepUpToken") || strings.Contains(err.Error(), string(token)) {
				t.Fatalf("the error %q does not name StepUpToken or repeats the token", err)
			}
			if received := receiver.take(); len(received) != 0 {
				t.Fatalf("the receiver saw %d requests, want 0", len(received))
			}
		})
	}
}

func TestDeleteAuthAccountRefusesASessionIDLongerThanDocumented(t *testing.T) {
	receiver := startHeaderReceiver(t, deletedAccount)
	headers := auth.DeleteAccountHeaders{StepUpSessionID: strings.Repeat("s", 49)}

	_, err := stepUpAccounts(t, receiver).Delete(context.Background(), stepUpAccountID, nil, headers)

	if !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("the delete gave %v, want a configuration error", err)
	}
	if received := receiver.take(); len(received) != 0 {
		t.Fatalf("the receiver saw %d requests, want 0", len(received))
	}
}

func TestStepUpTokenStaysOutOfEveryPrintedForm(t *testing.T) {
	headers := auth.DeleteAccountHeaders{StepUpSessionID: stepUpSessionID, StepUpToken: stepUpToken}
	var printed bytes.Buffer
	for _, verb := range []string{"%v", "%+v", "%#v", "%s", "%q", "%x", "%d"} {
		fmt.Fprintf(&printed, verb+"\n", headers)
		fmt.Fprintf(&printed, verb+"\n", headers.StepUpToken)
	}
	encoded, err := json.Marshal(headers)
	if err != nil {
		t.Fatalf("the headers did not encode: %v", err)
	}
	printed.Write(encoded)
	slog.New(slog.NewJSONHandler(&printed, nil)).Info("step-up", "headers", headers, "token", headers.StepUpToken)
	slog.New(slog.NewTextHandler(&printed, nil)).Info("step-up", "headers", headers, "token", headers.StepUpToken)

	if strings.Contains(printed.String(), stepUpToken) {
		t.Fatalf("a printed form carried the step-up token:\n%s", printed.String())
	}
	if !strings.Contains(printed.String(), stepUpSessionID) {
		t.Fatalf("the printed forms lost the session ID, which is not a credential:\n%s", printed.String())
	}
}
