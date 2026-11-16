import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadEventChannelsData = NonNullable<operations['readEventChannels']['responses']['200']['content']['application/json']['data']>[number]
type ReadEventChannelsQuery = NonNullable<operations['readEventChannels']['parameters']['query']>
type CreateEventChannelBody = NonNullable<operations['createEventChannel']['requestBody']>['content']['application/json']
type CreateEventChannelData = NonNullable<operations['createEventChannel']['responses']['201']['content']['application/json']['data']>
type ReadEventSubscriptionsData = NonNullable<operations['readEventSubscriptions']['responses']['200']['content']['application/json']['data']>[number]
type ReadEventSubscriptionsQuery = NonNullable<operations['readEventSubscriptions']['parameters']['query']>
type CreateEventSubscriptionBody = NonNullable<operations['createEventSubscription']['requestBody']>['content']['application/json']
type CreateEventSubscriptionData = NonNullable<operations['createEventSubscription']['responses']['201']['content']['application/json']['data']>
type ReadData = NonNullable<operations['readEvents']['responses']['200']['content']['application/json']['data']>[number]
type ReadQuery = NonNullable<operations['readEvents']['parameters']['query']>
type ReadEventChannelsCountData = NonNullable<operations['readEventChannelsCount']['responses']['200']['content']['application/json']['data']>
type ReadEventChannelsCountQuery = NonNullable<operations['readEventChannelsCount']['parameters']['query']>
type UpdateEventChannelBody = NonNullable<operations['updateEventChannel']['requestBody']>['content']['application/json']
type UpdateEventChannelData = NonNullable<operations['updateEventChannel']['responses']['200']['content']['application/json']['data']>
type DeleteEventChannelData = NonNullable<operations['deleteEventChannel']['responses']['200']['content']['application/json']['data']>
type ReadEventSubscriptionsCountData = NonNullable<operations['readEventSubscriptionsCount']['responses']['200']['content']['application/json']['data']>
type ReadEventSubscriptionsCountQuery = NonNullable<operations['readEventSubscriptionsCount']['parameters']['query']>
type UpdateEventSubscriptionBody = NonNullable<operations['updateEventSubscription']['requestBody']>['content']['application/json']
type UpdateEventSubscriptionData = NonNullable<operations['updateEventSubscription']['responses']['200']['content']['application/json']['data']>
type DeleteEventSubscriptionResponse = operations['deleteEventSubscription']['responses']['200']['content']['application/json']
type PauseEventSubscriptionData = NonNullable<operations['pauseEventSubscription']['responses']['200']['content']['application/json']['data']>
type ResumeEventSubscriptionData = NonNullable<operations['resumeEventSubscription']['responses']['200']['content']['application/json']['data']>
type PublishEventBody = NonNullable<operations['publishEvent']['requestBody']>['content']['application/json']
type PublishEventData = NonNullable<operations['publishEvent']['responses']['201']['content']['application/json']['data']>
type ReadCountData = NonNullable<operations['readEventsCount']['responses']['200']['content']['application/json']['data']>
type ReadCountQuery = NonNullable<operations['readEventsCount']['parameters']['query']>
type ReplayBody = NonNullable<operations['replayEvents']['requestBody']>['content']['application/json']
type ReplayResponse = operations['replayEvents']['responses']['200']['content']['application/json']

export function createRelayEvents(client: ConjoinClient) {
  return {
    readEventChannels: (query?: ReadEventChannelsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadEventChannelsData>('relay/event-channels/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createEventChannel: (data: CreateEventChannelBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateEventChannelData>('relay/event-channels/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readEventSubscriptions: (eventChannelId: string, query?: ReadEventSubscriptionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadEventSubscriptionsData>(`relay/event-channels/${encodePathParam(eventChannelId)}/subscriptions`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createEventSubscription: (eventChannelId: string, data: CreateEventSubscriptionBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateEventSubscriptionData>(`relay/event-channels/${encodePathParam(eventChannelId)}/subscriptions`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    read: (eventChannelId: string, query?: ReadQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadData>(`relay/event-channels/${encodePathParam(eventChannelId)}/events`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readEventChannelsCount: (query?: ReadEventChannelsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadEventChannelsCountData>('relay/event-channels/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    updateEventChannel: (eventChannelId: string, data: UpdateEventChannelBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateEventChannelData>(`relay/event-channels/${encodePathParam(eventChannelId)}`, { ...options, method: 'PATCH', body: data }),

    deleteEventChannel: (eventChannelId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteEventChannelData>(`relay/event-channels/${encodePathParam(eventChannelId)}`, { ...options, method: 'DELETE' }),

    readEventSubscriptionsCount: (eventChannelId: string, query?: ReadEventSubscriptionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadEventSubscriptionsCountData>(`relay/event-channels/${encodePathParam(eventChannelId)}/subscriptions/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    updateEventSubscription: (eventChannelId: string, subscriptionId: string, data: UpdateEventSubscriptionBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateEventSubscriptionData>(`relay/event-channels/${encodePathParam(eventChannelId)}/subscriptions/${encodePathParam(subscriptionId)}`, { ...options, method: 'PATCH', body: data }),

    deleteEventSubscription: (eventChannelId: string, subscriptionId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<DeleteEventSubscriptionResponse>(`relay/event-channels/${encodePathParam(eventChannelId)}/subscriptions/${encodePathParam(subscriptionId)}`, { ...options, method: 'DELETE' }),

    pauseEventSubscription: (eventChannelId: string, subscriptionId: string, options?: ConjoinCallOptions) =>
      client.fetch<PauseEventSubscriptionData>(`relay/event-channels/${encodePathParam(eventChannelId)}/subscriptions/${encodePathParam(subscriptionId)}/pause`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    resumeEventSubscription: (eventChannelId: string, subscriptionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ResumeEventSubscriptionData>(`relay/event-channels/${encodePathParam(eventChannelId)}/subscriptions/${encodePathParam(subscriptionId)}/resume`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    publishEvent: (eventChannelId: string, data: PublishEventBody, options?: ConjoinCallOptions) =>
      client.fetch<PublishEventData>(`relay/event-channels/${encodePathParam(eventChannelId)}/publish`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readCount: (eventChannelId: string, query?: ReadCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadCountData>(`relay/event-channels/${encodePathParam(eventChannelId)}/events/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    replay: (eventChannelId: string, data: ReplayBody, options?: ConjoinCallOptions) =>
      client.fetchJson<ReplayResponse>(`relay/event-channels/${encodePathParam(eventChannelId)}/replay`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),
  }
}
