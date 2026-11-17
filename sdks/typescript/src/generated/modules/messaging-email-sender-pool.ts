import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListManyData = NonNullable<operations['listManyEmailSenderPools']['responses']['200']['content']['application/json']['data']>[number]
type ListManyQuery = NonNullable<operations['listManyEmailSenderPools']['parameters']['query']>
type CreateBody = NonNullable<operations['createEmailSenderPool']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createEmailSenderPool']['responses']['201']['content']['application/json']['data']>
type ListManyCountData = NonNullable<operations['listManyEmailSenderPoolsCount']['responses']['200']['content']['application/json']['data']>
type ListManyCountQuery = NonNullable<operations['listManyEmailSenderPoolsCount']['parameters']['query']>
type AddEmailSendersToPoolBody = NonNullable<operations['addEmailSendersToPool']['requestBody']>['content']['application/json']
type AddEmailSendersToPoolData = NonNullable<operations['addEmailSendersToPool']['responses']['200']['content']['application/json']['data']>
type GetData = NonNullable<operations['getEmailSenderPool']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteEmailSenderPool']['responses']['200']['content']['application/json']['data']>

export function createMessagingEmailSenderPools(client: ConjoinClient) {
  return {
    listMany: (query?: ListManyQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListManyData>('messaging/email-sender-pools/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/email-sender-pools/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listManyCount: (query?: ListManyCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListManyCountData>('messaging/email-sender-pools/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    addEmailSendersToPool: (emailSenderPoolId: string, data: AddEmailSendersToPoolBody, options?: ConjoinCallOptions) =>
      client.fetch<AddEmailSendersToPoolData>(`messaging/email-sender-pools/${encodePathParam(emailSenderPoolId)}/senders`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    get: (emailSenderPoolId: string, options?: ConjoinCallOptions) =>
      client.fetch<GetData>(`messaging/email-sender-pools/${encodePathParam(emailSenderPoolId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    delete: (emailSenderPoolId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/email-sender-pools/${encodePathParam(emailSenderPoolId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
