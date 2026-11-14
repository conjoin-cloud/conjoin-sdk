import { afterEach, beforeEach, describe, expect, it } from 'vitest'
import { createConjoinClient } from '../../../src/core/client'
import {
  ConjoinAbortError,
  ConjoinAuthenticationError,
  ConjoinConflictError,
  ConjoinInternalServerError,
  ConjoinNetworkError,
  ConjoinNotFoundError,
  ConjoinPermissionDeniedError,
  ConjoinRateLimitError,
  ConjoinResponseError,
  ConjoinTimeoutError,
  ConjoinValidationError,
} from '../../../src/core/errors'
import type { ConjoinClient, ConjoinConfig } from '../../../src/core/types'
import { startUnreliableServer, type UnreliableServer } from './unreliable-server'

const API_KEY = 'cak_test_harbourledgertransport'
const REQUEST_ID_PATTERN = /^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/
const SERVER_IDEMPOTENCY_KEY_PATTERN = /^[A-Za-z0-9\-_:.]{1,64}$/
const CALLER_REQUEST_ID = 'cnj_req_0198f0f7-5d0b-7b4a-8d5a-cf5693f0b2c1'
const NEW_CUSTOMER = { email: 'ledger.owner@example.com' }

const errorBody = (status: number) => ({
  response: { type: status >= 500 ? 'SERVER_ERROR' : 'CLIENT_ERROR', code: status, message: 'The ledger refused it' },
  data: null,
  error: { code: 'ledger_locked', param: 'email', details: [{ message: 'is locked', path: 'body.email' }] },
})

describe('transport over an unreliable network', () => {
  let server: UnreliableServer
  let client: ConjoinClient

  const createClient = (overrides: Partial<ConjoinConfig> = {}): ConjoinClient =>
    createConjoinClient({ apiKey: API_KEY, baseUrl: server.baseUrl, timeout: 2_000, ...overrides })

  const createCustomer = (options: { acceptsIdempotencyKey: boolean; idempotencyKey?: string }, target = client) =>
    target.fetch('billing/customers/', { method: 'POST', body: NEW_CUSTOMER, ...options })

  beforeEach(async () => {
    server = await startUnreliableServer()
    client = createClient({ retry: { backoffMs: 1, maxDelayMs: 50 } })
  })

  afterEach(async () => {
    await server.stop()
  })

  it('stores one customer when the connection drops after the server stored the first attempt', async () => {
    server.queue({ kind: 'drop-after-store' })

    const customer = await createCustomer({ acceptsIdempotencyKey: true })

    expect(server.storedCustomers()).toEqual([{ customer_id: 'cus_1', email: NEW_CUSTOMER.email }])
    expect(customer).toEqual({ customer_id: 'cus_1', email: NEW_CUSTOMER.email })
    expect(server.attempts).toHaveLength(2)

    const [first, second] = server.attempts
    expect(first?.headers['idempotency-key']).toMatch(SERVER_IDEMPOTENCY_KEY_PATTERN)
    expect(second?.headers['idempotency-key']).toBe(first?.headers['idempotency-key'])
    expect(second?.headers['conjoin-request-id']).toBe(first?.headers['conjoin-request-id'])
  })

  it('sends a different idempotency key for each separate create', async () => {
    await createCustomer({ acceptsIdempotencyKey: true })
    await createCustomer({ acceptsIdempotencyKey: true })

    expect(server.storedCustomers()).toHaveLength(2)
    expect(server.attempts[0]?.headers['idempotency-key']).not.toBe(server.attempts[1]?.headers['idempotency-key'])
  })

  it('keeps the caller key on every retry of a create', async () => {
    server.queue({ kind: 'status', status: 503 }, { kind: 'drop-before-store' })

    await createCustomer({ acceptsIdempotencyKey: true, idempotencyKey: 'ledger-order-7731' })

    expect(server.attempts.map(attempt => attempt.headers['idempotency-key'])).toEqual([
      'ledger-order-7731',
      'ledger-order-7731',
      'ledger-order-7731',
    ])
    expect(server.storedCustomers()).toHaveLength(1)
  })

  it('never retries a create whose operation takes no idempotency key', async () => {
    server.queue({ kind: 'drop-after-store' })

    await expect(createCustomer({ acceptsIdempotencyKey: false })).rejects.toBeInstanceOf(ConjoinNetworkError)
    expect(server.attempts).toHaveLength(1)
    expect(server.storedCustomers()).toHaveLength(1)
  })

  it('never retries a create whose operation takes no key, even when the caller passes one', async () => {
    server.queue({ kind: 'status', status: 503, body: errorBody(503) })

    await expect(
      createCustomer({ acceptsIdempotencyKey: false, idempotencyKey: 'ledger-order-7732' }),
    ).rejects.toBeInstanceOf(ConjoinInternalServerError)
    expect(server.attempts).toHaveLength(1)
  })

  it.each([429, 500, 502, 503, 504])('retries a read after a %i', async status => {
    server.queue({ kind: 'status', status, body: errorBody(status) })

    await expect(client.fetchJson('billing/customers/cus_1')).resolves.toMatchObject({ data: { method: 'GET' } })
    expect(server.attempts).toHaveLength(2)
    expect(server.attempts[1]?.headers['conjoin-request-id']).toBe(server.attempts[0]?.headers['conjoin-request-id'])
  })

  it.each(['PUT', 'PATCH', 'DELETE'] as const)('retries a %s after a dropped connection', async method => {
    server.queue({ kind: 'drop-before-store' })

    await client.fetchJson('billing/customers/cus_1', { method, body: method === 'DELETE' ? undefined : {} })

    expect(server.attempts.map(attempt => attempt.method)).toEqual([method, method])
  })

  it.each([
    [400, ConjoinValidationError],
    [401, ConjoinAuthenticationError],
    [403, ConjoinPermissionDeniedError],
    [404, ConjoinNotFoundError],
    [409, ConjoinConflictError],
    [422, ConjoinValidationError],
    [501, ConjoinInternalServerError],
  ])('never retries a %i and reports its code, param, and details', async (status, ErrorClass) => {
    server.queue({ kind: 'status', status, body: errorBody(status) })

    const error = await client.fetchJson('billing/customers/cus_1').catch((caught: unknown) => caught)

    expect(Object.getPrototypeOf(error)).toBe(ErrorClass.prototype)
    expect(error).toMatchObject({
      status,
      code: 'ledger_locked',
      param: 'email',
      details: [{ message: 'is locked', path: 'body.email' }],
      requestId: server.attempts[0]?.headers['conjoin-request-id'],
    })
    expect(server.attempts).toHaveLength(1)
  })

  it('stops after the configured number of retries', async () => {
    const limited = createClient({ retry: { maxRetries: 2, backoffMs: 1 } })
    server.queue(...Array.from({ length: 5 }, () => ({ kind: 'status' as const, status: 503, body: errorBody(503) })))

    await expect(limited.fetchJson('billing/customers/cus_1')).rejects.toBeInstanceOf(ConjoinInternalServerError)
    expect(server.attempts).toHaveLength(3)
  })

  it('waits the Retry-After seconds before it retries', async () => {
    const patient = createClient({ retry: { backoffMs: 0, maxDelayMs: 60_000 } })
    server.queue({ kind: 'status', status: 429, headers: { 'retry-after': '1' }, body: errorBody(429) })

    await patient.fetchJson('billing/customers/cus_1')

    const [first, second] = server.attempts
    expect((second?.receivedAt ?? 0) - (first?.receivedAt ?? 0)).toBeGreaterThanOrEqual(950)
  })

  it('caps a Retry-After date at the client maximum delay', async () => {
    const capped = createClient({ retry: { backoffMs: 0, maxDelayMs: 200 } })
    const retryAt = new Date(Date.now() + 30_000).toUTCString()
    server.queue({ kind: 'status', status: 503, headers: { 'retry-after': retryAt }, body: errorBody(503) })

    await capped.fetchJson('billing/customers/cus_1')

    const [first, second] = server.attempts
    const gap = (second?.receivedAt ?? 0) - (first?.receivedAt ?? 0)
    expect(gap).toBeGreaterThanOrEqual(150)
    expect(gap).toBeLessThan(2_000)
  })

  it('reports the Retry-After of a 429 once the retries run out', async () => {
    const single = createClient({ retry: { maxRetries: 0 } })
    server.queue({ kind: 'status', status: 429, headers: { 'retry-after': '7' }, body: errorBody(429) })

    const error = await single.fetchJson('billing/customers/cus_1').catch((caught: unknown) => caught)

    expect(error).toBeInstanceOf(ConjoinRateLimitError)
    expect(error).toMatchObject({ retryAfterMs: 7_000 })
  })

  it('retries a read that timed out and returns the next answer', async () => {
    const quick = createClient({ timeout: 100, retry: { backoffMs: 1 } })
    server.queue({ kind: 'slow', delayMs: 600 })

    await expect(quick.fetchJson('billing/customers/cus_1')).resolves.toMatchObject({ data: { method: 'GET' } })
    expect(server.attempts).toHaveLength(2)
  })

  it('raises a timeout error that differs from a cancellation', async () => {
    const quick = createClient({ timeout: 100, retry: { maxRetries: 0 } })
    server.queue({ kind: 'slow', delayMs: 600 })

    const error = await quick.fetchJson('billing/customers/cus_1').catch((caught: unknown) => caught)

    expect(error).toBeInstanceOf(ConjoinTimeoutError)
    expect(error).not.toBeInstanceOf(ConjoinAbortError)
  })

  it('cancels a request in flight as soon as the caller aborts', async () => {
    server.queue({ kind: 'slow', delayMs: 5_000 })
    const controller = new AbortController()
    const startedAt = Date.now()
    setTimeout(() => controller.abort(), 50)

    const error = await client
      .fetchJson('billing/customers/cus_1', { signal: controller.signal })
      .catch((caught: unknown) => caught)

    expect(error).toBeInstanceOf(ConjoinAbortError)
    expect(error).not.toBeInstanceOf(ConjoinTimeoutError)
    expect(Date.now() - startedAt).toBeLessThan(1_000)
    expect(server.attempts).toHaveLength(1)
  })

  it('cancels during the wait before a retry', async () => {
    const patient = createClient({ retry: { maxDelayMs: 60_000 } })
    server.queue({ kind: 'status', status: 503, headers: { 'retry-after': '30' }, body: errorBody(503) })
    const controller = new AbortController()
    const startedAt = Date.now()
    setTimeout(() => controller.abort(), 200)

    const error = await patient
      .fetchJson('billing/customers/cus_1', { signal: controller.signal })
      .catch((caught: unknown) => caught)

    expect(error).toBeInstanceOf(ConjoinAbortError)
    expect(Date.now() - startedAt).toBeLessThan(1_500)
    expect(server.attempts).toHaveLength(1)
  })

  it('sends nothing when the caller has already aborted', async () => {
    await expect(client.fetchJson('billing/customers/cus_1', { signal: AbortSignal.abort() })).rejects.toBeInstanceOf(
      ConjoinAbortError,
    )
    expect(server.attempts).toHaveLength(0)
  })

  it('creates a different request ID for separate calls and keeps the caller ID on retries', async () => {
    await client.fetchJson('billing/customers/cus_1')
    await client.fetchJson('billing/customers/cus_2')
    server.queue({ kind: 'status', status: 502, body: errorBody(502) })
    await client.fetchJson('billing/customers/cus_3', { conjoinRequestId: CALLER_REQUEST_ID })

    const ids = server.attempts.map(attempt => attempt.headers['conjoin-request-id'])
    expect(ids[0]).toMatch(REQUEST_ID_PATTERN)
    expect(ids[1]).toMatch(REQUEST_ID_PATTERN)
    expect(ids[0]).not.toBe(ids[1])
    expect(ids.slice(2)).toEqual([CALLER_REQUEST_ID, CALLER_REQUEST_ID])
  })

  it('pages through a list with cursor[next] and keeps the other query parameters', async () => {
    const pages: Record<string, { data: string[]; next: string | null }> = {
      first: { data: ['cus_1', 'cus_2'], next: 'page_two' },
      page_two: { data: ['cus_3', 'cus_4'], next: 'page_three' },
      page_three: { data: ['cus_5'], next: null },
    }
    server.servePages(cursor => pages[cursor ?? 'first'] ?? { data: [], next: null })

    const page = await client.fetchList<string>('billing/customers/', { query: { limit: 2 } })
    const customers: string[] = []
    for await (const customer of page) customers.push(customer)

    expect(customers).toEqual(['cus_1', 'cus_2', 'cus_3', 'cus_4', 'cus_5'])
    expect(server.attempts.map(attempt => [attempt.query.get('cursor[next]'), attempt.query.get('limit')])).toEqual([
      [null, '2'],
      ['page_two', '2'],
      ['page_three', '2'],
    ])
  })

  it('stops paging when the server repeats a cursor', async () => {
    server.servePages(() => ({ data: ['cus_1'], next: 'page_loop' }))

    const page = await client.fetchList<string>('billing/customers/')
    const read = async () => {
      for await (const _customer of page) {
        if (server.attempts.length > 10) return
      }
    }

    await expect(read()).rejects.toBeInstanceOf(ConjoinResponseError)
    expect(server.attempts.length).toBeLessThanOrEqual(3)
  })
})

describe('regional address from the key', () => {
  it.each([
    ['cak_gh_live_harbourledger', 'https://api.gh.conjoin.cloud'],
    ['cak_eu_test_harbourledger', 'https://api.eu.conjoin.cloud'],
    ['cpk_gh_test_harbourledger', 'https://api.gh.conjoin.cloud'],
    ['cpk_eu_live_harbourledger', 'https://api.eu.conjoin.cloud'],
    ['cak_live_harbourledger', 'https://api.conjoin.cloud'],
    ['cak_us_live_harbourledger', 'https://api.conjoin.cloud'],
    ['cak_gh_staging_harbourledger', 'https://api.conjoin.cloud'],
    ['sk_eu_live_harbourledger', 'https://api.conjoin.cloud'],
  ])('sends %s to %s', (key, baseUrl) => {
    const config = key.startsWith('cpk_') ? { publishableKey: key } : { apiKey: key }

    expect(createConjoinClient(config).config.baseUrl).toBe(baseUrl)
  })
})
