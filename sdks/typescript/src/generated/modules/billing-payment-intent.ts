import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listPaymentIntents']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPaymentIntents']['parameters']['query']>
type CreateBody = NonNullable<operations['createPaymentIntent']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createPaymentIntent']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listPaymentIntentsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPaymentIntentsCount']['parameters']['query']>
type VerifyData = NonNullable<operations['verifyPaymentIntent']['responses']['200']['content']['application/json']['data']>

export function createBillingPaymentIntents(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/payment-intents/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/payment-intents/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/payment-intents/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    verify: (paymentIntentId: string, options?: ConjoinCallOptions) =>
      client.fetch<VerifyData>(`billing/payment-intents/${encodePathParam(paymentIntentId)}/verify`, { ...options, method: 'POST', scopes: ['billingEntityId'] }),
  }
}
