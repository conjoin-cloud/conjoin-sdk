package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListResourceGrantsQuery struct {
	AccountID    *string                     `json:"account_id,omitzero"`
	ResourceType *string                     `json:"resource_type,omitzero"`
	ResourceID   *string                     `json:"resource_id,omitzero"`
	Cursor       *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort         map[string]string           `json:"sort,omitzero"`
	Limit        any                         `json:"limit,omitzero"`
}

type ListResourceGrantsItem struct {
	ResourceGrantID    string                   `json:"resource_grant_id"`
	OrganizationID     string                   `json:"organization_id"`
	AccountID          string                   `json:"account_id"`
	AppID              string                   `json:"app_id"`
	ConjoinAccountID   string                   `json:"conjoin_account_id"`
	ConjoinProjectID   string                   `json:"conjoin_project_id"`
	LiveMode           bool                     `json:"live_mode"`
	ResourceType       string                   `json:"resource_type"`
	ResourceID         string                   `json:"resource_id"`
	PermissionKeys     []string                 `json:"permission_keys,omitzero"`
	GrantedByAccountID conjoin.Nullable[string] `json:"granted_by_account_id,omitzero"`
	GrantedAt          *string                  `json:"granted_at,omitzero"`
	Metadata           map[string]any           `json:"metadata,omitzero"`
	DateCreated        string                   `json:"date_created"`
	DateUpdated        string                   `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type GrantResourcePermissionRequest struct {
	AccountID      string   `json:"account_id"`
	ResourceType   string   `json:"resource_type"`
	ResourceID     string   `json:"resource_id"`
	PermissionKeys []string `json:"permission_keys"`
}

type GrantResourcePermissionResponse = ListResourceGrantsItem

type CheckResourcePermissionRequest struct {
	AccountID     string `json:"account_id"`
	ResourceType  string `json:"resource_type"`
	ResourceID    string `json:"resource_id"`
	PermissionKey string `json:"permission_key"`
}

type CheckResourcePermissionResponse struct {
	Allowed            bool     `json:"allowed"`
	GrantedPermissions []string `json:"granted_permissions"`
}

type ListResourceGrantsCountQuery = ListResourceGrantsQuery

type ListResourceGrantsCountResponse = ListCredentialsCountResponse

type RevokeResourcePermissionRequest struct {
	PermissionKeys []string `json:"permission_keys,omitzero"`
}

type RevokeResourcePermissionResponse = ListResourceGrantsItem
