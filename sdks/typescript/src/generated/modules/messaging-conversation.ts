import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listConversations']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listConversations']['parameters']['query']>
type CreateBody = NonNullable<operations['createConversation']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createConversation']['responses']['201']['content']['application/json']['data']>
type ListMessagesData = NonNullable<operations['listConversationMessages']['responses']['200']['content']['application/json']['data']>[number]
type ListMessagesQuery = NonNullable<operations['listConversationMessages']['parameters']['query']>
type ListRecipientsData = NonNullable<operations['listConversationRecipients']['responses']['200']['content']['application/json']['data']>[number]
type ListRecipientsQuery = NonNullable<operations['listConversationRecipients']['parameters']['query']>
type AddOneRecipientBody = NonNullable<operations['addOneConversationRecipient']['requestBody']>['content']['application/json']
type AddOneRecipientData = NonNullable<operations['addOneConversationRecipient']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listConversationsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listConversationsCount']['parameters']['query']>
type ListMessagesCountData = NonNullable<operations['listConversationMessagesCount']['responses']['200']['content']['application/json']['data']>
type ListMessagesCountQuery = NonNullable<operations['listConversationMessagesCount']['parameters']['query']>
type ListRecipientsCountData = NonNullable<operations['listConversationRecipientsCount']['responses']['200']['content']['application/json']['data']>
type ListRecipientsCountQuery = NonNullable<operations['listConversationRecipientsCount']['parameters']['query']>
type DuplicateBody = NonNullable<operations['duplicateConversation']['requestBody']>['content']['application/json']
type DuplicateData = NonNullable<operations['duplicateConversation']['responses']['201']['content']['application/json']['data']>
type SendMessageBody = NonNullable<operations['sendConversationMessage']['requestBody']>['content']['application/json']
type SendMessageData = NonNullable<operations['sendConversationMessage']['responses']['201']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteConversation']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateConversation']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateConversation']['responses']['200']['content']['application/json']['data']>
type ArchiveData = NonNullable<operations['archiveConversation']['responses']['200']['content']['application/json']['data']>
type ReadOneRecipientData = NonNullable<operations['readOneConversationRecipient']['responses']['200']['content']['application/json']['data']>
type DeleteRecipientsData = NonNullable<operations['deleteConversationRecipients']['responses']['200']['content']['application/json']['data']>
type AddManyRecipientsBody = NonNullable<operations['addManyConversationRecipients']['requestBody']>['content']['application/json']
type AddManyRecipientsData = NonNullable<operations['addManyConversationRecipients']['responses']['201']['content']['application/json']['data']>[number]

export function createMessagingConversations(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/conversations/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/conversations/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listMessages: (conversationId: string, query: ListMessagesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListMessagesData>(`messaging/conversations/${encodePathParam(conversationId)}/messages`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    listRecipients: (conversationId: string, query?: ListRecipientsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListRecipientsData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    addOneRecipient: (conversationId: string, data: AddOneRecipientBody, options?: ConjoinCallOptions) =>
      client.fetch<AddOneRecipientData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('messaging/conversations/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    listMessagesCount: (conversationId: string, query: ListMessagesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListMessagesCountData>(`messaging/conversations/${encodePathParam(conversationId)}/messages/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    listRecipientsCount: (conversationId: string, query?: ListRecipientsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListRecipientsCountData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    duplicate: (conversationId: string, data: DuplicateBody, options?: ConjoinCallOptions) =>
      client.fetch<DuplicateData>(`messaging/conversations/${encodePathParam(conversationId)}/duplicate`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    sendMessage: (conversationId: string, data: SendMessageBody, options?: ConjoinCallOptions) =>
      client.fetch<SendMessageData>(`messaging/conversations/${encodePathParam(conversationId)}/send`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    delete: (conversationId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/conversations/${encodePathParam(conversationId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    update: (conversationId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`messaging/conversations/${encodePathParam(conversationId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    archive: (conversationId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`messaging/conversations/${encodePathParam(conversationId)}/archive`, { ...options, method: 'POST', scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    readOneRecipient: (conversationId: string, recipientId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadOneRecipientData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients/${encodePathParam(recipientId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    deleteRecipients: (conversationId: string, recipientId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteRecipientsData>(`messaging/conversations/${encodePathParam(conversationId)}/recipients/${encodePathParam(recipientId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    addManyRecipients: (conversationId: string, data: AddManyRecipientsBody, options?: ConjoinCallOptions) =>
      client.fetchList<AddManyRecipientsData>(`messaging/conversations/${encodePathParam(conversationId)}/add-recipients`, { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),
  }
}
