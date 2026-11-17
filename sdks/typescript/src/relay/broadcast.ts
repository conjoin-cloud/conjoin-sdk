import { ConjoinNetworkError } from '../core/errors'
import type { ConjoinClient } from '../core/types'
import { type ChannelEntry, type ChannelState, createBroadcastChannel, readEvents } from './broadcast-channel'
import { assertChannel, encodeFrame, readToken, resolveBroadcastConfig } from './broadcast-config'
import { FramePacer, parseBroadcastFrame, readBroadcastEvent, readFrameString, SeenEventIds } from './broadcast-frames'
import {
  type BroadcastRequest,
  BroadcastRequests,
  ConjoinBroadcastError,
  closedByCaller,
  notConnected,
  REPLY_KINDS,
  toBroadcastErrorCode,
} from './broadcast-requests'
import { openBroadcastSocket } from './broadcast-socket'
import type {
  BroadcastConnection,
  BroadcastConnectionOptions,
  BroadcastEvent,
  BroadcastSubscribeOptions,
  ConnectionState,
} from './types'

const FRAMES_PER_SECOND_BELOW_SERVER_LIMIT = 25
const MAX_HISTORY_PAGES_PER_RECOVERY = 20
const NORMAL_CLOSE_CODE = 1000
const SOCKET_OPEN = 1

export function createBroadcastConnection(
  client: ConjoinClient,
  options: BroadcastConnectionOptions = {},
): BroadcastConnection {
  const {
    baseUrl,
    WebSocketImpl,
    maxAttempts,
    baseDelay,
    maxDelay,
    requestTimeout,
    autoReconnect,
    getConnectionToken,
  } = resolveBroadcastConfig(client, options)

  const requests = new BroadcastRequests()
  const channels = new Map<string, ChannelEntry>()
  const lanes = new Map<string, Promise<unknown>>()
  let state: ConnectionState = 'idle'
  let socket: WebSocket | null = null
  let socketId: number | null = null
  let pacer = new FramePacer(FRAMES_PER_SECOND_BELOW_SERVER_LIMIT)
  let generation = 0
  let reconnectAttempt = 0
  let reconnectTimer: ReturnType<typeof setTimeout> | null = null
  let connecting: Promise<void> | null = null
  let closedOnPurpose = false
  let opening: AbortController | null = null

  const reportError = (error: unknown): void => {
    try {
      options.onError?.(error instanceof Error ? error : new Error(String(error)))
    } catch {}
  }

  const setState = (next: ConnectionState): void => {
    if (state === next) return
    state = next
    try {
      options.onStateChange?.(next)
    } catch (error) {
      reportError(error)
    }
  }

  const sendFrame: BroadcastRequest = (kind, channel, frame) => {
    const ws = socket

    if (ws === null || ws.readyState !== SOCKET_OPEN) return Promise.reject(notConnected())

    const text = encodeFrame(frame)
    const reply = requests.open(kind, channel, requestTimeout)

    pacer
      .send(() => {
        if (ws.readyState === SOCKET_OPEN) ws.send(text)
      })
      .catch(reportError)

    return reply
  }

  const request: BroadcastRequest = (kind, channel, frame) => {
    const attempt = generation
    const lane = `${kind === 'subscribe' || kind === 'unsubscribe' ? 'membership' : kind}:${channel ?? ''}`
    const previous = lanes.get(lane) ?? Promise.resolve()
    const reply = previous.then(() => {
      if (attempt !== generation || closedOnPurpose) throw closedByCaller()
      return sendFrame(kind, channel, frame)
    })
    const settled = reply.then(
      () => undefined,
      () => undefined,
    )

    lanes.set(lane, settled)
    settled.then(() => {
      if (lanes.get(lane) === settled) lanes.delete(lane)
    })

    return reply
  }

  const notify = (channelState: ChannelState, event: BroadcastEvent): void => {
    if (!channelState.seen.remember(event.event_id)) return

    channelState.lastEventId = event.event_id

    for (const entry of [...channelState.listeners]) {
      if (!isActive(channelState) || !channelState.listeners.has(entry)) continue
      if (entry.eventType !== null && entry.eventType !== event.event_type) continue

      try {
        entry.listener(event)
      } catch (error) {
        reportError(error)
      }
    }
  }

  const isActive = (channelState: ChannelState): boolean => channels.get(channelState.channel)?.state === channelState

  const handleFrame = (raw: unknown): void => {
    const frame = parseBroadcastFrame(raw)
    const type = frame === null ? null : readFrameString(frame, 'type')

    if (frame === null || type === null) return

    if (type === 'event') {
      const event = readBroadcastEvent(frame)
      const entry = event === null ? undefined : channels.get(event.channel_id)
      if (event !== null && entry !== undefined) notify(entry.state, event)
      return
    }

    const kind = REPLY_KINDS[type]
    const channel = readFrameString(frame, 'channel')

    if (kind !== undefined) {
      requests.settle(kind, kind === 'connect' ? null : channel, frame)
      return
    }

    if (type === 'error') {
      const code = readFrameString(frame, 'code') ?? 'UNKNOWN_ERROR'
      const message = readFrameString(frame, 'message') ?? 'The realtime server reported an error'

      if (!requests.fail(code, message, channel)) {
        reportError(new ConjoinBroadcastError(message, toBroadcastErrorCode(code), channel))
      }
    }
  }

  const abandonSocket = (): void => {
    generation += 1
    opening?.abort()
    opening = null
    const ws = socket
    socket = null
    socketId = null
    ws?.close(NORMAL_CLOSE_CODE)
  }

  const sendSubscribe = async (channelState: ChannelState): Promise<void> => {
    const attempt = generation
    const authToken = await readToken(channelState.authToken)
    if (attempt !== generation || !isActive(channelState)) throw closedByCaller()

    await request('subscribe', channelState.channel, {
      type: 'subscribe',
      channel: channelState.channel,
      ...(authToken === undefined ? {} : { auth_token: authToken }),
    })
  }

  const recoverMissedEvents = async (channelState: ChannelState): Promise<void> => {
    const attempt = generation
    let lastEventId = channelState.lastEventId

    for (let page = 0; lastEventId !== null && page < MAX_HISTORY_PAGES_PER_RECOVERY; page++) {
      if (attempt !== generation || !isActive(channelState)) return
      const reply = await request('history', channelState.channel, {
        type: 'history',
        channel: channelState.channel,
        last_event_id: lastEventId,
      })
      const events = readEvents(reply.events)

      for (const event of events) notify(channelState, event)

      const newest = events.at(-1)
      if (reply.truncated !== true || newest === undefined) return
      lastEventId = newest.event_id
    }
  }

  const restoreChannels = (attempt: number, entries: ChannelEntry[]): Promise<void> => {
    let previous = Promise.resolve()
    for (const entry of entries) {
      entry.ready = previous.then(async () => {
        if (attempt !== generation || !isActive(entry.state)) throw closedByCaller()
        await sendSubscribe(entry.state)
        await recoverMissedEvents(entry.state)
      })
      previous = entry.ready.catch(error => {
        if (attempt !== generation || socket === null || !isActive(entry.state)) return
        channels.delete(entry.state.channel)
        reportError(error)
      })
    }
    return previous
  }

  const scheduleReconnect = (): void => {
    if (reconnectTimer !== null || closedOnPurpose) return

    if (!autoReconnect || reconnectAttempt >= maxAttempts) {
      channels.clear()
      setState('disconnected')
      reportError(new ConjoinNetworkError('The broadcast connection closed and the client stopped reconnecting'))
      return
    }

    const attempt = generation
    setState('reconnecting')
    if (closedOnPurpose || attempt !== generation) return
    const delay = Math.random() * Math.min(baseDelay * 2 ** reconnectAttempt, maxDelay)
    reconnectAttempt += 1

    reconnectTimer = setTimeout(() => {
      reconnectTimer = null
      establish().catch(error => {
        if (closedOnPurpose) return
        reportError(error)
        abandonSocket()
        scheduleReconnect()
      })
    }, delay)
  }

  const handleClose = (): void => {
    const wasConnected = state === 'connected'

    socket = null
    socketId = null
    requests.rejectAll(new ConjoinNetworkError('The broadcast connection closed'))

    if (closedOnPurpose) {
      setState('disconnected')
      return
    }

    if (wasConnected) scheduleReconnect()
  }

  const establish = async (): Promise<void> => {
    const attempt = ++generation

    if (state !== 'reconnecting') setState('connecting')
    if (attempt !== generation || closedOnPurpose) throw closedByCaller()

    const controller = new AbortController()
    opening = controller
    const ws = await openBroadcastSocket(
      baseUrl,
      WebSocketImpl,
      () => readToken(getConnectionToken),
      requestTimeout,
      controller.signal,
    )
    if (opening === controller) opening = null

    if (attempt !== generation || closedOnPurpose) {
      ws.close(NORMAL_CLOSE_CODE)
      throw closedByCaller()
    }

    socket = ws
    pacer = new FramePacer(FRAMES_PER_SECOND_BELOW_SERVER_LIMIT)
    ws.addEventListener('message', event => {
      if (attempt === generation) handleFrame(event.data)
    })
    ws.addEventListener('close', () => {
      if (attempt === generation) handleClose()
    })

    const connected = await request('connect', null, { type: 'connect' })

    socketId = typeof connected.socket_id === 'number' ? connected.socket_id : null
    reconnectAttempt = 0
    const restoring = restoreChannels(attempt, [...channels.values()])
    setState('connected')
    await restoring
  }

  const waitForSubscription = async (entry: ChannelEntry) => {
    for (;;) {
      const ready = entry.ready
      try {
        await ready
      } catch (error) {
        if (entry.ready !== ready) continue
        if (isActive(entry.state)) channels.delete(entry.state.channel)
        throw error
      }
      if (entry.ready !== ready) continue
      if (!isActive(entry.state)) throw closedByCaller()
      return entry.subscription
    }
  }

  const subscribe = async (channel: string, subscribeOptions: BroadcastSubscribeOptions = {}) => {
    assertChannel(channel)

    const existing = channels.get(channel)
    if (existing !== undefined) return waitForSubscription(existing)

    if (state !== 'connected') throw notConnected()

    const channelState: ChannelState = {
      channel,
      authToken: subscribeOptions.authToken,
      listeners: new Set(),
      lastEventId: null,
      seen: new SeenEventIds(),
    }
    const entry: ChannelEntry = {
      state: channelState,
      ready: sendSubscribe(channelState),
      subscription: createBroadcastChannel({
        channelState,
        request,
        isActive: () => isActive(channelState),
        isConnected: () => state === 'connected',
        forget: () => {
          if (isActive(channelState)) channels.delete(channel)
        },
      }),
    }
    channels.set(channel, entry)
    return waitForSubscription(entry)
  }

  const connect = (): Promise<void> => {
    if (state === 'connected') return Promise.resolve()
    if (connecting !== null) return connecting

    closedOnPurpose = false
    reconnectAttempt = 0
    if (reconnectTimer !== null) clearTimeout(reconnectTimer)
    reconnectTimer = null

    const pending = Promise.resolve()
      .then(establish)
      .catch(error => {
        abandonSocket()
        if (!closedOnPurpose) setState('disconnected')
        throw error
      })
      .finally(() => {
        if (connecting === pending) connecting = null
      })
    connecting = pending

    return pending
  }

  const disconnect = (): void => {
    closedOnPurpose = true
    if (reconnectTimer !== null) clearTimeout(reconnectTimer)
    reconnectTimer = null
    channels.clear()
    requests.rejectAll(closedByCaller())
    abandonSocket()
    setState('disconnected')
  }

  return {
    get state() {
      return state
    },
    get socketId() {
      return socketId
    },
    connect,
    disconnect,
    subscribe,
  }
}
