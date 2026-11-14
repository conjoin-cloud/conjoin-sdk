import { afterEach, beforeEach, expect, it } from 'vitest'
import { createConjoinClient } from '../../../src/core/client'
import { ConjoinNetworkError, ConjoinResponseError } from '../../../src/core/errors'
import { startUnreliableServer, type UnreliableServer } from './unreliable-server'

let server: UnreliableServer

beforeEach(async () => {
  server = await startUnreliableServer()
})

afterEach(async () => {
  await server.stop()
})

it('recovers a stored customer after a truncated response without duplicating the write', async () => {
  server.queue({ kind: 'drop-during-response' })
  const client = createConjoinClient({ apiKey: 'cak_test_transport', baseUrl: server.baseUrl, retry: { backoffMs: 0 } })
  const customer = await client.fetch('billing/customers/', {
    method: 'POST',
    body: { email: 'billing@example.com' },
    acceptsIdempotencyKey: true,
  })
  expect(server.storedCustomers()).toEqual([customer])
  expect(server.attempts).toHaveLength(2)
  expect(server.attempts[1]?.headers['idempotency-key']).toBe(server.attempts[0]?.headers['idempotency-key'])
  expect(server.attempts[1]?.headers['conjoin-request-id']).toBe(server.attempts[0]?.headers['conjoin-request-id'])
})

it('does not replay an undeclared write after a truncated response', async () => {
  server.queue({ kind: 'drop-during-response' })
  const client = createConjoinClient({ apiKey: 'cak_test_transport', baseUrl: server.baseUrl })
  await expect(
    client.fetch('billing/customers/', { method: 'POST', body: { email: 'billing@example.com' } }),
  ).rejects.toBeInstanceOf(ConjoinNetworkError)
  expect(server.storedCustomers()).toHaveLength(1)
  expect(server.attempts).toHaveLength(1)
})

it('rejects an oversized success without retrying and accepts the exact byte limit', async () => {
  const body = { data: 'é'.repeat(50) }
  const size = Buffer.byteLength(JSON.stringify(body))
  server.queue({ kind: 'status', status: 200, body }, { kind: 'status', status: 200, body })
  const client = createConjoinClient({
    apiKey: 'cak_test_transport',
    baseUrl: server.baseUrl,
    maxResponseBytes: size - 1,
  })
  await expect(client.fetch('billing/customers/')).rejects.toBeInstanceOf(ConjoinResponseError)
  expect(server.attempts).toHaveLength(1)
  const exact = createConjoinClient({ apiKey: 'cak_test_transport', baseUrl: server.baseUrl, maxResponseBytes: size })
  await expect(exact.fetch('billing/customers/')).resolves.toBe(body.data)
})
