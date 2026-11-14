package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadApiKeysQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ReadApiKeysQuery struct {
	ReferenceID *string                 `json:"reference_id,omitzero"`
	Cursor      *ReadApiKeysQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string       `json:"sort,omitzero"`
	Limit       any                     `json:"limit,omitzero"`
}

type ReadApiKeysItem struct {
	APIKeyID    string                   `json:"api_key_id"`
	EntityID    string                   `json:"entity_id"`
	ReferenceID conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ProjectID   string                   `json:"project_id"`
	Name        string                   `json:"name"`
	Description *string                  `json:"description,omitzero"`
	Roles       []string                 `json:"roles"`
	ServiceIDs  []string                 `json:"service_ids,omitzero"`
	TestMode    bool                     `json:"test_mode"`
	DateExpired *string                  `json:"date_expired,omitzero"`
	HasExpired  bool                     `json:"has_expired"`
	DateCreated string                   `json:"date_created"`
	DateUpdated conjoin.Nullable[string] `json:"date_updated,omitzero"`
}

type CreateApiKeyRequest struct {
	Name        string   `json:"name"`
	Description *string  `json:"description,omitzero"`
	ExpireAt    *string  `json:"expire_at,omitzero"`
	Roles       []string `json:"roles,omitzero"`
	ServiceIDs  []string `json:"service_ids,omitzero"`
	ReferenceID *string  `json:"reference_id,omitzero"`
	TestMode    *bool    `json:"test_mode,omitzero"`
}

type ReadApiKeysCountQuery = ReadApiKeysQuery

type ReadApiKeysCountResponse struct {
	Count int64 `json:"count"`
}

type RegenerateApiKeyRequest struct {
	Name        string   `json:"name"`
	Description *string  `json:"description,omitzero"`
	ExpireAt    *string  `json:"expire_at,omitzero"`
	Roles       []string `json:"roles,omitzero"`
	ServiceIDs  []string `json:"service_ids,omitzero"`
	TestMode    bool     `json:"test_mode"`
}

type UpdateApiKeyRequest struct {
	Name        string  `json:"name"`
	Description *string `json:"description,omitzero"`
}

type UpdateApiKeyResponse = ReadApiKeysItem
