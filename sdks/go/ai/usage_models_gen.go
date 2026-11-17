package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListUsageRecordsQuery struct {
	RecordType       *string                          `json:"record_type,omitzero"`
	Model            *string                          `json:"model,omitzero"`
	Provider         *string                          `json:"provider,omitzero"`
	BillingPeriod    *string                          `json:"billing_period,omitzero"`
	IsBillable       any                              `json:"is_billable,omitzero"`
	ConjoinRequestID *string                          `json:"conjoin_request_id,omitzero"`
	TraceSource      *string                          `json:"trace_source,omitzero"`
	RecordedAt       *ListByokConfigsQueryDateCreated `json:"recorded_at,omitzero"`
	DateCreated      *ListByokConfigsQueryDateCreated `json:"date_created,omitzero"`
	Cursor           *ListByokConfigsQueryCursor      `json:"cursor,omitzero"`
	Sort             map[string]string                `json:"sort,omitzero"`
	Limit            any                              `json:"limit,omitzero"`
}

type ListUsageRecordsItem struct {
	RecordID         string                   `json:"record_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	RequestID        conjoin.Nullable[string] `json:"request_id,omitzero"`
	ConjoinRequestID string                   `json:"conjoin_request_id"`
	TraceSource      conjoin.Nullable[string] `json:"trace_source,omitzero"`
	RecordType       string                   `json:"record_type"`
	Model            conjoin.Nullable[string] `json:"model,omitzero"`
	Provider         conjoin.Nullable[string] `json:"provider,omitzero"`
	InputTokens      float64                  `json:"input_tokens"`
	OutputTokens     float64                  `json:"output_tokens"`
	TotalTokens      float64                  `json:"total_tokens"`
	CostUsd          float64                  `json:"cost_usd"`
	LatencyMs        float64                  `json:"latency_ms"`
	IsBillable       bool                     `json:"is_billable"`
	BillingPeriod    string                   `json:"billing_period"`
	RecordedAt       string                   `json:"recorded_at"`
	DateCreated      string                   `json:"date_created"`
}

type ListUsageRecordsCountQuery = ListUsageRecordsQuery

type ListUsageRecordsCountResponse = ListByokConfigsCountResponse

type ReadUsageSummaryQuery struct {
	BillingPeriod *string `json:"billing_period,omitzero"`
	StartDate     *string `json:"start_date,omitzero"`
	EndDate       *string `json:"end_date,omitzero"`
}

type ReadUsageSummaryResponseBreakdownByModelItem struct {
	Model         string  `json:"model"`
	TotalTokens   float64 `json:"total_tokens"`
	TotalCostUsd  float64 `json:"total_cost_usd"`
	TotalRequests float64 `json:"total_requests"`
}

type ReadUsageSummaryResponseBreakdownByProviderItem struct {
	Provider      string  `json:"provider"`
	TotalTokens   float64 `json:"total_tokens"`
	TotalCostUsd  float64 `json:"total_cost_usd"`
	TotalRequests float64 `json:"total_requests"`
}

type ReadUsageSummaryResponseBreakdownByTypeItem struct {
	RecordType    string  `json:"record_type"`
	TotalTokens   float64 `json:"total_tokens"`
	TotalCostUsd  float64 `json:"total_cost_usd"`
	TotalRequests float64 `json:"total_requests"`
}

type ReadUsageSummaryResponse struct {
	TotalTokens         float64                                           `json:"total_tokens"`
	TotalCostUsd        float64                                           `json:"total_cost_usd"`
	TotalRequests       float64                                           `json:"total_requests"`
	BreakdownByModel    []ReadUsageSummaryResponseBreakdownByModelItem    `json:"breakdown_by_model"`
	BreakdownByProvider []ReadUsageSummaryResponseBreakdownByProviderItem `json:"breakdown_by_provider"`
	BreakdownByType     []ReadUsageSummaryResponseBreakdownByTypeItem     `json:"breakdown_by_type"`
	BillingPeriod       string                                            `json:"billing_period"`
}
