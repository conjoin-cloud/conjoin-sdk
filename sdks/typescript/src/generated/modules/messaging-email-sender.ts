import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type VerifyData = NonNullable<operations['verifyEmailSender']['responses']['200']['content']['application/json']['data']>
type ListManyBody = NonNullable<operations['listManyEmailSenders']['requestBody']>['content']['application/json']
type ListManyData = NonNullable<operations['listManyEmailSenders']['responses']['200']['content']['application/json']['data']>[number]
type ListOneData = NonNullable<operations['listOneEmailSender']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteEmailSender']['responses']['200']['content']['application/json']['data']>
type CreateBody = NonNullable<operations['createEmailSender']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createEmailSender']['responses']['201']['content']['application/json']['data']>
type EnableData = NonNullable<operations['enableEmailSender']['responses']['200']['content']['application/json']['data']>
type DisableData = NonNullable<operations['disableEmailSender']['responses']['200']['content']['application/json']['data']>
type TransferData = NonNullable<operations['transferEmailSender']['responses']['200']['content']['application/json']['data']>

export function createMessagingEmailSenders(client: ConjoinClient) {
  return {
    verify: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<VerifyData>(`messaging/email/senders/${encodePathParam(senderId)}/verify`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    listMany: (data: ListManyBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListManyData>('messaging/email/senders/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listOne: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<ListOneData>(`messaging/email/senders/${encodePathParam(senderId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    delete: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/email/senders/${encodePathParam(senderId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/email/senders/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    enable: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<EnableData>(`messaging/email/senders/${encodePathParam(senderId)}/enable`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    disable: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DisableData>(`messaging/email/senders/${encodePathParam(senderId)}/disable`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    transfer: (senderId: string, projectId: string, options?: ConjoinCallOptions) =>
      client.fetch<TransferData>(`messaging/email/senders/transfers/${encodePathParam(senderId)}/${encodePathParam(projectId)}`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),
  }
}
