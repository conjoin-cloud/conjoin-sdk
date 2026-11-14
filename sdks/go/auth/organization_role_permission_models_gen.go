package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListOrgRolePermissionsQuery struct {
	PermissionID *string                     `json:"permission_id,omitzero"`
	Cursor       *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort         map[string]string           `json:"sort,omitzero"`
	Limit        any                         `json:"limit,omitzero"`
}

type ListOrgRolePermissionsItem struct {
	RolePermissionID string                   `json:"role_permission_id"`
	OrganizationID   string                   `json:"organization_id"`
	RoleID           string                   `json:"role_id"`
	PermissionID     string                   `json:"permission_id"`
	AppID            string                   `json:"app_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
	PermissionKey    *string                  `json:"permission_key"`
}

type ListOrgRolePermissionsCountQuery = ListOrgRolePermissionsQuery

type ListOrgRolePermissionsCountResponse = ListCredentialsCountResponse

type AssignOrgRolePermissionRequest struct {
	PermissionKeys []string `json:"permission_keys"`
}

type AssignOrgRolePermissionResponseItem struct {
	RolePermissionID string                   `json:"role_permission_id"`
	OrganizationID   string                   `json:"organization_id"`
	RoleID           string                   `json:"role_id"`
	PermissionID     string                   `json:"permission_id"`
	AppID            string                   `json:"app_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type RemoveRolePermissionRequest = AssignOrgRolePermissionRequest

type RemoveRolePermissionResponse struct {
	RemovedCount int64 `json:"removed_count"`
}
