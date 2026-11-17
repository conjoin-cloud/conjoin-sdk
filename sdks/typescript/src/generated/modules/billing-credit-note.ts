import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listCreditNotes']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listCreditNotes']['parameters']['query']>
type CreateBody = NonNullable<operations['createCreditNote']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCreditNote']['responses']['201']['content']['application/json']['data']>
type ListCustomerCreditBalancesData = NonNullable<operations['listCustomerCreditBalances']['responses']['200']['content']['application/json']['data']>[number]
type ListCustomerCreditBalancesQuery = NonNullable<operations['listCustomerCreditBalances']['parameters']['query']>
type ListCountData = NonNullable<operations['listCreditNotesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listCreditNotesCount']['parameters']['query']>
type VoidData = NonNullable<operations['voidCreditNote']['responses']['200']['content']['application/json']['data']>
type ListCustomerCreditBalancesCountData = NonNullable<operations['listCustomerCreditBalancesCount']['responses']['200']['content']['application/json']['data']>
type ListCustomerCreditBalancesCountQuery = NonNullable<operations['listCustomerCreditBalancesCount']['parameters']['query']>

export function createBillingCreditNotes(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/credit-notes/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/credit-notes/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCustomerCreditBalances: (customerId: string, query?: ListCustomerCreditBalancesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListCustomerCreditBalancesData>(`billing/customers/${encodePathParam(customerId)}/credit-balances`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/credit-notes/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    void: (creditNoteId: string, options?: ConjoinCallOptions) =>
      client.fetch<VoidData>(`billing/credit-notes/${encodePathParam(creditNoteId)}/void`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCustomerCreditBalancesCount: (customerId: string, query?: ListCustomerCreditBalancesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCustomerCreditBalancesCountData>(`billing/customers/${encodePathParam(customerId)}/credit-balances/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),
  }
}
