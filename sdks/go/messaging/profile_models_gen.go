package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateProfileRequestFeatures struct {
	SMS   *bool `json:"sms,omitzero"`
	Email *bool `json:"email,omitzero"`
}

type CreateProfileRequestSMSConfig struct {
	Tracking *CreateEmailSenderRequestTracking `json:"tracking,omitzero"`
}

type CreateProfileRequestMultisendConfig struct {
	MessagePriority   *string  `json:"message_priority,omitzero"`
	RetryStatuses     []string `json:"retry_statuses,omitzero"`
	PreferredChannels []string `json:"preferred_channels"`
}

type CreateProfileRequestVerificationsConfig struct {
	PreferredSender *string `json:"preferred_sender,omitzero"`
}

type CreateProfileRequest struct {
	Name                 string                                   `json:"name"`
	Description          *string                                  `json:"description,omitzero"`
	Features             *CreateProfileRequestFeatures            `json:"features,omitzero"`
	ResourceRegion       *string                                  `json:"resource_region,omitzero"`
	SMSConfig            CreateProfileRequestSMSConfig            `json:"sms_config"`
	EmailConfig          CreateProfileRequestSMSConfig            `json:"email_config"`
	MultisendConfig      *CreateProfileRequestMultisendConfig     `json:"multisend_config,omitzero"`
	VerificationsConfig  *CreateProfileRequestVerificationsConfig `json:"verifications_config,omitzero"`
	Properties           map[string]any                           `json:"properties,omitzero"`
	MessageRetentionDays *float64                                 `json:"message_retention_days,omitzero"`
}

type CreateProfileResponseFeatures struct {
	SMS   bool `json:"sms"`
	Email bool `json:"email"`
}

type CreateProfileResponse struct {
	ProfileID            string                        `json:"profile_id"`
	ConjoinAccountID     string                        `json:"conjoin_account_id"`
	ConjoinProjectID     string                        `json:"conjoin_project_id"`
	LiveMode             bool                          `json:"live_mode"`
	ReferenceID          conjoin.Nullable[string]      `json:"reference_id,omitzero"`
	Name                 string                        `json:"name"`
	Description          *string                       `json:"description,omitzero"`
	IsSystemProfile      bool                          `json:"is_system_profile"`
	ResourceRegion       string                        `json:"resource_region"`
	Properties           map[string]any                `json:"properties,omitzero"`
	MessageRetentionDays float64                       `json:"message_retention_days"`
	Features             CreateProfileResponseFeatures `json:"features"`
	EmailConfig          map[string]any                `json:"email_config,omitzero"`
	SMSConfig            map[string]any                `json:"sms_config,omitzero"`
	MultisendConfig      map[string]any                `json:"multisend_config,omitzero"`
	VerificationConfig   map[string]any                `json:"verification_config,omitzero"`
	Status               string                        `json:"status"`
	DateCreated          string                        `json:"date_created"`
	DateUpdated          string                        `json:"date_updated"`
	DateDeleted          conjoin.Nullable[string]      `json:"date_deleted,omitzero"`
}

type EnableProfileResponse = CreateProfileResponse

type DisableProfileResponse = CreateProfileResponse

type CloseProfileResponse = CreateProfileResponse

type UpdateProfileRequest struct {
	Name                 *string                       `json:"name,omitzero"`
	Features             *CreateProfileRequestFeatures `json:"features,omitzero"`
	MessageRetentionDays *float64                      `json:"message_retention_days,omitzero"`
}

type UpdateProfileResponse = CreateProfileResponse

type ReadProfileResponse = CreateProfileResponse

type DeleteProfileResponse = CreateProfileResponse

type UpdateProfileEmailConfigRequestEmailConfigSuppression struct {
	Statuses []string `json:"statuses,omitzero"`
}

type UpdateProfileEmailConfigRequestEmailConfig struct {
	Suppression *UpdateProfileEmailConfigRequestEmailConfigSuppression `json:"suppression,omitzero"`
	Tracking    *CreateEmailSenderRequestTracking                      `json:"tracking,omitzero"`
}

type UpdateProfileEmailConfigRequest struct {
	EmailConfig UpdateProfileEmailConfigRequestEmailConfig `json:"email_config"`
}

type UpdateProfileEmailConfigResponse = CreateProfileResponse

type UpdateProfileMultisendConfigRequestMultisendConfig struct {
	PreferredChannels []string `json:"preferred_channels,omitzero"`
}

type UpdateProfileMultisendConfigRequest struct {
	MultisendConfig UpdateProfileMultisendConfigRequestMultisendConfig `json:"multisend_config"`
}

type UpdateProfileMultisendConfigResponse = CreateProfileResponse

type UpdateProfileVerificationsConfigRequest struct {
	VerificationsConfig CreateProfileRequestVerificationsConfig `json:"verifications_config"`
}

type UpdateProfileVerificationsConfigResponse = CreateProfileResponse

type ListProfilesRequestQuery struct {
	Name any `json:"name,omitzero"`
}

type ListProfilesRequest struct {
	Filter map[string]bool           `json:"filter,omitzero"`
	Query  *ListProfilesRequestQuery `json:"query,omitzero"`
	Sort   map[string]string         `json:"sort"`
	Limit  any                       `json:"limit,omitzero"`
}

type ListProfilesItem = CreateProfileResponse
