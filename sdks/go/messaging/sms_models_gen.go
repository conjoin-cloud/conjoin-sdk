package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSmsMessagesQuery struct {
	ConversationID any                                   `json:"conversation_id,omitzero"`
	BroadcastID    any                                   `json:"broadcast_id,omitzero"`
	RequestID      any                                   `json:"request_id,omitzero"`
	MessageID      any                                   `json:"message_id,omitzero"`
	RecipientID    any                                   `json:"recipient_id,omitzero"`
	ReferenceID    any                                   `json:"reference_id,omitzero"`
	Name           any                                   `json:"name,omitzero"`
	PhoneNumber    any                                   `json:"phone_number,omitzero"`
	Status         any                                   `json:"status,omitzero"`
	SentAt         *ListChannelAnalyticsQueryDateCreated `json:"sent_at,omitzero"`
	DateCreated    *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	Search         *string                               `json:"search,omitzero"`
	Cursor         *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort           map[string]string                     `json:"sort,omitzero"`
	Limit          any                                   `json:"limit,omitzero"`
}

type ListSmsMessagesItem struct {
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

type SendSmsResponse = ListSmsMessagesItem

type ListSmsMessagesCountQuery = ListSmsMessagesQuery

type ListSmsMessagesCountResponse = ListChannelAnalyticsCountResponse

type ReadSmsMessageResponse = ListSmsMessagesItem

type GenerateSmsSummaryRequest struct {
	Currency            string            `json:"currency"`
	Message             string            `json:"message"`
	To                  []any             `json:"to,omitzero"`
	DefaultPlaceholders map[string]string `json:"default_placeholders,omitzero"`
	TruncateMessage     *bool             `json:"truncate_message,omitzero"`
}

type GenerateSmsSummaryResponseDestinationsValue struct {
	TotalRecipients float64 `json:"total_recipients"`
	MessageParts    float64 `json:"message_parts"`
}

type GenerateSmsSummaryResponse struct {
	Destinations      map[string]GenerateSmsSummaryResponseDestinationsValue `json:"destinations"`
	TotalMessageParts float64                                                `json:"total_message_parts"`
	MessageBody       string                                                 `json:"message_body"`
	MaxCharacters     float64                                                `json:"max_characters"`
	PricePerPart      float64                                                `json:"price_per_part"`
	TotalPrice        float64                                                `json:"total_price"`
	Currency          string                                                 `json:"currency"`
}
