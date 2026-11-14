import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listCreditWallets']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listCreditWallets']['parameters']['query']>
type CreateBody = NonNullable<operations['createCreditWallet']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCreditWallet']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listCreditWalletsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listCreditWalletsCount']['parameters']['query']>
type UpdateBody = NonNullable<operations['updateCreditWallet']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCreditWallet']['responses']['200']['content']['application/json']['data']>
type GrantCreditsBody = NonNullable<operations['grantCredits']['requestBody']>['content']['application/json']
type GrantCreditsData = NonNullable<operations['grantCredits']['responses']['201']['content']['application/json']['data']>

export function createBillingCreditWallets(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/credit-wallets/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/credit-wallets/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/credit-wallets/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    update: (creditWalletId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/credit-wallets/${encodePathParam(creditWalletId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    grantCredits: (creditWalletId: string, data: GrantCreditsBody, options?: ConjoinCallOptions) =>
      client.fetch<GrantCreditsData>(`billing/credit-wallets/${encodePathParam(creditWalletId)}/grant`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),
  }
}
