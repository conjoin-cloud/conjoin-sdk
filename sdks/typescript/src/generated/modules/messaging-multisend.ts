import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createMultisend']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createMultisend']['responses']['200']['content']['application/json']['data']>
type ReadData = NonNullable<operations['readMultisend']['responses']['200']['content']['application/json']['data']>

export function createMessagingMultisends(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/broadcasts/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    read: (broadcastId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`messaging/broadcasts/${encodePathParam(broadcastId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),
  }
}
