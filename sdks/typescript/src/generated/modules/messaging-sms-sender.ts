import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateSmsSenderBody = NonNullable<operations['createSmsSender']['requestBody']>['content']['application/json']
type CreateSmsSenderData = NonNullable<operations['createSmsSender']['responses']['201']['content']['application/json']['data']>
type EnableSmsSenderData = NonNullable<operations['enableSmsSender']['responses']['200']['content']['application/json']['data']>
type DisableSmsSenderData = NonNullable<operations['disableSmsSender']['responses']['200']['content']['application/json']['data']>
type ListSmsSenderData = NonNullable<operations['listSmsSender']['responses']['200']['content']['application/json']['data']>
type DeleteSmsSenderData = NonNullable<operations['deleteSmsSender']['responses']['200']['content']['application/json']['data']>
type UpdateOneSmsSenderBody = NonNullable<operations['updateOneSmsSender']['requestBody']>['content']['application/json']
type UpdateOneSmsSenderData = NonNullable<operations['updateOneSmsSender']['responses']['200']['content']['application/json']['data']>
type TransferSmsSenderData = NonNullable<operations['transferSmsSender']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMSSenders(client: ConjoinClient) {
  return {
    createSmsSender: (data: CreateSmsSenderBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsSenderData>('messaging/sms/senders/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    enableSmsSender: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<EnableSmsSenderData>(`messaging/sms/senders/${encodePathParam(senderId)}/enable`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    disableSmsSender: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DisableSmsSenderData>(`messaging/sms/senders/${encodePathParam(senderId)}/disable`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    listSmsSender: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<ListSmsSenderData>(`messaging/sms/senders/${encodePathParam(senderId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteSmsSender: (senderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsSenderData>(`messaging/sms/senders/${encodePathParam(senderId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    updateOneSmsSender: (senderId: string, data: UpdateOneSmsSenderBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateOneSmsSenderData>(`messaging/sms/senders/${encodePathParam(senderId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    transferSmsSender: (senderId: string, projectId: string, options?: ConjoinCallOptions) =>
      client.fetch<TransferSmsSenderData>(`messaging/sms/senders/transfers/${encodePathParam(senderId)}/${encodePathParam(projectId)}`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),
  }
}
