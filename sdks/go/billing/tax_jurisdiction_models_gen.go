package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListTaxJurisdictionsQuery struct {
	Country     *string                      `json:"country,omitzero"`
	State       *string                      `json:"state,omitzero"`
	IsActive    any                          `json:"is_active,omitzero"`
	TaxType     *string                      `json:"tax_type,omitzero"`
	DateCreated *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string            `json:"sort,omitzero"`
	Limit       any                          `json:"limit,omitzero"`
}

type ListTaxJurisdictionsItemComponentBreakdownItem struct {
	TaxType string  `json:"tax_type"`
	Rate    float64 `json:"rate"`
	Name    string  `json:"name"`
	Order   float64 `json:"order"`
}

type ListTaxJurisdictionsItemExchangeRules struct {
	B2bExempt     bool `json:"b2b_exempt"`
	B2cExempt     bool `json:"b2c_exempt"`
	ReverseCharge bool `json:"reverse_charge"`
}

type ListTaxJurisdictionsItem struct {
	JurisdictionID     string                                           `json:"jurisdiction_id"`
	LiveMode           bool                                             `json:"live_mode"`
	Country            string                                           `json:"country"`
	State              conjoin.Nullable[string]                         `json:"state,omitzero"`
	TaxType            string                                           `json:"tax_type"`
	Rate               float64                                          `json:"rate"`
	ComponentBreakdown []ListTaxJurisdictionsItemComponentBreakdownItem `json:"component_breakdown,omitzero"`
	EffectiveFrom      string                                           `json:"effective_from"`
	EffectiveUntil     conjoin.Nullable[string]                         `json:"effective_until,omitzero"`
	Timezone           string                                           `json:"timezone"`
	ExchangeRules      *ListTaxJurisdictionsItemExchangeRules           `json:"exchange_rules,omitzero"`
	IsActive           bool                                             `json:"is_active"`
	DateCreated        string                                           `json:"date_created"`
	DateUpdated        string                                           `json:"date_updated"`
	DateDeleted        conjoin.Nullable[string]                         `json:"date_deleted,omitzero"`
}

type ListTaxJurisdictionsCountQuery = ListTaxJurisdictionsQuery

type ListTaxJurisdictionsCountResponse = ListChargesCountResponse

type QueryTaxRateQuery struct {
	Country string  `json:"country"`
	State   *string `json:"state,omitzero"`
	Date    *string `json:"date,omitzero"`
}

type QueryTaxRateResponseComponentBreakdownItem struct {
	TaxType string  `json:"tax_type"`
	Rate    float64 `json:"rate"`
	Name    string  `json:"name"`
}

type QueryTaxRateResponse struct {
	Country            string                                       `json:"country"`
	State              conjoin.Nullable[string]                     `json:"state,omitzero"`
	TaxType            string                                       `json:"tax_type"`
	Rate               float64                                      `json:"rate"`
	ComponentBreakdown []QueryTaxRateResponseComponentBreakdownItem `json:"component_breakdown,omitzero"`
}
