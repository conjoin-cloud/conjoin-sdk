import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ListEntitlementOverridesData = NonNullable<operations['listSelfEntitlementOverrides']['responses']['200']['content']['application/json']['data']>[number]
type ListEntitlementOverridesQuery = NonNullable<operations['listSelfEntitlementOverrides']['parameters']['query']>
type ListPriceBundlesData = NonNullable<operations['listSelfPriceBundles']['responses']['200']['content']['application/json']['data']>[number]
type ListPriceBundlesQuery = NonNullable<operations['listSelfPriceBundles']['parameters']['query']>
type ListEntitlementOverridesCountData = NonNullable<operations['listSelfEntitlementOverridesCount']['responses']['200']['content']['application/json']['data']>
type ListEntitlementOverridesCountQuery = NonNullable<operations['listSelfEntitlementOverridesCount']['parameters']['query']>
type ListPriceBundlesCountData = NonNullable<operations['listSelfPriceBundlesCount']['responses']['200']['content']['application/json']['data']>
type ListPriceBundlesCountQuery = NonNullable<operations['listSelfPriceBundlesCount']['parameters']['query']>

export function createBillingSelves(client: ConjoinClient) {
  return {
    listEntitlementOverrides: (query?: ListEntitlementOverridesQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetchList<ListEntitlementOverridesData>('billing/self/entitlement-overrides/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listPriceBundles: (query?: ListPriceBundlesQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetchList<ListPriceBundlesData>('billing/self/price-bundles/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listEntitlementOverridesCount: (query?: ListEntitlementOverridesCountQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ListEntitlementOverridesCountData>('billing/self/entitlement-overrides/count', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listPriceBundlesCount: (query?: ListPriceBundlesCountQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ListPriceBundlesCountData>('billing/self/price-bundles/count', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),
  }
}
