package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListMembershipsQuery struct {
	AccountID   *string                     `json:"account_id,omitzero"`
	Status      *string                     `json:"status,omitzero"`
	DateDeleted conjoin.Nullable[string]    `json:"date_deleted,omitzero"`
	Cursor      *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string           `json:"sort,omitzero"`
	Limit       any                         `json:"limit,omitzero"`
}

type ListMembershipsItem struct {
	AccountOrganizationID string                   `json:"account_organization_id"`
	AccountID             string                   `json:"account_id"`
	OrganizationID        string                   `json:"organization_id"`
	AppID                 string                   `json:"app_id"`
	ConjoinAccountID      string                   `json:"conjoin_account_id"`
	ConjoinProjectID      string                   `json:"conjoin_project_id"`
	LiveMode              bool                     `json:"live_mode"`
	JoinedAt              conjoin.Nullable[string] `json:"joined_at,omitzero"`
	Roles                 []string                 `json:"roles,omitzero"`
	Status                string                   `json:"status"`
	Metadata              map[string]any           `json:"metadata,omitzero"`
	DateCreated           string                   `json:"date_created"`
	DateUpdated           string                   `json:"date_updated"`
	DateDeleted           conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateMembershipRequest struct {
	AccountID string         `json:"account_id"`
	Roles     []string       `json:"roles"`
	Status    *string        `json:"status,omitzero"`
	JoinedAt  *string        `json:"joined_at,omitzero"`
	Metadata  map[string]any `json:"metadata,omitzero"`
}

type CreateMembershipResponse = ListMembershipsItem

type ListMembershipsCountQuery = ListMembershipsQuery

type ListMembershipsCountResponse = ListCredentialsCountResponse

type UpdateMembershipRequest struct {
	Roles    []string       `json:"roles,omitzero"`
	Status   *string        `json:"status,omitzero"`
	JoinedAt *string        `json:"joined_at,omitzero"`
	Metadata map[string]any `json:"metadata,omitzero"`
}

type UpdateMembershipResponse = ListMembershipsItem

type DeleteMembershipResponse = ListMembershipsItem

type GrantOrgAccountRoleRequest = GrantGlobalRoleRequest

type GrantOrgAccountRoleResponse = ListMembershipsItem

type RevokeOrgAccountRoleRequest = GrantGlobalRoleRequest

type RevokeOrgAccountRoleResponse = ListMembershipsItem
