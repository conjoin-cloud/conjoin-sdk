import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListMessageData = NonNullable<operations['listMessageTemplates']['responses']['200']['content']['application/json']['data']>[number]
type ListMessageQuery = NonNullable<operations['listMessageTemplates']['parameters']['query']>
type CreateMessageBody = NonNullable<operations['createMessageTemplate']['requestBody']>['content']['application/json']
type CreateMessageData = NonNullable<operations['createMessageTemplate']['responses']['201']['content']['application/json']['data']>
type ListMessageCountData = NonNullable<operations['listMessageTemplatesCount']['responses']['200']['content']['application/json']['data']>
type ListMessageCountQuery = NonNullable<operations['listMessageTemplatesCount']['parameters']['query']>
type ReadMessageData = NonNullable<operations['readMessageTemplate']['responses']['200']['content']['application/json']['data']>
type DeleteMessageData = NonNullable<operations['deleteMessageTemplate']['responses']['200']['content']['application/json']['data']>
type UpdateMessageBody = NonNullable<operations['updateMessageTemplate']['requestBody']>['content']['application/json']
type UpdateMessageData = NonNullable<operations['updateMessageTemplate']['responses']['200']['content']['application/json']['data']>

export function createMessagingTemplates(client: ConjoinClient) {
  return {
    listMessage: (query?: ListMessageQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListMessageData>('messaging/templates/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    createMessage: (data: CreateMessageBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateMessageData>('messaging/templates/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listMessageCount: (query?: ListMessageCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListMessageCountData>('messaging/templates/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    readMessage: (templateId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadMessageData>(`messaging/templates/${encodePathParam(templateId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteMessage: (templateId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteMessageData>(`messaging/templates/${encodePathParam(templateId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    updateMessage: (templateId: string, data: UpdateMessageBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateMessageData>(`messaging/templates/${encodePathParam(templateId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),
  }
}
