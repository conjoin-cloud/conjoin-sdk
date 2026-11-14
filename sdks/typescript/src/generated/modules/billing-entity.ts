import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listBillingEntities']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listBillingEntities']['parameters']['query']>
type CreateBody = NonNullable<operations['createBillingEntity']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createBillingEntity']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listBillingEntitiesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listBillingEntitiesCount']['parameters']['query']>
type OnboardBody = NonNullable<operations['onboardBillingEntities']['requestBody']>['content']['application/json']
type OnboardResponse = operations['onboardBillingEntities']['responses']['201']['content']['application/json']
type ReadData = NonNullable<operations['readBillingEntity']['responses']['200']['content']['application/json']['data']>
type ReadQuery = NonNullable<operations['readBillingEntity']['parameters']['query']>
type UpdateBody = NonNullable<operations['updateBillingEntity']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateBillingEntity']['responses']['200']['content']['application/json']['data']>
type CreatePayoutBankAccountBody = NonNullable<operations['createBillingPayoutBankAccount']['requestBody']>['content']['application/json']
type CreatePayoutBankAccountData = NonNullable<operations['createBillingPayoutBankAccount']['responses']['200']['content']['application/json']['data']>
type CreateAccountLinkBody = NonNullable<operations['createBillingEntityAccountLink']['requestBody']>['content']['application/json']
type CreateAccountLinkResponse = operations['createBillingEntityAccountLink']['responses']['200']['content']['application/json']
type SyncOnboardingResponse = operations['syncBillingEntityOnboarding']['responses']['200']['content']['application/json']
type CreatePaystackCredentialsBody = NonNullable<operations['createBillingEntityPaystackCredentials']['requestBody']>['content']['application/json']
type CreatePaystackCredentialsResponse = operations['createBillingEntityPaystackCredentials']['responses']['200']['content']['application/json']

export function createBillingEntities(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/entities/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/entities/', { ...options, method: 'POST', body: data }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/entities/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    onboard: (data: OnboardBody, options?: ConjoinCallOptions) =>
      client.fetchJson<OnboardResponse>('billing/entities/onboard', { ...options, method: 'POST', body: data }),

    read: (entityId: string, query?: ReadQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/entities/${encodePathParam(entityId)}`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    update: (entityId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/entities/${encodePathParam(entityId)}`, { ...options, method: 'PATCH', body: data }),

    createPayoutBankAccount: (entityId: string, data: CreatePayoutBankAccountBody, options?: ConjoinCallOptions) =>
      client.fetch<CreatePayoutBankAccountData>(`billing/entities/${encodePathParam(entityId)}/payout-bank-accounts`, { ...options, method: 'POST', body: data }),

    createAccountLink: (entityId: string, data: CreateAccountLinkBody, options?: ConjoinCallOptions) =>
      client.fetchJson<CreateAccountLinkResponse>(`billing/entities/${encodePathParam(entityId)}/account-links`, { ...options, method: 'POST', body: data }),

    syncOnboarding: (entityId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<SyncOnboardingResponse>(`billing/entities/${encodePathParam(entityId)}/sync`, { ...options, method: 'POST' }),

    createPaystackCredentials: (entityId: string, data: CreatePaystackCredentialsBody, options?: ConjoinCallOptions) =>
      client.fetchJson<CreatePaystackCredentialsResponse>(`billing/entities/${encodePathParam(entityId)}/paystack-credentials`, { ...options, method: 'POST', body: data }),
  }
}
