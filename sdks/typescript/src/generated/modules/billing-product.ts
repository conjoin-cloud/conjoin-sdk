import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listProducts']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listProducts']['parameters']['query']>
type CreateBody = NonNullable<operations['createProduct']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createProduct']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listProductsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listProductsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readProduct']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateProduct']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateProduct']['responses']['200']['content']['application/json']['data']>
type DeleteResponse = operations['deleteProduct']['responses']['200']['content']['application/json']
type ArchiveData = NonNullable<operations['archiveProduct']['responses']['200']['content']['application/json']['data']>
type RestoreData = NonNullable<operations['restoreProduct']['responses']['200']['content']['application/json']['data']>

export function createBillingProducts(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/products/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/products/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/products/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    read: (productId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/products/${encodePathParam(productId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),

    update: (productId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/products/${encodePathParam(productId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    delete: (productId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<DeleteResponse>(`billing/products/${encodePathParam(productId)}`, { ...options, method: 'DELETE', scopes: ['billingEntityId'] }),

    archive: (productId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`billing/products/${encodePathParam(productId)}/archive`, { ...options, method: 'POST', scopes: ['billingEntityId'] }),

    restore: (productId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreData>(`billing/products/${encodePathParam(productId)}/restore`, { ...options, method: 'POST', scopes: ['billingEntityId'] }),
  }
}
