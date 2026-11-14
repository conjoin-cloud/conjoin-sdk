import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listPaymentMethods']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPaymentMethods']['parameters']['query']>
type CreateBody = NonNullable<operations['createPaymentMethod']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createPaymentMethod']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listPaymentMethodsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPaymentMethodsCount']['parameters']['query']>
type DeleteData = NonNullable<operations['deletePaymentMethod']['responses']['200']['content']['application/json']['data']>

export function createBillingPaymentMethods(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/payment-methods/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/payment-methods/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/payment-methods/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    delete: (paymentMethodId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`billing/payment-methods/${encodePathParam(paymentMethodId)}`, { ...options, method: 'DELETE', scopes: ['billingEntityId'] }),
  }
}
