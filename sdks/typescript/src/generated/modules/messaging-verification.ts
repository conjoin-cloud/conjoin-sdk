import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListMessagesData = NonNullable<operations['listVerificationMessages']['responses']['200']['content']['application/json']['data']>[number]
type ListMessagesQuery = NonNullable<operations['listVerificationMessages']['parameters']['query']>
type CreateBody = NonNullable<operations['createVerification']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createVerification']['responses']['200']['content']['application/json']['data']>
type ListMessagesCountData = NonNullable<operations['listVerificationMessagesCount']['responses']['200']['content']['application/json']['data']>
type ListMessagesCountQuery = NonNullable<operations['listVerificationMessagesCount']['parameters']['query']>
type CheckBody = NonNullable<operations['checkVerification']['requestBody']>['content']['application/json']
type CheckData = NonNullable<operations['checkVerification']['responses']['200']['content']['application/json']['data']>
type ResendData = NonNullable<operations['resendVerification']['responses']['200']['content']['application/json']['data']>

export function createMessagingVerifications(client: ConjoinClient) {
  return {
    listMessages: (query: ListMessagesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListMessagesData>('messaging/verifications/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/verifications/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listMessagesCount: (query: ListMessagesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListMessagesCountData>('messaging/verifications/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    check: (verificationId: string, data: CheckBody, options?: ConjoinCallOptions) =>
      client.fetch<CheckData>(`messaging/verifications/${encodePathParam(verificationId)}/check`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    resend: (verificationId: string, options?: ConjoinCallOptions) =>
      client.fetch<ResendData>(`messaging/verifications/${encodePathParam(verificationId)}/resend`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
