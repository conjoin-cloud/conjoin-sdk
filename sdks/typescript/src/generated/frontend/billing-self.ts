import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ListPaymentMethodsData = NonNullable<operations['listSelfPaymentMethods']['responses']['200']['content']['application/json']['data']>[number]
type ListPaymentMethodsQuery = NonNullable<operations['listSelfPaymentMethods']['parameters']['query']>
type CreatePaymentMethodBody = NonNullable<operations['createSelfPaymentMethod']['requestBody']>['content']['application/json']
type CreatePaymentMethodData = NonNullable<operations['createSelfPaymentMethod']['responses']['201']['content']['application/json']['data']>
type ListPaymentMethodsCountData = NonNullable<operations['listSelfPaymentMethodsCount']['responses']['200']['content']['application/json']['data']>
type ListPaymentMethodsCountQuery = NonNullable<operations['listSelfPaymentMethodsCount']['parameters']['query']>
type ListEntitlementOverridesData = NonNullable<operations['listSelfEntitlementOverrides']['responses']['200']['content']['application/json']['data']>[number]
type ListEntitlementOverridesQuery = NonNullable<operations['listSelfEntitlementOverrides']['parameters']['query']>
type ListPriceBundlesData = NonNullable<operations['listSelfPriceBundles']['responses']['200']['content']['application/json']['data']>[number]
type ListPriceBundlesQuery = NonNullable<operations['listSelfPriceBundles']['parameters']['query']>
type ListEntitlementOverridesCountData = NonNullable<operations['listSelfEntitlementOverridesCount']['responses']['200']['content']['application/json']['data']>
type ListEntitlementOverridesCountQuery = NonNullable<operations['listSelfEntitlementOverridesCount']['parameters']['query']>
type ListPriceBundlesCountData = NonNullable<operations['listSelfPriceBundlesCount']['responses']['200']['content']['application/json']['data']>
type ListPriceBundlesCountQuery = NonNullable<operations['listSelfPriceBundlesCount']['parameters']['query']>
type ActivatePriceBundlesBody = NonNullable<operations['activateSelfPriceBundles']['requestBody']>['content']['application/json']
type ActivatePriceBundlesData = NonNullable<operations['activateSelfPriceBundles']['responses']['201']['content']['application/json']['data']>
type DeactivatePriceBundleBody = NonNullable<operations['deactivateSelfPriceBundle']['requestBody']>['content']['application/json']
type DeactivatePriceBundleData = NonNullable<operations['deactivateSelfPriceBundle']['responses']['200']['content']['application/json']['data']>

export function createBillingSelves(client: ConjoinClient) {
  return {
    listPaymentMethods: (query?: ListPaymentMethodsQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetchList<ListPaymentMethodsData>('billing/self/payment-methods/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    createPaymentMethod: (data: CreatePaymentMethodBody, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<CreatePaymentMethodData>('billing/self/payment-methods/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listPaymentMethodsCount: (query?: ListPaymentMethodsCountQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ListPaymentMethodsCountData>('billing/self/payment-methods/count', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listEntitlementOverrides: (query?: ListEntitlementOverridesQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetchList<ListEntitlementOverridesData>('billing/self/entitlement-overrides/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listPriceBundles: (query?: ListPriceBundlesQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetchList<ListPriceBundlesData>('billing/self/price-bundles/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listEntitlementOverridesCount: (query?: ListEntitlementOverridesCountQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ListEntitlementOverridesCountData>('billing/self/entitlement-overrides/count', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listPriceBundlesCount: (query?: ListPriceBundlesCountQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ListPriceBundlesCountData>('billing/self/price-bundles/count', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    activatePriceBundles: (data: ActivatePriceBundlesBody, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ActivatePriceBundlesData>('billing/self/price-bundle-activations/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    deactivatePriceBundle: (priceBundleActivationId: string, data: DeactivatePriceBundleBody, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<DeactivatePriceBundleData>(`billing/self/price-bundle-activations/${encodePathParam(priceBundleActivationId)}/deactivate`, { ...options, auth: { type: 'session', token: sessionToken }, method: 'POST', body: data, scopes: ['billingEntityId'] }),
  }
}
