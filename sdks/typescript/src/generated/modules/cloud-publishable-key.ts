import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listPublishableKeys']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPublishableKeys']['parameters']['query']>
type CreateData = NonNullable<operations['createPublishableKey']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listPublishableKeysCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPublishableKeysCount']['parameters']['query']>
type RotateData = NonNullable<operations['rotatePublishableKey']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updatePublishableKey']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updatePublishableKey']['responses']['200']['content']['application/json']['data']>
type RevokeData = NonNullable<operations['revokePublishableKey']['responses']['200']['content']['application/json']['data']>

export function createCloudPublishableKeys(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('cloud/publishable-keys/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('cloud/publishable-keys/', { ...options, method: 'POST' }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('cloud/publishable-keys/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    rotate: (publishableKeyId: string, options?: ConjoinCallOptions) =>
      client.fetch<RotateData>(`cloud/publishable-keys/${encodePathParam(publishableKeyId)}/rotate`, { ...options, method: 'POST' }),

    update: (publishableKeyId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`cloud/publishable-keys/${encodePathParam(publishableKeyId)}`, { ...options, method: 'PATCH', body: data }),

    revoke: (publishableKeyId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeData>(`cloud/publishable-keys/${encodePathParam(publishableKeyId)}`, { ...options, method: 'DELETE' }),
  }
}
