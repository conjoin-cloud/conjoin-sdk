package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListEntitlementOverridesQuery struct {
	OverrideID     *string                      `json:"override_id,omitzero"`
	CustomerID     *string                      `json:"customer_id,omitzero"`
	SubscriptionID *string                      `json:"subscription_id,omitzero"`
	PlanID         *string                      `json:"plan_id,omitzero"`
	FeatureID      *string                      `json:"feature_id,omitzero"`
	IsActive       any                          `json:"is_active,omitzero"`
	DateCreated    *ListChargesQueryDateCreated `json:"date_created,omitzero"`
	Cursor         *ListChargesQueryCursor      `json:"cursor,omitzero"`
	Sort           map[string]string            `json:"sort,omitzero"`
	Limit          any                          `json:"limit,omitzero"`
}

type ListEntitlementOverridesItem struct {
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

type CreateEntitlementOverrideRequest struct {
	CustomerID     string                   `json:"customer_id"`
	SubscriptionID string                   `json:"subscription_id"`
	PlanID         string                   `json:"plan_id"`
	FeatureID      string                   `json:"feature_id"`
	ValueType      string                   `json:"value_type"`
	IncludedUnits  *int64                   `json:"included_units,omitzero"`
	SoftLimit      *bool                    `json:"soft_limit,omitzero"`
	Reason         *string                  `json:"reason,omitzero"`
	EffectiveFrom  *string                  `json:"effective_from,omitzero"`
	EffectiveTo    conjoin.Nullable[string] `json:"effective_to,omitzero"`
}

type CreateEntitlementOverrideResponse = ListEntitlementOverridesItem

type ListEntitlementOverridesCountQuery = ListEntitlementOverridesQuery

type ListEntitlementOverridesCountResponse = ListChargesCountResponse

type UpdateEntitlementOverrideRequest struct {
	IncludedUnits *int64                   `json:"included_units,omitzero"`
	SoftLimit     *bool                    `json:"soft_limit,omitzero"`
	Reason        *string                  `json:"reason,omitzero"`
	EffectiveTo   conjoin.Nullable[string] `json:"effective_to,omitzero"`
	IsActive      *bool                    `json:"is_active,omitzero"`
}

type UpdateEntitlementOverrideResponse = ListEntitlementOverridesItem

type DeleteEntitlementOverrideResponseResponse struct {
	Type    string `json:"type"`
	Code    int64  `json:"code"`
	Message string `json:"message"`
}

type DeleteEntitlementOverrideResponse struct {
	Response *DeleteEntitlementOverrideResponseResponse `json:"response,omitzero"`
}
