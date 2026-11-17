import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListManySmsSenderPoolsData = NonNullable<operations['listManySmsSenderPools']['responses']['200']['content']['application/json']['data']>[number]
type ListManySmsSenderPoolsQuery = NonNullable<operations['listManySmsSenderPools']['parameters']['query']>
type CreateSmsSenderPoolBody = NonNullable<operations['createSmsSenderPool']['requestBody']>['content']['application/json']
type CreateSmsSenderPoolData = NonNullable<operations['createSmsSenderPool']['responses']['201']['content']['application/json']['data']>
type ListManySmsSenderPoolsCountData = NonNullable<operations['listManySmsSenderPoolsCount']['responses']['200']['content']['application/json']['data']>
type ListManySmsSenderPoolsCountQuery = NonNullable<operations['listManySmsSenderPoolsCount']['parameters']['query']>
type AddSmsSendersToPoolBody = NonNullable<operations['addSmsSendersToPool']['requestBody']>['content']['application/json']
type AddSmsSendersToPoolData = NonNullable<operations['addSmsSendersToPool']['responses']['200']['content']['application/json']['data']>
type GetSmsSenderPoolData = NonNullable<operations['getSmsSenderPool']['responses']['200']['content']['application/json']['data']>
type DeleteSmsSenderPoolData = NonNullable<operations['deleteSmsSenderPool']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMSSenderPools(client: ConjoinClient) {
  return {
    listManySmsSenderPools: (query?: ListManySmsSenderPoolsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListManySmsSenderPoolsData>('messaging/sms-sender-pools/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    createSmsSenderPool: (data: CreateSmsSenderPoolBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsSenderPoolData>('messaging/sms-sender-pools/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listManySmsSenderPoolsCount: (query?: ListManySmsSenderPoolsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListManySmsSenderPoolsCountData>('messaging/sms-sender-pools/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    addSmsSendersToPool: (smsSenderPoolId: string, data: AddSmsSendersToPoolBody, options?: ConjoinCallOptions) =>
      client.fetch<AddSmsSendersToPoolData>(`messaging/sms-sender-pools/${encodePathParam(smsSenderPoolId)}/senders`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    getSmsSenderPool: (smsSenderPoolId: string, options?: ConjoinCallOptions) =>
      client.fetch<GetSmsSenderPoolData>(`messaging/sms-sender-pools/${encodePathParam(smsSenderPoolId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteSmsSenderPool: (smsSenderPoolId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsSenderPoolData>(`messaging/sms-sender-pools/${encodePathParam(smsSenderPoolId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
