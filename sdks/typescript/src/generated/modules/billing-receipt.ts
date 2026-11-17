import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listReceipts']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listReceipts']['parameters']['query']>
type ListCountData = NonNullable<operations['listReceiptsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listReceiptsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readReceipt']['responses']['200']['content']['application/json']['data']>

export function createBillingReceipts(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/receipts/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/receipts/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    read: (receiptId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/receipts/${encodePathParam(receiptId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),
  }
}
