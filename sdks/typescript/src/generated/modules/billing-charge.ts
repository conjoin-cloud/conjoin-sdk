import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listCharges']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listCharges']['parameters']['query']>
type ListCountData = NonNullable<operations['listChargesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listChargesCount']['parameters']['query']>

export function createBillingCharges(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/charges/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/charges/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),
  }
}
