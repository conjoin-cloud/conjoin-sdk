import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listDiscounts']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listDiscounts']['parameters']['query']>
type CreateBody = NonNullable<operations['createDiscount']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createDiscount']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listDiscountsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listDiscountsCount']['parameters']['query']>
type DeleteData = NonNullable<operations['deleteDiscount']['responses']['200']['content']['application/json']['data']>

export function createBillingDiscounts(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/discounts/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/discounts/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/discounts/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    delete: (discountId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`billing/discounts/${encodePathParam(discountId)}`, { ...options, method: 'DELETE', scopes: ['billingEntityId'] }),
  }
}
