import { ConjoinError, ConjoinTimeoutError } from '../core/errors'

export type BroadcastFrame = Record<string, unknown>

export type BroadcastRequestKind = 'connect' | 'subscribe' | 'unsubscribe' | 'publish' | 'history'

type PendingRequest = {
  kind: BroadcastRequestKind
  channel: string | null
  resolve: (frame: BroadcastFrame) => void
  reject: (error: Error) => void
  timer: ReturnType<typeof setTimeout>
}

const KINDS_THAT_RAISE_ERROR_CODE: Readonly<Record<string, readonly BroadcastRequestKind[]>> = {
  CHANNEL_NOT_FOUND: ['subscribe'],
  AUTHORIZATION_FAILED: ['subscribe'],
  PERMISSION_DENIED: ['publish'],
  NOT_SUBSCRIBED: ['publish', 'history'],
}

export class ConjoinBroadcastError extends ConjoinError {
  readonly channel: string | null

  constructor(message: string, code: string, channel: string | null) {
    super(message, { code, param: channel === null ? null : 'channel' })
    this.name = 'ConjoinBroadcastError'
    this.channel = channel
  }
}

export const toBroadcastErrorCode = (serverCode: string): string => serverCode.toLowerCase()

export class BroadcastRequests {
  #pending: PendingRequest[] = []

  open(kind: BroadcastRequestKind, channel: string | null, timeoutMs: number): Promise<BroadcastFrame> {
    return new Promise((resolve, reject) => {
      const request: PendingRequest = {
        kind,
        channel,
        resolve,
        reject,
        timer: setTimeout(() => {
          this.#remove(request)
          reject(new ConjoinTimeoutError(`The realtime server did not answer the ${kind} within ${timeoutMs}ms`))
        }, timeoutMs),
      }

      this.#pending.push(request)
    })
  }

  settle(kind: BroadcastRequestKind, channel: string | null, frame: BroadcastFrame): boolean {
    const request = this.#pending.find(candidate => candidate.kind === kind && candidate.channel === channel)

    if (request === undefined) return false

    this.#remove(request)
    request.resolve(frame)

    return true
  }

  fail(serverCode: string, message: string, channel: string | null): boolean {
    const kinds = KINDS_THAT_RAISE_ERROR_CODE[serverCode]
    const request = this.#pending.find(
      candidate =>
        candidate.kind !== 'connect' &&
        candidate.channel === channel &&
        (kinds === undefined || kinds.includes(candidate.kind)),
    )

    if (request === undefined) return false

    this.#remove(request)
    request.reject(new ConjoinBroadcastError(message, toBroadcastErrorCode(serverCode), channel))

    return true
  }

  rejectAll(error: Error): void {
    const pending = this.#pending

    this.#pending = []

    for (const request of pending) {
      clearTimeout(request.timer)
      request.reject(error)
    }
  }

  #remove(request: PendingRequest): void {
    clearTimeout(request.timer)
    this.#pending = this.#pending.filter(candidate => candidate !== request)
  }
}
