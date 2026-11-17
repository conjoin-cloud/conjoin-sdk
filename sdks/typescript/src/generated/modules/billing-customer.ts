import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listCustomers']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listCustomers']['parameters']['query']>
type CreateBody = NonNullable<operations['createCustomer']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCustomer']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listCustomersCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listCustomersCount']['parameters']['query']>
type ReadData = NonNullable<operations['readCustomer']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateCustomer']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCustomer']['responses']['200']['content']['application/json']['data']>
type ArchiveData = NonNullable<operations['archiveCustomer']['responses']['200']['content']['application/json']['data']>
type RestoreData = NonNullable<operations['restoreCustomer']['responses']['200']['content']['application/json']['data']>

export function createBillingCustomers(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/customers/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/customers/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/customers/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    read: (customerId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/customers/${encodePathParam(customerId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),

    update: (customerId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/customers/${encodePathParam(customerId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    archive: (customerId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`billing/customers/${encodePathParam(customerId)}/archive`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    restore: (customerId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreData>(`billing/customers/${encodePathParam(customerId)}/restore`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),
  }
}
