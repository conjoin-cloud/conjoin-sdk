package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateVerificationRequestTokenOptionsExpiresAfter struct {
	Unit  *string  `json:"unit,omitzero"`
	Value *float64 `json:"value,omitzero"`
}

type CreateVerificationRequestTokenOptions struct {
	TokenType         *string                                            `json:"token_type,omitzero"`
	Length            *float64                                           `json:"length,omitzero"`
	HasDigits         *bool                                              `json:"has_digits,omitzero"`
	HasLowercaseChars *bool                                              `json:"has_lowercase_chars,omitzero"`
	HasUppercaseChars *bool                                              `json:"has_uppercase_chars,omitzero"`
	HasSpecialChars   *bool                                              `json:"has_special_chars,omitzero"`
	ExpiresAfter      *CreateVerificationRequestTokenOptionsExpiresAfter `json:"expires_after,omitzero"`
	ResendAfter       *CreateVerificationRequestTokenOptionsExpiresAfter `json:"resend_after,omitzero"`
}

type CreateVerificationRequest struct {
	Channel      *string                                `json:"channel,omitzero"`
	Recipient    any                                    `json:"recipient,omitzero"`
	Body         *string                                `json:"body,omitzero"`
	Subject      *string                                `json:"subject,omitzero"`
	ReferenceID  *string                                `json:"reference_id,omitzero"`
	Placeholders map[string]any                         `json:"placeholders,omitzero"`
	TokenOptions *CreateVerificationRequestTokenOptions `json:"token_options,omitzero"`
}

type CreateVerificationResponse struct {
	VerificationID              string                   `json:"verification_id"`
	ProfileID                   string                   `json:"profile_id"`
	ConjoinAccountID            string                   `json:"conjoin_account_id"`
	ConjoinProjectID            string                   `json:"conjoin_project_id"`
	LiveMode                    bool                     `json:"live_mode"`
	ReferenceID                 conjoin.Nullable[string] `json:"reference_id,omitzero"`
	MessageChannel              string                   `json:"message_channel"`
	MessageStatus               string                   `json:"message_status"`
	From                        string                   `json:"from"`
	MessageSubject              *string                  `json:"message_subject,omitzero"`
	Recipient                   map[string]any           `json:"recipient"`
	SentAt                      string                   `json:"sent_at"`
	TokenType                   string                   `json:"token_type"`
	VerificationStatus          string                   `json:"verification_status"`
	ExpiresAt                   string                   `json:"expires_at"`
	MaxVerificationAttempts     float64                  `json:"max_verification_attempts"`
	CurrentVerificationAttempts float64                  `json:"current_verification_attempts"`
	DateCreated                 string                   `json:"date_created"`
	DateUpdated                 string                   `json:"date_updated"`
	DateDeleted                 conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CheckVerificationRequest struct {
	Token string `json:"token"`
}

type CheckVerificationResponse = CreateVerificationResponse

type ResendVerificationRequestParams struct {
	VerificationID string `json:"verification_id"`
}

type ResendVerificationRequest struct {
	Params ResendVerificationRequestParams `json:"params"`
}

type ResendVerificationResponse = CreateVerificationResponse

type ListVerificationMessagesRequestQuery struct {
	Channel        string                               `json:"channel"`
	SenderID       any                                  `json:"sender_id,omitzero"`
	MessageID      any                                  `json:"message_id,omitzero"`
	VerificationID any                                  `json:"verification_id,omitzero"`
	ReferenceID    any                                  `json:"reference_id,omitzero"`
	DateCreated    *ListContactsRequestQueryDateCreated `json:"date_created,omitzero"`
}

type ListVerificationMessagesRequest struct {
	Cursor *ListContactsRequestCursor           `json:"cursor,omitzero"`
	Filter map[string]bool                      `json:"filter,omitzero"`
	Query  ListVerificationMessagesRequestQuery `json:"query"`
	Sort   map[string]string                    `json:"sort,omitzero"`
	Limit  any                                  `json:"limit,omitzero"`
}

type ListVerificationMessagesItem = CreateVerificationResponse
