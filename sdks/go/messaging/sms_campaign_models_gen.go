package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSmsCampaignsQuery = ListSmsBrandsQuery

type ListSmsCampaignsItem struct {
	CampaignID       string                   `json:"campaign_id"`
	ProfileID        string                   `json:"profile_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	BrandID          string                   `json:"brand_id"`
	UseCase          *string                  `json:"use_case,omitzero"`
	Description      *string                  `json:"description,omitzero"`
	Status           string                   `json:"status"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateSmsCampaignRequest struct {
	ReferenceID           *string  `json:"reference_id,omitzero"`
	BrandID               string   `json:"brand_id"`
	Title                 string   `json:"title"`
	Description           string   `json:"description"`
	MessageSamples        []string `json:"message_samples"`
	OptInMessage          *string  `json:"opt_in_message,omitzero"`
	OptOutMessage         string   `json:"opt_out_message"`
	HelpMessage           string   `json:"help_message"`
	UseCase               string   `json:"use_case"`
	SubUseCases           []string `json:"sub_use_cases,omitzero"`
	EmbedsLinks           *bool    `json:"embeds_links,omitzero"`
	EmbedsPhoneNumbers    *bool    `json:"embeds_phone_numbers,omitzero"`
	ProvisionNumberPool   *bool    `json:"provision_number_pool,omitzero"`
	AgeGated              *bool    `json:"age_gated,omitzero"`
	DirectLending         *bool    `json:"direct_lending,omitzero"`
	SubscriberOptIn       *bool    `json:"subscriber_opt_in,omitzero"`
	OptInKeywords         []string `json:"opt_in_keywords,omitzero"`
	OptOutKeywords        []string `json:"opt_out_keywords,omitzero"`
	HelpKeywords          []string `json:"help_keywords,omitzero"`
	MessageFlow           string   `json:"message_flow"`
	TermsAndConditionsURL string   `json:"terms_and_conditions_url"`
	PrivacyPolicyURL      string   `json:"privacy_policy_url"`
}

type CreateSmsCampaignResponse = ListSmsCampaignsItem

type ListSmsCampaignsCountQuery = ListSmsBrandsQuery

type ListSmsCampaignsCountResponse = ListChannelAnalyticsCountResponse

type ReadSmsCampaignResponse = ListSmsCampaignsItem

type UpdateSmsCampaignRequest struct {
	Title string `json:"title"`
}

type UpdateSmsCampaignResponse = ListSmsCampaignsItem

type DeleteSmsCampaignResponse = ListSmsCampaignsItem
