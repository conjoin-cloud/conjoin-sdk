import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listContactProperties']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listContactProperties']['parameters']['query']>
type CreateContactPropertyBody = NonNullable<operations['createContactProperty']['requestBody']>['content']['application/json']
type CreateContactPropertyData = NonNullable<operations['createContactProperty']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listContactPropertiesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listContactPropertiesCount']['parameters']['query']>
type FetchOneContactPropertyData = NonNullable<operations['fetchOneContactProperty']['responses']['200']['content']['application/json']['data']>
type DeleteContactPropertyData = NonNullable<operations['deleteContactProperty']['responses']['200']['content']['application/json']['data']>

export function createMessagingContactProperties(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/contact-properties/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    createContactProperty: (data: CreateContactPropertyBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateContactPropertyData>('messaging/contact-properties/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('messaging/contact-properties/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    fetchOneContactProperty: (contactPropertyId: string, options?: ConjoinCallOptions) =>
      client.fetch<FetchOneContactPropertyData>(`messaging/contact-properties/${encodePathParam(contactPropertyId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteContactProperty: (contactPropertyId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteContactPropertyData>(`messaging/contact-properties/${encodePathParam(contactPropertyId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
