import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type SendBody = NonNullable<operations['sendEmail']['requestBody']>['content']['multipart/form-data']
type SendData = NonNullable<operations['sendEmail']['responses']['200']['content']['application/json']['data']>
type ReadMessagesBody = NonNullable<operations['readEmailMessages']['requestBody']>['content']['application/json']
type ReadMessagesData = NonNullable<operations['readEmailMessages']['responses']['200']['content']['application/json']['data']>[number]
type GetSummaryData = NonNullable<operations['getEmailSummary']['responses']['200']['content']['application/json']['data']>

export function createMessagingEmails(client: ConjoinClient) {
  return {
    send: (data: SendBody, options?: ConjoinCallOptions) =>
      client.fetch<SendData>('messaging/email/send', { ...options, method: 'POST', body: data, contentType: 'multipart/form-data', scopes: ['messagingProfileId'] }),

    readMessages: (messageId: string, data: ReadMessagesBody, options?: ConjoinCallOptions) =>
      client.fetchList<ReadMessagesData>(`messaging/email/messages/${encodePathParam(messageId)}`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    getSummary: (options?: ConjoinCallOptions) =>
      client.fetch<GetSummaryData>('messaging/email/summary', { ...options, method: 'GET', scopes: ['messagingProfileId'] }),
  }
}
