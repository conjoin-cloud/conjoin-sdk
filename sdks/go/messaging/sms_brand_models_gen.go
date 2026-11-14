package messaging

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateSmsBrandRequestBusinessRepresentative struct {
	BusinessTitle string `json:"business_title"`
	JobPosition   string `json:"job_position"`
	FirstName     string `json:"first_name"`
	LastName      string `json:"last_name"`
	EmailAddress  string `json:"email_address"`
	PhoneNumber   string `json:"phone_number"`
}

type CreateSmsBrandRequest struct {
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

type CreateSmsBrandResponse struct {
	BrandID               string                   `json:"brand_id"`
	ProfileID             string                   `json:"profile_id"`
	ConjoinAccountID      string                   `json:"conjoin_account_id"`
	ConjoinProjectID      string                   `json:"conjoin_project_id"`
	LiveMode              bool                     `json:"live_mode"`
	ReferenceID           conjoin.Nullable[string] `json:"reference_id,omitzero"`
	DisplayName           string                   `json:"display_name"`
	BrandRegistrationType string                   `json:"brand_registration_type"`
	BrandTcrID            *string                  `json:"brand_tcr_id,omitzero"`
	SoleProprietorDetails map[string]any           `json:"sole_proprietor_details,omitzero"`
	BusinessDetails       map[string]any           `json:"business_details,omitzero"`
	Status                *string                  `json:"status,omitzero"`
	DateCreated           string                   `json:"date_created"`
	DateUpdated           string                   `json:"date_updated"`
	DateDeleted           conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type ReadSmsBrandResponse = CreateSmsBrandResponse

type UpdateSmsBrandRequestUpdatesCompanyDetails struct {
	LegalName           *string `json:"legal_name,omitzero"`
	BrandName           *string `json:"brand_name,omitzero"`
	CompanyEmail        *string `json:"company_email,omitzero"`
	SupportContactEmail *string `json:"support_contact_email,omitzero"`
	Website             *string `json:"website,omitzero"`
	Country             *string `json:"country,omitzero"`
	StateOrProvince     *string `json:"state_or_province,omitzero"`
	StreetAddress       *string `json:"street_address,omitzero"`
	PostalCode          *string `json:"postal_code,omitzero"`
	BusinessType        *string `json:"business_type,omitzero"`
	BusinessVertical    *string `json:"business_vertical,omitzero"`
}

type UpdateSmsBrandRequestUpdatesFinancialDetails struct {
	TaxID         *string `json:"tax_id,omitzero"`
	TaxIDCountry  *string `json:"tax_id_country,omitzero"`
	StockSymbol   *string `json:"stock_symbol,omitzero"`
	StockExchange *string `json:"stock_exchange,omitzero"`
}

type UpdateSmsBrandRequestUpdatesPrimaryContactDetails struct {
	FirstName   *string `json:"first_name,omitzero"`
	LastName    *string `json:"last_name,omitzero"`
	Email       *string `json:"email,omitzero"`
	PhoneNumber *string `json:"phone_number,omitzero"`
}

type UpdateSmsBrandRequestUpdates struct {
	DisplayName           *string                                            `json:"display_name,omitzero"`
	CompanyDetails        *UpdateSmsBrandRequestUpdatesCompanyDetails        `json:"company_details,omitzero"`
	FinancialDetails      *UpdateSmsBrandRequestUpdatesFinancialDetails      `json:"financial_details,omitzero"`
	PrimaryContactDetails *UpdateSmsBrandRequestUpdatesPrimaryContactDetails `json:"primary_contact_details,omitzero"`
}

type UpdateSmsBrandRequest struct {
	Updates UpdateSmsBrandRequestUpdates `json:"updates"`
}

type UpdateSmsBrandResponse = CreateSmsBrandResponse

type DeleteSmsBrandResponse = CreateSmsBrandResponse

type ListSmsBrandsRequestQuery struct {
	DateCreated ListContactsRequestQueryDateCreated `json:"date_created"`
	DateUpdated ListContactsRequestQueryDateCreated `json:"date_updated"`
	DateDeleted ListContactsRequestQueryDateCreated `json:"date_deleted"`
}

type ListSmsBrandsRequest struct {
	Filter map[string]bool           `json:"filter,omitzero"`
	Query  ListSmsBrandsRequestQuery `json:"query"`
	Sort   map[string]string         `json:"sort"`
	Limit  any                       `json:"limit,omitzero"`
}

type ListSmsBrandsItem = CreateSmsBrandResponse
