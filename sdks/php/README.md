# conjoin-cloud/conjoin-sdk

`conjoin-cloud/conjoin-sdk` is the official PHP SDK for [Conjoin](https://conjoin.delalify.com). It gives you a typed method for every operation in the Conjoin API, along with safe retries, request tracing, cancellation, and typed exceptions.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)

## Install

```bash
composer require conjoin-cloud/conjoin-sdk
```

The SDK needs PHP 8.2 or later with the `curl` and `json` extensions. It sends requests through Guzzle by default.

## Quick start

```php
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\Generated\Api\BillingCustomers;

$conjoin = new ConjoinClient(
    apiKey: 'cak_live_...',
    billingEntityId: 'entity_123',
);

$customers = new BillingCustomers($conjoin);

$customer = $customers->create([
    'name' => 'Billing owner',
    'email' => 'billing@example.com',
]);

echo $customer['customer_id'];
```

Every resource in `spec/openapi.json` has a class in `ConjoinCloud\Generated\Api`, and every resource in `spec/openapi-frontend.json` has a class in `ConjoinCloud\Generated\Frontend`. A call returns the `data` of the response with the PHP type that the document declares, which is an array for most calls, and a list call returns a `ListPage`.

## Configuration

```php
$conjoin = new ConjoinClient(
    apiKey: 'cak_eu_live_...',
    timeoutSeconds: 30.0,
    maxRetries: 3,
    backoffSeconds: 0.5,
    maxRetryDelaySeconds: 60.0,
);
```

Pass exactly one of `apiKey` or `publishableKey`. The SDK picks the regional host from the key, so a `cak_eu_live_` or `cpk_eu_live_` key calls `https://api.eu.conjoin.cloud`, a `gh` key calls `https://api.gh.conjoin.cloud`, and a key with no region code calls `https://api.conjoin.cloud`. Set `baseUrl` only when you need to reach another host.

Calls that need a scope read it from the client. Set `billingEntityId`, `messagingProfileId`, or `authAppId` when you create the client, or call `$conjoin->withScope(billingEntityId: 'entity_123')` to get a scoped copy. The SDK sends them as the `Billing-Entity-ID`, `Messaging-Profile-ID`, and `Auth-App-ID` headers, and a call that needs a scope that you didn't set throws a `ConfigurationException` before it sends anything.

The SDK reads at most 64 KiB of an error body and at most `maxResponseBytes` of a success body, which defaults to 16 MiB. A larger success body throws a `ResponseException` with the code `response_too_large`.

To send requests through another HTTP client, pass any PSR-18 client as `httpClient`. The SDK then applies its retries, request IDs, and body limit, while the timeout and any cancellation during a request depend on that client.

### Retries

The SDK retries `GET`, `PUT`, `PATCH`, and `DELETE` calls after a network failure, a timeout, or a `429`, `500`, `502`, `503`, or `504` response. It retries a `POST` only when the API declares an `Idempotency-Key` header for that operation. The SDK then generates a key for each call, or sends the one that you pass, and it keeps the same key on every retry:

```php
use ConjoinCloud\CallOptions;

$customers->create(
    ['email' => 'billing@example.com'],
    new CallOptions(idempotencyKey: 'signup-7f3a9c'),
);
```

A key has 1 to 64 characters from `A-Z`, `a-z`, `0-9`, `-`, `_`, `:`, and `.`. A `POST` whose operation declares no `Idempotency-Key` header goes out once, because the server can't tell a retry from a second request.

The SDK never retries a `501` or any other `4xx` response. When the server sends `Retry-After`, in seconds or as an HTTP date, the SDK waits that long, capped at `maxRetryDelaySeconds`. Otherwise it waits a random time between zero and `backoffSeconds * 2 ** attempt`, capped at the same limit. Pass `maxRetries` or `timeoutSeconds` in `CallOptions` to change them for one call.

### Cancellation

PHP has no standard abort signal, so a call takes a `Cancellation` in its options. The SDK checks it before every attempt, while a request waits on the network, and during every backoff wait:

```php
use ConjoinCloud\Cancellation\CancellationToken;
use ConjoinCloud\CallOptions;
use ConjoinCloud\Exception\CancelledException;

$token = new CancellationToken();

pcntl_async_signals(true);
pcntl_signal(SIGTERM, static fn () => $token->cancel());

try {
    $customers->read('cus_123', new CallOptions(cancellation: $token));
} catch (CancelledException $error) {
    echo 'Stopped before the call finished';
}
```

Implement the `Cancellation` interface to stop a call on your own condition, such as a deadline for a whole job. A cancelled call throws a `CancelledException`, while a call that runs past its timeout throws a `TimeoutException`.

### Request IDs

Every call sends a `Conjoin-Request-Id` header, and every retry of that call sends the same value. Pass `requestId` to the client or in `CallOptions` to reuse an ID from your own logs, or call `$conjoin->withRequestTrace($requestId)` to get a copy that sends one ID on every call. Every exception exposes the ID through `getRequestId()`.

## Lists

```php
$page = $customers->list(['limit' => 20]);

foreach ($page->data as $customer) {
    echo $customer['customer_id'];
}

$nextPage = $page->nextPage();

foreach ($page as $customer) {
    echo $customer['email'];
}
```

A list call returns a page with `response`, `data`, and `cursor`. `$page->nextPage()` fetches the page after it, or returns `null` on the last page, and `foreach` over the page walks every item across every page. The SDK throws a `ResponseException` when the server returns a cursor that it returned before, so a broken cursor can't loop forever.

## Errors

Every SDK exception extends `ConjoinException`:

```php
use ConjoinCloud\Exception\ConflictException;
use ConjoinCloud\Exception\ConjoinException;
use ConjoinCloud\Exception\NotFoundException;
use ConjoinCloud\Exception\RateLimitException;
use ConjoinCloud\Exception\ValidationException;

try {
    $customers->update('cus_123', ['name' => 'Billing owner']);
} catch (ValidationException $error) {
    foreach ($error->getFieldErrors() as $field) {
        echo "{$field->path}: {$field->message}\n";
    }
} catch (NotFoundException $error) {
    echo 'The customer does not exist.';
} catch (ConflictException $error) {
    var_dump($error->getErrorCode(), $error->getDetails());
} catch (RateLimitException $error) {
    echo "Retry after {$error->getRetryAfterSeconds()} seconds.";
} catch (ConjoinException $error) {
    echo $error->getErrorCode(), $error->getMessage(), $error->getRequestId();
}
```

Every exception exposes `getStatus()`, `getErrorCode()`, `getParam()`, `getDetails()`, and `getRequestId()`.

- `ValidationException` covers `400` and `422` responses, with field errors from `getFieldErrors()`.
- `AuthenticationException` covers `401` responses.
- `PermissionDeniedException` covers `403` responses.
- `NotFoundException` covers `404` responses.
- `ConflictException` covers `409` responses.
- `RateLimitException` covers `429` responses and exposes the `Retry-After` delay through `getRetryAfterSeconds()`.
- `ServerException` covers `5xx` responses.
- `ApiException` is the base class of every API exception, and it covers any other status.
- `ResponseException` covers a response body that the SDK can't read or that exceeds the body limit.
- `NetworkException` covers DNS failures, refused connections, and dropped connections.
- `TimeoutException` covers calls that run past the timeout.
- `CancelledException` covers calls that the caller cancelled.
- `ConfigurationException` covers client settings and call options that the SDK rejects before it sends anything.

Exceptions, `var_dump`, and `print_r` leave out the API key, the publishable key, and the SCIM token.

## Development

The generator in `codegen/` reads `spec/openapi.json` and `spec/openapi-frontend.json` and writes `src/Generated`. Run the checks from `sdks/php`:

```bash
composer install
php codegen/generate.php
vendor/bin/phpcs
vendor/bin/phpstan analyse --memory-limit=2G
vendor/bin/phpunit
```

## Support

- Read product documentation at <https://conjoin.delalify.com>.
- Report SDK issues at <https://github.com/conjoin-cloud/conjoin-sdk/issues>.

## License

This package uses the [MIT](../../LICENSE) license.
