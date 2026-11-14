import { afterEach, beforeEach, expect, it } from 'vitest'
import { createConjoinClient } from '../../../src/core/client'
import type { BroadcastConnection, BroadcastSubscription } from '../../../src/relay'
import { createBroadcastConnection } from '../../../src/relay'
import { startBroadcastServer } from './local-broadcast-server'

let server: Awaited<ReturnType<typeof startBroadcastServer>>
let connection: BroadcastConnection | undefined
const client = createConjoinClient({ apiKey: 'cak_test_transport' })

beforeEach(async () => {
  server = await startBroadcastServer()
})
afterEach(async () => {
  connection?.disconnect()
  await server.stop()
})

it('subscribes once when the connected callback subscribes and publishes', async () => {
  let subscription: Promise<BroadcastSubscription> | undefined
  connection = createBroadcastConnection(client, {
    url: server.url,
    getConnectionToken: async () => 'connection_token',
    onStateChange: state => {
      if (state === 'connected') subscription = connection?.subscribe('orders')
    },
  })
  await connection.connect()
  await (await subscription)?.publish('created', {})
  expect(server.frames.filter(frame => frame.type === 'subscribe')).toHaveLength(1)
  expect(server.frames.filter(frame => frame.type === 'publish')).toHaveLength(1)
})

it('honours disconnect from inside the reconnecting callback', async () => {
  connection = createBroadcastConnection(client, {
    url: server.url,
    getConnectionToken: async () => 'connection_token',
    reconnectBaseDelay: 0,
    onStateChange: state => {
      if (state === 'reconnecting') connection?.disconnect()
    },
  })
  await connection.connect()
  server.drop()
  await new Promise(resolve => setTimeout(resolve, 100))
  expect(connection.state).toBe('disconnected')
  expect(server.connections).toBe(1)
})

it('does not restore a subscription removed inside the connected callback', async () => {
  const errors: Error[] = []
  let subscription: BroadcastSubscription | undefined
  let unsubscribing: Promise<void> | undefined
  let connected = 0
  connection = createBroadcastConnection(client, {
    url: server.url,
    getConnectionToken: async () => 'connection_token',
    reconnectBaseDelay: 0,
    onError: error => errors.push(error),
    onStateChange: state => {
      if (state === 'connected' && ++connected === 2) unsubscribing = subscription?.unsubscribe()
    },
  })
  await connection.connect()
  subscription = await connection.subscribe('orders')
  server.drop()
  await new Promise(resolve => setTimeout(resolve, 100))
  await unsubscribing
  expect(server.frames.filter(frame => frame.type === 'subscribe')).toHaveLength(1)
  expect(server.frames.filter(frame => frame.type === 'unsubscribe')).toHaveLength(1)
  expect(errors).toEqual([])
})

it('times out an unanswered upgrade and closes it when the caller disconnects', async () => {
  await server.stop()
  server = await startBroadcastServer(false)
  connection = createBroadcastConnection(client, {
    url: server.url,
    getConnectionToken: async () => 'connection_token',
    requestTimeout: 50,
  })
  await expect(connection.connect()).rejects.toMatchObject({ code: 'timeout_error' })
  expect(server.connections).toBe(1)
  const pending = connection.connect()
  const rejection = expect(pending).rejects.toMatchObject({ code: 'broadcast_disconnected' })
  await new Promise(resolve => setTimeout(resolve, 10))
  connection.disconnect()
  await rejection
  expect(connection.state).toBe('disconnected')
})

it('keeps a restored channel when the previous connection token resolves late', async () => {
  let releaseToken: ((token: string) => void) | undefined
  const token = new Promise<string>(resolve => {
    releaseToken = resolve
  })
  let tokenReads = 0
  connection = createBroadcastConnection(client, {
    url: server.url,
    getConnectionToken: async () => 'connection_token',
    reconnectBaseDelay: 0,
  })
  await connection.connect()
  const initial = connection
    .subscribe('orders', {
      authToken: () => (++tokenReads === 1 ? token : 'channel_token'),
    })
    .catch((error: unknown) => error)
  const concurrent = connection.subscribe('orders').catch((error: unknown) => error)
  server.drop()
  const deadline = Date.now() + 2000
  while (!server.frames.some(frame => frame.type === 'subscribe')) {
    if (Date.now() > deadline) throw new Error('The channel was not restored')
    await new Promise(resolve => setTimeout(resolve, 5))
  }
  const restored = await connection.subscribe('orders')
  releaseToken?.('old_channel_token')
  expect(await initial).toBe(restored)
  expect(await concurrent).toBe(restored)
  await restored.publish('created', {})
  expect(server.frames.filter(frame => frame.type === 'subscribe')).toHaveLength(1)
  expect(server.frames.filter(frame => frame.type === 'publish')).toHaveLength(1)
})
