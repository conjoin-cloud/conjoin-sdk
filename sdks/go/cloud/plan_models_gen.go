package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadAccountPlanResponsePlanItemsItem struct {
	EntitlementKey         string                    `json:"entitlement_key"`
	ValueType              string                    `json:"value_type"`
	BooleanValue           conjoin.Nullable[bool]    `json:"boolean_value,omitzero"`
	IncludedUnits          conjoin.Nullable[float64] `json:"included_units,omitzero"`
	SoftLimit              conjoin.Nullable[bool]    `json:"soft_limit,omitzero"`
	ServiceKey             conjoin.Nullable[string]  `json:"service_key,omitzero"`
	SkuID                  conjoin.Nullable[string]  `json:"sku_id,omitzero"`
	PriceID                conjoin.Nullable[string]  `json:"price_id,omitzero"`
	ProductID              conjoin.Nullable[string]  `json:"product_id,omitzero"`
	OverageUnitPriceMicros conjoin.Nullable[float64] `json:"overage_unit_price_micros,omitzero"`
	OveragePriceID         conjoin.Nullable[string]  `json:"overage_price_id,omitzero"`
}

type ReadAccountPlanResponseSpendControlDefaultsAiCircuitBreakerLimitsItem struct {
	Currency    string  `json:"currency"`
	LimitMicros float64 `json:"limit_micros"`
}

type ReadAccountPlanResponseSpendControlDefaults struct {
	OverageBudgetMicros    float64                                                                 `json:"overage_budget_micros"`
	AiCircuitBreakerLimits []ReadAccountPlanResponseSpendControlDefaultsAiCircuitBreakerLimitsItem `json:"ai_circuit_breaker_limits"`
}

type ReadAccountPlanResponse struct {
	CloudPlanID          string                                                        `json:"cloud_plan_id"`
	Slug                 string                                                        `json:"slug"`
	Name                 string                                                        `json:"name"`
	Description          *string                                                       `json:"description,omitzero"`
	Status               string                                                        `json:"status"`
	Currency             string                                                        `json:"currency"`
	BillingBundleID      *string                                                       `json:"billing_bundle_id"`
	PlanItems            []ReadAccountPlanResponsePlanItemsItem                        `json:"plan_items"`
	SpendControlDefaults conjoin.Nullable[ReadAccountPlanResponseSpendControlDefaults] `json:"spend_control_defaults,omitzero"`
	EffectiveFrom        conjoin.Nullable[string]                                      `json:"effective_from,omitzero"`
	ReplacesPlanID       conjoin.Nullable[string]                                      `json:"replaces_plan_id,omitzero"`
	DateCreated          string                                                        `json:"date_created"`
	DateUpdated          conjoin.Nullable[string]                                      `json:"date_updated,omitzero"`
}

type ReadPlansQuery struct {
	Slug     *string                 `json:"slug,omitzero"`
	Status   *string                 `json:"status,omitzero"`
	Currency *string                 `json:"currency,omitzero"`
	Cursor   *ReadApiKeysQueryCursor `json:"cursor,omitzero"`
	Sort     map[string]string       `json:"sort,omitzero"`
	Limit    any                     `json:"limit,omitzero"`
}

type ReadPlansItem = ReadAccountPlanResponse

type ReadPlansCountQuery = ReadPlansQuery

type ReadPlansCountResponse = ReadApiKeysCountResponse

type ReadPlanResponse = ReadAccountPlanResponse
