import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listMessagingProfiles']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listMessagingProfiles']['parameters']['query']>
type CreateBody = NonNullable<operations['createMessagingProfile']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createMessagingProfile']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listMessagingProfilesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listMessagingProfilesCount']['parameters']['query']>
type EnableData = NonNullable<operations['enableMessagingProfile']['responses']['200']['content']['application/json']['data']>
type DisableData = NonNullable<operations['disableMessagingProfile']['responses']['200']['content']['application/json']['data']>
type EnableChannelsBody = NonNullable<operations['enableMessagingProfileChannels']['requestBody']>['content']['application/json']
type EnableChannelsData = NonNullable<operations['enableMessagingProfileChannels']['responses']['200']['content']['application/json']['data']>
type DisableChannelsBody = NonNullable<operations['disableMessagingProfileChannels']['requestBody']>['content']['application/json']
type DisableChannelsData = NonNullable<operations['disableMessagingProfileChannels']['responses']['200']['content']['application/json']['data']>
type CloseData = NonNullable<operations['closeMessagingProfile']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateMessagingProfile']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateMessagingProfile']['responses']['200']['content']['application/json']['data']>
type ReadData = NonNullable<operations['readMessagingProfile']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteMessagingProfile']['responses']['200']['content']['application/json']['data']>

export function createMessagingProfiles(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/profiles/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/profiles/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('messaging/profiles/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    enable: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<EnableData>(`messaging/profiles/${encodePathParam(profileId)}/enable`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    disable: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<DisableData>(`messaging/profiles/${encodePathParam(profileId)}/disable`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    enableChannels: (profileId: string, data: EnableChannelsBody, options?: ConjoinCallOptions) =>
      client.fetch<EnableChannelsData>(`messaging/profiles/${encodePathParam(profileId)}/enable-channels`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    disableChannels: (profileId: string, data: DisableChannelsBody, options?: ConjoinCallOptions) =>
      client.fetch<DisableChannelsData>(`messaging/profiles/${encodePathParam(profileId)}/disable-channels`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    close: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<CloseData>(`messaging/profiles/${encodePathParam(profileId)}/close`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    update: (profileId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`messaging/profiles/${encodePathParam(profileId)}`, { ...options, method: 'PATCH', body: data }),

    read: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`messaging/profiles/${encodePathParam(profileId)}`, { ...options, method: 'GET' }),

    delete: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/profiles/${encodePathParam(profileId)}`, { ...options, method: 'DELETE' }),
  }
}
