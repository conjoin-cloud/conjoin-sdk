# Conjoin Go SDK

`github.com/conjoin-cloud/conjoin-sdk/sdks/go` is the official Go SDK for [Conjoin](https://conjoin.delalify.com). It gives you a typed call for every operation in the Conjoin API, with retries, request tracing, regional hosts, and typed errors. The module uses only the Go standard library.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)

## Install

The module needs Go 1.26 or later:

```bash
go get github.com/conjoin-cloud/conjoin-sdk/sdks/go
```

## Quick Start

```go
package main

import (
	"context"
	"fmt"
	"log"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/billing"
)

func main() {
	client, err := conjoin.NewClient(
		conjoin.WithAPIKey("cak_live_..."),
		conjoin.WithBillingEntityID("entity_123"),
	)
	if err != nil {
		log.Fatal(err)
	}

	customers := billing.New(client).Customers

	customer, err := customers.Create(context.Background(), &billing.CreateCustomerRequest{
		Name:  new("Primary billing contact"),
		Email: "billing@example.com",
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(customer.CustomerID)
}
```

## Packages

Each product has a separate package, and each package has a `New(client)` function that returns its services:

- Import `.../sdks/go` as `conjoin` for `NewClient`, the options, `Page`, `Nullable`, and the error types.
- Import `.../sdks/go/auth` for accounts, sessions, OAuth, organizations, passkeys, MFA, and SCIM.
- Import `.../sdks/go/billing` for customers, subscriptions, invoices, products, prices, payment methods, and entitlements.
- Import `.../sdks/go/storage` for containers, objects, signed uploads, signed downloads, and ACLs.
- Import `.../sdks/go/messaging` for email, SMS, contacts, conversations, templates, and OTP.
- Import `.../sdks/go/relay` for broadcast, queues, events, the scheduler, memorystore, and search.
- Import `.../sdks/go/ai` for chat completions, models, providers, and usage.
- Import `.../sdks/go/cloud` for API keys, roles, projects, webhooks, audit records, and plans.
- Import `.../sdks/go/frontend/auth` and `.../sdks/go/frontend/cloud` for the calls that a publishable key can make.

## Configuration

```go
client, err := conjoin.NewClient(
	conjoin.WithAPIKey("cak_eu_live_..."),
	conjoin.WithTimeout(30*time.Second),
	conjoin.WithMaxRetries(3),
	conjoin.WithRetryBackoff(500*time.Millisecond),
	conjoin.WithMaxRetryDelay(60*time.Second),
)
```

Use `WithAPIKey` on a server and `WithPublishableKey` in a client that runs on a customer's device, and pass exactly one of them. The SDK picks the regional host from the key, so a `cak_eu_live_` or `cpk_eu_live_` key calls `https://api.eu.conjoin.cloud`, a `gh` key calls `https://api.gh.conjoin.cloud`, and a key with no region code calls `https://api.conjoin.cloud`. Pass `WithBaseURL` only when you need to reach another host, and pass `WithHTTPClient` to use your own `*http.Client`.

Calls that need a scope read it from the client. Pass `WithBillingEntityID`, `WithMessagingProfileID`, or `WithAuthAppID` when you create the client, or call `client.WithScope(conjoin.Scope{AuthAppID: "app_123"})` to get a scoped copy. The SDK sends them as the `Billing-Entity-ID`, `Messaging-Profile-ID`, and `Auth-App-ID` headers. When a call needs a scope that you didn't set, it returns an error that matches `conjoin.ErrConfiguration` before it sends anything.

### Retries

The SDK retries `GET`, `PUT`, `PATCH`, and `DELETE` calls after a network failure, a timeout, or a `429`, `500`, `502`, `503`, or `504` response. It retries a `POST` only when the API declares an `Idempotency-Key` header for that operation. The SDK then generates a key for each call, or sends the one that you pass with `conjoin.WithIdempotencyKey`, and it keeps the same key on every retry. A `POST` whose operation declares no `Idempotency-Key` header goes out once, because the server can't tell a retry from a second request.

The SDK never retries a `501` or any other `4xx` response. When the server sends `Retry-After`, the SDK waits that long, capped at the `WithMaxRetryDelay` limit. Otherwise it waits a random time between zero and the backoff multiplied by `2` to the power of the attempt number, capped at the same limit. Pass `WithMaxRetries` or `WithTimeout` to one call to change them for that call:

```go
customer, err := customers.Read(ctx, "cus_123", conjoin.WithMaxRetries(0), conjoin.WithTimeout(5*time.Second))
```

Cancel the context to stop a call. A cancelled call stops at once, during a backoff wait too, and returns an error that matches `context.Canceled` and `conjoin.ErrCanceled`. A call that runs past its timeout returns an error that matches `conjoin.ErrTimeout`.

### Request IDs

Every call sends a `Conjoin-Request-Id` header, and every retry of that call sends the same value. Pass `conjoin.WithRequestID` to the client or to one call to reuse an ID from your own logs. Every error from a call exposes the ID as `RequestID`.

## Lists

A list call returns a `*conjoin.Page[T]` with `Response`, `Data`, and `Cursor{Prev, Next}`:

```go
page, err := customers.List(ctx, &billing.ListCustomersQuery{Limit: 20})
if err != nil {
	return err
}
for _, customer := range page.Data {
	fmt.Println(customer.CustomerID)
}

if page.HasNextPage() {
	next, err := page.NextPage(ctx)
	if err != nil {
		return err
	}
	fmt.Println(len(next.Data))
}

for customer, err := range page.All(ctx) {
	if err != nil {
		return err
	}
	fmt.Println(customer.Email)
}
```

`NextPage` returns `conjoin.ErrNoNextPage` on the last page. `All` walks every item on this page and every page after it. When the server returns a cursor that it returned earlier in the same walk, the SDK stops and returns an error that matches `conjoin.ErrInvalidResponse`.

## Optional and nullable fields

An optional field is a pointer, so `nil` leaves it out of the request. An optional field that also accepts `null` is a `conjoin.Nullable[T]`, which leaves the field out when you don't set it:

```go
coupons := billing.New(client).Coupons

_, err := coupons.Update(ctx, "coupon_123", &billing.UpdateCouponRequest{
	ExpirationDate: conjoin.Null[string](),
})
```

Use `conjoin.Value("2027-01-01")` to send a value, and `Get` or `IsNull` to read one.

## Errors

```go
_, err := customers.Read(ctx, "cus_123")

var apiErr *conjoin.APIError
switch {
case errors.Is(err, conjoin.ErrNotFound):
	fmt.Println("the customer does not exist")
case errors.Is(err, conjoin.ErrValidation) && errors.As(err, &apiErr):
	for _, field := range apiErr.FieldErrors {
		fmt.Println(field.Path, field.Message)
	}
case errors.As(err, &apiErr):
	fmt.Println(apiErr.Status, apiErr.Code, apiErr.Param, apiErr.RequestID)
}
```

A response with an error status returns a `*conjoin.APIError` with `Status`, `Code`, `Message`, `Param`, `Details`, `FieldErrors`, `RetryAfter`, and `RequestID`. It matches one of these sentinels:

- `conjoin.ErrValidation` for `400` and `422`.
- `conjoin.ErrAuthentication` for `401`.
- `conjoin.ErrPermissionDenied` for `403`.
- `conjoin.ErrNotFound` for `404`.
- `conjoin.ErrConflict` for `409`.
- `conjoin.ErrRateLimited` for `429`, with the server's `Retry-After` in `RetryAfter`.
- `conjoin.ErrServer` for every `5xx`.

A call that never gets a response returns a `*conjoin.NetworkError`, `*conjoin.TimeoutError`, or `*conjoin.CanceledError`. A response that doesn't match the API documents returns a `*conjoin.ResponseError`, and a setting that the SDK refuses returns a `*conjoin.ConfigurationError`. Error messages never include your key.

## SCIM

The SCIM calls authenticate with a directory bearer token in place of your API key, so pass it to each call:

```go
directory := auth.New(client).SCIMs

groups, err := directory.ScimListGroups(ctx, "project_123", "app_123", conjoin.WithBearerToken(scimToken))
```

## Credentials that a call declares

Each call sends only the credential that its API document declares. A frontend call that signs in nobody sends no `Authorization` header, a call that needs the publishable key returns a `conjoin.ErrConfiguration` error when the client holds an API key, and none of them ever sends your API key. A call for the signed-in user takes the session token as its `sessionToken` argument, and an SSO portal call takes the portal ticket in its headers argument, which the SDK sends only in the `x-portal-ticket` header. These calls refuse `WithBearerToken`.

A call that declares a header of its own, such as the step-up headers on `Accounts.Delete`, takes a headers struct. The SDK checks each value against the documented length and format before it sends anything:

```go
deleted, err := auth.New(client).Accounts.Delete(ctx, "acc_123", nil, auth.DeleteAccountHeaders{
	StepUpSessionID: stepUpSessionID,
	StepUpToken:     conjoin.Credential(stepUpToken),
})
```

The step-up token, the session token, and the portal ticket have the type `conjoin.Credential`, which prints, logs, and encodes as `[redacted]`.

## Development

The generator reads `spec/openapi.json` and `spec/openapi-frontend.json` and writes every `*_gen.go` file:

```bash
go run ./internal/cmd/generate
go vet ./...
gofmt -l .
go test -race ./...
```

## License

MIT
