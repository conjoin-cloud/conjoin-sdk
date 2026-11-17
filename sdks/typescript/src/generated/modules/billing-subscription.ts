import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listSubscriptions']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listSubscriptions']['parameters']['query']>
type CreateBody = NonNullable<operations['createSubscription']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createSubscription']['responses']['201']['content']['application/json']['data']>
type ListCyclesData = NonNullable<operations['listSubscriptionCycles']['responses']['200']['content']['application/json']['data']>[number]
type ListCyclesQuery = NonNullable<operations['listSubscriptionCycles']['parameters']['query']>
type ListCountData = NonNullable<operations['listSubscriptionsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listSubscriptionsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readSubscription']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateSubscription']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateSubscription']['responses']['200']['content']['application/json']['data']>
type CreatePlanChangeBody = NonNullable<operations['createSubscriptionPlanChange']['requestBody']>['content']['application/json']
type CreatePlanChangeData = NonNullable<operations['createSubscriptionPlanChange']['responses']['200']['content']['application/json']['data']>
type CancelBody = NonNullable<operations['cancelSubscription']['requestBody']>['content']['application/json']
type CancelData = NonNullable<operations['cancelSubscription']['responses']['200']['content']['application/json']['data']>
type PauseBody = NonNullable<operations['pauseSubscription']['requestBody']>['content']['application/json']
type PauseData = NonNullable<operations['pauseSubscription']['responses']['200']['content']['application/json']['data']>
type ResumeData = NonNullable<operations['resumeSubscription']['responses']['200']['content']['application/json']['data']>
type RecordUsageBody = NonNullable<operations['recordSubscriptionUsage']['requestBody']>['content']['application/json']
type RecordUsageData = NonNullable<operations['recordSubscriptionUsage']['responses']['200']['content']['application/json']['data']>
type ReadUsageSummaryData = NonNullable<operations['readSubscriptionUsageSummary']['responses']['200']['content']['application/json']['data']>
type ReadUsageSummaryQuery = NonNullable<operations['readSubscriptionUsageSummary']['parameters']['query']>
type ListCyclesCountData = NonNullable<operations['listSubscriptionCyclesCount']['responses']['200']['content']['application/json']['data']>
type ListCyclesCountQuery = NonNullable<operations['listSubscriptionCyclesCount']['parameters']['query']>

export function createBillingSubscriptions(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/subscriptions/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/subscriptions/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCycles: (subscriptionId: string, query?: ListCyclesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListCyclesData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/cycles`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/subscriptions/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    read: (subscriptionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`billing/subscriptions/${encodePathParam(subscriptionId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),

    update: (subscriptionId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/subscriptions/${encodePathParam(subscriptionId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    createPlanChange: (subscriptionId: string, data: CreatePlanChangeBody, options?: ConjoinCallOptions) =>
      client.fetch<CreatePlanChangeData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/plan-changes`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    cancel: (subscriptionId: string, data: CancelBody, options?: ConjoinCallOptions) =>
      client.fetch<CancelData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/cancel`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    pause: (subscriptionId: string, data: PauseBody, options?: ConjoinCallOptions) =>
      client.fetch<PauseData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/pause`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    resume: (subscriptionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ResumeData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/resume`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    recordUsage: (subscriptionId: string, data: RecordUsageBody, options?: ConjoinCallOptions) =>
      client.fetch<RecordUsageData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/usage-records`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    readUsageSummary: (subscriptionId: string, query?: ReadUsageSummaryQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadUsageSummaryData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/usage-summaries`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    listCyclesCount: (subscriptionId: string, query?: ListCyclesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCyclesCountData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/cycles/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),
  }
}
