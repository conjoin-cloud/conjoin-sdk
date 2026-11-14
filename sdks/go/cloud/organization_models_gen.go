package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadOrganizationsQuery = ReadApiKeysQuery

type ReadOrganizationsItem struct {
	CloudAccountID string                   `json:"cloud_account_id"`
	EntityID       string                   `json:"entity_id"`
	ReferenceID    conjoin.Nullable[string] `json:"reference_id,omitzero"`
	OrganizationID string                   `json:"organization_id"`
	Name           string                   `json:"name"`
	Tags           []string                 `json:"tags,omitzero"`
	DateCreated    string                   `json:"date_created"`
	DateUpdated    conjoin.Nullable[string] `json:"date_updated,omitzero"`
}

type CreateOrganizationRequest = CreateProjectRequest

type CreateOrganizationResponse = ReadOrganizationsItem

type ReadOrganizationsCountQuery = ReadApiKeysQuery

type ReadOrganizationsCountResponse = ReadApiKeysCountResponse

type ReadOrganizationResponse = ReadOrganizationsItem

type UpdateOrganizationRequest = UpdateProjectRequest

type UpdateOrganizationResponse = ReadOrganizationsItem
