package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListInvitationsQuery struct {
	ReferenceID *string                     `json:"reference_id,omitzero"`
	Email       *string                     `json:"email,omitzero"`
	Status      *string                     `json:"status,omitzero"`
	DateDeleted conjoin.Nullable[string]    `json:"date_deleted,omitzero"`
	Cursor      *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string           `json:"sort,omitzero"`
	Limit       any                         `json:"limit,omitzero"`
}

type ListInvitationsItem struct {
	InvitationID       string                   `json:"invitation_id"`
	ReferenceID        string                   `json:"reference_id"`
	OrganizationID     string                   `json:"organization_id"`
	AppID              string                   `json:"app_id"`
	ConjoinAccountID   string                   `json:"conjoin_account_id"`
	ConjoinProjectID   string                   `json:"conjoin_project_id"`
	LiveMode           bool                     `json:"live_mode"`
	Email              string                   `json:"email"`
	Name               conjoin.Nullable[string] `json:"name,omitzero"`
	Roles              []string                 `json:"roles,omitzero"`
	ExpiresAt          conjoin.Nullable[string] `json:"expires_at,omitzero"`
	UsedAt             conjoin.Nullable[string] `json:"used_at,omitzero"`
	Status             string                   `json:"status"`
	InvitedByAccountID string                   `json:"invited_by_account_id"`
	Metadata           map[string]any           `json:"metadata,omitzero"`
	DateCreated        string                   `json:"date_created"`
	DateUpdated        string                   `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateInvitationRequest struct {
	ReferenceID      *string                  `json:"reference_id,omitzero"`
	Email            string                   `json:"email"`
	Name             conjoin.Nullable[string] `json:"name,omitzero"`
	Roles            []string                 `json:"roles,omitzero"`
	RedirectURI      conjoin.Nullable[string] `json:"redirect_uri,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	ExpiresInSeconds *float64                 `json:"expires_in_seconds,omitzero"`
}

type CreateInvitationResponse struct {
	InvitationID       string                   `json:"invitation_id"`
	ReferenceID        string                   `json:"reference_id"`
	OrganizationID     string                   `json:"organization_id"`
	AppID              string                   `json:"app_id"`
	ConjoinAccountID   string                   `json:"conjoin_account_id"`
	ConjoinProjectID   string                   `json:"conjoin_project_id"`
	LiveMode           bool                     `json:"live_mode"`
	Email              string                   `json:"email"`
	Name               conjoin.Nullable[string] `json:"name,omitzero"`
	Roles              []string                 `json:"roles,omitzero"`
	ExpiresAt          conjoin.Nullable[string] `json:"expires_at,omitzero"`
	UsedAt             conjoin.Nullable[string] `json:"used_at,omitzero"`
	Status             string                   `json:"status"`
	InvitedByAccountID string                   `json:"invited_by_account_id"`
	Metadata           map[string]any           `json:"metadata,omitzero"`
	DateCreated        string                   `json:"date_created"`
	DateUpdated        string                   `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string] `json:"date_deleted,omitzero"`
	InvitationURL      string                   `json:"invitation_url"`
}

type ListInvitationsCountQuery = ListInvitationsQuery

type ListInvitationsCountResponse = ListCredentialsCountResponse

type RevokeInvitationResponse = ListInvitationsItem

type ResendInvitationRequest struct {
	RedirectURI      conjoin.Nullable[string] `json:"redirect_uri,omitzero"`
	ExpiresInSeconds *float64                 `json:"expires_in_seconds,omitzero"`
}

type ResendInvitationResponse = CreateInvitationResponse
