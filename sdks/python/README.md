# conjoin-cloud

`conjoin-cloud` is the official Python SDK for Conjoin. It includes sync and async clients, generated calls for every operation in the Conjoin API documents, storage upload and download helpers, AI chat helpers, scope headers, safe retries, request tracing, response metadata, and typed Conjoin errors.

Python 3.10 or later is required.

## Install

Install the package with pip:

```bash
pip install conjoin-cloud
```

## Authentication

Create a client with exactly one credential:

```python
from conjoin_cloud import Conjoin

client = Conjoin(api_key='cak_live_...')
```

Use a publishable key in browser-adjacent flows:

```python
client = Conjoin(publishable_key='cpk_live_...')
```

Passing both raises a `ConjoinConfigurationError`. When you pass neither, the client reads `CONJOIN_API_KEY` or `CONJOIN_PUBLISHABLE_KEY`, and it raises the same error when both variables are set. Load `.env` files in your application before you create the client.

The SDK picks the regional host from the key, so a `cak_eu_live_` or `cpk_eu_live_` key calls `https://api.eu.conjoin.cloud`, a `gh` key calls `https://api.gh.conjoin.cloud`, and a key with no region code calls `https://api.conjoin.cloud`. Set `base_url` only when you need to reach another host.

## Sync Client

Use `Conjoin` in blocking Python code:

```python
from conjoin_cloud import Conjoin

with Conjoin(api_key='cak_live_...', auth_app_id='app_123') as client:
    page = client.auth.accounts.list()

    for account in page.data:
        print(account.account_id)
```

Generated calls are grouped by service and resource:

```python
page = client.auth.accounts.list()
customers = client.billing.customers.list()
customer = client.billing.customers.read('cust_123')
```

The calls in the frontend document live under `client.frontend`, as in `client.frontend.auth.accounts`.

Generated responses use Pydantic models. Python attributes use `snake_case`, and API wire aliases stay available when you dump a model with aliases:

```python
payload = page.data[0].model_dump(by_alias=True)
```

Use `client.request(...)` when you need an endpoint before a generated call exists:

```python
customer = client.request('GET', 'billing/customers/cust_123', scopes=('billing_entity_id',))
```

## Async Client

Use `AsyncConjoin` with `async with`:

```python
from conjoin_cloud import AsyncConjoin


async def main() -> None:
    async with AsyncConjoin(api_key='cak_live_...', auth_app_id='app_123') as client:
        page = await client.auth.accounts.list()

        async for account in page.iter_all():
            print(account.account_id)
```

The async client has the same generated call shape as the sync client. Cancelling the task that awaits a call stops the call at once, during a backoff wait too, and raises `asyncio.CancelledError`.

## Scope Headers

Calls that need a scope read it from the client. Set `billing_entity_id`, `messaging_profile_id`, or `auth_app_id` when you create the client, or call `with_scope(...)` to get a scoped copy that shares the same connection pool:

```python
billing = client.with_scope(billing_entity_id='entity_123')
customers = billing.billing.customers.list()
```

The SDK sends them as the `Billing-Entity-ID`, `Messaging-Profile-ID`, and `Auth-App-ID` headers. A call that needs a scope that you didn't set raises a `ConjoinConfigurationError` before it sends anything.

## Retries

The SDK retries `GET`, `PUT`, `PATCH`, and `DELETE` calls after a network failure, a timeout, or a `429`, `500`, `502`, `503`, or `504` response. It retries a `POST` only when the API declares an `Idempotency-Key` header for that operation. The SDK then generates a key for each call, or sends the one that you pass in `RequestOptions(idempotency_key=...)`, and it keeps the same key on every retry. A key is 1 to 64 characters of letters, digits, `-`, `_`, `:`, and `.`, and passing one on any other call raises a `ConjoinConfigurationError`.

A `POST` whose operation declares no `Idempotency-Key` header goes out once, because the server can't tell a retry from a second request.

The SDK never retries a `501` or any other `4xx` response. When the server sends `Retry-After`, as seconds or as an HTTP date, the SDK waits that long, capped at `max_retry_delay_seconds`. Otherwise it waits a random time between zero and `backoff_seconds * 2 ** attempt`, capped at the same limit:

```python
client = Conjoin(
    api_key='cak_live_...',
    timeout=30,
    max_retries=3,
    backoff_seconds=0.5,
    max_retry_delay_seconds=60,
)
```

Those values are the defaults. `timeout` applies to each phase of one attempt, which means connecting, sending the body, and waiting for each part of the response.

## Request Options and Response Metadata

Every generated call accepts `request_options` to change one call:

```python
from conjoin_cloud import RequestOptions

account = client.auth.accounts.read(
    'acct_123',
    request_options=RequestOptions(
        timeout=10,
        max_retries=1,
        conjoin_request_id='cnj_req_0198f0f7-5d0b-7b4a-8d5a-cf5693f0b2c1',
    ),
)
```

Use `with_response` when you need the HTTP response metadata:

```python
result = client.with_response.request(
    'GET',
    'billing/customers/cust_123',
    scopes=('billing_entity_id',),
)

print(result.status_code)
print(result.request_id)
print(result.data)
```

## Request IDs

Every call sends a `Conjoin-Request-Id` header, and every retry of that call sends the same value. Pass `conjoin_request_id` in the client settings or in the request options to reuse an ID from your own logs, or wrap related calls in `client.with_request_trace(lambda traced, request_id: ...)` so that they share one ID. Otherwise the SDK creates a fresh ID for every call. Every error exposes the ID as `error.request_id`.

## Pagination

List calls return typed `Page[T]` objects that hold `response`, `data`, and `cursor`. Call `iter_all()` to read every page in order:

```python
for account in client.auth.accounts.list().iter_all():
    print(account.account_id)
```

`next_page()` fetches one more page with the same filters and `cursor.next`, and it returns `None` on the last page. `iter_all()` raises a `ConjoinResponseError` when the server returns a cursor that it returned before.

## Storage

Use `client.storage.upload(...)` for single or resumable signed URL uploads. `body` accepts bytes, a path, a binary file object, or an iterable of bytes. Resumable uploads require a chunk size aligned to 256 KiB. The default chunk size is 8 MiB.

```python
from pathlib import Path

from conjoin_cloud import Conjoin, UploadProgress


def report_progress(progress: UploadProgress) -> None:
    print(f'{progress.loaded}/{progress.total} bytes')


with Conjoin(api_key='cak_live_...') as client:
    client.storage.upload(
        container='container_123',
        path='reports/monthly.csv',
        content_type='text/csv',
        body=Path('monthly.csv'),
        on_progress=report_progress,
    )
```

Downloads are context-managed so the response stream closes after use:

```python
with client.storage.download(container='container_123', path='reports/monthly.csv') as download:
    data = download.read()
```

The generated storage calls, such as `client.storage.objects.list(...)`, stay available next to the helpers. `ConjoinStorageError.storage_url` holds the signed URL without its query string, so the signature never reaches your logs.

## AI Chat

Call `client.ai.chat.complete(...)` for a non-streaming chat completion. It returns the completion in the OpenAI format, with `choices`, `usage`, and a `conjoin` field that holds the cost, the latency, and whether your own provider key served the call:

```python
completion = client.ai.chat.complete(
    model='your-model-id',
    messages=[{'role': 'user', 'content': 'Write a concise account update.'}],
)

print(completion.choices[0]['message']['content'], completion.usage)
```

Call `client.ai.chat.stream(...)` for typed SSE chunks:

```python
for chunk in client.ai.chat.stream(
    model='your-model-id',
    messages=[{'role': 'user', 'content': 'Stream a short payment reminder.'}],
):
    for choice in chunk.choices:
        if choice.delta.content:
            print(choice.delta.content, end='')
```

The async client supports `await client.ai.chat.complete(...)` and `async for chunk in client.ai.chat.stream(...)`.

## Messaging Email

Messaging calls read `Messaging-Profile-ID` from the client:

```python
client = Conjoin(api_key='cak_live_...', messaging_profile_id='msg_profile_123')

message = client.messaging.emails.send(
    {
        'from_': 'sender@example.com',
        'to': ['recipient@example.com'],
        'subject': 'Welcome',
        'text': 'Thanks for creating your account.',
    },
)

print(message.message_id)
```

Use `from_` as the Python field name because Python reserves `from`. The SDK sends the wire field as `from`.

## SCIM

Tenant SCIM operations use a SCIM bearer token:

```python
users = client.auth.scim.with_token('scim_token_...').scim_list_users(
    'cnj_proj_123',
    'app_123',
)
```

Public SCIM metadata endpoints, such as schemas and resource types, stay callable through the normal client.

## Credentials That a Call Declares

Each call sends only the credential that its API document declares. A frontend call that signs in nobody sends no `Authorization` header, a call that needs the publishable key raises `ConjoinConfigurationError` when the client holds an API key, and none of them ever sends your API key. A call for the signed-in user takes the session token as its `session_token` keyword, and an SSO portal call takes the portal ticket as its `portal_ticket` keyword, which the SDK sends only in the `x-portal-ticket` header. These calls refuse `request_options.auth`.

A call that declares a header of its own, such as the step-up headers on `accounts.delete`, takes each header as a keyword. The SDK checks each value against the documented length and format before it sends anything:

```python
from conjoin_cloud import Credential

client.auth.accounts.delete(
    'acc_123',
    step_up_session_id=step_up_session_id,
    step_up_token=Credential(step_up_token),
)
```

The step-up token, the session token, and the portal ticket take a `Credential`, whose `str` and `repr` show only `[redacted]`.

## Errors

Every SDK error extends `ConjoinError`:

```python
from conjoin_cloud import (
    ConjoinConflictError,
    ConjoinError,
    ConjoinNotFoundError,
    ConjoinRateLimitError,
    ConjoinValidationError,
)

try:
    client.billing.customers.read('cust_123')
except ConjoinValidationError as error:
    for field in error.errors:
        print(f'{field.path}: {field.message}')
except ConjoinNotFoundError:
    print('The customer does not exist.')
except ConjoinConflictError as error:
    print(error.code, error.details)
except ConjoinRateLimitError as error:
    print(f'Retry after {error.retry_after} seconds.')
except ConjoinError as error:
    print(error.code, error.message, error.request_id)
```

Every error exposes `status`, `code`, `param`, `details`, and `request_id`. `param` and `details` are `None` when the server sends neither.

- `ConjoinValidationError` covers `400` and `422` responses, with field-level details on `.errors`.
- `ConjoinAuthenticationError` covers `401` responses.
- `ConjoinPermissionDeniedError` covers `403` responses.
- `ConjoinNotFoundError` covers `404` responses.
- `ConjoinConflictError` covers `409` responses.
- `ConjoinRateLimitError` covers `429` responses and exposes `.retry_after` in seconds when the server sends `Retry-After`.
- `ConjoinInternalServerError` covers `5xx` responses.
- `ConjoinApiError` is the base class of every API error, and it covers any other status.
- `ConjoinResponseError` covers a response body that the SDK can't read.
- `ConjoinNetworkError` covers DNS failures, refused connections, and dropped connections.
- `ConjoinTimeoutError` covers calls that run past the configured timeout.
- `ConjoinConfigurationError` covers client settings and call options that the SDK rejects before it sends anything.
- `ConjoinStorageError` covers upload, download, and signed URL failures.

The SDK reads at most 64 KiB of an error body.

## Examples

The `examples/` directory includes focused scripts:

- `package_metadata.py` prints package metadata.
- `sync_client.py` shows sync client setup.
- `async_client.py` shows async client setup.
- `pagination.py` reads every page of accounts.
- `storage_upload_download.py` uploads and downloads a storage object.
- `ai_streaming.py` streams chat chunks.
- `messaging_email.py` sends a profile-scoped email.

The examples make no network calls when imported. Running them requires live credentials and any IDs, model names, or local files referenced by the script.

## Development

Create the Python environment from this package directory:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

Run package checks from this directory:

```bash
python3 scripts/run_python.py -m codegen
python3 scripts/run_python.py -m pytest
python3 scripts/run_python.py -m ruff check src tests examples scripts codegen
python3 scripts/run_python.py -m pyright
python3 scripts/run_python.py -m hatchling build
```

`codegen` reads `spec/openapi.json` and `spec/openapi-frontend.json` at the repository root and rewrites `src/conjoin_cloud/generated`. Two runs on the same documents produce the same files.

Run Nx tasks from the repository root:

```bash
pnpm nx run sdk-python:generate
pnpm nx run sdk-python:lint
pnpm nx run sdk-python:typecheck
pnpm nx run sdk-python:test
pnpm nx run sdk-python:build
```

Root Nx targets use `scripts/run_python.py`. The runner prefers `CONJOIN_PYTHON`, then this package's `.venv`, then an active `VIRTUAL_ENV`, then the current interpreter.
