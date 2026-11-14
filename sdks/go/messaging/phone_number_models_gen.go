package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

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
	Type           string                              `json:"type"`
	Title          string                              `json:"title"`
	Description    *string                             `json:"description,omitzero"`
	MessageType    *string                             `json:"message_type,omitzero"`
	CountryIsoCode string                              `json:"country_iso_code"`
	Features       *PurchasePhoneNumberRequestFeatures `json:"features,omitzero"`
	PhoneNumber    string                              `json:"phone_number"`
	Config         PurchasePhoneNumberRequestConfig    `json:"config"`
	CallbackURL    string                              `json:"callback_url"`
}

type PurchasePhoneNumberResponsePrice struct {
	Amount       float64 `json:"amount"`
	CurrencyCode string  `json:"currency_code"`
}

type PurchasePhoneNumberResponse struct {
	PhoneNumberID    string                            `json:"phone_number_id"`
	ProfileID        string                            `json:"profile_id"`
	ConjoinAccountID string                            `json:"conjoin_account_id"`
	ConjoinProjectID string                            `json:"conjoin_project_id"`
	LiveMode         bool                              `json:"live_mode"`
	ReferenceID      conjoin.Nullable[string]          `json:"reference_id,omitzero"`
	Type             string                            `json:"type"`
	PhoneNumber      string                            `json:"phone_number"`
	CountryIsoCode   string                            `json:"country_iso_code"`
	RegionCode       string                            `json:"region_code"`
	Title            string                            `json:"title"`
	Description      *string                           `json:"description,omitzero"`
	Price            *PurchasePhoneNumberResponsePrice `json:"price,omitzero"`
	RecurringCharge  map[string]any                    `json:"recurring_charge,omitzero"`
	Features         map[string]any                    `json:"features,omitzero"`
	ProvisionedAt    conjoin.Nullable[string]          `json:"provisioned_at,omitzero"`
	ExpiresAt        conjoin.Nullable[string]          `json:"expires_at,omitzero"`
	Status           string                            `json:"status"`
	DateCreated      string                            `json:"date_created"`
	DateUpdated      string                            `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]          `json:"date_deleted,omitzero"`
}

type UpdatePhoneNumberResponse = PurchasePhoneNumberResponse

type ListAvailablePhoneNumbersQueryQuery struct {
	Type       *string `json:"type,omitzero"`
	RegionCode string  `json:"region_code"`
}

type ListAvailablePhoneNumbersQuery struct {
	Query *ListAvailablePhoneNumbersQueryQuery `json:"query,omitzero"`
	Limit any                                  `json:"limit,omitzero"`
}

type ListAvailablePhoneNumbersItem = PurchasePhoneNumberResponse

type ListPhoneNumbersQueryQueryType struct {
	IsEmpty                   *bool    `json:"is_empty,omitzero"`
	Contains                  []string `json:"contains,omitzero"`
	LengthLessThan            *float64 `json:"length_less_than,omitzero"`
	LengthLessThanOrEquals    *float64 `json:"length_less_than_or_equals,omitzero"`
	LengthGreaterThan         *float64 `json:"length_greater_than,omitzero"`
	LengthGreaterThanOrEquals *float64 `json:"length_greater_than_or_equals,omitzero"`
}

type ListPhoneNumbersQueryQuery struct {
	PhoneNumberID any                             `json:"phone_number_id,omitzero"`
	Type          *ListPhoneNumbersQueryQueryType `json:"type,omitzero"`
	PhoneNumber   *string                         `json:"phone_number,omitzero"`
	RegionCode    any                             `json:"region_code,omitzero"`
}

type ListPhoneNumbersQuery struct {
	Filter map[string]bool             `json:"filter,omitzero"`
	Cursor *ListContactsRequestCursor  `json:"cursor,omitzero"`
	Query  *ListPhoneNumbersQueryQuery `json:"query,omitzero"`
	Search *ListContactsRequestSearch  `json:"search,omitzero"`
	Sort   map[string]string           `json:"sort,omitzero"`
	Limit  any                         `json:"limit,omitzero"`
}

type ListPhoneNumbersItem = PurchasePhoneNumberResponse

type ReleasePhoneNumberResponse = PurchasePhoneNumberResponse
