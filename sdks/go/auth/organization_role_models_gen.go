package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListOrgRolesQuery struct {
	ReferenceID *string                     `json:"reference_id,omitzero"`
	Key         *string                     `json:"key,omitzero"`
	DateDeleted *string                     `json:"date_deleted,omitzero"`
	Cursor      *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string           `json:"sort,omitzero"`
	Limit       any                         `json:"limit,omitzero"`
}

type ListOrgRolesItem struct {
	RoleID           string                   `json:"role_id"`
	OrganizationID   string                   `json:"organization_id"`
	AppID            string                   `json:"app_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	Key              string                   `json:"key"`
	Name             string                   `json:"name"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	Identifier       string                   `json:"identifier"`
	CreatorAccountID conjoin.Nullable[string] `json:"creator_account_id,omitzero"`
	ParentRoleID     conjoin.Nullable[string] `json:"parent_role_id,omitzero"`
	Scope            *string                  `json:"scope,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateOrgRoleRequest struct {
	ReferenceID  *string                  `json:"reference_id,omitzero"`
	Key          string                   `json:"key"`
	Name         string                   `json:"name"`
	Description  conjoin.Nullable[string] `json:"description,omitzero"`
	ParentRoleID conjoin.Nullable[string] `json:"parent_role_id,omitzero"`
	Scope        *string                  `json:"scope,omitzero"`
	Metadata     map[string]any           `json:"metadata,omitzero"`
}

type CreateOrgRoleResponse = ListOrgRolesItem

type ListOrgRolesCountQuery = ListOrgRolesQuery

type ListOrgRolesCountResponse = ListCredentialsCountResponse

type ReadOrgRoleResponse = ListOrgRolesItem

type UpdateOrgRoleRequest struct {
	Name         *string                  `json:"name,omitzero"`
	Key          *string                  `json:"key,omitzero"`
	Description  conjoin.Nullable[string] `json:"description,omitzero"`
	ParentRoleID conjoin.Nullable[string] `json:"parent_role_id,omitzero"`
	Metadata     map[string]any           `json:"metadata,omitzero"`
}

type UpdateOrgRoleResponse = ListOrgRolesItem

type DeleteOrgRoleResponse = ListOrgRolesItem

type ArchiveOrgRoleResponse = ListOrgRolesItem

type RestoreOrgRoleResponse = ListOrgRolesItem
