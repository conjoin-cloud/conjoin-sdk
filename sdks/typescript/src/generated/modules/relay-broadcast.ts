import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type GenerateConnectionTokenData = NonNullable<operations['generateBroadcastConnectionToken']['responses']['201']['content']['application/json']['data']>
type ReadChannelsData = NonNullable<operations['readBroadcastChannels']['responses']['200']['content']['application/json']['data']>[number]
type ReadChannelsQuery = NonNullable<operations['readBroadcastChannels']['parameters']['query']>
type CreateChannelBody = NonNullable<operations['createBroadcastChannel']['requestBody']>['content']['application/json']
type CreateChannelData = NonNullable<operations['createBroadcastChannel']['responses']['201']['content']['application/json']['data']>
type ReadChannelsCountData = NonNullable<operations['readBroadcastChannelsCount']['responses']['200']['content']['application/json']['data']>
type ReadChannelsCountQuery = NonNullable<operations['readBroadcastChannelsCount']['parameters']['query']>
type UpdateChannelBody = NonNullable<operations['updateBroadcastChannel']['requestBody']>['content']['application/json']
type UpdateChannelData = NonNullable<operations['updateBroadcastChannel']['responses']['200']['content']['application/json']['data']>
type DeleteChannelData = NonNullable<operations['deleteBroadcastChannel']['responses']['200']['content']['application/json']['data']>
type GenerateAuthTokenBody = NonNullable<operations['generateBroadcastAuthToken']['requestBody']>['content']['application/json']
type GenerateAuthTokenData = NonNullable<operations['generateBroadcastAuthToken']['responses']['201']['content']['application/json']['data']>
type PublishToBody = NonNullable<operations['publishToBroadcast']['requestBody']>['content']['application/json']
type PublishToData = NonNullable<operations['publishToBroadcast']['responses']['200']['content']['application/json']['data']>
type ReadPresenceData = NonNullable<operations['readBroadcastPresence']['responses']['200']['content']['application/json']['data']>

export function createRelayBroadcasts(client: ConjoinClient) {
  return {
    generateConnectionToken: (options?: ConjoinCallOptions) =>
      client.fetch<GenerateConnectionTokenData>('relay/broadcast-connection-tokens/', { ...options, method: 'POST' }),

    readChannels: (query?: ReadChannelsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadChannelsData>('relay/broadcast-channels/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createChannel: (data: CreateChannelBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateChannelData>('relay/broadcast-channels/', { ...options, method: 'POST', body: data }),

    readChannelsCount: (query?: ReadChannelsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadChannelsCountData>('relay/broadcast-channels/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    updateChannel: (broadcastChannelId: string, data: UpdateChannelBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateChannelData>(`relay/broadcast-channels/${encodePathParam(broadcastChannelId)}`, { ...options, method: 'PATCH', body: data }),

    deleteChannel: (broadcastChannelId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteChannelData>(`relay/broadcast-channels/${encodePathParam(broadcastChannelId)}`, { ...options, method: 'DELETE' }),

    generateAuthToken: (broadcastChannelId: string, data: GenerateAuthTokenBody, options?: ConjoinCallOptions) =>
      client.fetch<GenerateAuthTokenData>(`relay/broadcast-channels/${encodePathParam(broadcastChannelId)}/auth-tokens`, { ...options, method: 'POST', body: data }),

    publishTo: (broadcastChannelId: string, data: PublishToBody, options?: ConjoinCallOptions) =>
      client.fetch<PublishToData>(`relay/broadcast-channels/${encodePathParam(broadcastChannelId)}/publish`, { ...options, method: 'POST', body: data }),

    readPresence: (broadcastChannelId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadPresenceData>(`relay/broadcast-channels/${encodePathParam(broadcastChannelId)}/presence-members`, { ...options, method: 'GET' }),
  }
}
