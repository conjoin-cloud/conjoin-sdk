package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadProjectsQuery = ReadApiKeysQuery

type ReadProjectsItem struct {
	CloudAccountID string                   `json:"cloud_account_id"`
	EntityID       string                   `json:"entity_id"`
	ReferenceID    conjoin.Nullable[string] `json:"reference_id,omitzero"`
	ProjectID      string                   `json:"project_id"`
	OrganizationID string                   `json:"organization_id"`
	Name           *string                  `json:"name,omitzero"`
	Tags           []string                 `json:"tags"`
	DateCreated    string                   `json:"date_created"`
	DateUpdated    conjoin.Nullable[string] `json:"date_updated,omitzero"`
	DateDeleted    conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateProjectRequest struct {
	ReferenceID *string  `json:"reference_id,omitzero"`
	Name        string   `json:"name"`
	Tags        []string `json:"tags,omitzero"`
}

type CreateProjectResponse = ReadProjectsItem

type ReadProjectsCountQuery = ReadApiKeysQuery

type ReadProjectsCountResponse = ReadApiKeysCountResponse

type ReadProjectResponse = ReadProjectsItem

type UpdateProjectRequest struct {
	Name *string  `json:"name,omitzero"`
	Tags []string `json:"tags,omitzero"`
}

type UpdateProjectResponse = ReadProjectsItem
