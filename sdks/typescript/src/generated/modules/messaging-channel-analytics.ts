import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listChannelAnalytics']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listChannelAnalytics']['parameters']['query']>
type CreateReportBody = NonNullable<operations['createChannelAnalyticsReport']['requestBody']>['content']['application/json']
type CreateReportData = NonNullable<operations['createChannelAnalyticsReport']['responses']['200']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listChannelAnalyticsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listChannelAnalyticsCount']['parameters']['query']>
type GenerateSummariesData = NonNullable<operations['generateChannelAnalyticsSummaries']['responses']['200']['content']['application/json']['data']>
type GenerateSummariesQuery = NonNullable<operations['generateChannelAnalyticsSummaries']['parameters']['query']>
type IncrementOpensBody = NonNullable<operations['incrementChannelAnalyticsOpens']['requestBody']>['content']['application/json']
type IncrementOpensData = NonNullable<operations['incrementChannelAnalyticsOpens']['responses']['200']['content']['application/json']['data']>
type IncrementClicksBody = NonNullable<operations['incrementChannelAnalyticsClicks']['requestBody']>['content']['application/json']
type IncrementClicksData = NonNullable<operations['incrementChannelAnalyticsClicks']['responses']['200']['content']['application/json']['data']>
type IncrementDeliveriesBody = NonNullable<operations['incrementChannelAnalyticsDeliveries']['requestBody']>['content']['application/json']
type IncrementDeliveriesData = NonNullable<operations['incrementChannelAnalyticsDeliveries']['responses']['200']['content']['application/json']['data']>
type IncrementSubscribesBody = NonNullable<operations['incrementChannelAnalyticsSubscribes']['requestBody']>['content']['application/json']
type IncrementSubscribesData = NonNullable<operations['incrementChannelAnalyticsSubscribes']['responses']['200']['content']['application/json']['data']>
type IncrementUnsubscribesBody = NonNullable<operations['incrementChannelAnalyticsUnsubscribes']['requestBody']>['content']['application/json']
type IncrementUnsubscribesData = NonNullable<operations['incrementChannelAnalyticsUnsubscribes']['responses']['200']['content']['application/json']['data']>

export function createMessagingChannelAnalytics(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/analytics/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    createReport: (data: CreateReportBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateReportData>('messaging/analytics-reports/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('messaging/analytics/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    generateSummaries: (query: GenerateSummariesQuery, options?: ConjoinCallOptions) =>
      client.fetch<GenerateSummariesData>('messaging/analytics/stats', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    incrementOpens: (analyticsId: string, data: IncrementOpensBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementOpensData>(`messaging/analytics/${encodePathParam(analyticsId)}/opens`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    incrementClicks: (analyticsId: string, data: IncrementClicksBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementClicksData>(`messaging/analytics/${encodePathParam(analyticsId)}/clicks`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    incrementDeliveries: (analyticsId: string, data: IncrementDeliveriesBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementDeliveriesData>(`messaging/analytics/${encodePathParam(analyticsId)}/deliveries`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    incrementSubscribes: (analyticsId: string, data: IncrementSubscribesBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementSubscribesData>(`messaging/analytics/${encodePathParam(analyticsId)}/subscribes`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    incrementUnsubscribes: (analyticsId: string, data: IncrementUnsubscribesBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementUnsubscribesData>(`messaging/analytics/${encodePathParam(analyticsId)}/unsubscribes`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
