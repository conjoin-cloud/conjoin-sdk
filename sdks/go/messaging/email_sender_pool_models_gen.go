package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListManyEmailSenderPoolsQuery struct {
	PoolID      any                                   `json:"pool_id,omitzero"`
	ReferenceID any                                   `json:"reference_id,omitzero"`
	Capability  any                                   `json:"capability,omitzero"`
	DateCreated *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                     `json:"sort,omitzero"`
	Limit       any                                   `json:"limit,omitzero"`
}

type ListManyEmailSenderPoolsItem struct {
	PoolID           string                   `json:"pool_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
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

type CreateEmailSenderPoolRequest struct {
	ReferenceID *string  `json:"reference_id,omitzero"`
	Title       string   `json:"title"`
	Description *string  `json:"description,omitzero"`
	Capability  string   `json:"capability"`
	Senders     []string `json:"senders"`
}

type CreateEmailSenderPoolResponse = ListManyEmailSenderPoolsItem

type ListManyEmailSenderPoolsCountQuery = ListManyEmailSenderPoolsQuery

type ListManyEmailSenderPoolsCountResponse = ListChannelAnalyticsCountResponse

type AddEmailSendersToPoolRequest struct {
	Senders []string `json:"senders"`
}

type AddEmailSendersToPoolResponse = ListManyEmailSenderPoolsItem

type GetEmailSenderPoolResponse = ListManyEmailSenderPoolsItem

type DeleteEmailSenderPoolResponse = ListManyEmailSenderPoolsItem
