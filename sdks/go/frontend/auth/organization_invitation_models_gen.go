package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type AcceptOrganizationInvitationRequest struct {
	Token     string  `json:"token"`
	AccountID *string `json:"account_id,omitzero"`
}

type AcceptOrganizationInvitationResponseInvitationOrganization struct {
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

type AcceptOrganizationInvitationResponseInvitation struct {
	InvitationID       string                                                     `json:"invitation_id"`
	ReferenceID        string                                                     `json:"reference_id"`
	OrganizationID     string                                                     `json:"organization_id"`
	AppID              string                                                     `json:"app_id"`
	ConjoinAccountID   string                                                     `json:"conjoin_account_id"`
	ConjoinProjectID   string                                                     `json:"conjoin_project_id"`
	LiveMode           bool                                                       `json:"live_mode"`
	Email              string                                                     `json:"email"`
	Name               conjoin.Nullable[string]                                   `json:"name,omitzero"`
	Roles              []string                                                   `json:"roles,omitzero"`
	ExpiresAt          conjoin.Nullable[string]                                   `json:"expires_at,omitzero"`
	UsedAt             conjoin.Nullable[string]                                   `json:"used_at,omitzero"`
	Status             string                                                     `json:"status"`
	InvitedByAccountID string                                                     `json:"invited_by_account_id"`
	Metadata           map[string]any                                             `json:"metadata,omitzero"`
	DateCreated        string                                                     `json:"date_created"`
	DateUpdated        string                                                     `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string]                                   `json:"date_deleted,omitzero"`
	Organization       AcceptOrganizationInvitationResponseInvitationOrganization `json:"organization"`
}

type AcceptOrganizationInvitationResponse struct {
	NextAction string                                         `json:"next_action"`
	Invitation AcceptOrganizationInvitationResponseInvitation `json:"invitation"`
}
