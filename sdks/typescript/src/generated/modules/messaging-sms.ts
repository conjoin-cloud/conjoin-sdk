import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type SendSmsBody = NonNullable<operations['sendSms']['requestBody']>['content']['application/json']
type SendSmsData = NonNullable<operations['sendSms']['responses']['200']['content']['application/json']['data']>
type ReadSmsMessagesBody = NonNullable<operations['readSmsMessages']['requestBody']>['content']['application/json']
type ReadSmsMessagesData = NonNullable<operations['readSmsMessages']['responses']['200']['content']['application/json']['data']>[number]
type GenerateSmsSummaryBody = NonNullable<operations['generateSmsSummary']['requestBody']>['content']['application/json']
type GenerateSmsSummaryData = NonNullable<operations['generateSmsSummary']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMs(client: ConjoinClient) {
  return {
    sendSms: (data: SendSmsBody, options?: ConjoinCallOptions) =>
      client.fetch<SendSmsData>('messaging/sms/send', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    readSmsMessages: (messageId: string, data: ReadSmsMessagesBody, options?: ConjoinCallOptions) =>
      client.fetchList<ReadSmsMessagesData>(`messaging/sms/messages/${encodePathParam(messageId)}`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    generateSmsSummary: (data: GenerateSmsSummaryBody, options?: ConjoinCallOptions) =>
      client.fetch<GenerateSmsSummaryData>('messaging/sms/summary', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
