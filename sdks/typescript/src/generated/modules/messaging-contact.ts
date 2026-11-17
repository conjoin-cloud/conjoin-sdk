import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listContacts']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listContacts']['parameters']['query']>
type CreateBody = NonNullable<operations['createContact']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createContact']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listContactsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listContactsCount']['parameters']['query']>
type SuppressMessagesBody = NonNullable<operations['suppressContactMessages']['requestBody']>['content']['application/json']
type SuppressMessagesData = NonNullable<operations['suppressContactMessages']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateContact']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateContact']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteContact']['responses']['200']['content']['application/json']['data']>
type AddPropertiesBody = NonNullable<operations['addContactProperties']['requestBody']>['content']['application/json']
type AddPropertiesData = NonNullable<operations['addContactProperties']['responses']['200']['content']['application/json']['data']>
type UpdatePropertyBody = NonNullable<operations['updateContactProperty']['requestBody']>['content']['application/json']
type UpdatePropertyData = NonNullable<operations['updateContactProperty']['responses']['200']['content']['application/json']['data']>
type DeletePropertyValueData = NonNullable<operations['deleteContactPropertyValue']['responses']['200']['content']['application/json']['data']>

export function createMessagingContacts(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/contacts/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/contacts/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('messaging/contacts/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    suppressMessages: (contactId: string, data: SuppressMessagesBody, options?: ConjoinCallOptions) =>
      client.fetch<SuppressMessagesData>(`messaging/contacts/${encodePathParam(contactId)}/unsubscribe`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    update: (contactId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`messaging/contacts/${encodePathParam(contactId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    delete: (contactId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/contacts/${encodePathParam(contactId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    addProperties: (contactId: string, data: AddPropertiesBody, options?: ConjoinCallOptions) =>
      client.fetch<AddPropertiesData>(`messaging/contacts/${encodePathParam(contactId)}/properties`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    updateProperty: (contactId: string, propertyId: string, data: UpdatePropertyBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdatePropertyData>(`messaging/contacts/${encodePathParam(contactId)}/properties/${encodePathParam(propertyId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deletePropertyValue: (contactId: string, propertyId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeletePropertyValueData>(`messaging/contacts/${encodePathParam(contactId)}/properties/${encodePathParam(propertyId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
