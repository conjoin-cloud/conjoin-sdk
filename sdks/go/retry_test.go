package conjoin_test

import (
	"context"
	"errors"
	"net/http"
	"regexp"
	"strings"
	"testing"
	"time"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

var serverIdempotencyKeyPattern = regexp.MustCompile(`^[A-Za-z0-9\-_:.]{1,64}$`)

type newCustomer struct {
	Email string `json:"email"`
}

func createCustomer(ctx context.Context, client *conjoin.Client, acceptsKey bool, opts ...conjoin.CallOption) (storedCustomer, error) {
	var out storedCustomer
	err := client.Do(ctx, conjoin.Operation{
		Method:                http.MethodPost,
		Path:                  "billing/customers/",
		Body:                  &newCustomer{Email: "ledger.owner@example.com"},
		BodyRequired:          true,
		AcceptsIdempotencyKey: acceptsKey,
	}, &out, opts...)
	return out, err
}

func readCustomer(ctx context.Context, client *conjoin.Client, method string, opts ...conjoin.CallOption) error {
	op := conjoin.Operation{Method: method, Path: "billing/customers/{customer_id}", PathParams: []string{"cus_1"}}
	if method == http.MethodPut || method == http.MethodPatch {
		op.Body = map[string]string{"email": "ledger.owner@example.com"}
	}
	var out map[string]string
	return client.Do(ctx, op, &out, opts...)
}

func errorBody(status int) map[string]any {
	kind := "CLIENT_ERROR"
	if status >= 500 {
		kind = "SERVER_ERROR"
	}
	return map[string]any{
		"response": map[string]any{"type": kind, "code": status, "message": "The ledger refused it"},
		"data":     nil,
		"error":    map[string]any{"code": "ledger_locked", "param": "email", "details": []any{map[string]any{"message": "is locked", "path": "body.email"}}},
	}
}

func TestCreateThatDropsAfterTheServerStoredItStoresOneCustomer(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: dropAfterStore})

	customer, err := createCustomer(context.Background(), server.client(t), true)
	if err != nil {
		t.Fatalf("the create failed: %v", err)
	}

	stored := server.storedCustomers()
	if len(stored) != 1 || customer != stored[0] {
		t.Fatalf("the server stored %v and the SDK returned %v", stored, customer)
	}
	attempts := server.recorded()
	if len(attempts) != 2 {
		t.Fatalf("the server saw %d attempts, want 2", len(attempts))
	}
	key := attempts[0].header.Get("Idempotency-Key")
	if !serverIdempotencyKeyPattern.MatchString(key) || attempts[1].header.Get("Idempotency-Key") != key {
		t.Fatalf("the attempts carried the keys %q and %q", key, attempts[1].header.Get("Idempotency-Key"))
	}
	if attempts[0].header.Get("Conjoin-Request-Id") != attempts[1].header.Get("Conjoin-Request-Id") {
		t.Fatal("the retry carried a different request ID")
	}
	if attempts[0].body != attempts[1].body || attempts[1].body == "" {
		t.Fatalf("the retry sent the body %q after %q", attempts[1].body, attempts[0].body)
	}
}

func TestCreateThatTimesOutAfterTheServerStoredItStoresOneCustomer(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: slowAfterStore, delay: 2 * time.Second}, behaviour{kind: slowAfterStore, delay: 2 * time.Second})
	client := server.client(t, conjoin.WithTimeout(150*time.Millisecond))

	customer, err := createCustomer(context.Background(), client, true)
	if err != nil {
		t.Fatalf("the create failed: %v", err)
	}
	if stored := server.storedCustomers(); len(stored) != 1 || stored[0] != customer {
		t.Fatalf("the server stored %v after three attempts, and the SDK returned %v", stored, customer)
	}
	if attempts := server.recorded(); len(attempts) != 3 {
		t.Fatalf("the server saw %d attempts, want 3", len(attempts))
	}
}

func TestSeparateCreatesSendDifferentKeys(t *testing.T) {
	server := startUnreliableServer(t)
	client := server.client(t)
	for range 2 {
		if _, err := createCustomer(context.Background(), client, true); err != nil {
			t.Fatalf("the create failed: %v", err)
		}
	}
	attempts := server.recorded()
	if len(server.storedCustomers()) != 2 || attempts[0].header.Get("Idempotency-Key") == attempts[1].header.Get("Idempotency-Key") {
		t.Fatal("two separate creates shared an idempotency key")
	}
}

func TestCallerKeyIsSentOnEveryRetry(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusServiceUnavailable}, behaviour{kind: dropBeforeStore})

	if _, err := createCustomer(context.Background(), server.client(t), true, conjoin.WithIdempotencyKey("ledger-order-7731")); err != nil {
		t.Fatalf("the create failed: %v", err)
	}
	for _, attempt := range server.recorded() {
		if attempt.header.Get("Idempotency-Key") != "ledger-order-7731" {
			t.Fatalf("an attempt carried the key %q", attempt.header.Get("Idempotency-Key"))
		}
	}
	if len(server.recorded()) != 3 || len(server.storedCustomers()) != 1 {
		t.Fatalf("the server saw %d attempts and stored %d customers", len(server.recorded()), len(server.storedCustomers()))
	}
}

func TestInvalidCallerKeysAreRefusedBeforeSending(t *testing.T) {
	server := startUnreliableServer(t)
	client := server.client(t)
	for _, key := range []string{"", "has space", "semi;colon", "ledger\x00order", "ledger-order\n", strings.Repeat("a", 65)} {
		if _, err := createCustomer(context.Background(), client, true, conjoin.WithIdempotencyKey(key)); !errors.Is(err, conjoin.ErrConfiguration) {
			t.Fatalf("the key %q gave %v, want a configuration error", key, err)
		}
	}
	if err := readCustomer(context.Background(), client, http.MethodGet, conjoin.WithIdempotencyKey("ledger-order-7731")); !errors.Is(err, conjoin.ErrConfiguration) {
		t.Fatalf("a GET with a key gave %v, want a configuration error", err)
	}
	if len(server.recorded()) != 0 {
		t.Fatalf("the server saw %d attempts, want none", len(server.recorded()))
	}
}

func TestCreateWithoutDeclaredKeyIsNeverRetried(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: dropAfterStore})

	_, err := createCustomer(context.Background(), server.client(t), false)
	var networkError *conjoin.NetworkError
	if !errors.As(err, &networkError) {
		t.Fatalf("the create gave %v, want a network error", err)
	}
	if len(server.recorded()) != 1 || len(server.storedCustomers()) != 1 {
		t.Fatalf("the server saw %d attempts and stored %d customers", len(server.recorded()), len(server.storedCustomers()))
	}
	if server.recorded()[0].header.Get("Idempotency-Key") != "" {
		t.Fatal("a create without a declared key sent one")
	}
}

func TestCreateWithoutDeclaredKeyIgnoresTheCallerKeyForRetries(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusServiceUnavailable, body: errorBody(503)})

	_, err := createCustomer(context.Background(), server.client(t), false, conjoin.WithIdempotencyKey("ledger-order-7732"))
	if !errors.Is(err, conjoin.ErrServer) || len(server.recorded()) != 1 {
		t.Fatalf("the create gave %v after %d attempts", err, len(server.recorded()))
	}
}

func TestReadsRetryEveryRetryableStatus(t *testing.T) {
	for _, status := range []int{429, 500, 502, 503, 504} {
		server := startUnreliableServer(t)
		server.queue(behaviour{kind: statusAnswer, status: status, body: errorBody(status)})
		if err := readCustomer(context.Background(), server.client(t), http.MethodGet); err != nil {
			t.Fatalf("a read after a %d failed: %v", status, err)
		}
		attempts := server.recorded()
		if len(attempts) != 2 || attempts[0].header.Get("Conjoin-Request-Id") != attempts[1].header.Get("Conjoin-Request-Id") {
			t.Fatalf("a read after a %d made %d attempts", status, len(attempts))
		}
	}
}

func TestWritesOtherThanPostRetryADroppedConnectionWithTheSameBody(t *testing.T) {
	for _, method := range []string{http.MethodPut, http.MethodPatch, http.MethodDelete} {
		server := startUnreliableServer(t)
		server.queue(behaviour{kind: dropBeforeStore})
		if err := readCustomer(context.Background(), server.client(t), method); err != nil {
			t.Fatalf("a %s failed: %v", method, err)
		}
		attempts := server.recorded()
		if len(attempts) != 2 || attempts[0].method != method || attempts[1].body != attempts[0].body {
			t.Fatalf("a %s made the attempts %+v", method, attempts)
		}
	}
}

func TestRetriesStopAtTheConfiguredLimit(t *testing.T) {
	server := startUnreliableServer(t)
	for range 6 {
		server.queue(behaviour{kind: statusAnswer, status: http.StatusServiceUnavailable, body: errorBody(503)})
	}
	if err := readCustomer(context.Background(), server.client(t, conjoin.WithMaxRetries(2)), http.MethodGet); !errors.Is(err, conjoin.ErrServer) {
		t.Fatalf("the read gave %v, want a server error", err)
	}
	if len(server.recorded()) != 3 {
		t.Fatalf("the server saw %d attempts, want 3", len(server.recorded()))
	}
	if err := readCustomer(context.Background(), server.client(t), http.MethodGet, conjoin.WithMaxRetries(0)); !errors.Is(err, conjoin.ErrServer) {
		t.Fatalf("the read gave %v, want a server error", err)
	}
	if len(server.recorded()) != 4 {
		t.Fatalf("a call with no retries made %d attempts", len(server.recorded())-3)
	}
}

func gapBetweenAttempts(t *testing.T, server *unreliableServer) time.Duration {
	t.Helper()
	attempts := server.recorded()
	if len(attempts) != 2 {
		t.Fatalf("the server saw %d attempts, want 2", len(attempts))
	}
	return attempts[1].receivedAt.Sub(attempts[0].receivedAt)
}

func TestRetryAfterSecondsIsFollowed(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusTooManyRequests, header: map[string]string{"Retry-After": "1"}, body: errorBody(429)})
	client := server.client(t, conjoin.WithRetryBackoff(0), conjoin.WithMaxRetryDelay(time.Minute))
	if err := readCustomer(context.Background(), client, http.MethodGet); err != nil {
		t.Fatalf("the read failed: %v", err)
	}
	if gap := gapBetweenAttempts(t, server); gap < 950*time.Millisecond {
		t.Fatalf("the SDK retried after %s, before the Retry-After second", gap)
	}
}

func TestRetryAfterIsCappedByTheClientLimitInBothForms(t *testing.T) {
	for _, value := range []string{"3600", time.Now().Add(30 * time.Second).UTC().Format(http.TimeFormat)} {
		server := startUnreliableServer(t)
		server.queue(behaviour{kind: statusAnswer, status: http.StatusServiceUnavailable, header: map[string]string{"Retry-After": value}, body: errorBody(503)})
		client := server.client(t, conjoin.WithRetryBackoff(0), conjoin.WithMaxRetryDelay(200*time.Millisecond))
		if err := readCustomer(context.Background(), client, http.MethodGet); err != nil {
			t.Fatalf("the read failed: %v", err)
		}
		if gap := gapBetweenAttempts(t, server); gap < 150*time.Millisecond || gap > 2*time.Second {
			t.Fatalf("the Retry-After %q gave a wait of %s, want about 200ms", value, gap)
		}
	}
}

func TestRateLimitErrorReportsRetryAfterOnceRetriesRunOut(t *testing.T) {
	server := startUnreliableServer(t)
	server.queue(behaviour{kind: statusAnswer, status: http.StatusTooManyRequests, header: map[string]string{"Retry-After": "7"}, body: errorBody(429)})
	err := readCustomer(context.Background(), server.client(t, conjoin.WithMaxRetries(0)), http.MethodGet)
	var apiError *conjoin.APIError
	if !errors.As(err, &apiError) || !errors.Is(err, conjoin.ErrRateLimited) || apiError.RetryAfter != 7*time.Second {
		t.Fatalf("the read gave %v, want a rate limit error with a 7s Retry-After", err)
	}
}
