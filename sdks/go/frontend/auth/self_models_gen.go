package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSelfOrganizationsQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListSelfOrganizationsQuery struct {
	Cursor *ListSelfOrganizationsQueryCursor `json:"cursor,omitzero"`
	Sort   map[string]string                 `json:"sort,omitzero"`
	Limit  any                               `json:"limit,omitzero"`
}

type ListSelfOrganizationsItem struct {
	AccountOrganizationID string                   `json:"account_organization_id"`
	AccountID             string                   `json:"account_id"`
	OrganizationID        string                   `json:"organization_id"`
	JoinedAt              conjoin.Nullable[string] `json:"joined_at,omitzero"`
	Roles                 []string                 `json:"roles,omitzero"`
	Status                string                   `json:"status"`
	ConjoinAccountID      string                   `json:"conjoin_account_id"`
	ConjoinProjectID      string                   `json:"conjoin_project_id"`
	AppID                 string                   `json:"app_id"`
	LiveMode              bool                     `json:"live_mode"`
	Metadata              map[string]any           `json:"metadata,omitzero"`
	DateCreated           string                   `json:"date_created"`
	DateUpdated           string                   `json:"date_updated"`
	DateDeleted           conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListSelfSessionsQuery struct {
	Status         *string                           `json:"status,omitzero"`
	IncludeExpired any                               `json:"include_expired,omitzero"`
	Cursor         *ListSelfOrganizationsQueryCursor `json:"cursor,omitzero"`
	Sort           map[string]string                 `json:"sort,omitzero"`
	Limit          any                               `json:"limit,omitzero"`
}

type ListSelfSessionsItemLastActivity struct {
	IP          conjoin.Nullable[string]  `json:"ip,omitzero"`
	InitiatedAt conjoin.Nullable[string]  `json:"initiated_at,omitzero"`
	CountryCode conjoin.Nullable[string]  `json:"country_code,omitzero"`
	Latitude    conjoin.Nullable[float64] `json:"latitude,omitzero"`
	Longitude   conjoin.Nullable[float64] `json:"longitude,omitzero"`
}

type ListSelfSessionsItem struct {
	SessionID        string                            `json:"session_id"`
	AccountID        string                            `json:"account_id"`
	ClientID         string                            `json:"client_id"`
	AppID            string                            `json:"app_id"`
	ConjoinAccountID string                            `json:"conjoin_account_id"`
	ConjoinProjectID string                            `json:"conjoin_project_id"`
	LiveMode         bool                              `json:"live_mode"`
	ExpiresAt        conjoin.Nullable[string]          `json:"expires_at,omitzero"`
	LastActivity     *ListSelfSessionsItemLastActivity `json:"last_activity,omitzero"`
	Status           string                            `json:"status"`
	RevokedAt        conjoin.Nullable[string]          `json:"revoked_at,omitzero"`
	RevokedReason    conjoin.Nullable[string]          `json:"revoked_reason,omitzero"`
	Metadata         map[string]any                    `json:"metadata,omitzero"`
	DateCreated      string                            `json:"date_created"`
	DateUpdated      string                            `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]          `json:"date_deleted,omitzero"`
}

type ReadSelfProfileResponseEmailsItemVerification struct {
	Status     string  `json:"status"`
	VerifiedAt *string `json:"verified_at"`
}

type ReadSelfProfileResponseEmailsItem struct {
	Email        string                                        `json:"email"`
	IsPrimary    bool                                          `json:"is_primary"`
	Verification ReadSelfProfileResponseEmailsItemVerification `json:"verification"`
}

type ReadSelfProfileResponsePhonesItem struct {
	Phone        string                                        `json:"phone"`
	IsPrimary    bool                                          `json:"is_primary"`
	Verification ReadSelfProfileResponseEmailsItemVerification `json:"verification"`
}

type ReadSelfProfileResponse struct {
	AccountID        string                              `json:"account_id"`
	AppID            string                              `json:"app_id"`
	ConjoinAccountID string                              `json:"conjoin_account_id"`
	ConjoinProjectID string                              `json:"conjoin_project_id"`
	LiveMode         bool                                `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string]            `json:"reference_id,omitzero"`
	Emails           []ReadSelfProfileResponseEmailsItem `json:"emails,omitzero"`
	Phones           []ReadSelfProfileResponsePhonesItem `json:"phones,omitzero"`
	Name             conjoin.Nullable[string]            `json:"name,omitzero"`
	ImageURL         conjoin.Nullable[string]            `json:"image_url,omitzero"`
	Status           string                              `json:"status"`
	LastActiveAt     conjoin.Nullable[string]            `json:"last_active_at,omitzero"`
	DormantAt        conjoin.Nullable[string]            `json:"dormant_at,omitzero"`
	CustomAttributes map[string]any                      `json:"custom_attributes,omitzero"`
	GlobalRoles      []string                            `json:"global_roles,omitzero"`
	Metadata         map[string]any                      `json:"metadata,omitzero"`
	DateCreated      string                              `json:"date_created"`
	DateUpdated      string                              `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]            `json:"date_deleted,omitzero"`
}

type UpdateSelfProfileRequest struct {
	Name         *string                  `json:"name,omitzero"`
	PrimaryEmail *string                  `json:"primary_email,omitzero"`
	PrimaryPhone *string                  `json:"primary_phone,omitzero"`
	ImageURL     conjoin.Nullable[string] `json:"image_url,omitzero"`
}

type UpdateSelfProfileResponse = ReadSelfProfileResponse

type ListSelfSessionsCountQuery = ListSelfSessionsQuery

type ListSelfSessionsCountResponse struct {
	Count int64 `json:"count"`
}

type RevokeSelfSessionResponse struct {
	RevokedCount float64  `json:"revoked_count"`
	SessionIDs   []string `json:"session_ids,omitzero"`
}

type ListSelfOrganizationsCountQuery = ListSelfOrganizationsQuery

type ListSelfOrganizationsCountResponse = ListSelfSessionsCountResponse

type ReadSelfActiveOrganizationResponse struct {
	ActiveOrganizationID    *string  `json:"active_organization_id"`
	ActiveOrganizationRoles []string `json:"active_organization_roles"`
}

type UpdateSelfActiveOrganizationRequest struct {
	OrganizationID *string `json:"organization_id"`
}

type UpdateSelfActiveOrganizationResponse struct {
	ActiveOrganizationID *string `json:"active_organization_id"`
}
