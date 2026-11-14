import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createContact']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createContact']['responses']['201']['content']['application/json']['data']>
type SuppressMessagesBody = NonNullable<operations['suppressContactMessages']['requestBody']>['content']['application/json']
type SuppressMessagesData = NonNullable<operations['suppressContactMessages']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateContact']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateContact']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteContact']['responses']['200']['content']['application/json']['data']>
type ListBody = NonNullable<operations['listContacts']['requestBody']>['content']['application/json']
type ListData = NonNullable<operations['listContacts']['responses']['200']['content']['application/json']['data']>[number]
type AddPropertiesData = NonNullable<operations['addContactProperties']['responses']['200']['content']['application/json']['data']>
type UpdatePropertyData = NonNullable<operations['updateContactProperty']['responses']['200']['content']['application/json']['data']>
type DeletePropertiesData = NonNullable<operations['deleteContactProperties']['responses']['200']['content']['application/json']['data']>

export function createMessagingContacts(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/contacts/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    suppressMessages: (contactId: string, data: SuppressMessagesBody, options?: ConjoinCallOptions) =>
      client.fetch<SuppressMessagesData>(`messaging/contacts/${encodePathParam(contactId)}/unsubscribe`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    update: (contactId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`messaging/contacts/${encodePathParam(contactId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    delete: (contactId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/contacts/${encodePathParam(contactId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    list: (data: ListBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/contacts/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    addProperties: (contactId: string, options?: ConjoinCallOptions) =>
      client.fetch<AddPropertiesData>(`messaging/contacts/${encodePathParam(contactId)}/properties`, { ...options, method: 'PUT', scopes: ['messagingProfileId'] }),

    updateProperty: (contactId: string, options?: ConjoinCallOptions) =>
      client.fetch<UpdatePropertyData>(`messaging/contacts/${encodePathParam(contactId)}/properties`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    deleteProperties: (contactId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeletePropertiesData>(`messaging/contacts/${encodePathParam(contactId)}/properties`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
