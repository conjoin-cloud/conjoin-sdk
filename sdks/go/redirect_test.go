package conjoin_test

import (
	"context"
	"errors"
	"net/http"
	"net/http/httptest"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/auth"
)

func startRedirectingAPI(t *testing.T, target string) *headerReceiver {
	t.Helper()
	receiver := &headerReceiver{}
	receiver.server = httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		receiver.mu.Lock()
		receiver.received = append(receiver.received, receivedRequest{method: r.Method, path: r.URL.Path, rawQuery: r.URL.RawQuery, header: r.Header.Clone()})
		receiver.mu.Unlock()
		w.Header().Set("Location", target+r.URL.RequestURI())
		w.WriteHeader(http.StatusTemporaryRedirect)
	}))
	t.Cleanup(receiver.server.Close)
	return receiver
}

func TestARedirectNeverCarriesTheStepUpTokenToAnotherHost(t *testing.T) {
	cases := []struct {
		name   string
		client *http.Client
	}{
		{name: "the client the SDK builds"},
		{name: "a caller client with the default policy", client: &http.Client{}},
		{name: "a caller client that follows every redirect", client: &http.Client{CheckRedirect: func(*http.Request, []*http.Request) error { return nil }}},
	}
	for _, testCase := range cases {
		t.Run(testCase.name, func(t *testing.T) {
			otherHost := startHeaderReceiver(t, deletedAccount)
			api := startRedirectingAPI(t, otherHost.server.URL)
			options := []conjoin.ClientOption{
				conjoin.WithAPIKey(stepUpAPIKey),
				conjoin.WithBaseURL(api.server.URL),
				conjoin.WithAuthAppID(stepUpAuthApp),
				conjoin.WithMaxRetries(0),
			}
			if testCase.client != nil {
				options = append(options, conjoin.WithHTTPClient(testCase.client))
			}
			client, err := conjoin.NewClient(options...)
			if err != nil {
				t.Fatalf("the client did not start: %v", err)
			}
			headers := auth.DeleteAccountHeaders{StepUpSessionID: stepUpSessionID, StepUpToken: stepUpToken}

			_, err = auth.New(client).Accounts.Delete(context.Background(), stepUpAccountID, nil, headers)

			var apiError *conjoin.APIError
			if !errors.As(err, &apiError) || apiError.Status != http.StatusTemporaryRedirect {
				t.Fatalf("the delete returned %v, want the 307 as an API error", err)
			}
			if received := api.take(); len(received) != 1 || received[0].header.Get("Step-Up-Token") != stepUpToken {
				t.Fatalf("the API host saw %d requests, want 1 carrying the step-up token", len(received))
			}
			if received := otherHost.take(); len(received) != 0 {
				t.Fatalf("the other host saw %d requests", len(received))
			}
		})
	}
}

func TestTheSDKLeavesTheRedirectPolicyOfTheCallersClientAlone(t *testing.T) {
	supplied := &http.Client{}

	if _, err := conjoin.NewClient(conjoin.WithAPIKey(stepUpAPIKey), conjoin.WithHTTPClient(supplied)); err != nil {
		t.Fatalf("the client did not start: %v", err)
	}

	if supplied.CheckRedirect != nil {
		t.Fatal("the SDK changed the redirect policy of the caller's client")
	}
}
