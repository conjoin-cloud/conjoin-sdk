package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListOrgPermissionsQuery struct {
	PermissionID *string                     `json:"permission_id,omitzero"`
	ReferenceID  *string                     `json:"reference_id,omitzero"`
	Key          *string                     `json:"key,omitzero"`
	DateDeleted  *string                     `json:"date_deleted,omitzero"`
	Cursor       *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort         map[string]string           `json:"sort,omitzero"`
	Limit        any                         `json:"limit,omitzero"`
}

type ListOrgPermissionsItem struct {
	PermissionID     string                   `json:"permission_id"`
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
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateOrgPermissionRequest struct {
	ReferenceID *string                  `json:"reference_id,omitzero"`
	Key         string                   `json:"key"`
	Name        string                   `json:"name"`
	Description conjoin.Nullable[string] `json:"description,omitzero"`
	Metadata    map[string]any           `json:"metadata,omitzero"`
}

type CreateOrgPermissionResponse = ListOrgPermissionsItem

type ListOrgPermissionsCountQuery = ListOrgPermissionsQuery

type ListOrgPermissionsCountResponse = ListCredentialsCountResponse

type ReadOrgPermissionResponse = ListOrgPermissionsItem

type UpdateOrgPermissionRequest struct {
	Name        *string                  `json:"name,omitzero"`
	Key         *string                  `json:"key,omitzero"`
	Description conjoin.Nullable[string] `json:"description,omitzero"`
	Metadata    map[string]any           `json:"metadata,omitzero"`
}

type UpdateOrgPermissionResponse = ListOrgPermissionsItem

type DeleteOrgPermissionResponse = ListOrgPermissionsItem

type ArchiveOrgPermissionResponse = ListOrgPermissionsItem

type RestoreOrgPermissionResponse = ListOrgPermissionsItem
