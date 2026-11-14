import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createVerification']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createVerification']['responses']['200']['content']['application/json']['data']>
type CheckBody = NonNullable<operations['checkVerification']['requestBody']>['content']['application/json']
type CheckData = NonNullable<operations['checkVerification']['responses']['200']['content']['application/json']['data']>
type ResendBody = NonNullable<operations['resendVerification']['requestBody']>['content']['application/json']
type ResendData = NonNullable<operations['resendVerification']['responses']['200']['content']['application/json']['data']>
type ListMessagesBody = NonNullable<operations['listVerificationMessages']['requestBody']>['content']['application/json']
type ListMessagesData = NonNullable<operations['listVerificationMessages']['responses']['200']['content']['application/json']['data']>[number]

export function createMessagingVerifications(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/otps/send', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    check: (token: string, data: CheckBody, options?: ConjoinCallOptions) =>
      client.fetch<CheckData>(`messaging/otps/verify/${encodePathParam(token)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    resend: (verificationId: string, data: ResendBody, options?: ConjoinCallOptions) =>
      client.fetch<ResendData>(`messaging/otps/resend/${encodePathParam(verificationId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    listMessages: (data: ListMessagesBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListMessagesData>('messaging/otps/messages', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),
  }
}
