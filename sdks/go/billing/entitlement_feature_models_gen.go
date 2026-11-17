package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListEntitlementFeaturesQuery struct {
	Type        *string                                       `json:"type,omitzero"`
	Key         any                                           `json:"key,omitzero"`
	IsActive    any                                           `json:"is_active,omitzero"`
	DateCreated *ListChargesQueryDateCreated                  `json:"date_created,omitzero"`
	DateDeleted conjoin.Nullable[ListChargesQueryDateCreated] `json:"date_deleted,omitzero"`
	Cursor      *ListChargesQueryCursor                       `json:"cursor,omitzero"`
	Sort        map[string]string                             `json:"sort,omitzero"`
	Limit       any                                           `json:"limit,omitzero"`
}

type ListEntitlementFeaturesItemMeteringConfig struct {
	Consumable    bool   `json:"consumable"`
	ResetInterval string `json:"reset_interval"`
	Aggregation   string `json:"aggregation"`
}

type ListEntitlementFeaturesItemCreditConfig struct {
	WalletCurrency string  `json:"wallet_currency"`
	WalletLabel    *string `json:"wallet_label,omitzero"`
}

type ListEntitlementFeaturesItem struct {
	FeatureID        string                                                      `json:"feature_id"`
	ConjoinAccountID string                                                      `json:"conjoin_account_id"`
	ConjoinProjectID string                                                      `json:"conjoin_project_id"`
	Name             string                                                      `json:"name"`
	Key              string                                                      `json:"key"`
	Description      conjoin.Nullable[string]                                    `json:"description,omitzero"`
	Type             string                                                      `json:"type"`
	MeteringConfig   conjoin.Nullable[ListEntitlementFeaturesItemMeteringConfig] `json:"metering_config,omitzero"`
	CreditConfig     conjoin.Nullable[ListEntitlementFeaturesItemCreditConfig]   `json:"credit_config,omitzero"`
	IsActive         bool                                                        `json:"is_active"`
	LiveMode         bool                                                        `json:"live_mode"`
	DateCreated      string                                                      `json:"date_created"`
	DateUpdated      string                                                      `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]                                    `json:"date_deleted,omitzero"`
}

type CreateEntitlementFeatureRequest struct {
	Key            string                                     `json:"key"`
	Name           string                                     `json:"name"`
	Description    *string                                    `json:"description,omitzero"`
	Type           string                                     `json:"type"`
	MeteringConfig *ListEntitlementFeaturesItemMeteringConfig `json:"metering_config,omitzero"`
	CreditConfig   *ListEntitlementFeaturesItemCreditConfig   `json:"credit_config,omitzero"`
}

type CreateEntitlementFeatureResponse = ListEntitlementFeaturesItem

type ListEntitlementFeaturesCountQuery = ListEntitlementFeaturesQuery

type ListEntitlementFeaturesCountResponse = ListChargesCountResponse

type ReadEntitlementFeatureResponse = ListEntitlementFeaturesItem

type UpdateEntitlementFeatureRequest struct {
	Name           *string                                    `json:"name,omitzero"`
	Description    *string                                    `json:"description,omitzero"`
	Type           *string                                    `json:"type,omitzero"`
	MeteringConfig *ListEntitlementFeaturesItemMeteringConfig `json:"metering_config,omitzero"`
	CreditConfig   *ListEntitlementFeaturesItemCreditConfig   `json:"credit_config,omitzero"`
}

type UpdateEntitlementFeatureResponse = ListEntitlementFeaturesItem

type ArchiveEntitlementFeatureResponse = ListEntitlementFeaturesItem
