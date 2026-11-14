# @conjoin-cloud/sdk

`@conjoin-cloud/sdk` is the official TypeScript SDK for [Conjoin](https://conjoin.delalify.com). The package provides generated REST resources, storage helpers, AI chat helpers, framework adapters, server verification helpers, retries, request tracing, and typed errors.

The package ships ESM and CJS builds. Each product has its own subpath export, so bundlers can include the code you import.

[![npm version](https://img.shields.io/npm/v/@conjoin-cloud/sdk)](https://www.npmjs.com/package/@conjoin-cloud/sdk)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)

## Install

Install the package with your package manager:

```bash
npm install @conjoin-cloud/sdk
pnpm add @conjoin-cloud/sdk
yarn add @conjoin-cloud/sdk
```

Install peer dependencies for the entry points you import:

- Install `next` `>=16.2.6` when you import `@conjoin-cloud/sdk/next`.
- Install `express` `>=4.0.0` and `@types/express` `>=4.0.0` when you import `@conjoin-cloud/sdk/express`.
- Install `hono` `>=4.12.19` when you import `@conjoin-cloud/sdk/hono`.

## Quick Start

```ts
import { createConjoinClient } from '@conjoin-cloud/sdk'
import { createBillingCustomers } from '@conjoin-cloud/sdk/billing'

const conjoin = createConjoinClient({
  apiKey: 'cak_live_...',
  billingEntityId: 'entity_123',
})

const customers = createBillingCustomers(conjoin)

const customer = await customers.create({
  name: 'Harbour Ledger',
  email: 'billing@example.com',
})

console.log(customer.customer_id)
```

Import the product entry point you need. Importing `@conjoin-cloud/sdk/billing` keeps the bundle focused on billing code.

## Subpath Exports

- Import `@conjoin-cloud/sdk` for `createConjoinClient`, shared types, and error classes.
- Import `@conjoin-cloud/sdk/auth` for accounts, sessions, OAuth, organizations, passkeys, MFA, and SCIM.
- Import `@conjoin-cloud/sdk/billing` for customers, subscriptions, invoices, products, prices, payment methods, and entitlements.
- Import `@conjoin-cloud/sdk/storage` for containers, objects, signed uploads, signed downloads, and ACLs.
- Import `@conjoin-cloud/sdk/messaging` for email, SMS, contacts, conversations, templates, OTP, and profile-scoped clients.
- Import `@conjoin-cloud/sdk/relay` for WebSocket broadcast, queues, events, scheduler, memorystore, and search.
- Import `@conjoin-cloud/sdk/ai` for chat completions, streaming, models, providers, and usage resources.
- Import `@conjoin-cloud/sdk/cloud` for API keys, roles, projects, webhooks, audit resources, and plans.
- Import `@conjoin-cloud/sdk/server` for `verifyToken`, `verifyWebhook`, `createConjoinServer`, and `fetchConjoinBranding`.
- Import `@conjoin-cloud/sdk/next` for `auth()`, `currentAccount()`, `conjoinProxy`, and `createRouteMatcher`.
- Import `@conjoin-cloud/sdk/express` for `conjoinMiddleware`, `getAuth`, and `requireAuth`.
- Import `@conjoin-cloud/sdk/hono` for `conjoinMiddleware`, `getAuth`, and `requireAuth`.
- Import `@conjoin-cloud/sdk/database` and `@conjoin-cloud/sdk/runtime` for reserved entry points.

## Configuration

Create one client and pass it to generated resource factories:

```ts
const conjoin = createConjoinClient({
  apiKey: 'cak_eu_live_...',
  timeout: 30_000,
  retry: {
    maxRetries: 3,
    backoffMs: 500,
    maxDelayMs: 60_000,
  },
})
```

Use `apiKey` on the server and `publishableKey` in browser and mobile clients, and pass exactly one of them. The SDK picks the regional host from the key, so a `cak_eu_live_` or `cpk_eu_live_` key calls `https://api.eu.conjoin.cloud`, a `gh` key calls `https://api.gh.conjoin.cloud`, and a key with no region code calls `https://api.conjoin.cloud`. Set `baseUrl` only when you need to reach another host.

Calls that need a scope read it from the client. Set `billingEntityId`, `messagingProfileId`, or `authAppId` when you create the client, or call `conjoin.withScope({ billingEntityId })` to get a scoped copy. The SDK sends them as the `Billing-Entity-ID`, `Messaging-Profile-ID`, and `Auth-App-ID` headers, and a call that needs a scope that you didn't set throws a `ConjoinConfigurationError` before it sends anything.

### Retries

The SDK retries `GET`, `PUT`, `PATCH`, and `DELETE` calls after a network failure, a timeout, or a `429`, `500`, `502`, `503`, or `504` response. It retries a `POST` only when the API declares an `Idempotency-Key` header for that operation. The SDK then generates a key for each call, or sends the one that you pass, and it keeps the same key on every retry:

```ts
await customers.create(
  { email: 'billing@example.com' },
  { idempotencyKey: 'signup-7f3a9c' },
)
```

A `POST` whose operation declares no `Idempotency-Key` header goes out once, because the server can't tell a retry from a second request.

The SDK never retries a `501` or any other `4xx` response. When the server sends `Retry-After`, the SDK waits that long, capped at `retry.maxDelayMs`. Otherwise it waits a random time between zero and `backoffMs * 2 ** attempt`, capped at the same limit. Pass `maxRetries` or `timeout` in the call options to change them for one call.

Pass an `AbortSignal` as `signal` to cancel a call. An abort stops the call at once, during a backoff wait too, and raises a `ConjoinAbortError`, while a call that runs past `timeout` raises a `ConjoinTimeoutError`.

### Request IDs

Every call sends a `Conjoin-Request-Id` header, and every retry of that call sends the same value. Pass `conjoinRequestId` in the client settings or in the call options to reuse an ID from your own logs, or wrap related calls in `conjoin.withRequestTrace((client, requestId) => ...)` so that they share one ID. Every error exposes the ID as `error.requestId`.

## Auth

```ts
import { createAuthAccounts } from '@conjoin-cloud/sdk/auth'

const accounts = createAuthAccounts(conjoin.withScope({ authAppId: 'app_123' }))

const account = await accounts.create({
  name: 'Taylor Morgan',
  primary_email: 'member@example.com',
  reference_id: 'member_123',
})

console.log(account.account_id)
```

Accounts and sessions belong to a Conjoin auth application, so the auth calls need `authAppId` on the client.

## Billing

```ts
import { createBillingCustomers } from '@conjoin-cloud/sdk/billing'

const customers = createBillingCustomers(conjoin.withScope({ billingEntityId: 'entity_123' }))

const page = await customers.list({ limit: 20 })

for (const customer of page.data) {
  console.log(customer.customer_id)
}

const nextPage = await page.nextPage()

for await (const customer of page) {
  console.log(customer.email)
}
```

Billing calls need `billingEntityId` on the client. A list call returns a page with `response`, `data`, and `cursor: { prev, next }`. `page.nextPage()` fetches the page after it, or returns `null` on the last page, and `for await` walks every item across every page.

## Storage

Uploads and downloads use signed URLs, so browser and server code can move bytes directly to storage:

```ts
import {
  createStorageDownloader,
  createStorageUploader,
} from '@conjoin-cloud/sdk/storage'

const uploader = createStorageUploader(conjoin)
const downloader = createStorageDownloader(conjoin)

await uploader.upload({
  container: 'reports',
  path: 'finance/q4.pdf',
  contentType: 'application/pdf',
  body: file,
  onProgress: ({ percentage }) => {
    console.log(`${percentage.toFixed(1)}%`)
  },
})

const result = await downloader.download({
  container: 'reports',
  path: 'finance/q4.pdf',
})

const blob = await result.blob()
```

Use `createStorageContainers(conjoin)` for container administration. Use `createStorageObjectAcls(conjoin)` for object ACLs.

## Messaging

Messaging operations use the `Messaging-Profile-ID` header. Bind a profile once with `createMessaging`:

```ts
import { createMessaging } from '@conjoin-cloud/sdk/messaging'

const messaging = createMessaging(conjoin, {
  profileId: 'msg_profile_123',
})

await messaging.sms.sendSms({
  to: '+15551234567',
  body: 'Your verification code is 482910.',
})

await messaging.emails.send({
  to: 'member@example.com',
  subject: 'Welcome',
  html: '<h1>Welcome to Harbour Ledger</h1>',
})
```

The profiled messaging client exposes `emails`, `sms`, `multisend`, `contacts`, `conversations`, `templates`, `verifications`, `analytics`, `emailSenders`, `smsSenders`, `smsBrands`, `smsCampaigns`, `phoneNumbers`, and `profiles`.

## AI Chat

```ts
import { createAiChat } from '@conjoin-cloud/sdk/ai'

const chat = createAiChat(conjoin)

const response = await chat.complete({
  model: 'your-model-id',
  messages: [{ role: 'user', content: 'Explain cursor-based pagination.' }],
})

const stream = chat.stream({
  model: 'your-model-id',
  messages: [{ role: 'user', content: 'Draft a short payment reminder.' }],
})

for await (const chunk of stream) {
  process.stdout.write(chunk.choices?.[0]?.delta?.content ?? '')
}

stream.controller.abort()
```

`complete` returns the stored inference record, with its `status`, `token_usage`, `cost_usd`, and `latency_ms`. `stream` returns an `AsyncIterable<ChatCompletionChunk>` and an `AbortController`. Neither call retries until the API declares an `Idempotency-Key` header for chat completions, so a dropped connection never runs a completion twice.

## Relay Broadcast

```ts
import { createBroadcastConnection } from '@conjoin-cloud/sdk/relay'

const broadcast = createBroadcastConnection(conjoin, {
  getConnectionToken: async () => fetchConnectionTokenFromYourServer(),
})

await broadcast.connect()

const room = await broadcast.subscribe('support:room-42')

room.on('message', event => {
  console.log(`[${event.channel_id}]`, event.data)
})

await room.publish('message', { text: 'The ticket is ready for review.' })

const { events } = await room.history()
```

The connection opens a WebSocket at `/v1/relay/broadcast` on the API host, or at the full `ws` or `wss` URL that you pass as `url`, and it authenticates with the token that `getConnectionToken` returns. It reconnects after a dropped socket and subscribes to every channel again. Pass `authToken` to `subscribe` for a channel that needs a separate token. Use the per-resource relay factories for queues, events, scheduler, memorystore, and search.

## Server Verification

```ts
import { verifyToken, verifyWebhook } from '@conjoin-cloud/sdk/server'

const verified = await verifyToken(token, {
  jwksUrl: 'https://your-tenant.conjoin.cloud/.well-known/jwks.json',
  audience: 'your-app',
  issuer: 'https://conjoin.cloud',
})

console.log(verified.accountId, verified.sessionId, verified.organizationId)

const ok = verifyWebhook(rawBody, signatureHeader, webhookSecret)
```

`verifyToken` uses `jose` with a remote JWKS cached per `jwksUrl`. `verifyWebhook` checks a hex HMAC-SHA256 signature in constant time.

## Next.js App Router

Read authenticated state in route handlers:

```ts
import { auth } from '@conjoin-cloud/sdk/next'

export async function GET() {
  const session = await auth()

  if (session === null) {
    return new Response('Unauthorized', { status: 401 })
  }

  return Response.json({ accountId: session.accountId })
}
```

Protect middleware routes with `conjoinProxy`:

```ts
import { conjoinProxy, createRouteMatcher } from '@conjoin-cloud/sdk/next'
import { NextResponse } from 'next/server'

const isProtected = createRouteMatcher(['/dashboard(.*)', '/settings(.*)'])

export default conjoinProxy((auth, req) => {
  if (isProtected(req) && auth === null) {
    return NextResponse.redirect(new URL('/sign-in', req.url))
  }
})
```

The proxy reads a client-state cookie at the edge for routing decisions. Use `auth()` inside Server Components and Route Handlers when you need JWT verification.

`auth()` checks tokens against the JWKS on your project's auth domain. Set `CONJOIN_AUTH_DOMAIN`, or pass `authDomain` or `jwksUrl`, to point it there. With only `CONJOIN_PUBLISHABLE_KEY` set, the adapter reads the auth domain from your project's SDK settings and keeps it for five minutes. `currentAccount()` reads the signed-in account's profile from the same auth domain.

## Express

```ts
import express from 'express'
import {
  conjoinMiddleware,
  getAuth,
  requireAuth,
} from '@conjoin-cloud/sdk/express'

const app = express()

app.use(conjoinMiddleware({
  jwksUrl: 'https://your-tenant.conjoin.cloud/.well-known/jwks.json',
}))

app.get('/me', requireAuth, (req, res) => {
  const auth = getAuth(req)

  if (auth === null) {
    res.status(401).json({ error: 'Unauthorized' })
    return
  }

  res.json({ accountId: auth.accountId })
})
```

`getAuth(req)` returns `VerifiedToken | null`. `requireAuth` returns `401` when authentication is missing.

## Hono

```ts
import { Hono } from 'hono'
import {
  conjoinMiddleware,
  getAuth,
  requireAuth,
} from '@conjoin-cloud/sdk/hono'

const app = new Hono()

app.use('*', conjoinMiddleware({
  jwksUrl: 'https://your-tenant.conjoin.cloud/.well-known/jwks.json',
}))

app.get('/me', requireAuth, c => {
  const auth = getAuth(c)

  if (auth === null) {
    return c.json({ error: 'Unauthorized' }, 401)
  }

  return c.json({ accountId: auth.accountId })
})
```

`getAuth(c)` returns `VerifiedToken | null`. `requireAuth` returns `401` when authentication is missing.

## Errors

Every SDK error extends `ConjoinError`:

```ts
import {
  ConjoinConflictError,
  ConjoinError,
  ConjoinNotFoundError,
  ConjoinRateLimitError,
  ConjoinValidationError,
} from '@conjoin-cloud/sdk'

try {
  await customers.update('cus_123', { name: 'Harbour Ledger' })
} catch (err) {
  if (err instanceof ConjoinValidationError) {
    for (const field of err.errors) {
      console.log(`${field.path}: ${field.message}`)
    }
  } else if (err instanceof ConjoinNotFoundError) {
    console.log('The customer does not exist.')
  } else if (err instanceof ConjoinConflictError) {
    console.log(err.code, err.details)
  } else if (err instanceof ConjoinRateLimitError) {
    console.log(`Retry after ${err.retryAfterMs} ms.`)
  } else if (err instanceof ConjoinError) {
    console.log(err.code, err.message, err.requestId)
  }
}
```

Every error exposes `status`, `code`, `param`, `details`, and `requestId`. `param` is `null` and `details` is `null` when the server sends neither.

- `ConjoinValidationError` covers `400` and `422` responses, with field-level details on `.errors`.
- `ConjoinAuthenticationError` covers `401` responses.
- `ConjoinPermissionDeniedError` covers `403` responses.
- `ConjoinNotFoundError` covers `404` responses.
- `ConjoinConflictError` covers `409` responses.
- `ConjoinRateLimitError` covers `429` responses and exposes `.retryAfterMs` when the server sends `Retry-After`.
- `ConjoinInternalServerError` covers `5xx` responses.
- `ConjoinApiError` is the base class of every API error, and it covers any other status.
- `ConjoinResponseError` covers a response body that the SDK can't read.
- `ConjoinNetworkError` covers DNS failures and refused connections.
- `ConjoinTimeoutError` covers calls that run past the configured timeout.
- `ConjoinAbortError` covers calls that the caller aborted.
- `ConjoinConfigurationError` covers client settings and call options that the SDK rejects before it sends anything.
- `ConjoinStorageError` covers upload, download, and signed URL failures.
- `ConjoinError` is the base class of every SDK error.

## Bundle and Runtime

- The package exposes 14 entry points, one for each product or framework integration.
- Every entry point ships ESM, CJS, and `.d.ts` files.
- Factory functions let bundlers remove unused product code.
- Optional framework peer dependencies stay external at build time.

## Requirements

- Node.js 22.0.0 or later is required.
- TypeScript 5.x works for type-only consumers.
- Peer dependency versions are listed in the install section.

## Support

- Read product documentation at <https://conjoin.delalify.com>.
- Report SDK issues at <https://github.com/conjoin-cloud/conjoin-sdk/issues>.

## License

This package uses the [MIT](../../LICENSE) license.
