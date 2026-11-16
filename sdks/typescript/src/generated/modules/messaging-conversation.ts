import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createConversation']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createConversation']['responses']['201']['content']['application/json']['data']>
type CloneBody = NonNullable<operations['cloneConversation']['requestBody']>['content']['application/json']
type CloneData = NonNullable<operations['cloneConversation']['responses']['201']['content']['application/json']['data']>
type SendMessageBody = NonNullable<operations['sendConversationMessage']['requestBody']>['content']['application/json']
type SendMessageData = NonNullable<operations['sendConversationMessage']['responses']['201']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteConversation']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateConversation']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateConversation']['responses']['200']['content']['application/json']['data']>
type ArchiveData = NonNullable<operations['archiveConversation']['responses']['200']['content']['application/json']['data']>
type ListBody = NonNullable<operations['listConversations']['requestBody']>['content']['application/json']
type ListData = NonNullable<operations['listConversations']['responses']['200']['content']['application/json']['data']>[number]
type ReadMessagesBody = NonNullable<operations['readConversationMessages']['requestBody']>['content']['application/json']
type ReadMessagesData = NonNullable<operations['readConversationMessages']['responses']['200']['content']['application/json']['data']>[number]
type ReadOneRecipientData = NonNullable<operations['readOneConversationRecipient']['responses']['200']['content']['application/json']['data']>
type DeleteRecipientsData = NonNullable<operations['deleteConversationRecipients']['responses']['200']['content']['application/json']['data']>
type ReadManyRecipientsBody = NonNullable<operations['readManyConversationRecipients']['requestBody']>['content']['application/json']
type ReadManyRecipientsData = NonNullable<operations['readManyConversationRecipients']['responses']['200']['content']['application/json']['data']>[number]
type AddOneRecipientBody = NonNullable<operations['addOneConversationRecipient']['requestBody']>['content']['application/json']
type AddOneRecipientData = NonNullable<operations['addOneConversationRecipient']['responses']['201']['content']['application/json']['data']>
type AddManyRecipientsBody = NonNullable<operations['addManyConversationRecipients']['requestBody']>['content']['application/json']
type AddManyRecipientsData = NonNullable<operations['addManyConversationRecipients']['responses']['201']['content']['application/json']['data']>[number]

export function createMessagingConversations(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/conversations/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    clone: (conversationId: string, data: CloneBody, options?: ConjoinCallOptions) =>
      client.fetch<CloneData>(`messaging/conversations/${encodePathParam(conversationId)}/clone`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    sendMessage: (conversationId: string, data: SendMessageBody, options?: ConjoinCallOptions) =>
      client.fetch<SendMessageData>(`messaging/conversations/${encodePathParam(conversationId)}/send`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    delete: (conversationId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/conversations/${encodePathParam(conversationId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    update: (conversationId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`messaging/conversations/${encodePathParam(conversationId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    archive: (conversationId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`messaging/conversations/${encodePathParam(conversationId)}/archive`, { ...options, method: 'PATCH', scopes: ['messagingProfileId'] }),

    list: (data: ListBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/conversations/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true, cursorLocation: 'body' }),

    readMessages: (conversationId: string, parentMessageId: string, data: ReadMessagesBody, options?: ConjoinCallOptions) =>
      client.fetchList<ReadMessagesData>(`messaging/conversations/${encodePathParam(conversationId)}/messages/${encodePathParam(parentMessageId)}`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true, cursorLocation: 'body' }),

    readOneRecipient: (conversationId: string, recipientId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadOneRecipientData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients/${encodePathParam(recipientId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteRecipients: (conversationId: string, recipientId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteRecipientsData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients/${encodePathParam(recipientId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    readManyRecipients: (conversationId: string, data: ReadManyRecipientsBody, options?: ConjoinCallOptions) =>
      client.fetchList<ReadManyRecipientsData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients/retrieve`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true, cursorLocation: 'body' }),

    addOneRecipient: (conversationId: string, data: AddOneRecipientBody, options?: ConjoinCallOptions) =>
      client.fetch<AddOneRecipientData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    addManyRecipients: (conversationId: string, data: AddManyRecipientsBody, options?: ConjoinCallOptions) =>
      client.fetchList<AddManyRecipientsData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients/batch`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true, cursorLocation: 'none' }),
  }
}
