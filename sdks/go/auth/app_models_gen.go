package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListAppsQuery struct {
	AppID       *string                     `json:"app_id,omitzero"`
	ReferenceID *string                     `json:"reference_id,omitzero"`
	Slug        *string                     `json:"slug,omitzero"`
	Cursor      *ListCredentialsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string           `json:"sort,omitzero"`
	Limit       any                         `json:"limit,omitzero"`
}

type ListAppsItem struct {
	AppID            string                   `json:"app_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	Slug             string                   `json:"slug"`
	Name             string                   `json:"name"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	SupportEmail     conjoin.Nullable[string] `json:"support_email,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	Settings         map[string]any           `json:"settings,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateAppRequest struct {
	ReferenceID  *string                  `json:"reference_id,omitzero"`
	Slug         string                   `json:"slug"`
	Name         string                   `json:"name"`
	Description  conjoin.Nullable[string] `json:"description,omitzero"`
	SupportEmail conjoin.Nullable[string] `json:"support_email,omitzero"`
	Metadata     map[string]any           `json:"metadata,omitzero"`
}

type CreateAppResponse = ListAppsItem

type ListAppsCountQuery = ListAppsQuery

type ListAppsCountResponse = ListCredentialsCountResponse

type ReadAppResponse = ListAppsItem

type UpdateAppRequest struct {
	Name         *string                  `json:"name,omitzero"`
	Description  conjoin.Nullable[string] `json:"description,omitzero"`
	SupportEmail conjoin.Nullable[string] `json:"support_email,omitzero"`
	Metadata     map[string]any           `json:"metadata,omitzero"`
}

type UpdateAppResponse = ListAppsItem

type UpdateAppSettingsRequestGuardBruteForce struct {
	IsEnabled      *bool   `json:"is_enabled,omitzero"`
	Action         *string `json:"action,omitzero"`
	MaxAttempts    *int64  `json:"max_attempts,omitzero"`
	WindowSeconds  *int64  `json:"window_seconds,omitzero"`
	LockoutSeconds *int64  `json:"lockout_seconds,omitzero"`
}

type UpdateAppSettingsRequestGuardBotDetection struct {
	IsEnabled           *bool   `json:"is_enabled,omitzero"`
	Action              *string `json:"action,omitzero"`
	MinSubmissionTimeMs *int64  `json:"min_submission_time_ms,omitzero"`
}

type UpdateAppSettingsRequestGuardDeviceDetection struct {
	IsEnabled *bool   `json:"is_enabled,omitzero"`
	Action    *string `json:"action,omitzero"`
}

type UpdateAppSettingsRequestGuardImpossibleTravel struct {
	IsEnabled   *bool   `json:"is_enabled,omitzero"`
	Action      *string `json:"action,omitzero"`
	MaxSpeedKmh *int64  `json:"max_speed_kmh,omitzero"`
}

type UpdateAppSettingsRequestGuardSignupAbuse struct {
	IsEnabled       *bool   `json:"is_enabled,omitzero"`
	Action          *string `json:"action,omitzero"`
	MaxSignupsPerIP *int64  `json:"max_signups_per_ip,omitzero"`
	WindowSeconds   *int64  `json:"window_seconds,omitzero"`
}

type UpdateAppSettingsRequestGuardDormantAccount struct {
	IsEnabled            *bool   `json:"is_enabled,omitzero"`
	Action               *string `json:"action,omitzero"`
	DormantThresholdDays *int64  `json:"dormant_threshold_days,omitzero"`
}

type UpdateAppSettingsRequestGuardRegionRestrictions struct {
	IsEnabled        *bool    `json:"is_enabled,omitzero"`
	Action           *string  `json:"action,omitzero"`
	AllowedCountries []string `json:"allowed_countries,omitzero"`
	BlockedCountries []string `json:"blocked_countries,omitzero"`
}

type UpdateAppSettingsRequestGuardVerificationFlooding struct {
	IsEnabled     *bool   `json:"is_enabled,omitzero"`
	Action        *string `json:"action,omitzero"`
	MaxAttempts   *int64  `json:"max_attempts,omitzero"`
	WindowSeconds *int64  `json:"window_seconds,omitzero"`
}

type UpdateAppSettingsRequestGuardConcurrentSessions struct {
	IsEnabled          *bool   `json:"is_enabled,omitzero"`
	Action             *string `json:"action,omitzero"`
	MaxDistanceKm      *int64  `json:"max_distance_km,omitzero"`
	MaxSessionsToCheck *int64  `json:"max_sessions_to_check,omitzero"`
}

type UpdateAppSettingsRequestGuardDisposableEmail struct {
	IsEnabled      *bool    `json:"is_enabled,omitzero"`
	Action         *string  `json:"action,omitzero"`
	BlockedDomains []string `json:"blocked_domains,omitzero"`
}

type UpdateAppSettingsRequestGuard struct {
	IsEnabled            *bool                                              `json:"is_enabled,omitzero"`
	BruteForce           *UpdateAppSettingsRequestGuardBruteForce           `json:"brute_force,omitzero"`
	BotDetection         *UpdateAppSettingsRequestGuardBotDetection         `json:"bot_detection,omitzero"`
	DeviceDetection      *UpdateAppSettingsRequestGuardDeviceDetection      `json:"device_detection,omitzero"`
	ImpossibleTravel     *UpdateAppSettingsRequestGuardImpossibleTravel     `json:"impossible_travel,omitzero"`
	SignupAbuse          *UpdateAppSettingsRequestGuardSignupAbuse          `json:"signup_abuse,omitzero"`
	DormantAccount       *UpdateAppSettingsRequestGuardDormantAccount       `json:"dormant_account,omitzero"`
	RegionRestrictions   *UpdateAppSettingsRequestGuardRegionRestrictions   `json:"region_restrictions,omitzero"`
	AnonymousNetwork     *UpdateAppSettingsRequestGuardDeviceDetection      `json:"anonymous_network,omitzero"`
	NewCountry           *UpdateAppSettingsRequestGuardDeviceDetection      `json:"new_country,omitzero"`
	VerificationFlooding *UpdateAppSettingsRequestGuardVerificationFlooding `json:"verification_flooding,omitzero"`
	ConcurrentSessions   *UpdateAppSettingsRequestGuardConcurrentSessions   `json:"concurrent_sessions,omitzero"`
	DisposableEmail      *UpdateAppSettingsRequestGuardDisposableEmail      `json:"disposable_email,omitzero"`
}

type UpdateAppSettingsRequestCustomAttributesSchemaItemValidation struct {
	Min     *float64 `json:"min,omitzero"`
	Max     *float64 `json:"max,omitzero"`
	Pattern *string  `json:"pattern,omitzero"`
	Enum    []any    `json:"enum,omitzero"`
}

type UpdateAppSettingsRequestCustomAttributesSchemaItem struct {
	Name         string                                                        `json:"name"`
	Type         string                                                        `json:"type"`
	IsRequired   *bool                                                         `json:"is_required,omitzero"`
	DefaultValue any                                                           `json:"default_value,omitzero"`
	Validation   *UpdateAppSettingsRequestCustomAttributesSchemaItemValidation `json:"validation,omitzero"`
}

type UpdateAppSettingsRequestMessagingOptionsEmail struct {
	Provider       conjoin.Nullable[string] `json:"provider,omitzero"`
	EnabledMethods []string                 `json:"enabled_methods,omitzero"`
}

type UpdateAppSettingsRequestMessagingOptionsSMS struct {
	Provider conjoin.Nullable[string] `json:"provider,omitzero"`
}

type UpdateAppSettingsRequestMessagingOptions struct {
	Email *UpdateAppSettingsRequestMessagingOptionsEmail `json:"email,omitzero"`
	SMS   *UpdateAppSettingsRequestMessagingOptionsSMS   `json:"sms,omitzero"`
}

type UpdateAppSettingsRequestAuthenticationAllowList struct {
	IsEnabled *bool    `json:"is_enabled,omitzero"`
	Emails    []string `json:"emails,omitzero"`
	Domains   []string `json:"domains,omitzero"`
}

type UpdateAppSettingsRequestAuthenticationMFAStepUp struct {
	IsEnabled  *bool  `json:"is_enabled,omitzero"`
	TTLSeconds *int64 `json:"ttl_seconds,omitzero"`
}

type UpdateAppSettingsRequestAuthenticationMFATrustedDevices struct {
	IsEnabled         *bool  `json:"is_enabled,omitzero"`
	TrustDurationDays *int64 `json:"trust_duration_days,omitzero"`
	MaxPerAccount     *int64 `json:"max_per_account,omitzero"`
}

type UpdateAppSettingsRequestAuthenticationMFA struct {
	EnableTotp     *bool                                                    `json:"enable_totp,omitzero"`
	EnableSMS      *bool                                                    `json:"enable_sms,omitzero"`
	StepUp         *UpdateAppSettingsRequestAuthenticationMFAStepUp         `json:"step_up,omitzero"`
	TrustedDevices *UpdateAppSettingsRequestAuthenticationMFATrustedDevices `json:"trusted_devices,omitzero"`
}

type UpdateAppSettingsRequestAuthenticationIdentityResolutionOrgDomain struct {
	Enabled             *bool `json:"enabled,omitzero"`
	RequireVerification *bool `json:"require_verification,omitzero"`
}

type UpdateAppSettingsRequestAuthenticationIdentityResolution struct {
	Precedence                         []string                                                           `json:"precedence,omitzero"`
	OrgDomain                          *UpdateAppSettingsRequestAuthenticationIdentityResolutionOrgDomain `json:"org_domain,omitzero"`
	SSOCollisionDefault                *string                                                            `json:"sso_collision_default,omitzero"`
	MergePolicy                        *string                                                            `json:"merge_policy,omitzero"`
	AllowCrossOrganizationIdentityLink *bool                                                              `json:"allow_cross_organization_identity_link,omitzero"`
}

type UpdateAppSettingsRequestAuthentication struct {
	BlockEmailSubaddresses *bool                                                     `json:"block_email_subaddresses,omitzero"`
	PasskeyPrimaryEnabled  *bool                                                     `json:"passkey_primary_enabled,omitzero"`
	SignupMode             *string                                                   `json:"signup_mode,omitzero"`
	AllowList              *UpdateAppSettingsRequestAuthenticationAllowList          `json:"allow_list,omitzero"`
	BlockList              *UpdateAppSettingsRequestAuthenticationAllowList          `json:"block_list,omitzero"`
	EnabledMethods         []string                                                  `json:"enabled_methods,omitzero"`
	MFA                    *UpdateAppSettingsRequestAuthenticationMFA                `json:"mfa,omitzero"`
	IdentityResolution     *UpdateAppSettingsRequestAuthenticationIdentityResolution `json:"identity_resolution,omitzero"`
}

type UpdateAppSettingsRequestSessions struct {
	IsMultiUserSessionsEnabled               *bool                   `json:"is_multi_user_sessions_enabled,omitzero"`
	AllowMultipleDeviceSessions              *bool                   `json:"allow_multiple_device_sessions,omitzero"`
	MaxConcurrentSessionsPerAccountPerClient conjoin.Nullable[int64] `json:"max_concurrent_sessions_per_account_per_client,omitzero"`
	SessionExpirySeconds                     *int64                  `json:"session_expiry_seconds,omitzero"`
	AbsoluteSessionLifetimeSeconds           conjoin.Nullable[int64] `json:"absolute_session_lifetime_seconds,omitzero"`
	IdleTimeoutSeconds                       conjoin.Nullable[int64] `json:"idle_timeout_seconds,omitzero"`
	AccessTokenTTLSeconds                    *int64                  `json:"access_token_ttl_seconds,omitzero"`
	CookieSameSite                           *string                 `json:"cookie_same_site,omitzero"`
	EnableDeviceBinding                      *bool                   `json:"enable_device_binding,omitzero"`
	EnableNativeTokenIssuance                *bool                   `json:"enable_native_token_issuance,omitzero"`
}

type UpdateAppSettingsRequest struct {
	Guard                  *UpdateAppSettingsRequestGuard                       `json:"guard,omitzero"`
	CustomAttributesSchema []UpdateAppSettingsRequestCustomAttributesSchemaItem `json:"custom_attributes_schema,omitzero"`
	CloudZoneID            conjoin.Nullable[string]                             `json:"cloud_zone_id,omitzero"`
	BillingEntityID        conjoin.Nullable[string]                             `json:"billing_entity_id,omitzero"`
	MessagingOptions       *UpdateAppSettingsRequestMessagingOptions            `json:"messaging_options,omitzero"`
	Authentication         *UpdateAppSettingsRequestAuthentication              `json:"authentication,omitzero"`
	Sessions               *UpdateAppSettingsRequestSessions                    `json:"sessions,omitzero"`
}

type UpdateAppSettingsResponse = ListAppsItem

type RotateAppSigningKeysResponseResponse struct {
	Type    string `json:"type"`
	Code    int64  `json:"code"`
	Message string `json:"message"`
}

type RotateAppSigningKeysResponse struct {
	Response *RotateAppSigningKeysResponseResponse `json:"response,omitzero"`
}
