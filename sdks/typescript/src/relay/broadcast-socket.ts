import { ConjoinError, ConjoinNetworkError, ConjoinTimeoutError } from '../core/errors'
import type { BroadcastWebSocketConstructor } from './types'

export function openBroadcastSocket(
  baseUrl: string,
  WebSocketImpl: BroadcastWebSocketConstructor,
  getToken: () => Promise<string | undefined>,
  timeout: number,
  signal: AbortSignal,
): Promise<WebSocket> {
  return new Promise((resolve, reject) => {
    let ws: WebSocket | undefined
    let settled = false
    const cleanup = () => {
      clearTimeout(timer)
      signal.removeEventListener('abort', abort)
      ws?.removeEventListener('open', accept)
      ws?.removeEventListener('error', refuse)
      ws?.removeEventListener('close', refuse)
    }
    const fail = (error: unknown) => {
      if (settled) return
      settled = true
      cleanup()
      ws?.close()
      reject(error)
    }
    const abort = () =>
      fail(new ConjoinError('The caller closed the broadcast connection', { code: 'broadcast_disconnected' }))
    const refuse = () => fail(new ConjoinNetworkError('The realtime server refused the broadcast connection'))
    const accept = () => {
      if (settled || ws === undefined) return
      settled = true
      cleanup()
      resolve(ws)
    }
    const timer = setTimeout(() => fail(new ConjoinTimeoutError('The broadcast connection timed out')), timeout)
    signal.addEventListener('abort', abort, { once: true })
    if (signal.aborted) {
      abort()
      return
    }
    Promise.resolve()
      .then(getToken)
      .then(token => {
        if (settled) return
        ws = new WebSocketImpl(`${baseUrl}?token=${encodeURIComponent(token ?? '')}`)
        ws.addEventListener('open', accept, { once: true })
        ws.addEventListener('error', refuse, { once: true })
        ws.addEventListener('close', refuse, { once: true })
      })
      .catch(fail)
  })
}
