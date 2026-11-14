import {
  type BroadcastConnection,
  type BroadcastEvent,
  type BroadcastPublishResult,
  type BroadcastSubscription,
  type BroadcastTokenSource,
  type ConnectionState,
  createBroadcastConnection,
} from '@conjoin-cloud/sdk/relay'
import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { useConjoinClient } from './internal/use-conjoin-client'

type UseChannelOptions = {
  channel: string
  getConnectionToken: () => string | Promise<string>
  authToken?: BroadcastTokenSource
  autoConnect?: boolean
  maxEvents?: number
}

const DEFAULT_MAX_EVENTS = 200
const BROADCAST_PATH = '/v1/relay/broadcast'

const RELAY_URL_PATTERN = /^(https?|wss?):\/\/([a-z0-9.-]+(?::[0-9]{1,5})?)(\/[^?#]*)?$/i
const SECURE_SCHEMES: ReadonlySet<string> = new Set(['https', 'wss'])
const SLASH_CHAR_CODE = 47

function resolveBroadcastUrl(relayUrl: string | undefined): string | undefined {
  const match = relayUrl ? RELAY_URL_PATTERN.exec(relayUrl.trim()) : null
  if (!match) return undefined

  const [, scheme = '', host = '', path = ''] = match
  const socketScheme = SECURE_SCHEMES.has(scheme.toLowerCase()) ? 'wss' : 'ws'

  return `${socketScheme}://${host}${withoutTrailingSlashes(path)}${BROADCAST_PATH}`
}

function withoutTrailingSlashes(value: string): string {
  let end = value.length

  while (end > 0 && value.charCodeAt(end - 1) === SLASH_CHAR_CODE) {
    end -= 1
  }

  return value.slice(0, end)
}

const notConnectedError = () => new Error('The channel is not connected yet')

export function useChannel({
  channel,
  getConnectionToken,
  authToken,
  autoConnect = true,
  maxEvents = DEFAULT_MAX_EVENTS,
}: UseChannelOptions) {
  const { client, sdkConfig } = useConjoinClient()
  const [status, setStatus] = useState<ConnectionState>('idle')
  const [error, setError] = useState<Error | null>(null)
  const [events, setEvents] = useState<BroadcastEvent[]>([])

  const subscriptionRef = useRef<BroadcastSubscription | null>(null)
  const connectionRef = useRef<BroadcastConnection | null>(null)
  const maxEventsRef = useRef(maxEvents)
  const tokenSourceRef = useRef(getConnectionToken)
  const authTokenRef = useRef(authToken)
  maxEventsRef.current = maxEvents
  tokenSourceRef.current = getConnectionToken
  authTokenRef.current = authToken

  const broadcastUrl = useMemo(() => resolveBroadcastUrl(sdkConfig?.relay.url), [sdkConfig?.relay.url])

  useEffect(() => {
    if (!autoConnect) return

    let isCurrent = true
    const connection = createBroadcastConnection(client, {
      url: broadcastUrl,
      getConnectionToken: async () => tokenSourceRef.current(),
      onStateChange: setStatus,
      onError: setError,
    })
    connectionRef.current = connection

    const subscribeToChannel = async () => {
      await connection.connect()
      const subscription = await connection.subscribe(channel, { authToken: authTokenRef.current })

      if (!isCurrent) {
        await subscription.unsubscribe()
        return
      }

      subscriptionRef.current = subscription
      setEvents([])
      subscription.onAny(event => {
        setEvents(previous => {
          const next = [...previous, event]
          return next.length > maxEventsRef.current ? next.slice(-maxEventsRef.current) : next
        })
      })
    }

    subscribeToChannel().catch((caught: unknown) => {
      if (isCurrent) setError(caught instanceof Error ? caught : new Error(String(caught)))
    })

    return () => {
      isCurrent = false
      subscriptionRef.current = null
      connectionRef.current = null
      connection.disconnect()
    }
  }, [client, channel, broadcastUrl, autoConnect])

  const publish = useCallback(async (eventType: string, data: unknown): Promise<BroadcastPublishResult> => {
    const subscription = subscriptionRef.current
    if (subscription === null) throw notConnectedError()

    return subscription.publish(eventType, data)
  }, [])

  const history = useCallback(async (lastEventId?: string) => {
    const subscription = subscriptionRef.current
    if (subscription === null) throw notConnectedError()

    return subscription.history({ lastEventId })
  }, [])

  const disconnect = useCallback(() => {
    subscriptionRef.current = null
    connectionRef.current?.disconnect()
  }, [])

  return useMemo(
    () => ({ status, error, events, publish, history, disconnect }),
    [status, error, events, publish, history, disconnect],
  )
}
