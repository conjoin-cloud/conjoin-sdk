package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListPriceBundleActivationsQuery struct {
	Status        *string                      `json:"status,omitzero"`
	PriceBundleID *string                      `json:"price_bundle_id,omitzero"`
	BatchID       *string                      `json:"batch_id,omitzero"`
	DateCreated   *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	CustomerID    string                       `json:"customer_id"`
	Cursor        *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort          map[string]string            `json:"sort,omitzero"`
	Limit         any                          `json:"limit,omitzero"`
}

type ListPriceBundleActivationsItemResolvedItemsItemEntitlement struct {
	FeatureID     string   `json:"feature_id"`
	ValueType     string   `json:"value_type"`
	IncludedUnits *float64 `json:"included_units,omitzero"`
}

type ListPriceBundleActivationsItemResolvedItemsItem struct {
	PriceID     string                                                                       `json:"price_id"`
	Quantity    float64                                                                      `json:"quantity"`
	BillingMode *string                                                                      `json:"billing_mode,omitzero"`
	Entitlement conjoin.Nullable[ListPriceBundleActivationsItemResolvedItemsItemEntitlement] `json:"entitlement,omitzero"`
}

type ListPriceBundleActivationsItem struct {
	ConjoinAccountID     string                                            `json:"conjoin_account_id"`
	ConjoinProjectID     string                                            `json:"conjoin_project_id"`
	EntityID             string                                            `json:"entity_id"`
	ActivationID         string                                            `json:"activation_id"`
	PriceBundleID        string                                            `json:"price_bundle_id"`
	CustomerID           string                                            `json:"customer_id"`
	SubscriptionID       conjoin.Nullable[string]                          `json:"subscription_id,omitzero"`
	InvoiceID            conjoin.Nullable[string]                          `json:"invoice_id,omitzero"`
	ResolvedItems        []ListPriceBundleActivationsItemResolvedItemsItem `json:"resolved_items"`
	UpgradeStrategy      conjoin.Nullable[string]                          `json:"upgrade_strategy,omitzero"`
	PreviousActivationID conjoin.Nullable[string]                          `json:"previous_activation_id,omitzero"`
	TierGroup            conjoin.Nullable[string]                          `json:"tier_group,omitzero"`
	TierRank             conjoin.Nullable[float64]                         `json:"tier_rank,omitzero"`
	Status               string                                            `json:"status"`
	FailureReason        conjoin.Nullable[string]                          `json:"failure_reason,omitzero"`
	BatchID              conjoin.Nullable[string]                          `json:"batch_id,omitzero"`
	LiveMode             bool                                              `json:"live_mode"`
	DateCreated          string                                            `json:"date_created"`
	DateUpdated          string                                            `json:"date_updated"`
	DateDeleted          conjoin.Nullable[string]                          `json:"date_deleted,omitzero"`
}

type ActivatePriceBundleRequestBundlesItemQuantityOverridesItem struct {
	PriceID  string `json:"price_id"`
	Quantity int64  `json:"quantity"`
}

type ActivatePriceBundleRequestBundlesItem struct {
	BundleReference   string                                                       `json:"bundle_reference"`
	TrialEndDate      *string                                                      `json:"trial_end_date,omitzero"`
	QuantityOverrides []ActivatePriceBundleRequestBundlesItemQuantityOverridesItem `json:"quantity_overrides,omitzero"`
	ExcludedItems     []string                                                     `json:"excluded_items,omitzero"`
	UpgradeStrategy   *string                                                      `json:"upgrade_strategy,omitzero"`
}

type ActivatePriceBundleRequest struct {
	CustomerID                *string                                 `json:"customer_id,omitzero"`
	ReferenceID               *string                                 `json:"reference_id,omitzero"`
	Email                     *string                                 `json:"email,omitzero"`
	Name                      *string                                 `json:"name,omitzero"`
	PaymentMethodID           *string                                 `json:"payment_method_id,omitzero"`
	SubscriptionStrategy      *string                                 `json:"subscription_strategy,omitzero"`
	ProrationBehavior         *string                                 `json:"proration_behavior,omitzero"`
	ApplicationTiming         *string                                 `json:"application_timing,omitzero"`
	PaymentStrategy           *string                                 `json:"payment_strategy,omitzero"`
	TransitionTiming          *string                                 `json:"transition_timing,omitzero"`
	IncompatibleAddonBehavior *string                                 `json:"incompatible_addon_behavior,omitzero"`
	Bundles                   []ActivatePriceBundleRequestBundlesItem `json:"bundles"`
}

type ActivatePriceBundleResponse struct {
	BatchID     string                           `json:"batch_id"`
	Activations []ListPriceBundleActivationsItem `json:"activations"`
}

type ListPriceBundleActivationsCountQuery = ListPriceBundleActivationsQuery

type ListPriceBundleActivationsCountResponse = ListChargesCountResponse

type DeactivatePriceBundleRequest struct {
	Reason                       *string `json:"reason,omitzero"`
	CancellationFallbackBehavior *string `json:"cancellation_fallback_behavior,omitzero"`
}

type DeactivatePriceBundleResponse = ListPriceBundleActivationsItem

type ReadAvailableBundleTransitionsQuery struct {
	CustomerID string `json:"customer_id"`
}

type ReadAvailableBundleTransitionsResponseCurrentTierPricingItemTiersItem struct {
	FlatAmount float64  `json:"flat_amount"`
	UnitAmount float64  `json:"unit_amount"`
	UpTo       *float64 `json:"up_to"`
}

type ReadAvailableBundleTransitionsResponseCurrentTierPricingItemRecurring struct {
	Interval      string  `json:"interval"`
	IntervalCount float64 `json:"interval_count"`
}

type ReadAvailableBundleTransitionsResponseCurrentTierPricingItem struct {
	Kind           *string                                                                 `json:"kind,omitzero"`
	PriceID        *string                                                                 `json:"price_id,omitzero"`
	Currency       *string                                                                 `json:"currency,omitzero"`
	Amount         *float64                                                                `json:"amount,omitzero"`
	BillingScheme  *string                                                                 `json:"billing_scheme,omitzero"`
	Interval       *string                                                                 `json:"interval,omitzero"`
	IntervalCount  *float64                                                                `json:"interval_count,omitzero"`
	TaxBehavior    *string                                                                 `json:"tax_behavior,omitzero"`
	Type           *string                                                                 `json:"type,omitzero"`
	TiersMode      *string                                                                 `json:"tiers_mode,omitzero"`
	Tiers          []ReadAvailableBundleTransitionsResponseCurrentTierPricingItemTiersItem `json:"tiers,omitzero"`
	Recurring      *ReadAvailableBundleTransitionsResponseCurrentTierPricingItemRecurring  `json:"recurring,omitzero"`
	AggregateUsage conjoin.Nullable[string]                                                `json:"aggregate_usage,omitzero"`
}

type ReadAvailableBundleTransitionsResponseCurrentTier struct {
	ActivationID  string                                                         `json:"activation_id"`
	PriceBundleID string                                                         `json:"price_bundle_id"`
	ReferenceID   string                                                         `json:"reference_id"`
	Name          string                                                         `json:"name"`
	Description   *string                                                        `json:"description"`
	TierGroup     string                                                         `json:"tier_group"`
	TierRank      float64                                                        `json:"tier_rank"`
	IsDefaultTier bool                                                           `json:"is_default_tier"`
	Pricing       []ReadAvailableBundleTransitionsResponseCurrentTierPricingItem `json:"pricing"`
}

type ReadAvailableBundleTransitionsResponsePendingTierChange struct {
	Source        *string                   `json:"source,omitzero"`
	ActivationID  *string                   `json:"activation_id,omitzero"`
	PriceBundleID conjoin.Nullable[string]  `json:"price_bundle_id,omitzero"`
	ReferenceID   conjoin.Nullable[string]  `json:"reference_id,omitzero"`
	Name          conjoin.Nullable[string]  `json:"name,omitzero"`
	TierGroup     conjoin.Nullable[string]  `json:"tier_group,omitzero"`
	TierRank      conjoin.Nullable[float64] `json:"tier_rank,omitzero"`
	Status        *string                   `json:"status,omitzero"`
	ScheduleID    *string                   `json:"schedule_id,omitzero"`
	PhaseID       *string                   `json:"phase_id,omitzero"`
	EffectiveAt   *string                   `json:"effective_at,omitzero"`
}

type ReadAvailableBundleTransitionsResponseAvailableUpgradesDataItem struct {
	PriceBundleID string                                                         `json:"price_bundle_id"`
	ReferenceID   string                                                         `json:"reference_id"`
	Name          string                                                         `json:"name"`
	Description   *string                                                        `json:"description"`
	TierGroup     string                                                         `json:"tier_group"`
	TierRank      float64                                                        `json:"tier_rank"`
	IsDefaultTier bool                                                           `json:"is_default_tier"`
	Pricing       []ReadAvailableBundleTransitionsResponseCurrentTierPricingItem `json:"pricing"`
}

type ReadAvailableBundleTransitionsResponseAvailableUpgrades struct {
	Data    []ReadAvailableBundleTransitionsResponseAvailableUpgradesDataItem `json:"data"`
	HasMore bool                                                              `json:"has_more"`
}

type ReadAvailableBundleTransitionsResponseAvailableAddonsDataItem struct {
	PriceBundleID         string                                                         `json:"price_bundle_id"`
	ReferenceID           string                                                         `json:"reference_id"`
	Name                  string                                                         `json:"name"`
	Description           *string                                                        `json:"description"`
	RequiredTierGroup     *string                                                        `json:"required_tier_group"`
	MinTierRank           *float64                                                       `json:"min_tier_rank"`
	CompatibleBundleIDs   []string                                                       `json:"compatible_bundle_ids"`
	IsActivatable         bool                                                           `json:"is_activatable"`
	IncompatibilityReason *string                                                        `json:"incompatibility_reason"`
	Pricing               []ReadAvailableBundleTransitionsResponseCurrentTierPricingItem `json:"pricing"`
}

type ReadAvailableBundleTransitionsResponseAvailableAddons struct {
	Data    []ReadAvailableBundleTransitionsResponseAvailableAddonsDataItem `json:"data"`
	HasMore bool                                                            `json:"has_more"`
}

type ReadAvailableBundleTransitionsResponseActiveAddonsDataItem struct {
	ActivationID        string                                                         `json:"activation_id"`
	PriceBundleID       string                                                         `json:"price_bundle_id"`
	ReferenceID         string                                                         `json:"reference_id"`
	Name                string                                                         `json:"name"`
	Description         *string                                                        `json:"description"`
	RequiredTierGroup   *string                                                        `json:"required_tier_group"`
	MinTierRank         *float64                                                       `json:"min_tier_rank"`
	CompatibleBundleIDs []string                                                       `json:"compatible_bundle_ids"`
	Pricing             []ReadAvailableBundleTransitionsResponseCurrentTierPricingItem `json:"pricing"`
}

type ReadAvailableBundleTransitionsResponseActiveAddons struct {
	Data    []ReadAvailableBundleTransitionsResponseActiveAddonsDataItem `json:"data"`
	HasMore bool                                                         `json:"has_more"`
}

type ReadAvailableBundleTransitionsResponse struct {
	CustomerID          string                                                   `json:"customer_id"`
	EntityID            string                                                   `json:"entity_id"`
	CurrentTier         *ReadAvailableBundleTransitionsResponseCurrentTier       `json:"current_tier"`
	PendingTierChange   *ReadAvailableBundleTransitionsResponsePendingTierChange `json:"pending_tier_change"`
	AvailableUpgrades   ReadAvailableBundleTransitionsResponseAvailableUpgrades  `json:"available_upgrades"`
	AvailableDowngrades ReadAvailableBundleTransitionsResponseAvailableUpgrades  `json:"available_downgrades"`
	AvailableAddons     ReadAvailableBundleTransitionsResponseAvailableAddons    `json:"available_addons"`
	ActiveAddons        ReadAvailableBundleTransitionsResponseActiveAddons       `json:"active_addons"`
}

type ListPriceBundlesQuery struct {
	ReferenceID  *string                                       `json:"reference_id,omitzero"`
	Status       *string                                       `json:"status,omitzero"`
	AutoActivate any                                           `json:"auto_activate,omitzero"`
	DateCreated  *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateDeleted  conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor       *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort         map[string]string                             `json:"sort,omitzero"`
	Limit        any                                           `json:"limit,omitzero"`
}

type ListPriceBundlesItemItemsItemEntitlement struct {
	FeatureID       *string  `json:"feature_id,omitzero"`
	FeatureKey      *string  `json:"feature_key,omitzero"`
	ValueType       string   `json:"value_type"`
	IncludedUnits   *float64 `json:"included_units,omitzero"`
	SoftLimit       *bool    `json:"soft_limit,omitzero"`
	OveragePriceID  *string  `json:"overage_price_id,omitzero"`
	OveragePriceKey *string  `json:"overage_price_key,omitzero"`
}

type ListPriceBundlesItemItemsItem struct {
	PriceID            *string                                                    `json:"price_id,omitzero"`
	PriceKey           *string                                                    `json:"price_key,omitzero"`
	DefaultQuantity    float64                                                    `json:"default_quantity"`
	QuantityAdjustable bool                                                       `json:"quantity_adjustable"`
	BillingMode        *string                                                    `json:"billing_mode,omitzero"`
	Required           bool                                                       `json:"required"`
	Entitlement        conjoin.Nullable[ListPriceBundlesItemItemsItemEntitlement] `json:"entitlement,omitzero"`
}

type ListPriceBundlesItemManagedCatalogProductFeaturesItem struct {
	Name        string  `json:"name"`
	Description *string `json:"description,omitzero"`
}

type ListPriceBundlesItemManagedCatalogProduct struct {
	ProductID           *string                                                 `json:"product_id,omitzero"`
	ReferenceID         *string                                                 `json:"reference_id,omitzero"`
	Name                string                                                  `json:"name"`
	Description         conjoin.Nullable[string]                                `json:"description,omitzero"`
	StatementDescriptor conjoin.Nullable[string]                                `json:"statement_descriptor,omitzero"`
	UnitLabel           string                                                  `json:"unit_label"`
	IsActive            *bool                                                   `json:"is_active,omitzero"`
	Images              []string                                                `json:"images,omitzero"`
	Features            []ListPriceBundlesItemManagedCatalogProductFeaturesItem `json:"features,omitzero"`
}

type ListPriceBundlesItemManagedCatalogPricesItemTiersItem struct {
	FlatAmount float64                   `json:"flat_amount"`
	UnitAmount float64                   `json:"unit_amount"`
	UpTo       conjoin.Nullable[float64] `json:"up_to,omitzero"`
}

type ListPriceBundlesItemManagedCatalogPricesItemRecurring struct {
	Interval           string                   `json:"interval"`
	IntervalCount      *float64                 `json:"interval_count,omitzero"`
	UsageType          *string                  `json:"usage_type,omitzero"`
	UsageSeatsIncluded *float64                 `json:"usage_seats_included,omitzero"`
	AggregateUsage     conjoin.Nullable[string] `json:"aggregate_usage,omitzero"`
}

type ListPriceBundlesItemManagedCatalogPricesItem struct {
	PriceKey      string                                                  `json:"price_key"`
	PriceID       *string                                                 `json:"price_id,omitzero"`
	ReferenceID   *string                                                 `json:"reference_id,omitzero"`
	Currency      string                                                  `json:"currency"`
	Amount        float64                                                 `json:"amount"`
	Type          string                                                  `json:"type"`
	BillingScheme string                                                  `json:"billing_scheme"`
	Tiers         []ListPriceBundlesItemManagedCatalogPricesItemTiersItem `json:"tiers,omitzero"`
	TiersMode     *string                                                 `json:"tiers_mode,omitzero"`
	Recurring     *ListPriceBundlesItemManagedCatalogPricesItemRecurring  `json:"recurring,omitzero"`
	IsActive      *bool                                                   `json:"is_active,omitzero"`
	TaxBehavior   *string                                                 `json:"tax_behavior,omitzero"`
}

type ListPriceBundlesItemManagedCatalogEntitlementFeaturesItem struct {
	FeatureKey     string                                                      `json:"feature_key"`
	FeatureID      *string                                                     `json:"feature_id,omitzero"`
	Name           string                                                      `json:"name"`
	Description    conjoin.Nullable[string]                                    `json:"description,omitzero"`
	Type           string                                                      `json:"type"`
	MeteringConfig conjoin.Nullable[ListEntitlementFeaturesItemMeteringConfig] `json:"metering_config,omitzero"`
	CreditConfig   conjoin.Nullable[ListEntitlementFeaturesItemCreditConfig]   `json:"credit_config,omitzero"`
}

type ListPriceBundlesItemManagedCatalog struct {
	Product             ListPriceBundlesItemManagedCatalogProduct                   `json:"product"`
	Prices              []ListPriceBundlesItemManagedCatalogPricesItem              `json:"prices"`
	EntitlementFeatures []ListPriceBundlesItemManagedCatalogEntitlementFeaturesItem `json:"entitlement_features,omitzero"`
}

type ListPriceBundlesItem struct {
	ConjoinAccountID    string                                               `json:"conjoin_account_id"`
	ConjoinProjectID    string                                               `json:"conjoin_project_id"`
	EntityID            string                                               `json:"entity_id"`
	PriceBundleID       string                                               `json:"price_bundle_id"`
	ReferenceID         string                                               `json:"reference_id"`
	Name                string                                               `json:"name"`
	Description         conjoin.Nullable[string]                             `json:"description,omitzero"`
	AuthoringMode       string                                               `json:"authoring_mode"`
	Items               []ListPriceBundlesItemItemsItem                      `json:"items"`
	ManagedCatalog      conjoin.Nullable[ListPriceBundlesItemManagedCatalog] `json:"managed_catalog,omitzero"`
	DiscountCouponID    conjoin.Nullable[string]                             `json:"discount_coupon_id,omitzero"`
	AutoActivate        bool                                                 `json:"auto_activate"`
	TierGroup           conjoin.Nullable[string]                             `json:"tier_group,omitzero"`
	TierRank            conjoin.Nullable[float64]                            `json:"tier_rank,omitzero"`
	IsDefaultTier       bool                                                 `json:"is_default_tier"`
	RequiredTierGroup   conjoin.Nullable[string]                             `json:"required_tier_group,omitzero"`
	MinTierRank         conjoin.Nullable[float64]                            `json:"min_tier_rank,omitzero"`
	CompatibleBundleIDs conjoin.Nullable[[]string]                           `json:"compatible_bundle_ids,omitzero"`
	Status              string                                               `json:"status"`
	LiveMode            bool                                                 `json:"live_mode"`
	DateCreated         string                                               `json:"date_created"`
	DateUpdated         string                                               `json:"date_updated"`
	DateDeleted         conjoin.Nullable[string]                             `json:"date_deleted,omitzero"`
}

type CreatePriceBundleRequestItemsItemEntitlement struct {
	FeatureID       *string `json:"feature_id,omitzero"`
	FeatureKey      *string `json:"feature_key,omitzero"`
	ValueType       string  `json:"value_type"`
	IncludedUnits   *int64  `json:"included_units,omitzero"`
	SoftLimit       *bool   `json:"soft_limit,omitzero"`
	OveragePriceID  *string `json:"overage_price_id,omitzero"`
	OveragePriceKey *string `json:"overage_price_key,omitzero"`
}
