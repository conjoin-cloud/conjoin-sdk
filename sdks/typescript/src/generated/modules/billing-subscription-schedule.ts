import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listSubscriptionSchedules']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listSubscriptionSchedules']['parameters']['query']>
type CreateBody = NonNullable<operations['createSubscriptionSchedule']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createSubscriptionSchedule']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listSubscriptionSchedulesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listSubscriptionSchedulesCount']['parameters']['query']>
type GetData = NonNullable<operations['getSubscriptionSchedule']['responses']['200']['content']['application/json']['data']>
type CancelData = NonNullable<operations['cancelSubscriptionSchedule']['responses']['200']['content']['application/json']['data']>
type ReleaseData = NonNullable<operations['releaseSubscriptionSchedule']['responses']['200']['content']['application/json']['data']>

export function createBillingSubscriptionSchedules(client: ConjoinClient) {
  return {
    list: (subscriptionId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/schedules`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (subscriptionId: string, data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/schedules`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'] }),

    listCount: (subscriptionId: string, query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>(`billing/subscriptions/${encodePathParam(subscriptionId)}/schedules/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    get: (subscriptionScheduleId: string, options?: ConjoinCallOptions) =>
      client.fetch<GetData>(`billing/subscription-schedules/${encodePathParam(subscriptionScheduleId)}`, { ...options, method: 'GET', scopes: ['billingEntityId'] }),

    cancel: (subscriptionScheduleId: string, options?: ConjoinCallOptions) =>
      client.fetch<CancelData>(`billing/subscription-schedules/${encodePathParam(subscriptionScheduleId)}/cancel`, { ...options, method: 'POST', scopes: ['billingEntityId'] }),

    release: (subscriptionScheduleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReleaseData>(`billing/subscription-schedules/${encodePathParam(subscriptionScheduleId)}/release`, { ...options, method: 'POST', scopes: ['billingEntityId'] }),
  }
}
