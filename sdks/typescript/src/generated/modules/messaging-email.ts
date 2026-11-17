import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type SendBody = NonNullable<operations['sendEmail']['requestBody']>['content']['multipart/form-data']
type SendData = NonNullable<operations['sendEmail']['responses']['200']['content']['application/json']['data']>
type ReadMessagesBody = NonNullable<operations['readEmailMessages']['requestBody']>['content']['application/json']
type ReadMessagesData = NonNullable<operations['readEmailMessages']['responses']['200']['content']['application/json']['data']>[number]
type GenerateSummaryBody = NonNullable<operations['generateEmailSummary']['requestBody']>['content']['application/json']
type GenerateSummaryData = NonNullable<operations['generateEmailSummary']['responses']['200']['content']['application/json']['data']>

export function createMessagingEmails(client: ConjoinClient) {
  return {
    send: (data: SendBody, options?: ConjoinCallOptions) =>
      client.fetch<SendData>('messaging/email/send', { ...options, method: 'POST', body: data, contentType: 'multipart/form-data', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    readMessages: (messageId: string, data: ReadMessagesBody, options?: ConjoinCallOptions) =>
      client.fetchList<ReadMessagesData>(`messaging/email/messages/${encodePathParam(messageId)}`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    generateSummary: (data: GenerateSummaryBody, options?: ConjoinCallOptions) =>
      client.fetch<GenerateSummaryData>('messaging/email/summary', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
