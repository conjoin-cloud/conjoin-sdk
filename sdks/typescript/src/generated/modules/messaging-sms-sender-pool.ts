import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateSmsSenderPoolBody = NonNullable<operations['createSmsSenderPool']['requestBody']>['content']['application/json']
type CreateSmsSenderPoolData = NonNullable<operations['createSmsSenderPool']['responses']['201']['content']['application/json']['data']>
type AddSmsSendersToPoolBody = NonNullable<operations['addSmsSendersToPool']['requestBody']>['content']['application/json']
type AddSmsSendersToPoolData = NonNullable<operations['addSmsSendersToPool']['responses']['200']['content']['application/json']['data']>
type GetSmsSenderPoolData = NonNullable<operations['getSmsSenderPool']['responses']['200']['content']['application/json']['data']>
type DeleteSmsSenderPoolData = NonNullable<operations['deleteSmsSenderPool']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMSSenderPools(client: ConjoinClient) {
  return {
    createSmsSenderPool: (data: CreateSmsSenderPoolBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsSenderPoolData>('messaging/sms/sender-pools/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    addSmsSendersToPool: (poolId: string, data: AddSmsSendersToPoolBody, options?: ConjoinCallOptions) =>
      client.fetch<AddSmsSendersToPoolData>(`messaging/sms/sender-pools/${encodePathParam(poolId)}/senders`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    getSmsSenderPool: (poolId: string, options?: ConjoinCallOptions) =>
      client.fetch<GetSmsSenderPoolData>(`messaging/sms/sender-pools/${encodePathParam(poolId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteSmsSenderPool: (poolId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsSenderPoolData>(`messaging/sms/sender-pools/${encodePathParam(poolId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
