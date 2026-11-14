import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createEmailSenderPool']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createEmailSenderPool']['responses']['201']['content']['application/json']['data']>
type AddEmailSendersToPoolBody = NonNullable<operations['addEmailSendersToPool']['requestBody']>['content']['application/json']
type AddEmailSendersToPoolData = NonNullable<operations['addEmailSendersToPool']['responses']['200']['content']['application/json']['data']>
type GetData = NonNullable<operations['getEmailSenderPool']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteEmailSenderPool']['responses']['200']['content']['application/json']['data']>

export function createMessagingEmailSenderPools(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/email/sender-pools/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    addEmailSendersToPool: (poolId: string, data: AddEmailSendersToPoolBody, options?: ConjoinCallOptions) =>
      client.fetch<AddEmailSendersToPoolData>(`messaging/email/sender-pools/${encodePathParam(poolId)}/senders`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    get: (poolId: string, options?: ConjoinCallOptions) =>
      client.fetch<GetData>(`messaging/email/sender-pools/${encodePathParam(poolId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    delete: (poolId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/email/sender-pools/${encodePathParam(poolId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
