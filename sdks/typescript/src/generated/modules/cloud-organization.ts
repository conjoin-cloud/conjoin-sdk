import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['readCloudOrganizations']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['readCloudOrganizations']['parameters']['query']>
type CreateBody = NonNullable<operations['createCloudOrganization']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCloudOrganization']['responses']['201']['content']['application/json']['data']>
type ReadCountData = NonNullable<operations['readCloudOrganizationsCount']['responses']['200']['content']['application/json']['data']>
type ReadCountQuery = NonNullable<operations['readCloudOrganizationsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readCloudOrganization']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateCloudOrganization']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCloudOrganization']['responses']['200']['content']['application/json']['data']>

export function createCloudOrganizations(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('cloud/organizations/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('cloud/organizations/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readCount: (query?: ReadCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadCountData>('cloud/organizations/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (organizationId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`cloud/organizations/${encodePathParam(organizationId)}`, { ...options, method: 'GET' }),

    update: (organizationId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`cloud/organizations/${encodePathParam(organizationId)}`, { ...options, method: 'PATCH', body: data }),
  }
}
