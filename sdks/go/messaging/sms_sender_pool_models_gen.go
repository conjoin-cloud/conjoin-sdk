package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateSmsSenderPoolRequest = CreateEmailSenderPoolRequest

type CreateSmsSenderPoolResponse struct {
	PoolID           string                   `json:"pool_id"`
	ProfileID        string                   `json:"profile_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Senders          []string                 `json:"senders"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type AddSmsSendersToPoolRequest = AddEmailSendersToPoolRequest

type AddSmsSendersToPoolResponse = CreateSmsSenderPoolResponse

type GetSmsSenderPoolResponse = CreateSmsSenderPoolResponse

type DeleteSmsSenderPoolResponse = CreateSmsSenderPoolResponse
