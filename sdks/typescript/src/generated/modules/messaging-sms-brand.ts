import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateSmsBrandBody = NonNullable<operations['createSmsBrand']['requestBody']>['content']['application/json']
type CreateSmsBrandData = NonNullable<operations['createSmsBrand']['responses']['201']['content']['application/json']['data']>
type ReadSmsBrandData = NonNullable<operations['readSmsBrand']['responses']['200']['content']['application/json']['data']>
type UpdateSmsBrandBody = NonNullable<operations['updateSmsBrand']['requestBody']>['content']['application/json']
type UpdateSmsBrandData = NonNullable<operations['updateSmsBrand']['responses']['200']['content']['application/json']['data']>
type DeleteSmsBrandData = NonNullable<operations['deleteSmsBrand']['responses']['200']['content']['application/json']['data']>
type ListSmsBrandsBody = NonNullable<operations['listSmsBrands']['requestBody']>['content']['application/json']
type ListSmsBrandsData = NonNullable<operations['listSmsBrands']['responses']['200']['content']['application/json']['data']>[number]

export function createMessagingSMSBrands(client: ConjoinClient) {
  return {
    createSmsBrand: (data: CreateSmsBrandBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsBrandData>('messaging/sms/brands/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    readSmsBrand: (brandId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSmsBrandData>(`messaging/sms/brands/${encodePathParam(brandId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    updateSmsBrand: (brandId: string, data: UpdateSmsBrandBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSmsBrandData>(`messaging/sms/brands/${encodePathParam(brandId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deleteSmsBrand: (brandId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsBrandData>(`messaging/sms/brands/${encodePathParam(brandId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    listSmsBrands: (data: ListSmsBrandsBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListSmsBrandsData>('messaging/sms/brands/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),
  }
}
