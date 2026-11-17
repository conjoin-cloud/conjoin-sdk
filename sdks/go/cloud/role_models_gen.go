package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadRolesQuery = ReadApiKeysQuery

type ReadRolesItem struct {
	CloudAccountID   string                   `json:"cloud_account_id"`
	EntityID         string                   `json:"entity_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	RoleID           string                   `json:"role_id"`
	Name             string                   `json:"name"`
	Title            string                   `json:"title"`
	Description      *string                  `json:"description,omitzero"`
	TotalPermissions float64                  `json:"total_permissions"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      conjoin.Nullable[string] `json:"date_updated,omitzero"`
}

type CreateRoleRequest struct {
	ReferenceID *string  `json:"reference_id,omitzero"`
	Title       string   `json:"title"`
	Name        string   `json:"name"`
	Description *string  `json:"description,omitzero"`
	ProjectID   string   `json:"project_id"`
	Permissions []string `json:"permissions"`
}

type CreateRoleResponse = ReadRolesItem

type ReadRolesCountQuery = ReadApiKeysQuery

type ReadRolesCountResponse = ReadApiKeysCountResponse

type UpdateRoleRequest struct {
	Title       *string  `json:"title,omitzero"`
	Description *string  `json:"description,omitzero"`
	Permissions []string `json:"permissions,omitzero"`
}

type UpdateRoleResponse = ReadRolesItem
