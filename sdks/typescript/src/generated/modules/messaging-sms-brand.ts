import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListSmsBrandsData = NonNullable<operations['listSmsBrands']['responses']['200']['content']['application/json']['data']>[number]
type ListSmsBrandsQuery = NonNullable<operations['listSmsBrands']['parameters']['query']>
type CreateSmsBrandBody = NonNullable<operations['createSmsBrand']['requestBody']>['content']['application/json']
type CreateSmsBrandData = NonNullable<operations['createSmsBrand']['responses']['201']['content']['application/json']['data']>
type ListSmsBrandsCountData = NonNullable<operations['listSmsBrandsCount']['responses']['200']['content']['application/json']['data']>
type ListSmsBrandsCountQuery = NonNullable<operations['listSmsBrandsCount']['parameters']['query']>
type ReadSmsBrandData = NonNullable<operations['readSmsBrand']['responses']['200']['content']['application/json']['data']>
type UpdateSmsBrandBody = NonNullable<operations['updateSmsBrand']['requestBody']>['content']['application/json']
type UpdateSmsBrandData = NonNullable<operations['updateSmsBrand']['responses']['200']['content']['application/json']['data']>
type DeleteSmsBrandData = NonNullable<operations['deleteSmsBrand']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMSBrands(client: ConjoinClient) {
  return {
    listSmsBrands: (query?: ListSmsBrandsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListSmsBrandsData>('messaging/sms-brands/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    createSmsBrand: (data: CreateSmsBrandBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsBrandData>('messaging/sms-brands/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listSmsBrandsCount: (query?: ListSmsBrandsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListSmsBrandsCountData>('messaging/sms-brands/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    readSmsBrand: (smsBrandId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSmsBrandData>(`messaging/sms-brands/${encodePathParam(smsBrandId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    updateSmsBrand: (smsBrandId: string, data: UpdateSmsBrandBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSmsBrandData>(`messaging/sms-brands/${encodePathParam(smsBrandId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deleteSmsBrand: (smsBrandId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsBrandData>(`messaging/sms-brands/${encodePathParam(smsBrandId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
