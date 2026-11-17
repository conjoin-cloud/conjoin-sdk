package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListConversationsQuery struct {
	ConversationID any                                   `json:"conversation_id,omitzero"`
	ReferenceID    any                                   `json:"reference_id,omitzero"`
	Title          any                                   `json:"title,omitzero"`
	AcceptsReplies any                                   `json:"accepts_replies,omitzero"`
	DateCreated    *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	DateArchived   *ListChannelAnalyticsQueryDateCreated `json:"date_archived,omitzero"`
	Search         *string                               `json:"search,omitzero"`
	Cursor         *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort           map[string]string                     `json:"sort,omitzero"`
	Limit          any                                   `json:"limit,omitzero"`
}

type ListConversationsItem struct {
	ConversationID   string                           `json:"conversation_id"`
	ProfileID        string                           `json:"profile_id"`
	ConjoinAccountID string                           `json:"conjoin_account_id"`
	ConjoinProjectID string                           `json:"conjoin_project_id"`
	LiveMode         bool                             `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string]         `json:"reference_id,omitzero"`
	Title            string                           `json:"title"`
	Description      *string                          `json:"description,omitzero"`
	MessageChannels  map[string]any                   `json:"message_channels"`
	Senders          conjoin.Nullable[map[string]any] `json:"senders,omitzero"`
	AcceptsReplies   bool                             `json:"accepts_replies"`
	TotalRecipients  float64                          `json:"total_recipients"`
	Placeholders     conjoin.Nullable[map[string]any] `json:"placeholders,omitzero"`
	DateArchived     conjoin.Nullable[string]         `json:"date_archived,omitzero"`
	DateCreated      string                           `json:"date_created"`
	DateUpdated      string                           `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]         `json:"date_deleted,omitzero"`
}

type CreateConversationRequestSendersSMS struct {
	Type         *string `json:"type,omitzero"`
	SenderPoolID *string `json:"sender_pool_id,omitzero"`
	Sender       *string `json:"sender,omitzero"`
}

type CreateConversationRequestSenders struct {
	SMS   *CreateConversationRequestSendersSMS `json:"sms,omitzero"`
	Email *CreateConversationRequestSendersSMS `json:"email,omitzero"`
}

type CreateConversationRequest struct {
	ReferenceID         *string                           `json:"reference_id,omitzero"`
	Title               string                            `json:"title"`
	Channels            []string                          `json:"channels"`
	Description         *string                           `json:"description,omitzero"`
	Senders             *CreateConversationRequestSenders `json:"senders,omitzero"`
	Recipients          []CreateContactRequest            `json:"recipients,omitzero"`
	DefaultPlaceholders map[string]string                 `json:"default_placeholders,omitzero"`
	AcceptsReplies      *bool                             `json:"accepts_replies,omitzero"`
}

type CreateConversationResponse = ListConversationsItem

type ListConversationMessagesQuery struct {
	ParentMessageID *string                          `json:"parent_message_id,omitzero"`
	ReferenceID     any                              `json:"reference_id,omitzero"`
	Search          *string                          `json:"search,omitzero"`
	Channel         string                           `json:"channel"`
	Cursor          *ListChannelAnalyticsQueryCursor `json:"cursor,omitzero"`
	Sort            map[string]string                `json:"sort,omitzero"`
	Limit           any                              `json:"limit,omitzero"`
}

type ListConversationMessagesItem struct {
	MessageID           *string                  `json:"message_id,omitzero"`
	ProfileID           *string                  `json:"profile_id,omitzero"`
	ConjoinAccountID    *string                  `json:"conjoin_account_id,omitzero"`
	ConjoinProjectID    *string                  `json:"conjoin_project_id,omitzero"`
	LiveMode            *bool                    `json:"live_mode,omitzero"`
	ReferenceID         conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ConversationID      conjoin.Nullable[string] `json:"conversation_id,omitzero"`
	ParentMessageID     conjoin.Nullable[string] `json:"parent_message_id,omitzero"`
	Type                *string                  `json:"type,omitzero"`
	ReplyTo             conjoin.Nullable[string] `json:"reply_to,omitzero"`
	DefaultPlaceholders map[string]any           `json:"default_placeholders,omitzero"`
	SentAt              *string                  `json:"sent_at,omitzero"`
	Body                *string                  `json:"body,omitzero"`
	TruncateMessage     *bool                    `json:"truncate_message,omitzero"`
	SendAt              conjoin.Nullable[string] `json:"send_at,omitzero"`
	Status              *string                  `json:"status,omitzero"`
	DateCreated         *string                  `json:"date_created,omitzero"`
	DateUpdated         *string                  `json:"date_updated,omitzero"`
	DateDeleted         conjoin.Nullable[string] `json:"date_deleted,omitzero"`
	ReplyCount          *float64                 `json:"reply_count,omitzero"`
	From                *string                  `json:"from,omitzero"`
	Subject             *string                  `json:"subject,omitzero"`
	Cc                  []string                 `json:"cc,omitzero"`
	Bcc                 []string                 `json:"bcc,omitzero"`
	Attachments         []map[string]any         `json:"attachments,omitzero"`
	Tracking            map[string]any           `json:"tracking,omitzero"`
	AcceptsReplies      *bool                    `json:"accepts_replies,omitzero"`
}

type ListConversationRecipientsQuery struct {
	ReferenceID any                                   `json:"reference_id,omitzero"`
	ContactID   any                                   `json:"contact_id,omitzero"`
	DateCreated *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                     `json:"sort,omitzero"`
	Limit       any                                   `json:"limit,omitzero"`
}

type ListConversationRecipientsItem struct {
	ProfileID        string                   `json:"profile_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ContactID        string                   `json:"contact_id"`
	ConversationID   string                   `json:"conversation_id"`
	RecipientID      string                   `json:"recipient_id"`
	DateArchived     conjoin.Nullable[string] `json:"date_archived,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type AddOneConversationRecipientRequest = CreateContactRequest

type AddOneConversationRecipientResponse = ListConversationRecipientsItem

type ListConversationsCountQuery = ListConversationsQuery

type ListConversationsCountResponse = ListChannelAnalyticsCountResponse

type ListConversationMessagesCountQuery = ListConversationMessagesQuery

type ListConversationMessagesCountResponse = ListChannelAnalyticsCountResponse

type ListConversationRecipientsCountQuery = ListConversationRecipientsQuery

type ListConversationRecipientsCountResponse = ListChannelAnalyticsCountResponse

type DuplicateConversationRequest struct {
	Title          *string `json:"title,omitzero"`
	Description    *string `json:"description,omitzero"`
	AcceptsReplies *bool   `json:"accepts_replies,omitzero"`
}

type DuplicateConversationResponse = ListConversationsItem

type SendConversationMessageRequestMessagesSMS struct {
	ReferenceID         *string        `json:"reference_id,omitzero"`
	TemplateID          *string        `json:"template_id,omitzero"`
	SenderPoolID        *string        `json:"sender_pool_id,omitzero"`
	From                *string        `json:"from,omitzero"`
	DefaultPlaceholders map[string]any `json:"default_placeholders,omitzero"`
	Body                *string        `json:"body,omitzero"`
	ReplyTo             *string        `json:"reply_to,omitzero"`
}

type SendConversationMessageRequestMessagesEmailAttachmentsItem struct {
	ContentID *string `json:"content_id,omitzero"`
	FileName  string  `json:"file_name"`
	MimeType  string  `json:"mime_type"`
	Content   string  `json:"content"`
}

type SendConversationMessageRequestMessagesEmail struct {
	ReferenceID         *string                                                      `json:"reference_id,omitzero"`
	TemplateID          *string                                                      `json:"template_id,omitzero"`
	SenderPoolID        *string                                                      `json:"sender_pool_id,omitzero"`
	From                *string                                                      `json:"from,omitzero"`
	DefaultPlaceholders map[string]any                                               `json:"default_placeholders,omitzero"`
	Subject             string                                                       `json:"subject"`
	HTML                *string                                                      `json:"html,omitzero"`
	Text                *string                                                      `json:"text,omitzero"`
	Cc                  []string                                                     `json:"cc,omitzero"`
	Bcc                 []string                                                     `json:"bcc,omitzero"`
	Attachments         []SendConversationMessageRequestMessagesEmailAttachmentsItem `json:"attachments,omitzero"`
	ReplyTo             *string                                                      `json:"reply_to,omitzero"`
	AcceptsReplies      *bool                                                        `json:"accepts_replies,omitzero"`
}

type SendConversationMessageRequestMessages struct {
	SMS   *SendConversationMessageRequestMessagesSMS   `json:"sms,omitzero"`
	Email *SendConversationMessageRequestMessagesEmail `json:"email,omitzero"`
}

type SendConversationMessageRequestToItem struct {
	ReferenceID  *string        `json:"reference_id,omitzero"`
	PhoneNumber  *string        `json:"phone_number,omitzero"`
	Email        *string        `json:"email,omitzero"`
	Placeholders map[string]any `json:"placeholders,omitzero"`
	Timezone     *string        `json:"timezone,omitzero"`
}

type SendConversationMessageRequest struct {
	MessagePriority      *string                                `json:"message_priority,omitzero"`
	Messages             SendConversationMessageRequestMessages `json:"messages"`
	MessageRetryStatuses []string                               `json:"message_retry_statuses,omitzero"`
	To                   []SendConversationMessageRequestToItem `json:"to,omitzero"`
	DefaultPlaceholders  map[string]any                         `json:"default_placeholders,omitzero"`
	Body                 *string                                `json:"body,omitzero"`
	SendAt               *string                                `json:"send_at,omitzero"`
}

type DeleteConversationResponse = ListConversationsItem

type UpdateConversationRequest = DuplicateConversationRequest

type UpdateConversationResponse = ListConversationsItem

type ArchiveConversationResponse = ListConversationsItem

type ReadOneConversationRecipientResponse = ListConversationRecipientsItem

type DeleteConversationRecipientsResponse = ListConversationRecipientsItem

type AddManyConversationRecipientsRequest struct {
	Recipients []CreateContactRequest `json:"recipients"`
}

type AddManyConversationRecipientsItem = ListConversationRecipientsItem
