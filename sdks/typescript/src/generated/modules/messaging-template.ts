import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateMessageBody = NonNullable<operations['createMessageTemplate']['requestBody']>['content']['application/json']
type CreateMessageData = NonNullable<operations['createMessageTemplate']['responses']['201']['content']['application/json']['data']>
type ListMessageBody = NonNullable<operations['listMessageTemplates']['requestBody']>['content']['application/json']
type ListMessageData = NonNullable<operations['listMessageTemplates']['responses']['200']['content']['application/json']['data']>[number]
type ReadMessageData = NonNullable<operations['readMessageTemplate']['responses']['200']['content']['application/json']['data']>
type DeleteMessageData = NonNullable<operations['deleteMessageTemplate']['responses']['200']['content']['application/json']['data']>
type UpdateMessageBody = NonNullable<operations['updateMessageTemplate']['requestBody']>['content']['application/json']
type UpdateMessageData = NonNullable<operations['updateMessageTemplate']['responses']['200']['content']['application/json']['data']>
type DeleteMessagesBody = NonNullable<operations['deleteMessageTemplates']['requestBody']>['content']['application/json']
type DeleteMessagesResponse = operations['deleteMessageTemplates']['responses']['200']['content']['application/json']

export function createMessagingTemplates(client: ConjoinClient) {
  return {
    createMessage: (data: CreateMessageBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateMessageData>('messaging/templates/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listMessage: (data: ListMessageBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListMessageData>('messaging/templates/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    readMessage: (templateId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadMessageData>(`messaging/templates/${encodePathParam(templateId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteMessage: (templateId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteMessageData>(`messaging/templates/${encodePathParam(templateId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    updateMessage: (templateId: string, data: UpdateMessageBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateMessageData>(`messaging/templates/${encodePathParam(templateId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deleteMessages: (data: DeleteMessagesBody, options?: ConjoinCallOptions) =>
      client.fetchJson<DeleteMessagesResponse>('messaging/templates/wipe', { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),
  }
}
