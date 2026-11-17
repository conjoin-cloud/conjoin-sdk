import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListManySmsSendersData = NonNullable<operations['listManySmsSenders']['responses']['200']['content']['application/json']['data']>[number]
type ListManySmsSendersQuery = NonNullable<operations['listManySmsSenders']['parameters']['query']>
type CreateSmsSenderBody = NonNullable<operations['createSmsSender']['requestBody']>['content']['application/json']
type CreateSmsSenderData = NonNullable<operations['createSmsSender']['responses']['201']['content']['application/json']['data']>
type ListManySmsSendersCountData = NonNullable<operations['listManySmsSendersCount']['responses']['200']['content']['application/json']['data']>
type ListManySmsSendersCountQuery = NonNullable<operations['listManySmsSendersCount']['parameters']['query']>
type ReadSmsSenderData = NonNullable<operations['readSmsSender']['responses']['200']['content']['application/json']['data']>
type UpdateOneSmsSenderBody = NonNullable<operations['updateOneSmsSender']['requestBody']>['content']['application/json']
type UpdateOneSmsSenderData = NonNullable<operations['updateOneSmsSender']['responses']['200']['content']['application/json']['data']>
type DeleteSmsSenderData = NonNullable<operations['deleteSmsSender']['responses']['200']['content']['application/json']['data']>
type EnableSmsSenderData = NonNullable<operations['enableSmsSender']['responses']['200']['content']['application/json']['data']>
type DisableSmsSenderData = NonNullable<operations['disableSmsSender']['responses']['200']['content']['application/json']['data']>
type TransferSmsSenderBody = NonNullable<operations['transferSmsSender']['requestBody']>['content']['application/json']
type TransferSmsSenderData = NonNullable<operations['transferSmsSender']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMSSenders(client: ConjoinClient) {
  return {
    listManySmsSenders: (query?: ListManySmsSendersQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListManySmsSendersData>('messaging/sms-senders/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    createSmsSender: (data: CreateSmsSenderBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsSenderData>('messaging/sms-senders/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listManySmsSendersCount: (query?: ListManySmsSendersCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListManySmsSendersCountData>('messaging/sms-senders/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    readSmsSender: (smsSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSmsSenderData>(`messaging/sms-senders/${encodePathParam(smsSenderId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    updateOneSmsSender: (smsSenderId: string, data: UpdateOneSmsSenderBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateOneSmsSenderData>(`messaging/sms-senders/${encodePathParam(smsSenderId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deleteSmsSender: (smsSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsSenderData>(`messaging/sms-senders/${encodePathParam(smsSenderId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    enableSmsSender: (smsSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<EnableSmsSenderData>(`messaging/sms-senders/${encodePathParam(smsSenderId)}/enable`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    disableSmsSender: (smsSenderId: string, options?: ConjoinCallOptions) =>
      client.fetch<DisableSmsSenderData>(`messaging/sms-senders/${encodePathParam(smsSenderId)}/disable`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    transferSmsSender: (smsSenderId: string, data: TransferSmsSenderBody, options?: ConjoinCallOptions) =>
      client.fetch<TransferSmsSenderData>(`messaging/sms-senders/${encodePathParam(smsSenderId)}/transfer`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
