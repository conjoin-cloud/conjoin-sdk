package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPricesQuery struct {
	ReferenceID *string                                       `json:"reference_id,omitzero"`
	ProductID   *string                                       `json:"product_id,omitzero"`
	Currency    *string                                       `json:"currency,omitzero"`
	Type        *string                                       `json:"type,omitzero"`
	IsActive    any                                           `json:"is_active,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateUpdated *ListChargesQueryDateCreated                  `json:"date_updated,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListPricesItemRecurring struct {
	Interval       string                   `json:"interval"`
	IntervalCount  float64                  `json:"interval_count"`
	UsageType      *string                  `json:"usage_type,omitzero"`
	AggregateUsage conjoin.Nullable[string] `json:"aggregate_usage,omitzero"`
}

type ListPricesItem struct {
	ConjoinAccountID string                                                  `json:"conjoin_account_id"`
	ConjoinProjectID string                                                  `json:"conjoin_project_id"`
	EntityID         string                                                  `json:"entity_id"`
	PriceID          string                                                  `json:"price_id"`
	ReferenceID      string                                                  `json:"reference_id"`
	ProductID        string                                                  `json:"product_id"`
	Currency         string                                                  `json:"currency"`
	CurrencyOptions  conjoin.Nullable[map[string]any]                        `json:"currency_options,omitzero"`
	Amount           float64                                                 `json:"amount"`
	Type             string                                                  `json:"type"`
	BillingScheme    string                                                  `json:"billing_scheme"`
	Tiers            []ListPriceBundlesItemManagedCatalogPricesItemTiersItem `json:"tiers,omitzero"`
	TiersMode        *string                                                 `json:"tiers_mode,omitzero"`
	Recurring        *ListPricesItemRecurring                                `json:"recurring,omitzero"`
	IsActive         bool                                                    `json:"is_active"`
	TaxBehavior      *string                                                 `json:"tax_behavior,omitzero"`
	BillingMetadata  map[string]any                                          `json:"billing_metadata,omitzero"`
	DateCreated      string                                                  `json:"date_created"`
	DateUpdated      string                                                  `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]                                `json:"date_deleted,omitzero"`
	LiveMode         bool                                                    `json:"live_mode"`
}

type CreatePriceRequestCurrencyOptionsValue struct {
	Amount      int64  `json:"amount"`
	TaxBehavior string `json:"tax_behavior"`
}

type CreatePriceRequest struct {
	ProductID       string                                                      `json:"product_id"`
	ReferenceID     *string                                                     `json:"reference_id,omitzero"`
	Currency        string                                                      `json:"currency"`
	CurrencyOptions map[string]CreatePriceRequestCurrencyOptionsValue           `json:"currency_options,omitzero"`
	Amount          int64                                                       `json:"amount"`
	Type            string                                                      `json:"type"`
	BillingScheme   string                                                      `json:"billing_scheme"`
	Tiers           []CreatePriceBundleRequestManagedCatalogPricesItemTiersItem `json:"tiers,omitzero"`
	TiersMode       *string                                                     `json:"tiers_mode,omitzero"`
	Recurring       *CreatePriceBundleRequestManagedCatalogPricesItemRecurring  `json:"recurring,omitzero"`
	IsActive        *bool                                                       `json:"is_active,omitzero"`
	TaxBehavior     *string                                                     `json:"tax_behavior,omitzero"`
	Metadata        map[string]any                                              `json:"metadata,omitzero"`
}

type CreatePriceResponse = ListPricesItem

type ListPricesCountQuery = ListPricesQuery

type ListPricesCountResponse = ListChargesCountResponse

type ReadPriceResponse = ListPricesItem

type UpdatePriceRequest struct {
	Type          *string                                                     `json:"type,omitzero"`
	BillingScheme *string                                                     `json:"billing_scheme,omitzero"`
	Tiers         []CreatePriceBundleRequestManagedCatalogPricesItemTiersItem `json:"tiers,omitzero"`
	TiersMode     *string                                                     `json:"tiers_mode,omitzero"`
	Recurring     *CreatePriceBundleRequestManagedCatalogPricesItemRecurring  `json:"recurring,omitzero"`
	IsActive      *bool                                                       `json:"is_active,omitzero"`
	TaxBehavior   *string                                                     `json:"tax_behavior,omitzero"`
	Metadata      map[string]any                                              `json:"metadata,omitzero"`
}

type UpdatePriceResponse = ListPricesItem

type DeletePriceResponse = DeleteEntitlementOverrideResponse

type ArchivePriceResponse = ListPricesItem

type RestorePriceResponse = ListPricesItem
