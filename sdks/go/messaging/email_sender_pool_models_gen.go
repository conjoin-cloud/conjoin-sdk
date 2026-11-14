package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateEmailSenderPoolRequest struct {
	Title       string   `json:"title"`
	Description *string  `json:"description,omitzero"`
	Capability  string   `json:"capability"`
	Senders     []string `json:"senders"`
}

type CreateEmailSenderPoolResponse struct {
	PoolID           string                   `json:"pool_id"`
	ProfileID        string                   `json:"profile_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Title            string                   `json:"title"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	Capability       string                   `json:"capability"`
	Senders          []string                 `json:"senders"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type AddEmailSendersToPoolRequest struct {
	Senders []string `json:"senders"`
}

type AddEmailSendersToPoolResponse = CreateEmailSenderPoolResponse

type GetEmailSenderPoolResponse = CreateEmailSenderPoolResponse

type DeleteEmailSenderPoolResponse = CreateEmailSenderPoolResponse
