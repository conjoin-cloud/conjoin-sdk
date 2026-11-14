package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type SendEmailRequest struct {
	ReferenceID         *string                                                      `json:"reference_id,omitzero"`
	TemplateID          *string                                                      `json:"template_id,omitzero"`
	SenderPoolID        *string                                                      `json:"sender_pool_id,omitzero"`
	From                *string                                                      `json:"from,omitzero"`
	To                  []any                                                        `json:"to,omitzero"`
	DefaultPlaceholders map[string]any                                               `json:"default_placeholders,omitzero"`
	Subject             string                                                       `json:"subject"`
	HTML                *string                                                      `json:"html,omitzero"`
	Text                *string                                                      `json:"text,omitzero"`
	Cc                  []string                                                     `json:"cc,omitzero"`
	Bcc                 []string                                                     `json:"bcc,omitzero"`
	Attachments         []SendConversationMessageRequestMessagesEmailAttachmentsItem `json:"attachments,omitzero"`
	ReplyTo             *string                                                      `json:"reply_to,omitzero"`
	SendAt              *string                                                      `json:"send_at,omitzero"`
	CreateConversation  *bool                                                        `json:"create_conversation,omitzero"`
	AcceptsReplies      *bool                                                        `json:"accepts_replies,omitzero"`
}

type SendEmailResponse struct {
	MessageID        string                   `json:"message_id"`
	ProfileID        string                   `json:"profile_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ConversationID   conjoin.Nullable[string] `json:"conversation_id,omitzero"`
	ParentMessageID  conjoin.Nullable[string] `json:"parent_message_id,omitzero"`
	Type             string                   `json:"type"`
	From             string                   `json:"from"`
	Subject          string                   `json:"subject"`
	Body             string                   `json:"body"`
	Cc               []string                 `json:"cc,omitzero"`
	Bcc              []string                 `json:"bcc,omitzero"`
	ReplyTo          conjoin.Nullable[string] `json:"reply_to,omitzero"`
	Attachments      []map[string]any         `json:"attachments,omitzero"`
	Tracking         map[string]any           `json:"tracking,omitzero"`
	SendAt           conjoin.Nullable[string] `json:"send_at,omitzero"`
	SentAt           string                   `json:"sent_at"`
	AcceptsReplies   bool                     `json:"accepts_replies"`
	Status           string                   `json:"status"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ReadEmailMessagesRequestBodyQuery struct {
	ConversationID any                                  `json:"conversation_id,omitzero"`
	BroadcastID    any                                  `json:"broadcast_id,omitzero"`
	RequestID      any                                  `json:"request_id,omitzero"`
	MessageID      any                                  `json:"message_id,omitzero"`
	Subject        any                                  `json:"subject,omitzero"`
	RecipientID    any                                  `json:"recipient_id,omitzero"`
	Name           any                                  `json:"name,omitzero"`
	SendAt         *ListContactsRequestQueryDateCreated `json:"send_at,omitzero"`
	Email          any                                  `json:"email,omitzero"`
	Status         any                                  `json:"status,omitzero"`
}

type ReadEmailMessagesRequestBody struct {
	Cursor *ListContactsRequestCursor         `json:"cursor,omitzero"`
	Query  *ReadEmailMessagesRequestBodyQuery `json:"query,omitzero"`
	Search *ListContactsRequestSearch         `json:"search,omitzero"`
	Sort   map[string]string                  `json:"sort,omitzero"`
	Limit  any                                `json:"limit,omitzero"`
}

type ReadEmailMessagesRequest struct {
	Body ReadEmailMessagesRequestBody `json:"body"`
}

type ReadEmailMessagesItem = SendEmailResponse

type GetEmailSummaryResponse struct {
	TotalParts      float64 `json:"total_parts"`
	TotalRecipients float64 `json:"total_recipients"`
	CostPerPart     float64 `json:"cost_per_part"`
	TotalCost       float64 `json:"total_cost"`
	Currency        string  `json:"currency"`
}
