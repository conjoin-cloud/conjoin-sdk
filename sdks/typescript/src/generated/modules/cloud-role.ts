import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadData = NonNullable<operations['readCloudRoles']['responses']['200']['content']['application/json']['data']>[number]
type ReadQuery = NonNullable<operations['readCloudRoles']['parameters']['query']>
type CreateBody = NonNullable<operations['createCloudRole']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCloudRole']['responses']['201']['content']['application/json']['data']>
type ReadCountData = NonNullable<operations['readCloudRolesCount']['responses']['200']['content']['application/json']['data']>
type ReadCountQuery = NonNullable<operations['readCloudRolesCount']['parameters']['query']>
type UpdateBody = NonNullable<operations['updateCloudRole']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCloudRole']['responses']['200']['content']['application/json']['data']>

export function createCloudRoles(client: ConjoinClient) {
  return {
    read: (query?: ReadQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadData>('cloud/roles/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('cloud/roles/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readCount: (query?: ReadCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadCountData>('cloud/roles/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    update: (roleId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`cloud/roles/${encodePathParam(roleId)}`, { ...options, method: 'PATCH', body: data }),
  }
}
