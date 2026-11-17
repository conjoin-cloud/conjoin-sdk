package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListOrganizationsQuery struct {
	OrganizationID *string                     `json:"organization_id,omitzero"`
	AccountID      *string                     `json:"account_id,omitzero"`
	ReferenceID    *string                     `json:"reference_id,omitzero"`
	Slug           *string                     `json:"slug,omitzero"`
	DateDeleted    conjoin.Nullable[string]    `json:"date_deleted,omitzero"`
	Cursor         *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort           map[string]string           `json:"sort,omitzero"`
	Limit          any                         `json:"limit,omitzero"`
}

type ListOrganizationsItem struct {
	OrganizationID   string                   `json:"organization_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	AppID            string                   `json:"app_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	Name             string                   `json:"name"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	Slug             string                   `json:"slug"`
	ImageURL         conjoin.Nullable[string] `json:"image_url,omitzero"`
	OwnerAccountID   conjoin.Nullable[string] `json:"owner_account_id,omitzero"`
	TotalMembers     *float64                 `json:"total_members,omitzero"`
	Settings         map[string]any           `json:"settings,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateOrganizationRequest struct {
	ReferenceID *string                  `json:"reference_id,omitzero"`
	Slug        string                   `json:"slug"`
	Name        string                   `json:"name"`
	Description conjoin.Nullable[string] `json:"description,omitzero"`
	ImageURL    conjoin.Nullable[string] `json:"image_url,omitzero"`
	Metadata    map[string]any           `json:"metadata,omitzero"`
}

type CreateOrganizationResponse = ListOrganizationsItem

type ListOrganizationsCountQuery = ListOrganizationsQuery

type ListOrganizationsCountResponse = ListCredentialsCountResponse

type ReadOrganizationResponse = ListOrganizationsItem

type UpdateOrganizationRequest struct {
	Name        *string                  `json:"name,omitzero"`
	Slug        *string                  `json:"slug,omitzero"`
	Description conjoin.Nullable[string] `json:"description,omitzero"`
	ImageURL    conjoin.Nullable[string] `json:"image_url,omitzero"`
	Metadata    map[string]any           `json:"metadata,omitzero"`
}

type UpdateOrganizationResponse = ListOrganizationsItem

type DeleteOrganizationQuery struct {
	Permanent any `json:"permanent,omitzero"`
	Force     any `json:"force,omitzero"`
}

type DeleteOrganizationResponse = ListOrganizationsItem

type UpdateOrganizationSettingsRequestMembership struct {
	Limit                   *int64 `json:"limit,omitzero"`
	InvitationExpirySeconds *int64 `json:"invitation_expiry_seconds,omitzero"`
}

type UpdateOrganizationSettingsRequestGroups struct {
	MaxPerOrg          *int64 `json:"max_per_org,omitzero"`
	MaxMembersPerGroup *int64 `json:"max_members_per_group,omitzero"`
	MaxRolesPerGroup   *int64 `json:"max_roles_per_group,omitzero"`
}

type UpdateOrganizationSettingsRequest struct {
	Membership     *UpdateOrganizationSettingsRequestMembership `json:"membership,omitzero"`
	Authentication *UpdateAppSettingsRequestAuthentication      `json:"authentication,omitzero"`
	Sessions       *UpdateAppSettingsRequestSessions            `json:"sessions,omitzero"`
	Groups         *UpdateOrganizationSettingsRequestGroups     `json:"groups,omitzero"`
	Unset          []string                                     `json:"unset,omitzero"`
}

type UpdateOrganizationSettingsResponse = ListOrganizationsItem
