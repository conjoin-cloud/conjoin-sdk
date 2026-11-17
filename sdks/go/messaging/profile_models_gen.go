package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListProfilesQuery struct {
	ReferenceID any                                   `json:"reference_id,omitzero"`
	Name        any                                   `json:"name,omitzero"`
	DateCreated *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                     `json:"sort,omitzero"`
	Limit       any                                   `json:"limit,omitzero"`
}

type ListProfilesItemFeatures struct {
	SMS   bool `json:"sms"`
	Email bool `json:"email"`
}

type ListProfilesItem struct {
	ProfileID            string                   `json:"profile_id"`
	ConjoinAccountID     string                   `json:"conjoin_account_id"`
	ConjoinProjectID     string                   `json:"conjoin_project_id"`
	LiveMode             bool                     `json:"live_mode"`
	ReferenceID          conjoin.Nullable[string] `json:"reference_id,omitzero"`
	Name                 string                   `json:"name"`
	Description          *string                  `json:"description,omitzero"`
	IsSystemProfile      bool                     `json:"is_system_profile"`
	ResourceRegion       string                   `json:"resource_region"`
	Properties           map[string]any           `json:"properties,omitzero"`
	MessageRetentionDays float64                  `json:"message_retention_days"`
	Features             ListProfilesItemFeatures `json:"features"`
	EmailConfig          map[string]any           `json:"email_config,omitzero"`
	SMSConfig            map[string]any           `json:"sms_config,omitzero"`
	MultisendConfig      map[string]any           `json:"multisend_config,omitzero"`
	VerificationConfig   map[string]any           `json:"verification_config,omitzero"`
	Status               string                   `json:"status"`
	DateCreated          string                   `json:"date_created"`
	DateUpdated          string                   `json:"date_updated"`
	DateDeleted          conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

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
	ReferenceID          *string                                  `json:"reference_id,omitzero"`
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

type CreateProfileResponse = ListProfilesItem

type ListProfilesCountQuery = ListProfilesQuery

type ListProfilesCountResponse = ListChannelAnalyticsCountResponse

type EnableProfileResponse = ListProfilesItem

type DisableProfileResponse = ListProfilesItem

type EnableProfileChannelsRequest = SuppressContactMessagesRequest

type EnableProfileChannelsResponse = ListProfilesItem

type DisableProfileChannelsRequest = SuppressContactMessagesRequest

type DisableProfileChannelsResponse = ListProfilesItem

type CloseProfileResponse = ListProfilesItem

type UpdateProfileRequestEmailConfigSuppression struct {
	Statuses []string `json:"statuses,omitzero"`
}

type UpdateProfileRequestEmailConfig struct {
	Suppression *UpdateProfileRequestEmailConfigSuppression `json:"suppression,omitzero"`
	Tracking    *CreateEmailSenderRequestTracking           `json:"tracking,omitzero"`
}

type UpdateProfileRequestMultisendConfig struct {
	PreferredChannels []string `json:"preferred_channels,omitzero"`
}

type UpdateProfileRequest struct {
	Name                 *string                                  `json:"name,omitzero"`
	MessageRetentionDays *float64                                 `json:"message_retention_days,omitzero"`
	EmailConfig          *UpdateProfileRequestEmailConfig         `json:"email_config,omitzero"`
	MultisendConfig      *UpdateProfileRequestMultisendConfig     `json:"multisend_config,omitzero"`
	VerificationsConfig  *CreateProfileRequestVerificationsConfig `json:"verifications_config,omitzero"`
}

type UpdateProfileResponse = ListProfilesItem

type ReadProfileResponse = ListProfilesItem

type DeleteProfileResponse = ListProfilesItem
