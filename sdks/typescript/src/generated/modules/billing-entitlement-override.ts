import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listEntitlementOverrides']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listEntitlementOverrides']['parameters']['query']>
type CreateBody = NonNullable<operations['createEntitlementOverride']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createEntitlementOverride']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listEntitlementOverridesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listEntitlementOverridesCount']['parameters']['query']>
type UpdateBody = NonNullable<operations['updateEntitlementOverride']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateEntitlementOverride']['responses']['200']['content']['application/json']['data']>
type DeleteResponse = operations['deleteEntitlementOverride']['responses']['200']['content']['application/json']

export function createBillingEntitlementOverrides(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/entitlement-overrides/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/entitlement-overrides/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/entitlement-overrides/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    update: (entitlementOverrideId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/entitlement-overrides/${encodePathParam(entitlementOverrideId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    delete: (entitlementOverrideId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<DeleteResponse>(`billing/entitlement-overrides/${encodePathParam(entitlementOverrideId)}`, { ...options, method: 'DELETE', scopes: ['billingEntityId'] }),
  }
}
