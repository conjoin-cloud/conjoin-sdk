import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListBody = NonNullable<operations['listChannelAnalytics']['requestBody']>['content']['application/json']
type ListData = NonNullable<operations['listChannelAnalytics']['responses']['200']['content']['application/json']['data']>[number]
type GenerateSummariesBody = NonNullable<operations['generateChannelAnalyticsSummaries']['requestBody']>['content']['application/json']
type GenerateSummariesData = NonNullable<operations['generateChannelAnalyticsSummaries']['responses']['200']['content']['application/json']['data']>
type CreateReportBody = NonNullable<operations['createChannelAnalyticsReport']['requestBody']>['content']['application/json']
type CreateReportData = NonNullable<operations['createChannelAnalyticsReport']['responses']['200']['content']['application/json']['data']>
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
    list: (data: ListBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/email/analytics/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true, cursorLocation: 'body' }),

    generateSummaries: (channelId: string, data: GenerateSummariesBody, options?: ConjoinCallOptions) =>
      client.fetch<GenerateSummariesData>(`messaging/email/analytics/channels/${encodePathParam(channelId)}/generate`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    createReport: (messageId: string, channelId: string, data: CreateReportBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateReportData>(`messaging/email/analytics/messages/${encodePathParam(messageId)}/channels/${encodePathParam(channelId)}/reports`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    incrementOpens: (analyticsId: string, data: IncrementOpensBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementOpensData>(`messaging/email/analytics/${encodePathParam(analyticsId)}/opens`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    incrementClicks: (analyticsId: string, data: IncrementClicksBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementClicksData>(`messaging/email/analytics/${encodePathParam(analyticsId)}/clicks`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    incrementDeliveries: (analyticsId: string, data: IncrementDeliveriesBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementDeliveriesData>(`messaging/email/analytics/${encodePathParam(analyticsId)}/deliveries`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    incrementSubscribes: (analyticsId: string, data: IncrementSubscribesBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementSubscribesData>(`messaging/email/analytics/${encodePathParam(analyticsId)}/subscribes`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    incrementUnsubscribes: (analyticsId: string, data: IncrementUnsubscribesBody, options?: ConjoinCallOptions) =>
      client.fetch<IncrementUnsubscribesData>(`messaging/email/analytics/${encodePathParam(analyticsId)}/unsubscribes`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),
  }
}
