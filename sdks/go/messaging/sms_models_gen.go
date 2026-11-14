package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type SendSmsRequest struct {
	ReferenceID         *string        `json:"reference_id,omitzero"`
	TemplateID          *string        `json:"template_id,omitzero"`
	SenderPoolID        *string        `json:"sender_pool_id,omitzero"`
	From                *string        `json:"from,omitzero"`
	To                  []any          `json:"to,omitzero"`
	DefaultPlaceholders map[string]any `json:"default_placeholders,omitzero"`
	Body                *string        `json:"body,omitzero"`
	TruncateMessage     *bool          `json:"truncate_message,omitzero"`
	SendAt              *string        `json:"send_at,omitzero"`
	ReplyTo             *string        `json:"reply_to,omitzero"`
	CreateConversation  *bool          `json:"create_conversation,omitzero"`
}

type SendSmsResponse struct {
	MessageID           string                   `json:"message_id"`
	ProfileID           string                   `json:"profile_id"`
	ConjoinAccountID    string                   `json:"conjoin_account_id"`
	ConjoinProjectID    string                   `json:"conjoin_project_id"`
	LiveMode            bool                     `json:"live_mode"`
	ReferenceID         conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ConversationID      conjoin.Nullable[string] `json:"conversation_id,omitzero"`
	ParentMessageID     conjoin.Nullable[string] `json:"parent_message_id,omitzero"`
	Type                string                   `json:"type"`
	ReplyTo             conjoin.Nullable[string] `json:"reply_to,omitzero"`
	DefaultPlaceholders map[string]any           `json:"default_placeholders,omitzero"`
	SentAt              string                   `json:"sent_at"`
	Body                string                   `json:"body"`
	TruncateMessage     bool                     `json:"truncate_message"`
	SendAt              conjoin.Nullable[string] `json:"send_at,omitzero"`
	Status              string                   `json:"status"`
	DateCreated         string                   `json:"date_created"`
	DateUpdated         string                   `json:"date_updated"`
	DateDeleted         conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ReadSmsMessagesRequestBodyQuery struct {
	ConversationID any `json:"conversation_id,omitzero"`
	BroadcastID    any `json:"broadcast_id,omitzero"`
	RequestID      any `json:"request_id,omitzero"`
	MessageID      any `json:"message_id,omitzero"`
	RecipientID    any `json:"recipient_id,omitzero"`
	Name           any `json:"name,omitzero"`
	PhoneNumber    any `json:"phone_number,omitzero"`
	Status         any `json:"status,omitzero"`
}

type ReadSmsMessagesRequestBody struct {
	Cursor *ListContactsRequestCursor       `json:"cursor,omitzero"`
	Query  *ReadSmsMessagesRequestBodyQuery `json:"query,omitzero"`
	Search *ListContactsRequestSearch       `json:"search,omitzero"`
	Sort   map[string]string                `json:"sort,omitzero"`
	Limit  any                              `json:"limit,omitzero"`
}

type ReadSmsMessagesRequest struct {
	Body ReadSmsMessagesRequestBody `json:"body"`
}

type ReadSmsMessagesItem = SendSmsResponse

type GetSmsSummaryResponse = GetEmailSummaryResponse
