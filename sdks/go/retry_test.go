package conjoin_test

import (
	"context"
	"errors"
	"net/http"
	"regexp"
	"testing"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

var serverIdempotencyKeyPattern = regexp.MustCompile(`^[A-Za-z0-9\-_:.]{1,64}$`)

type newCustomer struct {
	Email string `json:"email"`
}

func createCustomer(ctx context.Context, client *conjoin.Client, acceptsKey bool) (storedCustomer, error) {
	var out storedCustomer
	err := client.Do(ctx, conjoin.Operation{
		Method:                http.MethodPost,
		Path:                  "billing/customers/",
		Body:                  &newCustomer{Email: "ledger.owner@example.com"},
		BodyRequired:          true,
		AcceptsIdempotencyKey: acceptsKey,
	}, &out)
	return out, err
}

func readCustomer(ctx context.Context, client *conjoin.Client) error {
	op := conjoin.Operation{Method: http.MethodGet, Path: "billing/customers/{customer_id}", PathParams: []string{"cus_1"}}
	var out map[string]string
	return client.Do(ctx, op, &out)
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
	if attempts[0].body != attempts[1].body || attempts[1].body == "" {
		t.Fatalf("the retry sent the body %q after %q", attempts[1].body, attempts[0].body)
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
