import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listEntitlementFeatures']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listEntitlementFeatures']['parameters']['query']>
type CreateBody = NonNullable<operations['createEntitlementFeature']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createEntitlementFeature']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listEntitlementFeaturesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listEntitlementFeaturesCount']['parameters']['query']>
type ReadData = NonNullable<operations['readEntitlementFeature']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateEntitlementFeature']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateEntitlementFeature']['responses']['200']['content']['application/json']['data']>
type ArchiveData = NonNullable<operations['archiveEntitlementFeature']['responses']['200']['content']['application/json']['data']>

export function createBillingEntitlementFeatures(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/entitlement-features/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/entitlement-features/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/entitlement-features/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (entitlementFeatureId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/entitlement-features/${encodePathParam(entitlementFeatureId)}`, { ...options, method: 'GET' }),

    update: (entitlementFeatureId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/entitlement-features/${encodePathParam(entitlementFeatureId)}`, { ...options, method: 'PATCH', body: data }),

    archive: (entitlementFeatureId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`billing/entitlement-features/${encodePathParam(entitlementFeatureId)}/archive`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),
  }
}
