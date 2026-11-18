package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSelfPaymentMethodsQueryDateCreated struct {
	Equals    *string `json:"equals,omitzero"`
	NotEquals *string `json:"not_equals,omitzero"`
	Gt        *string `json:"gt,omitzero"`
	Lt        *string `json:"lt,omitzero"`
	Gte       *string `json:"gte,omitzero"`
	Lte       *string `json:"lte,omitzero"`
}

type ListSelfPaymentMethodsQueryCursor struct {
	Prev *string `json:"prev,omitzero"`
	Next *string `json:"next,omitzero"`
}

type ListSelfPaymentMethodsQuery struct {
	IsActive    any                                     `json:"is_active,omitzero"`
	IsDefault   any                                     `json:"is_default,omitzero"`
	DateCreated *ListSelfPaymentMethodsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListSelfPaymentMethodsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                       `json:"sort,omitzero"`
	Limit       any                                     `json:"limit,omitzero"`
}

type ListSelfPaymentMethodsItem struct {
	EntityID          string                    `json:"entity_id"`
	PaymentMethodID   string                    `json:"payment_method_id"`
	ReferenceID       string                    `json:"reference_id"`
	CustomerID        string                    `json:"customer_id"`
	Name              conjoin.Nullable[string]  `json:"name,omitzero"`
	Type              conjoin.Nullable[string]  `json:"type,omitzero"`
	Brand             conjoin.Nullable[string]  `json:"brand,omitzero"`
	CountryOfIssuance conjoin.Nullable[string]  `json:"country_of_issuance,omitzero"`
	Last4             conjoin.Nullable[string]  `json:"last4,omitzero"`
	ExpMonth          conjoin.Nullable[float64] `json:"exp_month,omitzero"`
	ExpYear           conjoin.Nullable[float64] `json:"exp_year,omitzero"`
	IsDefault         bool                      `json:"is_default"`
	IsActive          bool                      `json:"is_active"`
	DateCreated       string                    `json:"date_created"`
	DateUpdated       string                    `json:"date_updated"`
	DateDeleted       conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type CreateSelfPaymentMethodRequest struct {
	Name      *string `json:"name,omitzero"`
	IsDefault *bool   `json:"is_default,omitzero"`
}

type CreateSelfPaymentMethodResponse struct {
	PaymentMethodID  string `json:"payment_method_id"`
	AuthorisationURL string `json:"authorisation_url"`
}

type ListSelfPaymentMethodsCountQuery = ListSelfPaymentMethodsQuery

type ListSelfPaymentMethodsCountResponse struct {
	Count int64 `json:"count"`
}

type ListSelfEntitlementOverridesQuery struct {
	FeatureID      *string                                 `json:"feature_id,omitzero"`
	SubscriptionID *string                                 `json:"subscription_id,omitzero"`
	IsActive       any                                     `json:"is_active,omitzero"`
	DateCreated    *ListSelfPaymentMethodsQueryDateCreated `json:"date_created,omitzero"`
	Cursor         *ListSelfPaymentMethodsQueryCursor      `json:"cursor,omitzero"`
	Sort           map[string]string                       `json:"sort,omitzero"`
	Limit          any                                     `json:"limit,omitzero"`
}

type ListSelfEntitlementOverridesItem struct {
	OverrideID       string                    `json:"override_id"`
	ConjoinAccountID string                    `json:"conjoin_account_id"`
	ConjoinProjectID string                    `json:"conjoin_project_id"`
	EntityID         string                    `json:"entity_id"`
	CustomerID       string                    `json:"customer_id"`
	SubscriptionID   string                    `json:"subscription_id"`
	PlanID           string                    `json:"plan_id"`
	FeatureID        string                    `json:"feature_id"`
	ValueType        string                    `json:"value_type"`
	IncludedUnits    conjoin.Nullable[float64] `json:"included_units,omitzero"`
	SoftLimit        conjoin.Nullable[bool]    `json:"soft_limit,omitzero"`
	Reason           conjoin.Nullable[string]  `json:"reason,omitzero"`
	EffectiveFrom    string                    `json:"effective_from"`
	EffectiveTo      conjoin.Nullable[string]  `json:"effective_to,omitzero"`
	IsActive         bool                      `json:"is_active"`
	LiveMode         bool                      `json:"live_mode"`
	DateCreated      string                    `json:"date_created"`
	DateUpdated      string                    `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]  `json:"date_deleted,omitzero"`
}

type ListSelfPriceBundlesQuery struct {
	ReferenceID *string                                 `json:"reference_id,omitzero"`
	DateCreated *ListSelfPaymentMethodsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ListSelfPaymentMethodsQueryCursor      `json:"cursor,omitzero"`
	Sort        map[string]string                       `json:"sort,omitzero"`
	Limit       any                                     `json:"limit,omitzero"`
}

type ListSelfPriceBundlesItemItemsItemEntitlement struct {
	FeatureID       *string  `json:"feature_id,omitzero"`
	FeatureKey      *string  `json:"feature_key,omitzero"`
	ValueType       string   `json:"value_type"`
	IncludedUnits   *float64 `json:"included_units,omitzero"`
	SoftLimit       *bool    `json:"soft_limit,omitzero"`
	OveragePriceID  *string  `json:"overage_price_id,omitzero"`
	OveragePriceKey *string  `json:"overage_price_key,omitzero"`
}

type ListSelfPriceBundlesItemItemsItem struct {
	PriceID            *string                                                        `json:"price_id,omitzero"`
	PriceKey           *string                                                        `json:"price_key,omitzero"`
	DefaultQuantity    float64                                                        `json:"default_quantity"`
	QuantityAdjustable bool                                                           `json:"quantity_adjustable"`
	BillingMode        *string                                                        `json:"billing_mode,omitzero"`
	Required           bool                                                           `json:"required"`
	Entitlement        conjoin.Nullable[ListSelfPriceBundlesItemItemsItemEntitlement] `json:"entitlement,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalogProductFeaturesItem struct {
	Name        string  `json:"name"`
	Description *string `json:"description,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalogProduct struct {
	ProductID           *string                                                     `json:"product_id,omitzero"`
	ReferenceID         *string                                                     `json:"reference_id,omitzero"`
	Name                string                                                      `json:"name"`
	Description         conjoin.Nullable[string]                                    `json:"description,omitzero"`
	StatementDescriptor conjoin.Nullable[string]                                    `json:"statement_descriptor,omitzero"`
	UnitLabel           string                                                      `json:"unit_label"`
	IsActive            *bool                                                       `json:"is_active,omitzero"`
	Images              []string                                                    `json:"images,omitzero"`
	Features            []ListSelfPriceBundlesItemManagedCatalogProductFeaturesItem `json:"features,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalogPricesItemTiersItem struct {
	FlatAmount float64                   `json:"flat_amount"`
	UnitAmount float64                   `json:"unit_amount"`
	UpTo       conjoin.Nullable[float64] `json:"up_to,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalogPricesItemRecurring struct {
	Interval           string                   `json:"interval"`
	IntervalCount      *float64                 `json:"interval_count,omitzero"`
	UsageType          *string                  `json:"usage_type,omitzero"`
	UsageSeatsIncluded *float64                 `json:"usage_seats_included,omitzero"`
	AggregateUsage     conjoin.Nullable[string] `json:"aggregate_usage,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalogPricesItem struct {
	PriceKey      string                                                      `json:"price_key"`
	PriceID       *string                                                     `json:"price_id,omitzero"`
	ReferenceID   *string                                                     `json:"reference_id,omitzero"`
	Currency      string                                                      `json:"currency"`
	Amount        float64                                                     `json:"amount"`
	Type          string                                                      `json:"type"`
	BillingScheme string                                                      `json:"billing_scheme"`
	Tiers         []ListSelfPriceBundlesItemManagedCatalogPricesItemTiersItem `json:"tiers,omitzero"`
	TiersMode     *string                                                     `json:"tiers_mode,omitzero"`
	Recurring     *ListSelfPriceBundlesItemManagedCatalogPricesItemRecurring  `json:"recurring,omitzero"`
	IsActive      *bool                                                       `json:"is_active,omitzero"`
	TaxBehavior   *string                                                     `json:"tax_behavior,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalogEntitlementFeaturesItemMeteringConfig struct {
	Consumable    bool   `json:"consumable"`
	ResetInterval string `json:"reset_interval"`
	Aggregation   string `json:"aggregation"`
}

type ListSelfPriceBundlesItemManagedCatalogEntitlementFeaturesItemCreditConfig struct {
	WalletCurrency string  `json:"wallet_currency"`
	WalletLabel    *string `json:"wallet_label,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalogEntitlementFeaturesItem struct {
	FeatureKey     string                                                                                        `json:"feature_key"`
	FeatureID      *string                                                                                       `json:"feature_id,omitzero"`
	Name           string                                                                                        `json:"name"`
	Description    conjoin.Nullable[string]                                                                      `json:"description,omitzero"`
	Type           string                                                                                        `json:"type"`
	MeteringConfig conjoin.Nullable[ListSelfPriceBundlesItemManagedCatalogEntitlementFeaturesItemMeteringConfig] `json:"metering_config,omitzero"`
	CreditConfig   conjoin.Nullable[ListSelfPriceBundlesItemManagedCatalogEntitlementFeaturesItemCreditConfig]   `json:"credit_config,omitzero"`
}

type ListSelfPriceBundlesItemManagedCatalog struct {
	Product             ListSelfPriceBundlesItemManagedCatalogProduct                   `json:"product"`
	Prices              []ListSelfPriceBundlesItemManagedCatalogPricesItem              `json:"prices"`
	EntitlementFeatures []ListSelfPriceBundlesItemManagedCatalogEntitlementFeaturesItem `json:"entitlement_features,omitzero"`
}

type ListSelfPriceBundlesItem struct {
	ConjoinAccountID    string                                                   `json:"conjoin_account_id"`
	ConjoinProjectID    string                                                   `json:"conjoin_project_id"`
	EntityID            string                                                   `json:"entity_id"`
	PriceBundleID       string                                                   `json:"price_bundle_id"`
	ReferenceID         string                                                   `json:"reference_id"`
	Name                string                                                   `json:"name"`
	Description         conjoin.Nullable[string]                                 `json:"description,omitzero"`
	AuthoringMode       string                                                   `json:"authoring_mode"`
	Items               []ListSelfPriceBundlesItemItemsItem                      `json:"items"`
	ManagedCatalog      conjoin.Nullable[ListSelfPriceBundlesItemManagedCatalog] `json:"managed_catalog,omitzero"`
	DiscountCouponID    conjoin.Nullable[string]                                 `json:"discount_coupon_id,omitzero"`
	AutoActivate        bool                                                     `json:"auto_activate"`
	TierGroup           conjoin.Nullable[string]                                 `json:"tier_group,omitzero"`
	TierRank            conjoin.Nullable[float64]                                `json:"tier_rank,omitzero"`
	IsDefaultTier       bool                                                     `json:"is_default_tier"`
	RequiredTierGroup   conjoin.Nullable[string]                                 `json:"required_tier_group,omitzero"`
	MinTierRank         conjoin.Nullable[float64]                                `json:"min_tier_rank,omitzero"`
	CompatibleBundleIDs conjoin.Nullable[[]string]                               `json:"compatible_bundle_ids,omitzero"`
	Status              string                                                   `json:"status"`
	LiveMode            bool                                                     `json:"live_mode"`
	DateCreated         string                                                   `json:"date_created"`
	DateUpdated         string                                                   `json:"date_updated"`
	DateDeleted         conjoin.Nullable[string]                                 `json:"date_deleted,omitzero"`
}

type ListSelfEntitlementOverridesCountQuery = ListSelfEntitlementOverridesQuery

type ListSelfEntitlementOverridesCountResponse = ListSelfPaymentMethodsCountResponse

type ListSelfPriceBundlesCountQuery = ListSelfPriceBundlesQuery

type ListSelfPriceBundlesCountResponse = ListSelfPaymentMethodsCountResponse

type ActivateSelfPriceBundlesRequestBundlesItem struct {
	BundleReference string `json:"bundle_reference"`
}

type ActivateSelfPriceBundlesRequest struct {
	PaymentMethodID string                                       `json:"payment_method_id"`
	Bundles         []ActivateSelfPriceBundlesRequestBundlesItem `json:"bundles"`
}

type ActivateSelfPriceBundlesResponseActivationsItemResolvedItemsItemEntitlement struct {
	FeatureID     string   `json:"feature_id"`
	ValueType     string   `json:"value_type"`
	IncludedUnits *float64 `json:"included_units,omitzero"`
}

type ActivateSelfPriceBundlesResponseActivationsItemResolvedItemsItem struct {
	PriceID     string                                                                                        `json:"price_id"`
	Quantity    float64                                                                                       `json:"quantity"`
	BillingMode *string                                                                                       `json:"billing_mode,omitzero"`
	Entitlement conjoin.Nullable[ActivateSelfPriceBundlesResponseActivationsItemResolvedItemsItemEntitlement] `json:"entitlement,omitzero"`
}

type ActivateSelfPriceBundlesResponseActivationsItem struct {
	ConjoinAccountID     string                                                             `json:"conjoin_account_id"`
	ConjoinProjectID     string                                                             `json:"conjoin_project_id"`
	EntityID             string                                                             `json:"entity_id"`
	ActivationID         string                                                             `json:"activation_id"`
	PriceBundleID        string                                                             `json:"price_bundle_id"`
	CustomerID           string                                                             `json:"customer_id"`
	SubscriptionID       conjoin.Nullable[string]                                           `json:"subscription_id,omitzero"`
	InvoiceID            conjoin.Nullable[string]                                           `json:"invoice_id,omitzero"`
	ResolvedItems        []ActivateSelfPriceBundlesResponseActivationsItemResolvedItemsItem `json:"resolved_items"`
	UpgradeStrategy      conjoin.Nullable[string]                                           `json:"upgrade_strategy,omitzero"`
	PreviousActivationID conjoin.Nullable[string]                                           `json:"previous_activation_id,omitzero"`
	TierGroup            conjoin.Nullable[string]                                           `json:"tier_group,omitzero"`
	TierRank             conjoin.Nullable[float64]                                          `json:"tier_rank,omitzero"`
	Status               string                                                             `json:"status"`
	FailureReason        conjoin.Nullable[string]                                           `json:"failure_reason,omitzero"`
	BatchID              conjoin.Nullable[string]                                           `json:"batch_id,omitzero"`
	LiveMode             bool                                                               `json:"live_mode"`
	DateCreated          string                                                             `json:"date_created"`
	DateUpdated          string                                                             `json:"date_updated"`
	DateDeleted          conjoin.Nullable[string]                                           `json:"date_deleted,omitzero"`
}

type ActivateSelfPriceBundlesResponse struct {
	BatchID     string                                            `json:"batch_id"`
	Activations []ActivateSelfPriceBundlesResponseActivationsItem `json:"activations"`
}

type DeactivateSelfPriceBundleRequest struct {
	Reason *string `json:"reason,omitzero"`
}

type DeactivateSelfPriceBundleResponse = ActivateSelfPriceBundlesResponseActivationsItem
