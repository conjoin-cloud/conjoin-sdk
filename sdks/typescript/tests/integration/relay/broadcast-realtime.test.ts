import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest'
import { createConjoinClient } from '../../../src/core/client'
import { ConjoinNetworkError } from '../../../src/core/errors'
import type { BroadcastConnection, BroadcastConnectionOptions, BroadcastEvent } from '../../../src/relay'
import { ConjoinBroadcastError, createBroadcastConnection } from '../../../src/relay'
import { type RealtimeApp, startRealtimeApp } from './realtime-app'

const monorepoDirectory = process.env.CONJOIN_MONOREPO_DIR
const WAIT_TIMEOUT_MS = 5_000
const WAIT_POLL_MS = 20
const QUIET_PERIOD_MS = 500

class DroppableWebSocket extends WebSocket {
  static opened: DroppableWebSocket[] = []

  constructor(url: string) {
    super(url)
    DroppableWebSocket.opened.push(this)
  }
}

const waitFor = async (condition: () => boolean, description: string): Promise<void> => {
  const startedAt = Date.now()

  while (!condition()) {
    if (Date.now() - startedAt > WAIT_TIMEOUT_MS) throw new Error(`Timed out waiting for ${description}`)
    await new Promise(resolve => setTimeout(resolve, WAIT_POLL_MS))
  }
}

const brokenConnectionError = async (promise: Promise<unknown>): Promise<unknown> =>
  promise.then(
    () => undefined,
    (error: unknown) => error,
  )

describe.skipIf(monorepoDirectory === undefined)('broadcast client against the realtime app', () => {
  let app: RealtimeApp
  const connections: BroadcastConnection[] = []

  const connect = async (token: string, options: BroadcastConnectionOptions = {}): Promise<BroadcastConnection> => {
    const client = createConjoinClient({ apiKey: 'cak_live_storefront', baseUrl: `http://127.0.0.1:${app.port}` })
    const connection = createBroadcastConnection(client, { getConnectionToken: async () => token, ...options })
    connections.push(connection)
    await connection.connect()

    return connection
  }

  beforeAll(
    async () => {
      if (monorepoDirectory === undefined) return
      app = await startRealtimeApp(monorepoDirectory)
    },
    11 * 60 * 1000,
  )

  afterEach(() => {
    for (const connection of connections.splice(0)) connection.disconnect()
  })

  afterAll(
    async () => {
      await app?.stop()
    },
    3 * 60 * 1000,
  )

  it('delivers a published event to the other subscribers and to nobody in another project', async () => {
    const publisher = await connect(app.tokens.storefrontConnection)
    const reader = await connect(app.tokens.storefrontConnection)
    const outsider = await connect(app.tokens.otherTenantConnection)

    const publishing = await publisher.subscribe(app.channel, { authToken: app.tokens.orderPublisher })
    const reading = await reader.subscribe(app.channel, { authToken: async () => app.tokens.orderReader })
    const outsiderError = await brokenConnectionError(
      outsider.subscribe(app.channel, { authToken: app.tokens.otherTenantOrderReader }),
    )

    expect(outsiderError).toBeInstanceOf(ConjoinBroadcastError)
    expect(outsiderError).toMatchObject({ code: 'channel_not_found', channel: app.channel })
    expect(publisher.socketId).not.toBeNull()

    const received: BroadcastEvent[] = []
    const ignored: BroadcastEvent[] = []
    reading.on('order.shipped', event => received.push(event))
    reading.on('order.cancelled', event => ignored.push(event))

    const { eventId } = await publishing.publish('order.shipped', { order_id: 'ord_7731', carrier: 'parcel' })

    await waitFor(() => received.length === 1, 'the reader to receive the event')
    expect(received[0]).toMatchObject({
      event_id: eventId,
      channel_id: app.channel,
      event_type: 'order.shipped',
      data: { order_id: 'ord_7731', carrier: 'parcel' },
    })
    expect(ignored).toEqual([])

    const history = await reading.history()
    expect(history.events.map(event => event.event_id)).toContain(eventId)
  })

  it('stops delivering events to a subscriber after it unsubscribes', async () => {
    const publisher = await connect(app.tokens.storefrontConnection)
    const leaver = await connect(app.tokens.storefrontConnection)
    const witness = await connect(app.tokens.storefrontConnection)

    const publishing = await publisher.subscribe(app.channel, { authToken: app.tokens.orderPublisher })
    const leaving = await leaver.subscribe(app.channel, { authToken: app.tokens.orderReader })
    const watching = await witness.subscribe(app.channel, { authToken: app.tokens.orderReader })
    const leaverEvents: BroadcastEvent[] = []
    const witnessEvents: BroadcastEvent[] = []
    leaving.onAny(event => leaverEvents.push(event))
    watching.onAny(event => witnessEvents.push(event))

    await leaving.unsubscribe()
    await publishing.publish('order.cancelled', { order_id: 'ord_7732' })

    await waitFor(() => witnessEvents.length === 1, 'the witness to receive the event')
    await new Promise(resolve => setTimeout(resolve, QUIET_PERIOD_MS))
    expect(leaverEvents).toEqual([])
    await expect(leaving.publish('order.cancelled', {})).rejects.toMatchObject({ code: 'not_subscribed' })
  })

  it('refuses a private channel without a channel token and a publish without permission', async () => {
    const reader = await connect(app.tokens.storefrontConnection)

    await expect(reader.subscribe(app.channel)).rejects.toMatchObject({
      code: 'authorization_failed',
      channel: app.channel,
    })

    const reading = await reader.subscribe(app.channel, { authToken: app.tokens.orderReader })

    await expect(reading.publish('order.shipped', { order_id: 'ord_7733' })).rejects.toMatchObject({
      code: 'permission_denied',
      channel: app.channel,
    })
  })

  it('refuses a connection with a bad token or a token for test mode', async () => {
    await expect(connect('not-a-broadcast-token')).rejects.toBeInstanceOf(ConjoinNetworkError)
    await expect(connect(app.tokens.storefrontTestModeConnection)).rejects.toBeInstanceOf(ConjoinNetworkError)
  })

  it('replays the events published while the connection was down, each once and in order', async () => {
    const publisher = await connect(app.tokens.storefrontConnection)
    const reader = await connect(app.tokens.storefrontConnection, {
      WebSocket: DroppableWebSocket,
      reconnectBaseDelay: 300,
      reconnectMaxDelay: 300,
    })
    const publishing = await publisher.subscribe(app.channel, { authToken: app.tokens.orderPublisher })
    const reading = await reader.subscribe(app.channel, { authToken: app.tokens.orderReader })
    const received: string[] = []
    reading.onAny(event => received.push(event.event_id))

    const first = await publishing.publish('order.shipped', { order_id: 'ord_7740' })
    await waitFor(() => received.length === 1, 'the first event')

    DroppableWebSocket.opened.at(-1)?.close()
    await waitFor(() => reader.state === 'reconnecting', 'the reader to notice the drop')

    const second = await publishing.publish('order.shipped', { order_id: 'ord_7741' })
    const third = await publishing.publish('order.shipped', { order_id: 'ord_7742' })

    await waitFor(() => received.length >= 3 && reader.state === 'connected', 'the missed events')
    await new Promise(resolve => setTimeout(resolve, QUIET_PERIOD_MS))
    expect(received).toEqual([first.eventId, second.eventId, third.eventId])
  })
})
