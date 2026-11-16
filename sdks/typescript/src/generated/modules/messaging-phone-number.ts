import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type PurchaseBody = NonNullable<operations['purchasePhoneNumber']['requestBody']>['content']['application/json']
type PurchaseData = NonNullable<operations['purchasePhoneNumber']['responses']['201']['content']['application/json']['data']>
type UpdateData = NonNullable<operations['updatePhoneNumber']['responses']['200']['content']['application/json']['data']>
type ListAvailableData = NonNullable<operations['listAvailablePhoneNumbers']['responses']['200']['content']['application/json']['data']>[number]
type ListAvailableQuery = NonNullable<operations['listAvailablePhoneNumbers']['parameters']['query']>
type ListData = NonNullable<operations['listPhoneNumbers']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPhoneNumbers']['parameters']['query']>
type ReleaseData = NonNullable<operations['releasePhoneNumber']['responses']['200']['content']['application/json']['data']>

export function createMessagingPhoneNumbers(client: ConjoinClient) {
  return {
    purchase: (phoneNumber: string, data: PurchaseBody, options?: ConjoinCallOptions) =>
      client.fetch<PurchaseData>(`messaging/phone-numbers/${encodePathParam(phoneNumber)}/provision`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    update: (phoneNumber: string, projectId: string, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`messaging/phone-numbers/transfer/${encodePathParam(phoneNumber)}/project/${encodePathParam(projectId)}`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    listAvailable: (query?: ListAvailableQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListAvailableData>('messaging/phone-numbers/available', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'], cursorLocation: 'none' }),

    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/phone-numbers/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    release: (phoneNumber: string, options?: ConjoinCallOptions) =>
      client.fetch<ReleaseData>(`messaging/phone-numbers/${encodePathParam(phoneNumber)}/release`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
