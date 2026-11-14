package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateByokConfigRequest struct {
	Provider      string                   `json:"provider"`
	ProviderName  string                   `json:"provider_name"`
	APIKey        string                   `json:"api_key"`
	EndpointURL   conjoin.Nullable[string] `json:"endpoint_url,omitzero"`
	AllowedModels []string                 `json:"allowed_models,omitzero"`
	Description   conjoin.Nullable[string] `json:"description,omitzero"`
	ReferenceID   conjoin.Nullable[string] `json:"reference_id,omitzero"`
	Metadata      map[string]any           `json:"metadata,omitzero"`
}

type CreateByokConfigResponse struct {
	ByokConfigID     string                   `json:"byok_config_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      *string                  `json:"reference_id"`
	Provider         string                   `json:"provider"`
	ProviderName     string                   `json:"provider_name"`
	HasAPIKey        bool                     `json:"has_api_key"`
	EndpointURL      *string                  `json:"endpoint_url"`
	AllowedModels    []string                 `json:"allowed_models"`
	IsEnabled        bool                     `json:"is_enabled"`
	Status           string                   `json:"status"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	Metadata         map[string]any           `json:"metadata"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListByokConfigsQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListByokConfigsQueryQueryDateCreated struct {
	Equals    *string `json:"equals,omitzero"`
	NotEquals *string `json:"not_equals,omitzero"`
	Gt        *string `json:"gt,omitzero"`
	Lt        *string `json:"lt,omitzero"`
	Gte       *string `json:"gte,omitzero"`
	Lte       *string `json:"lte,omitzero"`
}

type ListByokConfigsQueryQuery struct {
	Provider    *string                               `json:"provider,omitzero"`
	Status      *string                               `json:"status,omitzero"`
	IsEnabled   *bool                                 `json:"is_enabled,omitzero"`
	DateCreated *ListByokConfigsQueryQueryDateCreated `json:"date_created,omitzero"`
}

type ListByokConfigsQuery struct {
	Cursor *ListByokConfigsQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string           `json:"sort,omitzero"`
	Limit  any                         `json:"limit,omitzero"`
	Query  *ListByokConfigsQueryQuery  `json:"query,omitzero"`
}

type ListByokConfigsItem = CreateByokConfigResponse

type ReadByokConfigResponse = CreateByokConfigResponse

type UpdateByokConfigRequest struct {
	ProviderName  *string                  `json:"provider_name,omitzero"`
	APIKey        *string                  `json:"api_key,omitzero"`
	EndpointURL   conjoin.Nullable[string] `json:"endpoint_url,omitzero"`
	AllowedModels []string                 `json:"allowed_models,omitzero"`
	IsEnabled     *bool                    `json:"is_enabled,omitzero"`
	Status        *string                  `json:"status,omitzero"`
	Description   conjoin.Nullable[string] `json:"description,omitzero"`
	Metadata      map[string]any           `json:"metadata,omitzero"`
}

type UpdateByokConfigResponse = CreateByokConfigResponse

type DeleteByokConfigResponse = CreateByokConfigResponse

type TestByokConnectionResponse struct {
	Connected bool   `json:"connected"`
	Provider  string `json:"provider"`
	Message   string `json:"message"`
}
