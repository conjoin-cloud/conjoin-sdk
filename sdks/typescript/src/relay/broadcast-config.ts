import { ConjoinConfigurationError } from '../core/errors'
import type { ConjoinClient } from '../core/types'
import { createRelayBroadcasts } from '../generated/modules/relay-broadcast'
import type { BroadcastFrame } from './broadcast-requests'
import type { BroadcastConnectionOptions, BroadcastTokenSource } from './types'

const BROADCAST_PATH = '/v1/relay/broadcast'
const DEFAULT_MAX_RECONNECT_ATTEMPTS = 10
const DEFAULT_RECONNECT_BASE_DELAY_MS = 1_000
const DEFAULT_RECONNECT_MAX_DELAY_MS = 30_000
const DEFAULT_REQUEST_TIMEOUT_MS = 10_000
const MAX_FRAME_BYTES = 64 * 1024

const BROADCAST_URL_PATTERN = /^wss?:\/\/[^\s/?#]+(\/[^\s?#]*)?$/i

function resolveBroadcastUrl(client: ConjoinClient, options: BroadcastConnectionOptions): string {
  const raw = options.url ?? `${client.config.baseUrl.replace(/^http/, 'ws')}${BROADCAST_PATH}`

  if (!BROADCAST_URL_PATTERN.test(raw)) {
    throw new ConjoinConfigurationError('The broadcast url must be an absolute ws or wss URL without a query')
  }

  return raw
}

export async function readToken(source: BroadcastTokenSource | undefined): Promise<string | undefined> {
  if (source === undefined) return undefined

  const token = typeof source === 'string' ? source : await source()

  if (typeof token !== 'string' || token.length === 0) {
    throw new ConjoinConfigurationError('A broadcast token must be a non-empty string')
  }

  return token
}

export function encodeFrame(frame: BroadcastFrame): string {
  let text: string

  try {
    text = JSON.stringify(frame)
  } catch {
    throw new ConjoinConfigurationError('The broadcast data cannot be sent as JSON')
  }

  if (new TextEncoder().encode(text).byteLength > MAX_FRAME_BYTES) {
    throw new ConjoinConfigurationError(`A broadcast message must be ${MAX_FRAME_BYTES} bytes or fewer`)
  }

  return text
}

export function assertChannel(channel: string): void {
  if (typeof channel !== 'string' || channel.length === 0 || channel.trim() !== channel) {
    throw new ConjoinConfigurationError('A channel must be a non-empty string without surrounding spaces')
  }
}

export function resolveBroadcastConfig(client: ConjoinClient, options: BroadcastConnectionOptions) {
  const baseUrl = resolveBroadcastUrl(client, options)
  const WebSocketImpl = options.WebSocket ?? globalThis.WebSocket
  const maxAttempts = options.maxReconnectAttempts ?? DEFAULT_MAX_RECONNECT_ATTEMPTS
  const baseDelay = options.reconnectBaseDelay ?? DEFAULT_RECONNECT_BASE_DELAY_MS
  const maxDelay = options.reconnectMaxDelay ?? DEFAULT_RECONNECT_MAX_DELAY_MS
  const requestTimeout = options.requestTimeout ?? DEFAULT_REQUEST_TIMEOUT_MS
  const autoReconnect = options.autoReconnect !== false
  const getConnectionToken =
    options.getConnectionToken ?? (async () => (await createRelayBroadcasts(client).generateConnectionToken()).token)

  if (WebSocketImpl === undefined) {
    throw new ConjoinConfigurationError('This runtime has no WebSocket, so pass one in the WebSocket option')
  }

  for (const [name, value] of Object.entries({
    reconnectBaseDelay: baseDelay,
    reconnectMaxDelay: maxDelay,
    requestTimeout,
  })) {
    if (!Number.isFinite(value) || value < 0 || value > 2 ** 31 - 1 || (name === 'requestTimeout' && value === 0)) {
      throw new ConjoinConfigurationError(`${name} is outside the supported timer range`)
    }
  }
  if (!Number.isSafeInteger(maxAttempts) || maxAttempts < 0) {
    throw new ConjoinConfigurationError('maxReconnectAttempts must be a non-negative safe integer')
  }

  return { baseUrl, WebSocketImpl, maxAttempts, baseDelay, maxDelay, requestTimeout, autoReconnect, getConnectionToken }
}
