import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateContactPropertyBody = NonNullable<operations['createContactProperty']['requestBody']>['content']['application/json']
type CreateContactPropertyData = NonNullable<operations['createContactProperty']['responses']['201']['content']['application/json']['data']>
type FetchOneContactPropertyData = NonNullable<operations['fetchOneContactProperty']['responses']['200']['content']['application/json']['data']>
type DeleteContactPropertyData = NonNullable<operations['deleteContactProperty']['responses']['200']['content']['application/json']['data']>
type ListBody = NonNullable<operations['listContactProperties']['requestBody']>['content']['application/json']
type ListData = NonNullable<operations['listContactProperties']['responses']['200']['content']['application/json']['data']>[number]
type DeleteManyBody = NonNullable<operations['deleteManyContactProperties']['requestBody']>['content']['application/json']
type DeleteManyData = NonNullable<operations['deleteManyContactProperties']['responses']['200']['content']['application/json']['data']>[number]

export function createMessagingContactProperties(client: ConjoinClient) {
  return {
    createContactProperty: (data: CreateContactPropertyBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateContactPropertyData>('messaging/contacts/properties', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    fetchOneContactProperty: (propertyId: string, options?: ConjoinCallOptions) =>
      client.fetch<FetchOneContactPropertyData>(`messaging/contacts/properties/${encodePathParam(propertyId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteContactProperty: (propertyId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteContactPropertyData>(`messaging/contacts/properties/${encodePathParam(propertyId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    list: (data: ListBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/contacts/properties/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true, cursorLocation: 'body' }),

    deleteMany: (data: DeleteManyBody, options?: ConjoinCallOptions) =>
      client.fetchList<DeleteManyData>('messaging/contacts/properties/remove', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true, cursorLocation: 'none' }),
  }
}
