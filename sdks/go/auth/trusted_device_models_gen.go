package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListTrustedDevicesQuery = ListPasskeysQuery

type ListTrustedDevicesItem struct {
	TrustedDeviceID   string                   `json:"trusted_device_id"`
	AccountID         string                   `json:"account_id"`
	AppID             string                   `json:"app_id"`
	ConjoinAccountID  string                   `json:"conjoin_account_id"`
	ConjoinProjectID  string                   `json:"conjoin_project_id"`
	LiveMode          bool                     `json:"live_mode"`
	IPPrefix          conjoin.Nullable[string] `json:"ip_prefix,omitzero"`
	UserAgent         conjoin.Nullable[string] `json:"user_agent,omitzero"`
	Label             conjoin.Nullable[string] `json:"label,omitzero"`
	TrustedAt         *string                  `json:"trusted_at,omitzero"`
	ExpiresAt         *string                  `json:"expires_at,omitzero"`
	AbsoluteExpiresAt *string                  `json:"absolute_expires_at,omitzero"`
	LastUsedAt        conjoin.Nullable[string] `json:"last_used_at,omitzero"`
	Status            string                   `json:"status"`
	Metadata          map[string]any           `json:"metadata,omitzero"`
	DateCreated       string                   `json:"date_created"`
	DateUpdated       string                   `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ListTrustedDevicesCountQuery = ListPasskeysQuery

type ListTrustedDevicesCountResponse = ListCredentialsCountResponse

type RevokeAllTrustedDevicesResponse struct {
	RevokedCount float64 `json:"revoked_count"`
}

type RevokeTrustedDeviceResponse = ListTrustedDevicesItem
