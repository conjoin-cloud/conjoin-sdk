package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListClientsQuery struct {
	ClientID    *string                     `json:"client_id,omitzero"`
	ReferenceID *string                     `json:"reference_id,omitzero"`
	Cursor      *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string           `json:"sort,omitzero"`
	Limit       any                         `json:"limit,omitzero"`
}

type ListClientsItem struct {
	ClientID           string                   `json:"client_id"`
	AppID              string                   `json:"app_id"`
	ConjoinAccountID   string                   `json:"conjoin_account_id"`
	ConjoinProjectID   string                   `json:"conjoin_project_id"`
	LiveMode           bool                     `json:"live_mode"`
	ReferenceID        conjoin.Nullable[string] `json:"reference_id,omitzero"`
	AuthStatus         conjoin.Nullable[string] `json:"auth_status,omitzero"`
	VerificationOption conjoin.Nullable[string] `json:"verification_option,omitzero"`
	MFAOption          conjoin.Nullable[string] `json:"mfa_option,omitzero"`
	DeviceID           conjoin.Nullable[string] `json:"device_id,omitzero"`
	UserIP             conjoin.Nullable[string] `json:"user_ip,omitzero"`
	UserAgent          conjoin.Nullable[string] `json:"user_agent,omitzero"`
	DeviceConfig       map[string]any           `json:"device_config,omitzero"`
	Metadata           map[string]any           `json:"metadata,omitzero"`
	DateCreated        string                   `json:"date_created"`
	DateUpdated        string                   `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateClientRequest struct {
	ReferenceID *string        `json:"reference_id,omitzero"`
	Metadata    map[string]any `json:"metadata,omitzero"`
}

type CreateClientResponse = ListClientsItem

type ListClientsCountQuery = ListClientsQuery

type ListClientsCountResponse = ListCredentialsCountResponse

type ReadClientResponse = ListClientsItem
