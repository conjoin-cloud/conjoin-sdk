import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listPrices']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPrices']['parameters']['query']>
type CreateBody = NonNullable<operations['createPrice']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createPrice']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listPricesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPricesCount']['parameters']['query']>
type ReadData = NonNullable<operations['readPrice']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updatePrice']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updatePrice']['responses']['200']['content']['application/json']['data']>
type DeleteResponse = operations['deletePrice']['responses']['200']['content']['application/json']
type ArchiveData = NonNullable<operations['archivePrice']['responses']['200']['content']['application/json']['data']>
type RestoreData = NonNullable<operations['restorePrice']['responses']['200']['content']['application/json']['data']>

export function createBillingPrices(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/prices/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/prices/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/prices/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    read: (priceId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/prices/${encodePathParam(priceId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),

    update: (priceId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/prices/${encodePathParam(priceId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    delete: (priceId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<DeleteResponse>(`billing/prices/${encodePathParam(priceId)}`, { ...options, method: 'DELETE', scopes: ['billingEntityId'] }),

    archive: (priceId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`billing/prices/${encodePathParam(priceId)}/archive`, { ...options, method: 'POST', scopes: ['billingEntityId'] }),

    restore: (priceId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreData>(`billing/prices/${encodePathParam(priceId)}/restore`, { ...options, method: 'POST', scopes: ['billingEntityId'] }),
  }
}
