package cloud

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadSpendControlResponse struct {
	CloudAccountID         string                                                                  `json:"cloud_account_id"`
	SpendControlID         string                                                                  `json:"spend_control_id"`
	Currency               string                                                                  `json:"currency"`
	OverageBudgetMicros    float64                                                                 `json:"overage_budget_micros"`
	AiCircuitBreakerLimits []ReadAccountPlanResponseSpendControlDefaultsAiCircuitBreakerLimitsItem `json:"ai_circuit_breaker_limits"`
	AlertThresholds        []float64                                                               `json:"alert_thresholds"`
	AlertEmailEnabled      bool                                                                    `json:"alert_email_enabled"`
	AlertSMSEnabled        bool                                                                    `json:"alert_sms_enabled"`
	AlertWebhookEnabled    bool                                                                    `json:"alert_webhook_enabled"`
	DateCreated            string                                                                  `json:"date_created"`
	DateUpdated            conjoin.Nullable[string]                                                `json:"date_updated,omitzero"`
}

type UpdateSpendControlRequestAiCircuitBreakerLimitsItem struct {
	Currency    string `json:"currency"`
	LimitMicros int64  `json:"limit_micros"`
}

type UpdateSpendControlRequest struct {
	OverageBudgetMicros    *int64                                                `json:"overage_budget_micros,omitzero"`
	AiCircuitBreakerLimits []UpdateSpendControlRequestAiCircuitBreakerLimitsItem `json:"ai_circuit_breaker_limits,omitzero"`
	AlertThresholds        []int64                                               `json:"alert_thresholds,omitzero"`
	AlertEmailEnabled      *bool                                                 `json:"alert_email_enabled,omitzero"`
	AlertSMSEnabled        *bool                                                 `json:"alert_sms_enabled,omitzero"`
	AlertWebhookEnabled    *bool                                                 `json:"alert_webhook_enabled,omitzero"`
}

type UpdateSpendControlResponse = ReadSpendControlResponse

type ReadSpendControlUsageResponseAiUsageItem struct {
	Currency      string  `json:"currency"`
	CurrentMicros float64 `json:"current_micros"`
	LimitMicros   float64 `json:"limit_micros"`
}

type ReadSpendControlUsageResponseServiceOverageBreakdownItem struct {
	ServiceKey           string  `json:"service_key"`
	OverageCurrentMicros float64 `json:"overage_current_micros"`
}

type ReadSpendControlUsageResponse struct {
	CloudAccountID          string                                                     `json:"cloud_account_id"`
	BillingPeriod           string                                                     `json:"billing_period"`
	Currency                string                                                     `json:"currency"`
	OverageBudgetMicros     float64                                                    `json:"overage_budget_micros"`
	OverageUsedMicros       float64                                                    `json:"overage_used_micros"`
	AiUsage                 []ReadSpendControlUsageResponseAiUsageItem                 `json:"ai_usage"`
	ServiceOverageBreakdown []ReadSpendControlUsageResponseServiceOverageBreakdownItem `json:"service_overage_breakdown"`
	BillingCycleResetsAt    string                                                     `json:"billing_cycle_resets_at"`
}
