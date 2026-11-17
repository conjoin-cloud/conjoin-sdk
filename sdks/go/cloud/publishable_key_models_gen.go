package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPublishableKeysQuery struct {
	Cursor *ReadApiKeysQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string       `json:"sort,omitzero"`
	Limit  any                     `json:"limit,omitzero"`
}

type ListPublishableKeysItem struct {
	PublishableKeyID string                   `json:"publishable_key_id"`
	ProjectID        string                   `json:"project_id"`
	TestMode         bool                     `json:"test_mode"`
	AllowedDomains   []string                 `json:"allowed_domains"`
	IsActive         bool                     `json:"is_active"`
	DateRevoked      conjoin.Nullable[string] `json:"date_revoked,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      conjoin.Nullable[string] `json:"date_updated,omitzero"`
}

type ListPublishableKeysCountQuery = ListPublishableKeysQuery

type ListPublishableKeysCountResponse = ReadApiKeysCountResponse

type UpdatePublishableKeyRequest struct {
	AllowedDomains []string `json:"allowed_domains"`
}

type UpdatePublishableKeyResponse = ListPublishableKeysItem
