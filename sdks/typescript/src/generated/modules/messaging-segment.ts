import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateOneBody = NonNullable<operations['createOneSegment']['requestBody']>['content']['application/json']
type CreateOneData = NonNullable<operations['createOneSegment']['responses']['201']['content']['application/json']['data']>
type UpdateOneBody = NonNullable<operations['updateOneSegment']['requestBody']>['content']['application/json']
type UpdateOneData = NonNullable<operations['updateOneSegment']['responses']['201']['content']['application/json']['data']>
type DeleteOneData = NonNullable<operations['deleteOneSegment']['responses']['201']['content']['application/json']['data']>
type ListManyBody = NonNullable<operations['listManySegments']['requestBody']>['content']['application/json']
type ListManyData = NonNullable<operations['listManySegments']['responses']['201']['content']['application/json']['data']>

export function createMessagingSegments(client: ConjoinClient) {
  return {
    createOne: (data: CreateOneBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateOneData>('messaging/segments/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    updateOne: (segmentId: string, data: UpdateOneBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateOneData>(`messaging/segments/${encodePathParam(segmentId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deleteOne: (segmentId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteOneData>(`messaging/segments/${encodePathParam(segmentId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    listMany: (data: ListManyBody, options?: ConjoinCallOptions) =>
      client.fetch<ListManyData>('messaging/segments/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),
  }
}
