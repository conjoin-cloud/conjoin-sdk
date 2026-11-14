package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListGroupsQuery struct {
	ReferenceID        *string                     `json:"reference_id,omitzero"`
	Name               *string                     `json:"name,omitzero"`
	Slug               *string                     `json:"slug,omitzero"`
	ProvisioningSource *string                     `json:"provisioning_source,omitzero"`
	ExternalID         *string                     `json:"external_id,omitzero"`
	DateDeleted        conjoin.Nullable[string]    `json:"date_deleted,omitzero"`
	Cursor             *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort               map[string]string           `json:"sort,omitzero"`
	Limit              any                         `json:"limit,omitzero"`
}

type ListGroupsItem struct {
	GroupID            string                   `json:"group_id"`
	OrganizationID     string                   `json:"organization_id"`
	AppID              string                   `json:"app_id"`
	ConjoinAccountID   string                   `json:"conjoin_account_id"`
	ConjoinProjectID   string                   `json:"conjoin_project_id"`
	LiveMode           bool                     `json:"live_mode"`
	ReferenceID        conjoin.Nullable[string] `json:"reference_id,omitzero"`
	Slug               string                   `json:"slug"`
	Name               string                   `json:"name"`
	Description        conjoin.Nullable[string] `json:"description,omitzero"`
	ImageURL           conjoin.Nullable[string] `json:"image_url,omitzero"`
	TotalMembers       *float64                 `json:"total_members,omitzero"`
	Roles              []string                 `json:"roles,omitzero"`
	ProvisioningSource *string                  `json:"provisioning_source,omitzero"`
	ExternalID         conjoin.Nullable[string] `json:"external_id,omitzero"`
	SyncLocked         *bool                    `json:"sync_locked,omitzero"`
	LastSyncedAt       conjoin.Nullable[string] `json:"last_synced_at,omitzero"`
	Metadata           map[string]any           `json:"metadata,omitzero"`
	DateCreated        string                   `json:"date_created"`
	DateUpdated        string                   `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateGroupRequest struct {
	Name        string   `json:"name"`
	Description *string  `json:"description,omitzero"`
	Slug        *string  `json:"slug,omitzero"`
	ImageURL    *string  `json:"image_url,omitzero"`
	Roles       []string `json:"roles,omitzero"`
	ReferenceID *string  `json:"reference_id,omitzero"`
}

type CreateGroupResponse = ListGroupsItem

type ListGroupMembersQuery = ListAccountOrganizationMembershipsQuery

type ListGroupMembersItem struct {
	GroupMembershipID string                   `json:"group_membership_id"`
	OrganizationID    string                   `json:"organization_id"`
	GroupID           string                   `json:"group_id"`
	AccountID         string                   `json:"account_id"`
	AppID             string                   `json:"app_id"`
	ConjoinAccountID  string                   `json:"conjoin_account_id"`
	ConjoinProjectID  string                   `json:"conjoin_project_id"`
	LiveMode          bool                     `json:"live_mode"`
	JoinedAt          conjoin.Nullable[string] `json:"joined_at,omitzero"`
	Status            string                   `json:"status"`
	Metadata          map[string]any           `json:"metadata,omitzero"`
	DateCreated       string                   `json:"date_created"`
	DateUpdated       string                   `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListGroupMembersCountQuery = ListAccountOrganizationMembershipsQuery

type ListGroupMembersCountResponse = ListCredentialsCountResponse

type ListGroupsCountQuery = ListGroupsQuery

type ListGroupsCountResponse = ListCredentialsCountResponse

type UpdateGroupRequest struct {
	Name        *string  `json:"name,omitzero"`
	Description *string  `json:"description,omitzero"`
	Slug        *string  `json:"slug,omitzero"`
	ImageURL    *string  `json:"image_url,omitzero"`
	Roles       []string `json:"roles,omitzero"`
}

type UpdateGroupResponse = ListGroupsItem

type DeleteGroupResponse = ListGroupsItem

type AddGroupMemberRequest = ReadEffectivePermissionsQuery

type AddGroupMemberResponse = ListGroupsItem

type RemoveGroupMemberRequest = ReadEffectivePermissionsQuery

type RemoveGroupMemberResponse = ListGroupsItem

type BulkSyncGroupMembersRequest struct {
	Add    []string `json:"add,omitzero"`
	Remove []string `json:"remove,omitzero"`
}

type BulkSyncGroupMembersResponse = ListGroupsItem
