import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListManyData = NonNullable<operations['listManyEmailSenders']['responses']['200']['content']['application/json']['data']>[number]
type ListManyQuery = NonNullable<operations['listManyEmailSenders']['parameters']['query']>
type CreateBody = NonNullable<operations['createEmailSender']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createEmailSender']['responses']['201']['content']['application/json']['data']>
type ListManyCountData = NonNullable<operations['listManyEmailSendersCount']['responses']['200']['content']['application/json']['data']>
type ListManyCountQuery = NonNullable<operations['listManyEmailSendersCount']['parameters']['query']>
type ReadData = NonNullable<operations['readEmailSender']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteEmailSender']['responses']['200']['content']['application/json']['data']>
type VerifyData = NonNullable<operations['verifyEmailSender']['responses']['200']['content']['application/json']['data']>
type EnableData = NonNullable<operations['enableEmailSender']['responses']['200']['content']['application/json']['data']>
type DisableData = NonNullable<operations['disableEmailSender']['responses']['200']['content']['application/json']['data']>
type TransferBody = NonNullable<operations['transferEmailSender']['requestBody']>['content']['application/json']
type TransferData = NonNullable<operations['transferEmailSender']['responses']['200']['content']['application/json']['data']>

export function createMessagingEmailSenders(client: ConjoinClient) {
  return {
    listMany: (query?: ListManyQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListManyData>('messaging/email-senders/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/email-senders/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listManyCount: (query?: ListManyCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListManyCountData>('messaging/email-senders/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    read: (emailSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`messaging/email-senders/${encodePathParam(emailSenderId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    delete: (emailSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/email-senders/${encodePathParam(emailSenderId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    verify: (emailSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<VerifyData>(`messaging/email-senders/${encodePathParam(emailSenderId)}/verify`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    enable: (emailSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<EnableData>(`messaging/email-senders/${encodePathParam(emailSenderId)}/enable`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    disable: (emailSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DisableData>(`messaging/email-senders/${encodePathParam(emailSenderId)}/disable`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    transfer: (emailSenderId: string, data: TransferBody, options?: ConjoinCallOptions) =>
      client.fetch<TransferData>(`messaging/email-senders/${encodePathParam(emailSenderId)}/transfer`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
