package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadPublicProjectBrandingQuery struct {
	OrganizationID *string `json:"organization_id,omitzero"`
}

type ReadPublicProjectBrandingResponse struct {
	BrandingID    string                           `json:"branding_id"`
	ProjectID     string                           `json:"project_id"`
	SchemaVersion float64                          `json:"schema_version"`
	General       map[string]any                   `json:"general,omitzero"`
	Colors        map[string]any                   `json:"colors,omitzero"`
	Typography    map[string]any                   `json:"typography,omitzero"`
	Borders       map[string]any                   `json:"borders,omitzero"`
	Spacing       map[string]any                   `json:"spacing,omitzero"`
	Shadows       map[string]any                   `json:"shadows,omitzero"`
	Components    map[string]any                   `json:"components,omitzero"`
	Layout        map[string]any                   `json:"layout,omitzero"`
	Animation     map[string]any                   `json:"animation,omitzero"`
	Accessibility map[string]any                   `json:"accessibility,omitzero"`
	Organization  conjoin.Nullable[map[string]any] `json:"organization,omitzero"`
	DateCreated   string                           `json:"date_created"`
	DateUpdated   conjoin.Nullable[string]         `json:"date_updated,omitzero"`
}
