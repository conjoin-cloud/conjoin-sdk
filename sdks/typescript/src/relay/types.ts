export type ConnectionState = 'idle' | 'connecting' | 'connected' | 'disconnected' | 'reconnecting'

export type BroadcastEvent<T = unknown> = {
  event_id: string
  channel_id: string
  event_type: string
  data: T
  published_at: string
  publisher_id: string
}

export type BroadcastListener<T = unknown> = (event: BroadcastEvent<T>) => void

export type BroadcastTokenSource = string | (() => string | Promise<string>)

export type BroadcastWebSocketConstructor = new (url: string) => WebSocket

export type BroadcastConnectionOptions = {
  url?: string
  getConnectionToken?: () => Promise<string>
  autoReconnect?: boolean
  maxReconnectAttempts?: number
  reconnectBaseDelay?: number
  reconnectMaxDelay?: number
  requestTimeout?: number
  WebSocket?: BroadcastWebSocketConstructor
  onStateChange?: (state: ConnectionState) => void
  onError?: (error: Error) => void
}

export type BroadcastSubscribeOptions = {
  authToken?: BroadcastTokenSource
}

export type BroadcastHistory = {
  events: BroadcastEvent[]
  truncated: boolean
}

export type BroadcastPublishResult = {
  eventId: string
}

export type BroadcastSubscription = {
  readonly channel: string
  on: <T = unknown>(eventType: string, listener: BroadcastListener<T>) => () => void
  onAny: <T = unknown>(listener: BroadcastListener<T>) => () => void
  publish: (eventType: string, data: unknown) => Promise<BroadcastPublishResult>
  history: (options?: { lastEventId?: string }) => Promise<BroadcastHistory>
  unsubscribe: () => Promise<void>
}

export type BroadcastConnection = {
  readonly state: ConnectionState
  readonly socketId: number | null
  connect: () => Promise<void>
  disconnect: () => void
  subscribe: (channel: string, options?: BroadcastSubscribeOptions) => Promise<BroadcastSubscription>
}
