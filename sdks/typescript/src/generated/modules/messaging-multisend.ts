import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createMultisend']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createMultisend']['responses']['200']['content']['application/json']['data']>
type ReadData = NonNullable<operations['readMultisend']['responses']['200']['content']['application/json']['data']>

export function createMessagingMultisends(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/multisend/send', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    read: (messageId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`messaging/multisend/${encodePathParam(messageId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),
  }
}
