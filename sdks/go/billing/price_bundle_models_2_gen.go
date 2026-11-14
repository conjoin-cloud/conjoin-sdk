package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreatePriceBundleRequestItemsItem struct {
	PriceID            *string                                       `json:"price_id,omitzero"`
	PriceKey           *string                                       `json:"price_key,omitzero"`
	DefaultQuantity    int64                                         `json:"default_quantity"`
	QuantityAdjustable *bool                                         `json:"quantity_adjustable,omitzero"`
	BillingMode        *string                                       `json:"billing_mode,omitzero"`
	Required           *bool                                         `json:"required,omitzero"`
	Entitlement        *CreatePriceBundleRequestItemsItemEntitlement `json:"entitlement,omitzero"`
}

type CreatePriceBundleRequestManagedCatalogProduct struct {
	ProductID           *string                                                 `json:"product_id,omitzero"`
	ReferenceID         *string                                                 `json:"reference_id,omitzero"`
	Name                string                                                  `json:"name"`
	Description         *string                                                 `json:"description,omitzero"`
	StatementDescriptor *string                                                 `json:"statement_descriptor,omitzero"`
	UnitLabel           string                                                  `json:"unit_label"`
	IsActive            *bool                                                   `json:"is_active,omitzero"`
	Images              []string                                                `json:"images,omitzero"`
	Features            []ListPriceBundlesItemManagedCatalogProductFeaturesItem `json:"features,omitzero"`
}

type CreatePriceBundleRequestManagedCatalogPricesItemTiersItem struct {
	FlatAmount int64  `json:"flat_amount"`
	UnitAmount int64  `json:"unit_amount"`
	UpTo       *int64 `json:"up_to,omitzero"`
}

type CreatePriceBundleRequestManagedCatalogPricesItemRecurring struct {
	Interval           string                   `json:"interval"`
	IntervalCount      *int64                   `json:"interval_count,omitzero"`
	UsageType          *string                  `json:"usage_type,omitzero"`
	UsageSeatsIncluded *int64                   `json:"usage_seats_included,omitzero"`
	AggregateUsage     conjoin.Nullable[string] `json:"aggregate_usage,omitzero"`
}

type CreatePriceBundleRequestManagedCatalogPricesItem struct {
	PriceKey      string                                                      `json:"price_key"`
	PriceID       *string                                                     `json:"price_id,omitzero"`
	ReferenceID   *string                                                     `json:"reference_id,omitzero"`
	Currency      string                                                      `json:"currency"`
	Amount        int64                                                       `json:"amount"`
	Type          string                                                      `json:"type"`
	BillingScheme string                                                      `json:"billing_scheme"`
	Tiers         []CreatePriceBundleRequestManagedCatalogPricesItemTiersItem `json:"tiers,omitzero"`
	TiersMode     *string                                                     `json:"tiers_mode,omitzero"`
	Recurring     *CreatePriceBundleRequestManagedCatalogPricesItemRecurring  `json:"recurring,omitzero"`
	IsActive      *bool                                                       `json:"is_active,omitzero"`
	TaxBehavior   *string                                                     `json:"tax_behavior,omitzero"`
}

type CreatePriceBundleRequestManagedCatalogEntitlementFeaturesItem struct {
	FeatureKey     string                                     `json:"feature_key"`
	FeatureID      *string                                    `json:"feature_id,omitzero"`
	Name           string                                     `json:"name"`
	Description    *string                                    `json:"description,omitzero"`
	Type           string                                     `json:"type"`
	MeteringConfig *ListEntitlementFeaturesItemMeteringConfig `json:"metering_config,omitzero"`
	CreditConfig   *ListEntitlementFeaturesItemCreditConfig   `json:"credit_config,omitzero"`
}

type CreatePriceBundleRequestManagedCatalog struct {
	Product             CreatePriceBundleRequestManagedCatalogProduct                   `json:"product"`
	Prices              []CreatePriceBundleRequestManagedCatalogPricesItem              `json:"prices"`
	EntitlementFeatures []CreatePriceBundleRequestManagedCatalogEntitlementFeaturesItem `json:"entitlement_features,omitzero"`
}

type CreatePriceBundleRequest struct {
	ReferenceID         *string                                 `json:"reference_id,omitzero"`
	Name                string                                  `json:"name"`
	Description         *string                                 `json:"description,omitzero"`
	AuthoringMode       *string                                 `json:"authoring_mode,omitzero"`
	Items               []CreatePriceBundleRequestItemsItem     `json:"items"`
	ManagedCatalog      *CreatePriceBundleRequestManagedCatalog `json:"managed_catalog,omitzero"`
	DiscountCouponID    *string                                 `json:"discount_coupon_id,omitzero"`
	AutoActivate        *bool                                   `json:"auto_activate,omitzero"`
	TierGroup           conjoin.Nullable[string]                `json:"tier_group,omitzero"`
	TierRank            conjoin.Nullable[int64]                 `json:"tier_rank,omitzero"`
	IsDefaultTier       *bool                                   `json:"is_default_tier,omitzero"`
	RequiredTierGroup   conjoin.Nullable[string]                `json:"required_tier_group,omitzero"`
	MinTierRank         conjoin.Nullable[int64]                 `json:"min_tier_rank,omitzero"`
	CompatibleBundleIDs conjoin.Nullable[[]string]              `json:"compatible_bundle_ids,omitzero"`
	Status              *string                                 `json:"status,omitzero"`
	Metadata            map[string]any                          `json:"metadata,omitzero"`
}

type CreatePriceBundleResponse = ListPriceBundlesItem

type ListPriceBundlesCountQuery = ListPriceBundlesQuery

type ListPriceBundlesCountResponse = ListChargesCountResponse

type ReadPriceBundleResponse = ListPriceBundlesItem

type UpdatePriceBundleRequest struct {
	Name                *string                                 `json:"name,omitzero"`
	Description         *string                                 `json:"description,omitzero"`
	Items               []CreatePriceBundleRequestItemsItem     `json:"items,omitzero"`
	ManagedCatalog      *CreatePriceBundleRequestManagedCatalog `json:"managed_catalog,omitzero"`
	DiscountCouponID    *string                                 `json:"discount_coupon_id,omitzero"`
	AutoActivate        *bool                                   `json:"auto_activate,omitzero"`
	TierGroup           conjoin.Nullable[string]                `json:"tier_group,omitzero"`
	TierRank            conjoin.Nullable[int64]                 `json:"tier_rank,omitzero"`
	IsDefaultTier       *bool                                   `json:"is_default_tier,omitzero"`
	RequiredTierGroup   conjoin.Nullable[string]                `json:"required_tier_group,omitzero"`
	MinTierRank         conjoin.Nullable[int64]                 `json:"min_tier_rank,omitzero"`
	CompatibleBundleIDs conjoin.Nullable[[]string]              `json:"compatible_bundle_ids,omitzero"`
	Status              *string                                 `json:"status,omitzero"`
	Metadata            map[string]any                          `json:"metadata,omitzero"`
}

type UpdatePriceBundleResponse = ListPriceBundlesItem

type ArchivePriceBundleResponse = ListPriceBundlesItem

type RestorePriceBundleResponse = ListPriceBundlesItem

type PublishPriceBundleResponse = ListPriceBundlesItem
