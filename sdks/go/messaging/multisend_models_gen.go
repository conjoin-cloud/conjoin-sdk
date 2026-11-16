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

type CreateMultisendResponseSMSMessagesItem struct {
	PhoneNumber string `json:"phone_number"`
	Status      string `json:"status"`
}

type CreateMultisendResponseSMS struct {
	MessageBroadcastID string                                   `json:"message_broadcast_id"`
	RequestID          string                                   `json:"request_id"`
	Status             string                                   `json:"status"`
	Messages           []CreateMultisendResponseSMSMessagesItem `json:"messages"`
}

type CreateMultisendResponseEmailMessagesItem struct {
	Email  string `json:"email"`
	Status string `json:"status"`
}

type CreateMultisendResponseEmail struct {
	MessageBroadcastID string                                     `json:"message_broadcast_id"`
	RequestID          string                                     `json:"request_id"`
	Status             string                                     `json:"status"`
	Messages           []CreateMultisendResponseEmailMessagesItem `json:"messages"`
}

type CreateMultisendResponse struct {
	SMS   *CreateMultisendResponseSMS   `json:"sms,omitzero"`
	Email *CreateMultisendResponseEmail `json:"email,omitzero"`
}

type ReadMultisendResponse struct {
	BroadcastID          string                   `json:"broadcast_id"`
	ProfileID            string                   `json:"profile_id"`
	ConjoinAccountID     string                   `json:"conjoin_account_id"`
	ConjoinProjectID     string                   `json:"conjoin_project_id"`
	LiveMode             bool                     `json:"live_mode"`
	ReferenceID          conjoin.Nullable[string] `json:"reference_id,omitzero"`
	DateCreated          string                   `json:"date_created"`
	DateUpdated          string                   `json:"date_updated"`
	DateDeleted          conjoin.Nullable[string] `json:"date_deleted,omitzero"`
	Originator           string                   `json:"originator"`
	OriginatorPrimaryID  string                   `json:"originator_primary_id"`
	OriginatorRequestID  string                   `json:"originator_request_id"`
	MessagePriority      string                   `json:"message_priority"`
	MessageChannels      []string                 `json:"message_channels"`
	MessageRequests      map[string]string        `json:"message_requests"`
	MessageRetryStatuses []string                 `json:"message_retry_statuses"`
	SendAt               conjoin.Nullable[string] `json:"send_at,omitzero"`
	SentAt               conjoin.Nullable[string] `json:"sent_at,omitzero"`
}
