package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSubscriptionsQuery struct {
	ReferenceID *string                 `json:"reference_id,omitzero"`
	CustomerID  *string                 `json:"customer_id,omitzero"`
	Status      *string                 `json:"status,omitzero"`
	Cursor      *ListChargesQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string       `json:"sort,omitzero"`
	Limit       any                     `json:"limit,omitzero"`
}

type ListSubscriptionsItemPlansItem struct {
	PlanID             string                   `json:"plan_id"`
	PriceID            conjoin.Nullable[string] `json:"price_id,omitzero"`
	DiscountID         conjoin.Nullable[string] `json:"discount_id,omitzero"`
	Currency           string                   `json:"currency"`
	UnitPrice          float64                  `json:"unit_price"`
	Quantity           float64                  `json:"quantity"`
	DiscountAmount     float64                  `json:"discount_amount"`
	Amount             float64                  `json:"amount"`
	AmountAfterTaxes   float64                  `json:"amount_after_taxes"`
	Description        string                   `json:"description"`
	StartDate          conjoin.Nullable[string] `json:"start_date,omitzero"`
	EndDate            conjoin.Nullable[string] `json:"end_date,omitzero"`
	Interval           string                   `json:"interval"`
	IntervalCount      float64                  `json:"interval_count"`
	UsageType          *string                  `json:"usage_type,omitzero"`
	AggregateUsage     conjoin.Nullable[string] `json:"aggregate_usage,omitzero"`
	TaxBehavior        *string                  `json:"tax_behavior,omitzero"`
	SourceActivationID conjoin.Nullable[string] `json:"source_activation_id,omitzero"`
}

type ListSubscriptionsItemRenewalNotifications struct {
	DaysBefore []float64 `json:"days_before,omitzero"`
}

type ListSubscriptionsItemLatestStateTransition struct {
	StateHistoryID conjoin.Nullable[string] `json:"state_history_id,omitzero"`
	PreviousStatus conjoin.Nullable[string] `json:"previous_status,omitzero"`
	TransitionDate conjoin.Nullable[string] `json:"transition_date,omitzero"`
}

type ListSubscriptionsItemProration struct {
	Behavior          string `json:"behavior"`
	ApplicationTiming string `json:"application_timing"`
}

type ListSubscriptionsItemCancellation struct {
	CanceledDate        conjoin.Nullable[string] `json:"canceled_date,omitzero"`
	TerminationBehavior conjoin.Nullable[string] `json:"termination_behavior,omitzero"`
	RefundPolicy        conjoin.Nullable[string] `json:"refund_policy,omitzero"`
	Reason              conjoin.Nullable[string] `json:"reason,omitzero"`
}

type ListSubscriptionsItemCurrentCycle struct {
	CycleID         conjoin.Nullable[string] `json:"cycle_id,omitzero"`
	PeriodStart     conjoin.Nullable[string] `json:"period_start,omitzero"`
	PeriodEnd       conjoin.Nullable[string] `json:"period_end,omitzero"`
	NextBillingDate conjoin.Nullable[string] `json:"next_billing_date,omitzero"`
}

type ListSubscriptionsItem struct {
	SubscriptionID        string                                                      `json:"subscription_id"`
	ReferenceID           string                                                      `json:"reference_id"`
	CustomerID            string                                                      `json:"customer_id"`
	EntityID              string                                                      `json:"entity_id"`
	Plans                 []ListSubscriptionsItemPlansItem                            `json:"plans"`
	Status                string                                                      `json:"status"`
	StartDate             string                                                      `json:"start_date"`
	EndDate               conjoin.Nullable[string]                                    `json:"end_date,omitzero"`
	TrialStartDate        conjoin.Nullable[string]                                    `json:"trial_start_date,omitzero"`
	TrialEndDate          conjoin.Nullable[string]                                    `json:"trial_end_date,omitzero"`
	Currency              string                                                      `json:"currency"`
	InvoicingOption       string                                                      `json:"invoicing_option"`
	PaymentStrategy       string                                                      `json:"payment_strategy"`
	PaymentMethod         conjoin.Nullable[string]                                    `json:"payment_method,omitzero"`
	DaysUntilDue          conjoin.Nullable[float64]                                   `json:"days_until_due,omitzero"`
	CycleStartDate        conjoin.Nullable[string]                                    `json:"cycle_start_date,omitzero"`
	AutoRenew             conjoin.Nullable[bool]                                      `json:"auto_renew,omitzero"`
	RenewalNotifications  conjoin.Nullable[ListSubscriptionsItemRenewalNotifications] `json:"renewal_notifications,omitzero"`
	LatestStateTransition *ListSubscriptionsItemLatestStateTransition                 `json:"latest_state_transition,omitzero"`
	Proration             conjoin.Nullable[ListSubscriptionsItemProration]            `json:"proration,omitzero"`
	Cancellation          conjoin.Nullable[ListSubscriptionsItemCancellation]         `json:"cancellation,omitzero"`
	CurrentCycle          conjoin.Nullable[ListSubscriptionsItemCurrentCycle]         `json:"current_cycle,omitzero"`
	DateCreated           string                                                      `json:"date_created"`
	DateUpdated           string                                                      `json:"date_updated"`
	DateDeleted           conjoin.Nullable[string]                                    `json:"date_deleted,omitzero"`
	LiveMode              bool                                                        `json:"live_mode"`
}

type CreateSubscriptionRequestPlansItem struct {
	Currency           string  `json:"currency"`
	UnitPrice          int64   `json:"unit_price"`
	Quantity           int64   `json:"quantity"`
	Description        *string `json:"description,omitzero"`
	Interval           string  `json:"interval"`
	IntervalCount      *int64  `json:"interval_count,omitzero"`
	UsageType          *string `json:"usage_type,omitzero"`
	AggregateUsage     *string `json:"aggregate_usage,omitzero"`
	TaxBehavior        *string `json:"tax_behavior,omitzero"`
	SourceActivationID *string `json:"source_activation_id,omitzero"`
	DiscountID         *string `json:"discount_id,omitzero"`
}

type CreateSubscriptionRequestRenewalNotifications struct {
	DaysBefore []int64 `json:"days_before,omitzero"`
}

type CreateSubscriptionRequestProration struct {
	Behavior          *string `json:"behavior,omitzero"`
	ApplicationTiming *string `json:"application_timing,omitzero"`
}

type CreateSubscriptionRequest struct {
	ReferenceID          *string                                        `json:"reference_id,omitzero"`
	CustomerID           string                                         `json:"customer_id"`
	PriceIDs             []string                                       `json:"price_ids,omitzero"`
	Plans                []CreateSubscriptionRequestPlansItem           `json:"plans,omitzero"`
	TrialEndDate         *string                                        `json:"trial_end_date,omitzero"`
	InvoicingOption      *string                                        `json:"invoicing_option,omitzero"`
	PaymentStrategy      *string                                        `json:"payment_strategy,omitzero"`
	PaymentMethod        *string                                        `json:"payment_method,omitzero"`
	DaysUntilDue         *int64                                         `json:"days_until_due,omitzero"`
	CycleStartDate       *string                                        `json:"cycle_start_date,omitzero"`
	AutoRenew            *bool                                          `json:"auto_renew,omitzero"`
	RenewalNotifications *CreateSubscriptionRequestRenewalNotifications `json:"renewal_notifications,omitzero"`
	Proration            *CreateSubscriptionRequestProration            `json:"proration,omitzero"`
}

type CreateSubscriptionResponse = ListSubscriptionsItem

type ListSubscriptionCyclesQuery struct {
	CycleID *string                 `json:"cycle_id,omitzero"`
	Status  *string                 `json:"status,omitzero"`
	Cursor  *ListChargesQueryCursor `json:"cursor,omitzero"`
	Sort    map[string]string       `json:"sort,omitzero"`
	Limit   any                     `json:"limit,omitzero"`
}

type ListSubscriptionCyclesItemUsageDataItem struct {
	PlanIDs       []string `json:"plan_ids"`
	UsageQuantity float64  `json:"usage_quantity"`
	UsageAmount   float64  `json:"usage_amount"`
}

type ListSubscriptionCyclesItem struct {
	CycleID          string                                    `json:"cycle_id"`
	SubscriptionID   string                                    `json:"subscription_id"`
	EntityID         string                                    `json:"entity_id"`
	ConjoinAccountID string                                    `json:"conjoin_account_id"`
	ConjoinProjectID string                                    `json:"conjoin_project_id"`
	CycleSequence    float64                                   `json:"cycle_sequence"`
	PeriodStart      string                                    `json:"period_start"`
	PeriodEnd        string                                    `json:"period_end"`
	InvoiceID        conjoin.Nullable[string]                  `json:"invoice_id,omitzero"`
	Status           string                                    `json:"status"`
	Amount           float64                                   `json:"amount"`
	Currency         string                                    `json:"currency"`
	UsageData        []ListSubscriptionCyclesItemUsageDataItem `json:"usage_data,omitzero"`
	BilledAt         conjoin.Nullable[string]                  `json:"billed_at,omitzero"`
	DateCreated      string                                    `json:"date_created"`
	DateUpdated      string                                    `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]                  `json:"date_deleted,omitzero"`
	LiveMode         bool                                      `json:"live_mode"`
}

type ListSubscriptionsCountQuery = ListSubscriptionsQuery

type ListSubscriptionsCountResponse = ListChargesCountResponse

type ReadSubscriptionResponse = ListSubscriptionsItem

type UpdateSubscriptionRequest struct {
	PaymentMethod        *string                                                         `json:"payment_method,omitzero"`
	AutoRenew            *bool                                                           `json:"auto_renew,omitzero"`
	RenewalNotifications conjoin.Nullable[CreateSubscriptionRequestRenewalNotifications] `json:"renewal_notifications,omitzero"`
	Proration            conjoin.Nullable[ListSubscriptionsItemProration]                `json:"proration,omitzero"`
}

type UpdateSubscriptionResponse = ListSubscriptionsItem

type CreateSubscriptionPlanChangeRequestItemsItem struct {
	PriceID        string  `json:"price_id"`
	Quantity       *int64  `json:"quantity,omitzero"`
	ReplacesPlanID *string `json:"replaces_plan_id,omitzero"`
	DiscountID     *string `json:"discount_id,omitzero"`
}

type CreateSubscriptionPlanChangeRequest struct {
	Items             []CreateSubscriptionPlanChangeRequestItemsItem `json:"items"`
	ProrationBehavior *string                                        `json:"proration_behavior,omitzero"`
	ApplicationTiming *string                                        `json:"application_timing,omitzero"`
}

type CreateSubscriptionPlanChangeResponse struct {
	Subscription             ListSubscriptionsItem `json:"subscription"`
	AppliedProrationBehavior string                `json:"applied_proration_behavior"`
}

type CancelSubscriptionRequest struct {
	TerminationBehavior string  `json:"termination_behavior"`
	RefundPolicy        *string `json:"refund_policy,omitzero"`
	Reason              *string `json:"reason,omitzero"`
}

type CancelSubscriptionResponse = ListSubscriptionsItem

type PauseSubscriptionRequest struct {
	Reason *string `json:"reason,omitzero"`
}

type PauseSubscriptionResponse = ListSubscriptionsItem

type ResumeSubscriptionResponse = ListSubscriptionsItem

type RecordSubscriptionUsageRequestRecordsItem struct {
	Quantity  int64          `json:"quantity"`
	Action    *string        `json:"action,omitzero"`
	Timestamp *string        `json:"timestamp,omitzero"`
	Metadata  map[string]any `json:"metadata,omitzero"`
}

type RecordSubscriptionUsageRequest struct {
	PlanID  string                                      `json:"plan_id"`
	CycleID *string                                     `json:"cycle_id,omitzero"`
	Records []RecordSubscriptionUsageRequestRecordsItem `json:"records"`
}

type ReadSubscriptionUsageSummaryQuery struct {
	CycleID *string `json:"cycle_id,omitzero"`
}

type ReadSubscriptionUsageSummaryResponseItem struct {
	PlanID         string  `json:"plan_id"`
	PlanName       string  `json:"plan_name"`
	UsageType      string  `json:"usage_type"`
	AggregateUsage *string `json:"aggregate_usage"`
	UsageQuantity  float64 `json:"usage_quantity"`
	UsageAmount    float64 `json:"usage_amount"`
	Currency       string  `json:"currency"`
}

type ListSubscriptionCyclesCountQuery = ListSubscriptionCyclesQuery

type ListSubscriptionCyclesCountResponse = ListChargesCountResponse
