package billing

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ListSubscriptionSchedulesQuery struct {
	CustomerID *string                 `json:"customer_id,omitzero"`
	Status     *string                 `json:"status,omitzero"`
	Cursor     *ListChargesQueryCursor `json:"cursor,omitzero"`
	Sort       map[string]string       `json:"sort,omitzero"`
	Limit      any                     `json:"limit,omitzero"`
}

type ListSubscriptionSchedulesItemPhasesItemItemsItem struct {
	PriceID        string   `json:"price_id"`
	Quantity       *float64 `json:"quantity,omitzero"`
	ReplacesPlanID *string  `json:"replaces_plan_id,omitzero"`
}

type ListSubscriptionSchedulesItemPhasesItem struct {
	PhaseID               string                                             `json:"phase_id"`
	StartDate             string                                             `json:"start_date"`
	EndDate               string                                             `json:"end_date"`
	Items                 []ListSubscriptionSchedulesItemPhasesItemItemsItem `json:"items"`
	ProrationBehavior     string                                             `json:"proration_behavior"`
	ApplicationTiming     string                                             `json:"application_timing"`
	TrialEnd              conjoin.Nullable[string]                           `json:"trial_end,omitzero"`
	Status                string                                             `json:"status"`
	AppliedChangeID       conjoin.Nullable[string]                           `json:"applied_change_id,omitzero"`
	AppliedAt             conjoin.Nullable[string]                           `json:"applied_at,omitzero"`
	AttemptCount          float64                                            `json:"attempt_count"`
	FirstApplyAttemptedAt conjoin.Nullable[string]                           `json:"first_apply_attempted_at,omitzero"`
	LastErrorCode         conjoin.Nullable[string]                           `json:"last_error_code,omitzero"`
}

type ListSubscriptionSchedulesItem struct {
	ScheduleID        string                                    `json:"schedule_id"`
	SubscriptionID    string                                    `json:"subscription_id"`
	CustomerID        string                                    `json:"customer_id"`
	EntityID          string                                    `json:"entity_id"`
	Status            string                                    `json:"status"`
	Phases            []ListSubscriptionSchedulesItemPhasesItem `json:"phases"`
	CurrentPhaseIndex conjoin.Nullable[float64]                 `json:"current_phase_index,omitzero"`
	EndBehavior       string                                    `json:"end_behavior"`
	ReleasedDate      conjoin.Nullable[string]                  `json:"released_date,omitzero"`
	CanceledDate      conjoin.Nullable[string]                  `json:"canceled_date,omitzero"`
	CompletedDate     conjoin.Nullable[string]                  `json:"completed_date,omitzero"`
	DateCreated       string                                    `json:"date_created"`
	DateUpdated       conjoin.Nullable[string]                  `json:"date_updated,omitzero"`
	DateDeleted       conjoin.Nullable[string]                  `json:"date_deleted,omitzero"`
	LiveMode          bool                                      `json:"live_mode"`
}

type CreateSubscriptionScheduleRequestPhasesItemItemsItem struct {
	PriceID        string  `json:"price_id"`
	Quantity       *int64  `json:"quantity,omitzero"`
	ReplacesPlanID *string `json:"replaces_plan_id,omitzero"`
}

type CreateSubscriptionScheduleRequestPhasesItem struct {
	StartDate         string                                                 `json:"start_date"`
	EndDate           string                                                 `json:"end_date"`
	Items             []CreateSubscriptionScheduleRequestPhasesItemItemsItem `json:"items"`
	ProrationBehavior *string                                                `json:"proration_behavior,omitzero"`
	ApplicationTiming *string                                                `json:"application_timing,omitzero"`
	TrialEnd          *string                                                `json:"trial_end,omitzero"`
}

type CreateSubscriptionScheduleRequest struct {
	Phases      []CreateSubscriptionScheduleRequestPhasesItem `json:"phases"`
	EndBehavior string                                        `json:"end_behavior"`
}

type CreateSubscriptionScheduleResponse = ListSubscriptionSchedulesItem

type ListSubscriptionSchedulesCountQuery = ListSubscriptionSchedulesQuery

type ListSubscriptionSchedulesCountResponse = ListChargesCountResponse

type GetSubscriptionScheduleResponse = ListSubscriptionSchedulesItem

type CancelSubscriptionScheduleResponse = ListSubscriptionSchedulesItem

type ReleaseSubscriptionScheduleResponse = ListSubscriptionSchedulesItem
