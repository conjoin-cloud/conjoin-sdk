import type { BroadcastRequest, ChannelState } from './broadcast'
import { readBroadcastEvent, readFrameString } from './broadcast-frames'
import { ConjoinBroadcastError } from './broadcast-requests'
import type { BroadcastEvent, BroadcastHistory, BroadcastListener, BroadcastSubscription } from './types'

export const readEvents = (value: unknown): BroadcastEvent[] =>
  Array.isArray(value) ? value.flatMap(item => readBroadcastEvent(item) ?? []) : []

type BroadcastChannelOptions = {
  channelState: ChannelState
  request: BroadcastRequest
  isActive: () => boolean
  isConnected: () => boolean
  forget: () => void
}

export function createBroadcastChannel({
  channelState,
  request,
  isActive,
  isConnected,
  forget,
}: BroadcastChannelOptions): BroadcastSubscription {
  const { channel } = channelState

  const assertActive = (): void => {
    if (!isActive()) {
      throw new ConjoinBroadcastError(`The client is not subscribed to ${channel}`, 'not_subscribed', channel)
    }
  }

  const addListener = (eventType: string | null, listener: BroadcastListener): (() => void) => {
    const entry = { eventType, listener }
    channelState.listeners.add(entry)

    return () => {
      channelState.listeners.delete(entry)
    }
  }

  return {
    channel,
    on: (eventType, listener) => addListener(eventType, listener as BroadcastListener),
    onAny: listener => addListener(null, listener as BroadcastListener),
    publish: async (eventType, data) => {
      assertActive()

      const reply = await request('publish', channel, { type: 'publish', channel, event_type: eventType, data })
      const eventId = readFrameString(reply, 'event_id')

      if (eventId === null) {
        throw new ConjoinBroadcastError(
          'The realtime server confirmed a publish without an event id',
          'invalid_reply',
          channel,
        )
      }

      return { eventId }
    },
    history: async (historyOptions = {}): Promise<BroadcastHistory> => {
      assertActive()

      const reply = await request('history', channel, {
        type: 'history',
        channel,
        ...(historyOptions.lastEventId === undefined ? {} : { last_event_id: historyOptions.lastEventId }),
      })

      return { events: readEvents(reply.events), truncated: reply.truncated === true }
    },
    unsubscribe: async () => {
      if (!isActive()) return

      forget()
      channelState.listeners.clear()

      if (isConnected()) await request('unsubscribe', channel, { type: 'unsubscribe', channel })
    },
  }
}
