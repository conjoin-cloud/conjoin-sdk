import type { BroadcastFrame } from './broadcast-requests'
import type { BroadcastEvent } from './types'

const RATE_WINDOW_MS = 1_000
const SEEN_EVENT_IDS_PER_CHANNEL = 1_000

export const isBroadcastFrame = (value: unknown): value is BroadcastFrame =>
  Boolean(value) && typeof value === 'object' && !Array.isArray(value)

export const parseBroadcastFrame = (raw: unknown): BroadcastFrame | null => {
  if (typeof raw !== 'string') return null

  try {
    const parsed: unknown = JSON.parse(raw)

    return isBroadcastFrame(parsed) ? parsed : null
  } catch {
    return null
  }
}

export const readBroadcastEvent = (value: unknown): BroadcastEvent | null => {
  if (!isBroadcastFrame(value)) return null

  const { event_id, channel_id, event_type, published_at, publisher_id } = value

  if (typeof event_id !== 'string' || typeof channel_id !== 'string' || typeof event_type !== 'string') return null

  return {
    event_id,
    channel_id,
    event_type,
    data: value.data,
    published_at: typeof published_at === 'string' ? published_at : '',
    publisher_id: typeof publisher_id === 'string' ? publisher_id : '',
  }
}

export const readFrameString = (frame: BroadcastFrame, key: string): string | null => {
  const value = frame[key]

  return typeof value === 'string' ? value : null
}

export class SeenEventIds {
  #ids = new Set<string>()

  remember(eventId: string): boolean {
    if (this.#ids.has(eventId)) return false

    this.#ids.add(eventId)

    if (this.#ids.size > SEEN_EVENT_IDS_PER_CHANNEL) {
      const [oldest] = this.#ids
      if (oldest !== undefined) this.#ids.delete(oldest)
    }

    return true
  }
}

export class FramePacer {
  #sentAt: number[] = []
  #queue: Promise<void> = Promise.resolve()

  constructor(readonly framesPerSecond: number) {}

  send(write: () => void): Promise<void> {
    const sending = this.#queue.then(async () => {
      await this.#waitForRoom()
      this.#sentAt.push(Date.now())
      write()
    })

    this.#queue = sending.catch(() => undefined)

    return sending
  }

  async #waitForRoom(): Promise<void> {
    for (;;) {
      const now = Date.now()
      this.#sentAt = this.#sentAt.filter(sentAt => now - sentAt < RATE_WINDOW_MS)

      const [oldest] = this.#sentAt

      if (this.#sentAt.length < this.framesPerSecond || oldest === undefined) return

      await new Promise(resolve => setTimeout(resolve, RATE_WINDOW_MS - (now - oldest)))
    }
  }
}
