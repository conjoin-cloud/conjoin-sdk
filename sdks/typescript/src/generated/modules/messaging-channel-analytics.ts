import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listChannelAnalytics']['responses']['200']['content']['application/json']['data']>[number]
type GenerateSummariesData = NonNullable<operations['generateChannelAnalyticsSummaries']['responses']['201']['content']['application/json']['data']>
type CreateReportData = NonNullable<operations['createChannelAnalyticsReport']['responses']['200']['content']['application/json']['data']>
type IncrementOpensData = NonNullable<operations['incrementChannelAnalyticsOpens']['responses']['200']['content']['application/json']['data']>
type IncrementClicksData = NonNullable<operations['incrementChannelAnalyticsClicks']['responses']['200']['content']['application/json']['data']>
type IncrementDeliveriesData = NonNullable<operations['incrementChannelAnalyticsDeliveries']['responses']['200']['content']['application/json']['data']>
type IncrementSubscribesData = NonNullable<operations['incrementChannelAnalyticsSubscribes']['responses']['200']['content']['application/json']['data']>
type IncrementUnsubscribesData = NonNullable<operations['incrementChannelAnalyticsUnsubscribes']['responses']['200']['content']['application/json']['data']>

export function createMessagingChannelAnalytics(client: ConjoinClient) {
  return {
    list: (options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/analytics/', { ...options, method: 'POST', scopes: ['messagingProfileId'] }),

    generateSummaries: (channelId: string, options?: ConjoinCallOptions) =>
      client.fetch<GenerateSummariesData>(`messaging/analytics/channels/${encodePathParam(channelId)}/generate`, { ...options, method: 'POST', scopes: ['messagingProfileId'] }),

    createReport: (messageId: string, channelId: string, options?: ConjoinCallOptions) =>
      client.fetch<CreateReportData>(`messaging/analytics/messages/${encodePathParam(messageId)}/channels/${encodePathParam(channelId)}/reports`, { ...options, method: 'POST', scopes: ['messagingProfileId'] }),

    incrementOpens: (analyticsId: string, options?: ConjoinCallOptions) =>
      client.fetch<IncrementOpensData>(`messaging/analytics/${encodePathParam(analyticsId)}/opens`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    incrementClicks: (analyticsId: string, options?: ConjoinCallOptions) =>
      client.fetch<IncrementClicksData>(`messaging/analytics/${encodePathParam(analyticsId)}/clicks`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    incrementDeliveries: (analyticsId: string, options?: ConjoinCallOptions) =>
      client.fetch<IncrementDeliveriesData>(`messaging/analytics/${encodePathParam(analyticsId)}/deliveries`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    incrementSubscribes: (analyticsId: string, options?: ConjoinCallOptions) =>
      client.fetch<IncrementSubscribesData>(`messaging/analytics/${encodePathParam(analyticsId)}/subscribes`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    incrementUnsubscribes: (analyticsId: string, options?: ConjoinCallOptions) =>
      client.fetch<IncrementUnsubscribesData>(`messaging/analytics/${encodePathParam(analyticsId)}/unsubscribes`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),
  }
}
