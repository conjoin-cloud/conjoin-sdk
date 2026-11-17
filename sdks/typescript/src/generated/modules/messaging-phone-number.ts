import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listPhoneNumbers']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPhoneNumbers']['parameters']['query']>
type PurchaseBody = NonNullable<operations['purchasePhoneNumber']['requestBody']>['content']['application/json']
type PurchaseData = NonNullable<operations['purchasePhoneNumber']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listPhoneNumbersCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPhoneNumbersCount']['parameters']['query']>
type TransferBody = NonNullable<operations['transferPhoneNumber']['requestBody']>['content']['application/json']
type TransferData = NonNullable<operations['transferPhoneNumber']['responses']['200']['content']['application/json']['data']>
type ReleaseData = NonNullable<operations['releasePhoneNumber']['responses']['200']['content']['application/json']['data']>
type ListAvailableData = NonNullable<operations['listAvailablePhoneNumbers']['responses']['200']['content']['application/json']['data']>[number]
type ListAvailableQuery = NonNullable<operations['listAvailablePhoneNumbers']['parameters']['query']>

export function createMessagingPhoneNumbers(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/phone-numbers/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    purchase: (data: PurchaseBody, options?: ConjoinCallOptions) =>
      client.fetch<PurchaseData>('messaging/phone-numbers/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('messaging/phone-numbers/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    transfer: (phoneNumberId: string, data: TransferBody, options?: ConjoinCallOptions) =>
      client.fetch<TransferData>(`messaging/phone-numbers/${encodePathParam(phoneNumberId)}/transfer`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    release: (phoneNumberId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReleaseData>(`messaging/phone-numbers/${encodePathParam(phoneNumberId)}/release`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listAvailable: (query?: ListAvailableQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListAvailableData>('messaging/available-phone-numbers/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),
  }
}
