package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateMultisendRequest struct {
	MessagePriority      *string                                `json:"message_priority,omitzero"`
	Messages             SendConversationMessageRequestMessages `json:"messages"`
	MessageRetryStatuses []string                               `json:"message_retry_statuses,omitzero"`
	To                   []SendConversationMessageRequestToItem `json:"to,omitzero"`
	DefaultPlaceholders  map[string]any                         `json:"default_placeholders,omitzero"`
	Body                 *string                                `json:"body,omitzero"`
	SendAt               *string                                `json:"send_at,omitzero"`
	CreateConversation   *bool                                  `json:"create_conversation,omitzero"`
}

type CreateMultisendResponse struct {
	MessageID        string                   `json:"message_id"`
	ProfileID        string                   `json:"profile_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ParentMessageID  conjoin.Nullable[string] `json:"parent_message_id,omitzero"`
	ConversationID   conjoin.Nullable[string] `json:"conversation_id,omitzero"`
	Type             string                   `json:"type"`
	ChannelMessages  map[string]any           `json:"channel_messages"`
	Priority         []string                 `json:"priority"`
	SendAt           conjoin.Nullable[string] `json:"send_at,omitzero"`
	SentAt           string                   `json:"sent_at"`
	AcceptsReplies   bool                     `json:"accepts_replies"`
	Status           *string                  `json:"status,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ReadMultisendResponse = CreateMultisendResponse
