import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listRefunds']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listRefunds']['parameters']['query']>
type CreateBody = NonNullable<operations['createRefund']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createRefund']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listRefundsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listRefundsCount']['parameters']['query']>

export function createBillingRefunds(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/refunds/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/refunds/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/refunds/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),
  }
}
