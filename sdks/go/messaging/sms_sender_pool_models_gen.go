package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListManySmsSenderPoolsQuery = ListManyEmailSenderPoolsQuery

type ListManySmsSenderPoolsItem struct {
	PoolID           string                   `json:"pool_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ProfileID        string                   `json:"profile_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Senders          []string                 `json:"senders"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateSmsSenderPoolRequest = CreateEmailSenderPoolRequest

type CreateSmsSenderPoolResponse = ListManySmsSenderPoolsItem

type ListManySmsSenderPoolsCountQuery = ListManyEmailSenderPoolsQuery

type ListManySmsSenderPoolsCountResponse = ListChannelAnalyticsCountResponse

type AddSmsSendersToPoolRequest = AddEmailSendersToPoolRequest

type AddSmsSendersToPoolResponse = ListManySmsSenderPoolsItem

type GetSmsSenderPoolResponse = ListManySmsSenderPoolsItem

type DeleteSmsSenderPoolResponse = ListManySmsSenderPoolsItem
