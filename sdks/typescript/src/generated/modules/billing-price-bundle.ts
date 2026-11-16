import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListActivationsData = NonNullable<operations['listPriceBundleActivations']['responses']['200']['content']['application/json']['data']>[number]
type ListActivationsQuery = NonNullable<operations['listPriceBundleActivations']['parameters']['query']>
type ActivateBody = NonNullable<operations['activatePriceBundle']['requestBody']>['content']['application/json']
type ActivateData = NonNullable<operations['activatePriceBundle']['responses']['201']['content']['application/json']['data']>
type ListActivationsCountData = NonNullable<operations['listPriceBundleActivationsCount']['responses']['200']['content']['application/json']['data']>
type ListActivationsCountQuery = NonNullable<operations['listPriceBundleActivationsCount']['parameters']['query']>
type DeactivateBody = NonNullable<operations['deactivatePriceBundle']['requestBody']>['content']['application/json']
type DeactivateData = NonNullable<operations['deactivatePriceBundle']['responses']['200']['content']['application/json']['data']>
type ReadAvailableBundleTransitionsData = NonNullable<operations['readAvailableBundleTransitions']['responses']['200']['content']['application/json']['data']>
type ReadAvailableBundleTransitionsQuery = NonNullable<operations['readAvailableBundleTransitions']['parameters']['query']>
type ListData = NonNullable<operations['listPriceBundles']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPriceBundles']['parameters']['query']>
type CreateBody = NonNullable<operations['createPriceBundle']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createPriceBundle']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listPriceBundlesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPriceBundlesCount']['parameters']['query']>
type ReadData = NonNullable<operations['readPriceBundle']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updatePriceBundle']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updatePriceBundle']['responses']['200']['content']['application/json']['data']>
type ArchiveData = NonNullable<operations['archivePriceBundle']['responses']['200']['content']['application/json']['data']>
type RestoreData = NonNullable<operations['restorePriceBundle']['responses']['200']['content']['application/json']['data']>
type PublishData = NonNullable<operations['publishPriceBundle']['responses']['200']['content']['application/json']['data']>

export function createBillingPriceBundles(client: ConjoinClient) {
  return {
    listActivations: (query: ListActivationsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListActivationsData>('billing/price-bundle-activations/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    activate: (data: ActivateBody, options?: ConjoinCallOptions) =>
      client.fetch<ActivateData>('billing/price-bundle-activations/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listActivationsCount: (query: ListActivationsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListActivationsCountData>('billing/price-bundle-activations/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    deactivate: (priceBundleActivationId: string, data: DeactivateBody, options?: ConjoinCallOptions) =>
      client.fetch<DeactivateData>(`billing/price-bundle-activations/${encodePathParam(priceBundleActivationId)}/deactivate`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    readAvailableBundleTransitions: (query: ReadAvailableBundleTransitionsQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadAvailableBundleTransitionsData>('billing/price-bundle-transitions/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/price-bundles/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/price-bundles/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/price-bundles/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    read: (priceBundleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/price-bundles/${encodePathParam(priceBundleId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),

    update: (priceBundleId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/price-bundles/${encodePathParam(priceBundleId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    archive: (priceBundleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`billing/price-bundles/${encodePathParam(priceBundleId)}/archive`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    restore: (priceBundleId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreData>(`billing/price-bundles/${encodePathParam(priceBundleId)}/restore`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    publish: (priceBundleId: string, options?: ConjoinCallOptions) =>
      client.fetch<PublishData>(`billing/price-bundles/${encodePathParam(priceBundleId)}/publish`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),
  }
}
