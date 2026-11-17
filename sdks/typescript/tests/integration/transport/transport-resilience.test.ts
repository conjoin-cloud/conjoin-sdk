import { afterEach, beforeEach, describe, expect, it } from 'vitest'
import { createConjoinClient } from '../../../src/core/client'
import { ConjoinNetworkError } from '../../../src/core/errors'
import type { ConjoinClient } from '../../../src/core/types'
import { startUnreliableServer, type UnreliableServer } from './unreliable-server'

const API_KEY = 'cak_test_harbourledgertransport'
const SERVER_IDEMPOTENCY_KEY_PATTERN = /^[A-Za-z0-9\-_:.]{1,64}$/
const NEW_CUSTOMER = { email: 'ledger.owner@example.com' }

describe('transport over an unreliable network', () => {
  let server: UnreliableServer
  let client: ConjoinClient

  const createCustomer = (options: { acceptsIdempotencyKey: boolean }) =>
    client.fetch('billing/customers/', { method: 'POST', body: NEW_CUSTOMER, ...options })

  beforeEach(async () => {
    server = await startUnreliableServer()
    client = createConjoinClient({
      apiKey: API_KEY,
      baseUrl: server.baseUrl,
      timeout: 2_000,
      retry: { backoffMs: 1, maxDelayMs: 50 },
    })
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
  })

  it('sends a different idempotency key for each separate create', async () => {
    await createCustomer({ acceptsIdempotencyKey: true })
    await createCustomer({ acceptsIdempotencyKey: true })

    expect(server.storedCustomers()).toHaveLength(2)
    expect(server.attempts[0]?.headers['idempotency-key']).not.toBe(server.attempts[1]?.headers['idempotency-key'])
  })

  it('never retries a create whose operation takes no idempotency key', async () => {
    server.queue({ kind: 'drop-after-store' })

    await expect(createCustomer({ acceptsIdempotencyKey: false })).rejects.toBeInstanceOf(ConjoinNetworkError)
    expect(server.attempts).toHaveLength(1)
    expect(server.storedCustomers()).toHaveLength(1)
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
