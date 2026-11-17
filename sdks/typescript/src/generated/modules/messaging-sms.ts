import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListSmsMessagesData = NonNullable<operations['listSmsMessages']['responses']['200']['content']['application/json']['data']>[number]
type ListSmsMessagesQuery = NonNullable<operations['listSmsMessages']['parameters']['query']>
type SendSmsBody = NonNullable<operations['sendSms']['requestBody']>['content']['application/json']
type SendSmsData = NonNullable<operations['sendSms']['responses']['200']['content']['application/json']['data']>
type ListSmsMessagesCountData = NonNullable<operations['listSmsMessagesCount']['responses']['200']['content']['application/json']['data']>
type ListSmsMessagesCountQuery = NonNullable<operations['listSmsMessagesCount']['parameters']['query']>
type ReadSmsMessageData = NonNullable<operations['readSmsMessage']['responses']['200']['content']['application/json']['data']>
type GenerateSmsSummaryBody = NonNullable<operations['generateSmsSummary']['requestBody']>['content']['application/json']
type GenerateSmsSummaryData = NonNullable<operations['generateSmsSummary']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMs(client: ConjoinClient) {
  return {
    listSmsMessages: (query?: ListSmsMessagesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListSmsMessagesData>('messaging/sms-messages/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    sendSms: (data: SendSmsBody, options?: ConjoinCallOptions) =>
      client.fetch<SendSmsData>('messaging/sms-messages/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listSmsMessagesCount: (query?: ListSmsMessagesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListSmsMessagesCountData>('messaging/sms-messages/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    readSmsMessage: (smsMessageId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSmsMessageData>(`messaging/sms-messages/${encodePathParam(smsMessageId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    generateSmsSummary: (data: GenerateSmsSummaryBody, options?: ConjoinCallOptions) =>
      client.fetch<GenerateSmsSummaryData>('messaging/sms-message-previews/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
