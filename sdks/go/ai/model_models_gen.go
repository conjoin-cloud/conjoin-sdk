package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListModelsQueryQuery struct {
	Vendor           *string `json:"vendor,omitzero"`
	PlanAvailability *string `json:"plan_availability,omitzero"`
	IsActive         *bool   `json:"is_active,omitzero"`
	TextInput        *bool   `json:"text_input,omitzero"`
	ImageInput       *bool   `json:"image_input,omitzero"`
}

type ListModelsQuery struct {
	Cursor *ListByokConfigsQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string           `json:"sort,omitzero"`
	Limit  any                         `json:"limit,omitzero"`
	Query  *ListModelsQueryQuery       `json:"query,omitzero"`
}

type ListModelsItemPricing struct {
	InputPerMillionTokens  float64 `json:"input_per_million_tokens"`
	OutputPerMillionTokens float64 `json:"output_per_million_tokens"`
	Currency               string  `json:"currency"`
	LastVerifiedAt         string  `json:"last_verified_at"`
}

type ListModelsItem struct {
	ModelID          string                   `json:"model_id"`
	Vendor           string                   `json:"vendor"`
	DisplayName      string                   `json:"display_name"`
	Capabilities     map[string]any           `json:"capabilities"`
	Pricing          ListModelsItemPricing    `json:"pricing"`
	ContextWindow    float64                  `json:"context_window"`
	MaxOutputTokens  float64                  `json:"max_output_tokens"`
	PlanAvailability string                   `json:"plan_availability"`
	IsActive         bool                     `json:"is_active"`
	ReleaseDate      conjoin.Nullable[string] `json:"release_date,omitzero"`
	DeprecationDate  conjoin.Nullable[string] `json:"deprecation_date,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
}

type ReadModelResponse = ListModelsItem
