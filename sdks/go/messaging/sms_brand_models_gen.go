package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSmsBrandsQuery struct {
	ReferenceID any                                   `json:"reference_id,omitzero"`
	DateCreated *ListChannelAnalyticsQueryDateCreated `json:"date_created,omitzero"`
	DateUpdated *ListChannelAnalyticsQueryDateCreated `json:"date_updated,omitzero"`
	DateDeleted *ListChannelAnalyticsQueryDateCreated `json:"date_deleted,omitzero"`
	Cursor      *ListChannelAnalyticsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                     `json:"sort,omitzero"`
	Limit       any                                   `json:"limit,omitzero"`
}

type ListSmsBrandsItem struct {
	BrandID               string                   `json:"brand_id"`
	ProfileID             string                   `json:"profile_id"`
	ConjoinAccountID      string                   `json:"conjoin_account_id"`
	ConjoinProjectID      string                   `json:"conjoin_project_id"`
	LiveMode              bool                     `json:"live_mode"`
	ReferenceID           conjoin.Nullable[string] `json:"reference_id,omitzero"`
	DisplayName           string                   `json:"display_name"`
	BrandRegistrationType string                   `json:"brand_registration_type"`
	BrandTcrID            conjoin.Nullable[string] `json:"brand_tcr_id,omitzero"`
	SoleProprietorDetails map[string]any           `json:"sole_proprietor_details,omitzero"`
	BusinessDetails       map[string]any           `json:"business_details,omitzero"`
	Status                *string                  `json:"status,omitzero"`
	DateCreated           string                   `json:"date_created"`
	DateUpdated           string                   `json:"date_updated"`
	DateDeleted           conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateSmsBrandRequestBusinessRepresentative struct {
	BusinessTitle string `json:"business_title"`
	JobPosition   string `json:"job_position"`
	FirstName     string `json:"first_name"`
	LastName      string `json:"last_name"`
	EmailAddress  string `json:"email_address"`
	PhoneNumber   string `json:"phone_number"`
}

type CreateSmsBrandRequest struct {
	ReferenceID              *string                                      `json:"reference_id,omitzero"`
	DisplayName              string                                       `json:"display_name"`
	BrandRegistrationType    *string                                      `json:"brand_registration_type,omitzero"`
	BrandName                *string                                      `json:"brand_name,omitzero"`
	BrandCountryCode         *string                                      `json:"brand_country_code,omitzero"`
	BrandCity                *string                                      `json:"brand_city,omitzero"`
	BrandRegion              *string                                      `json:"brand_region,omitzero"`
	BrandStreetAddress1      *string                                      `json:"brand_street_address_1,omitzero"`
	BrandStreetAddress2      *string                                      `json:"brand_street_address_2,omitzero"`
	BrandPostalCode          *string                                      `json:"brand_postal_code,omitzero"`
	BrandVertical            *string                                      `json:"brand_vertical,omitzero"`
	MFAPhoneNumber           *string                                      `json:"mfa_phone_number,omitzero"`
	FirstName                *string                                      `json:"first_name,omitzero"`
	LastName                 *string                                      `json:"last_name,omitzero"`
	PhoneNumber              *string                                      `json:"phone_number,omitzero"`
	EmailAddress             *string                                      `json:"email_address,omitzero"`
	BrandType                *string                                      `json:"brand_type,omitzero"`
	BusinessType             *string                                      `json:"business_type,omitzero"`
	BusinessLegalName        *string                                      `json:"business_legal_name,omitzero"`
	BusinessEmailAddress     *string                                      `json:"business_email_address,omitzero"`
	SupportEmailAddress      *string                                      `json:"support_email_address,omitzero"`
	BusinessWebsiteURL       *string                                      `json:"business_website_url,omitzero"`
	BusinessCountryCode      *string                                      `json:"business_country_code,omitzero"`
	BusinessCity             *string                                      `json:"business_city,omitzero"`
	BusinessRegion           *string                                      `json:"business_region,omitzero"`
	BusinessStreetAddress1   *string                                      `json:"business_street_address_1,omitzero"`
	BusinessStreetAddress2   *string                                      `json:"business_street_address_2,omitzero"`
	BusinessPostalCode       *string                                      `json:"business_postal_code,omitzero"`
	BusinessIndustry         *string                                      `json:"business_industry,omitzero"`
	BusinessTaxIDType        *string                                      `json:"business_tax_id_type,omitzero"`
	BusinessTaxIDNumber      *string                                      `json:"business_tax_id_number,omitzero"`
	BusinessTaxCountryCode   *string                                      `json:"business_tax_country_code,omitzero"`
	BusinessStockTicker      *string                                      `json:"business_stock_ticker,omitzero"`
	BusinessStockExchange    *string                                      `json:"business_stock_exchange,omitzero"`
	BusinessSocialMediaURLs  []string                                     `json:"business_social_media_urls,omitzero"`
	BusinessOperationRegions []string                                     `json:"business_operation_regions,omitzero"`
	BusinessRepresentative   *CreateSmsBrandRequestBusinessRepresentative `json:"business_representative,omitzero"`
	SkipSecondaryVetting     *bool                                        `json:"skip_secondary_vetting,omitzero"`
}

type CreateSmsBrandResponse = ListSmsBrandsItem

type ListSmsBrandsCountQuery = ListSmsBrandsQuery

type ListSmsBrandsCountResponse = ListChannelAnalyticsCountResponse

type ReadSmsBrandResponse = ListSmsBrandsItem

type UpdateSmsBrandRequest struct {
	DisplayName string `json:"display_name"`
}

type UpdateSmsBrandResponse = ListSmsBrandsItem

type DeleteSmsBrandResponse = ListSmsBrandsItem
