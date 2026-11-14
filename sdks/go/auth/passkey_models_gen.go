package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPasskeysQuery struct {
	Status *string                     `json:"status,omitzero"`
	Cursor *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string           `json:"sort,omitzero"`
	Limit  any                         `json:"limit,omitzero"`
}

type ListPasskeysItem struct {
	CredentialID   string                   `json:"credential_id"`
	Kind           string                   `json:"kind"`
	Status         string                   `json:"status"`
	SetAt          conjoin.Nullable[string] `json:"set_at,omitzero"`
	LastUsedAt     conjoin.Nullable[string] `json:"last_used_at,omitzero"`
	LastVerifiedAt conjoin.Nullable[string] `json:"last_verified_at,omitzero"`
	Transports     []string                 `json:"transports,omitzero"`
	Aaguid         conjoin.Nullable[string] `json:"aaguid,omitzero"`
	DateCreated    string                   `json:"date_created"`
}

type ListPasskeysCountQuery = ListPasskeysQuery

type ListPasskeysCountResponse = ListCredentialsCountResponse

type ReadPasskeyResponse = ListPasskeysItem

type DeletePasskeyResponse = ListPasskeysItem
