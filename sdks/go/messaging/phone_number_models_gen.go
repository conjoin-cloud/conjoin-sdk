package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPhoneNumbersQuery struct {
	ReferenceID   any                              `json:"reference_id,omitzero"`
	PhoneNumberID any                              `json:"phone_number_id,omitzero"`
	Type          any                              `json:"type,omitzero"`
	PhoneNumber   *string                          `json:"phone_number,omitzero"`
	RegionCode    any                              `json:"region_code,omitzero"`
	Search        *string                          `json:"search,omitzero"`
	Cursor        *ListChannelAnalyticsQueryCursor `json:"cursor,omitzero"`
	Sort          map[string]string                `json:"sort,omitzero"`
	Limit         any                              `json:"limit,omitzero"`
}

type ListPhoneNumbersItemPrice struct {
	Amount       string `json:"amount"`
	CurrencyCode string `json:"currency_code"`
}

type ListPhoneNumbersItem struct {
	PhoneNumberID    string                     `json:"phone_number_id"`
	ProfileID        string                     `json:"profile_id"`
	ConjoinAccountID string                     `json:"conjoin_account_id"`
	ConjoinProjectID string                     `json:"conjoin_project_id"`
	LiveMode         bool                       `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string]   `json:"reference_id,omitzero"`
	Type             string                     `json:"type"`
	PhoneNumber      string                     `json:"phone_number"`
	CountryIsoCode   string                     `json:"country_iso_code"`
	RegionCode       string                     `json:"region_code"`
	Title            string                     `json:"title"`
	Description      *string                    `json:"description,omitzero"`
	Price            *ListPhoneNumbersItemPrice `json:"price,omitzero"`
	RecurringCharge  map[string]any             `json:"recurring_charge,omitzero"`
	Features         map[string]any             `json:"features,omitzero"`
	ProvisionedAt    conjoin.Nullable[string]   `json:"provisioned_at,omitzero"`
	ExpiresAt        conjoin.Nullable[string]   `json:"expires_at,omitzero"`
	Status           string                     `json:"status"`
	DateCreated      string                     `json:"date_created"`
	DateUpdated      string                     `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]   `json:"date_deleted,omitzero"`
}

type PurchasePhoneNumberRequestFeatures struct {
	SMS *bool `json:"sms,omitzero"`
	Mms *bool `json:"mms,omitzero"`
}

type PurchasePhoneNumberRequestConfigSMS struct {
	CampaignID *string `json:"campaign_id,omitzero"`
}

type PurchasePhoneNumberRequestConfig struct {
	SMS *PurchasePhoneNumberRequestConfigSMS `json:"sms,omitzero"`
}

type PurchasePhoneNumberRequest struct {
	ReferenceID    *string                             `json:"reference_id,omitzero"`
	PhoneNumber    string                              `json:"phone_number"`
	Type           string                              `json:"type"`
	Title          string                              `json:"title"`
	Description    *string                             `json:"description,omitzero"`
	MessageType    *string                             `json:"message_type,omitzero"`
	CountryIsoCode string                              `json:"country_iso_code"`
	Features       *PurchasePhoneNumberRequestFeatures `json:"features,omitzero"`
	Config         *PurchasePhoneNumberRequestConfig   `json:"config,omitzero"`
	CallbackURL    *string                             `json:"callback_url,omitzero"`
}

type PurchasePhoneNumberResponse = ListPhoneNumbersItem

type ListPhoneNumbersCountQuery = ListPhoneNumbersQuery

type ListPhoneNumbersCountResponse = ListChannelAnalyticsCountResponse

type TransferPhoneNumberRequest = TransferEmailSenderRequest

type TransferPhoneNumberResponse = ListPhoneNumbersItem

type ReleasePhoneNumberResponse = ListPhoneNumbersItem

type ListAvailablePhoneNumbersQuery struct {
	Type       *string `json:"type,omitzero"`
	RegionCode *string `json:"region_code,omitzero"`
	Limit      any     `json:"limit,omitzero"`
}

type ListAvailablePhoneNumbersItemCapabilities struct {
	SMS   *bool `json:"sms,omitzero"`
	Mms   *bool `json:"mms,omitzero"`
	Voice *bool `json:"voice,omitzero"`
}

type ListAvailablePhoneNumbersItemRecurringCharge struct {
	Amount           string  `json:"amount"`
	CurrencyCode     string  `json:"currency_code"`
	DurationType     string  `json:"duration_type"`
	DurationQuantity float64 `json:"duration_quantity"`
}

type ListAvailablePhoneNumbersItem struct {
	Type                        string                                       `json:"type"`
	PhoneNumber                 string                                       `json:"phone_number"`
	CountryIsoCode              string                                       `json:"country_iso_code"`
	Capabilities                ListAvailablePhoneNumbersItemCapabilities    `json:"capabilities"`
	Price                       ListPhoneNumbersItemPrice                    `json:"price"`
	RecurringCharge             ListAvailablePhoneNumbersItemRecurringCharge `json:"recurring_charge"`
	RequiresSupportingDocuments bool                                         `json:"requires_supporting_documents"`
}
