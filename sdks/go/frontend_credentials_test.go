package conjoin_test

import (
	"context"
	"errors"
	"strings"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
	frontendauth "github.com/conjoin-cloud/conjoin-sdk/sdks/go/frontend/auth"
	frontendcloud "github.com/conjoin-cloud/conjoin-sdk/sdks/go/frontend/cloud"
)

const (
	frontendSecretKey      = "cak_live_harbourledgerserverside"
	frontendPublishableKey = "cpk_live_harbourledgerbrowser"
	frontendSessionToken   = "sess_harbourledger_signedin_owner"
	frontendPortalTicket   = "ptk_harbourledger_portal_ticket"
	frontendSuccess        = `{"response":{"type":"SUCCESS","code":200,"message":"Success"},"data":{}}`
)

func frontendClient(t *testing.T, receiver *headerReceiver, key conjoin.ClientOption) *conjoin.Client {
	t.Helper()
	client, err := conjoin.NewClient(key, conjoin.WithBaseURL(receiver.server.URL), conjoin.WithMaxRetries(0))
	if err != nil {
		t.Fatalf("the client did not start: %v", err)
	}
	return client
}

func everyReceivedValue(received []receivedRequest) string {
	var values strings.Builder
	for _, request := range received {
		values.WriteString(request.path + "?" + request.rawQuery + "\n")
		for name, entries := range request.header {
			values.WriteString(name + ": " + strings.Join(entries, ", ") + "\n")
		}
	}
	return values.String()
}

func TestFrontendCallsFromASecretKeyClientNeverSendTheSecretKey(t *testing.T) {
	receiver := startHeaderReceiver(t, frontendSuccess)
	client := frontendClient(t, receiver, conjoin.WithAPIKey(frontendSecretKey))
	ctx := context.Background()

	if _, err := frontendauth.New(client).Clients.GetJwks(ctx); err != nil {
		t.Fatalf("the public call failed: %v", err)
	}
	if _, err := frontendauth.New(client).Selves.ReadProfile(ctx, frontendSessionToken); err != nil {
		t.Fatalf("the session call failed: %v", err)
	}
	_, err := frontendcloud.New(client).SDKs.ReadSdkSettings(ctx)
	if !errors.Is(err, conjoin.ErrConfiguration) || !strings.Contains(err.Error(), "WithPublishableKey") {
		t.Fatalf("the publishable-key call gave %v, want a configuration error that names WithPublishableKey", err)
	}

	received := receiver.take()
	if len(received) != 2 {
		t.Fatalf("the receiver saw %d requests, want 2", len(received))
	}
	if got := received[0].header.Get("Authorization"); got != "" {
		t.Fatalf("the public call sent the Authorization header %q", got)
	}
	if got := received[1].header.Get("Authorization"); got != "Bearer "+frontendSessionToken {
		t.Fatalf("the session call sent the Authorization header %q", got)
	}
	if strings.Contains(everyReceivedValue(received), frontendSecretKey) {
		t.Fatalf("the receiver saw the secret key:\n%s", everyReceivedValue(received))
	}
}

func TestFrontendCallsSendThePublishableKeyOnlyWhereTheDocumentAsksForIt(t *testing.T) {
	receiver := startHeaderReceiver(t, frontendSuccess)
	client := frontendClient(t, receiver, conjoin.WithPublishableKey(frontendPublishableKey))
	ctx := context.Background()

	if _, err := frontendcloud.New(client).SDKs.ReadSdkSettings(ctx); err != nil {
		t.Fatalf("the publishable-key call failed: %v", err)
	}
	if _, err := frontendauth.New(client).Clients.GetJwks(ctx); err != nil {
		t.Fatalf("the public call failed: %v", err)
	}

	received := receiver.take()
	if len(received) != 2 || received[0].header.Get("Authorization") != "Bearer "+frontendPublishableKey || received[1].header.Get("Authorization") != "" {
		t.Fatalf("the receiver saw %s", everyReceivedValue(received))
	}
}

func TestFrontendSessionCallsRefuseAMissingTokenAndAnOverride(t *testing.T) {
	receiver := startHeaderReceiver(t, frontendSuccess)
	selves := frontendauth.New(frontendClient(t, receiver, conjoin.WithPublishableKey(frontendPublishableKey))).Selves
	ctx := context.Background()

	if _, err := selves.ReadProfile(ctx, ""); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("a session call without a token gave %v, want a configuration error", err)
	}
	if _, err := selves.ReadProfile(ctx, frontendSessionToken, conjoin.WithBearerToken(frontendSecretKey)); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("a session call with a bearer override gave %v, want a configuration error", err)
	}
	if received := receiver.take(); len(received) != 0 {
		t.Fatalf("the receiver saw %d requests, want 0", len(received))
	}
}

func TestPortalTicketTravelsOnlyInItsHeader(t *testing.T) {
	receiver := startHeaderReceiver(t, frontendSuccess)
	portals := frontendauth.New(frontendClient(t, receiver, conjoin.WithPublishableKey(frontendPublishableKey))).SSOPortals

	if _, err := portals.ReadSsoPortalContext(context.Background(), frontendauth.ReadSsoPortalContextHeaders{PortalTicket: frontendPortalTicket}); err != nil {
		t.Fatalf("the portal call failed: %v", err)
	}

	received := receiver.take()
	if len(received) != 1 {
		t.Fatalf("the receiver saw %d requests, want 1", len(received))
	}
	request := received[0]
	if request.header.Get("X-Portal-Ticket") != frontendPortalTicket || request.header.Get("Authorization") != "" {
		t.Fatalf("the portal call sent %s", everyReceivedValue(received))
	}
	if strings.Contains(request.rawQuery, frontendPortalTicket) {
		t.Fatalf("the query string %q carried the portal ticket", request.rawQuery)
	}
}

func TestPortalTicketIsRequiredAndNeverRepeatedInAnError(t *testing.T) {
	receiver := startHeaderReceiver(t, frontendSuccess)
	portals := frontendauth.New(frontendClient(t, receiver, conjoin.WithPublishableKey(frontendPublishableKey))).SSOPortals
	malformed := conjoin.Credential("ptk_harbourledger portal_ticket")

	if _, err := portals.ReadSsoPortalContext(context.Background(), frontendauth.ReadSsoPortalContextHeaders{}); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("a portal call without a ticket gave %v, want a configuration error", err)
	}
	_, err := portals.ReadSsoPortalContext(context.Background(), frontendauth.ReadSsoPortalContextHeaders{PortalTicket: malformed})
	if !errors.Is(err, conjoin.ErrConfiguration) || strings.Contains(err.Error(), string(malformed)) {
		t.Fatalf("a malformed ticket gave %v", err)
	}
	if received := receiver.take(); len(received) != 0 {
		t.Fatalf("the receiver saw %d requests, want 0", len(received))
	}
}
