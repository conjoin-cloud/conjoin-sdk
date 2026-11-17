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
	path     string
	rawQuery string
	header   http.Header
}

type headerReceiver struct {
	server   *httptest.Server
	mu       sync.Mutex
	received []receivedRequest
}

func (r *headerReceiver) record(request *http.Request) {
	r.mu.Lock()
	defer r.mu.Unlock()
	r.received = append(r.received, receivedRequest{path: request.URL.Path, rawQuery: request.URL.RawQuery, header: request.Header.Clone()})
}

func startHeaderReceiver(t *testing.T, body string) *headerReceiver {
	t.Helper()
	receiver := &headerReceiver{}
	receiver.server = httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		receiver.record(r)
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
