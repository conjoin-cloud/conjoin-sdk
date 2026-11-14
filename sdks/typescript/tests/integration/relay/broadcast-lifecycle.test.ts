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
  let subscription: BroadcastSubscription | undefined
  let unsubscribing: Promise<void> | undefined
  let connected = 0
  connection = createBroadcastConnection(client, {
    url: server.url,
    getConnectionToken: async () => 'connection_token',
    reconnectBaseDelay: 0,
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
})
