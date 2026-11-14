import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type SendSmsBody = NonNullable<operations['sendSms']['requestBody']>['content']['application/json']
type SendSmsData = NonNullable<operations['sendSms']['responses']['200']['content']['application/json']['data']>
type ReadSmsMessagesBody = NonNullable<operations['readSmsMessages']['requestBody']>['content']['application/json']
type ReadSmsMessagesData = NonNullable<operations['readSmsMessages']['responses']['200']['content']['application/json']['data']>[number]
type GetSmsSummaryData = NonNullable<operations['getSmsSummary']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMs(client: ConjoinClient) {
  return {
    sendSms: (data: SendSmsBody, options?: ConjoinCallOptions) =>
      client.fetch<SendSmsData>('messaging/sms/send', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    readSmsMessages: (messageId: string, data: ReadSmsMessagesBody, options?: ConjoinCallOptions) =>
      client.fetchList<ReadSmsMessagesData>(`messaging/sms/messages/${encodePathParam(messageId)}`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    getSmsSummary: (options?: ConjoinCallOptions) =>
      client.fetch<GetSmsSummaryData>('messaging/sms/summary', { ...options, method: 'GET', scopes: ['messagingProfileId'] }),
  }
}
