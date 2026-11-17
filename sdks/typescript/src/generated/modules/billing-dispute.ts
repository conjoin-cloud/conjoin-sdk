import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listDisputes']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listDisputes']['parameters']['query']>
type ListCountData = NonNullable<operations['listDisputesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listDisputesCount']['parameters']['query']>
type GetData = NonNullable<operations['getDispute']['responses']['200']['content']['application/json']['data']>

export function createBillingDisputes(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/disputes/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/disputes/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    get: (disputeId: string, options?: ConjoinCallOptions) =>
      client.fetch<GetData>(`billing/disputes/${encodePathParam(disputeId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),
  }
}
