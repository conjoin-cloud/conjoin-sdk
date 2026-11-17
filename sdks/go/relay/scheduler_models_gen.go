package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadSchedulerDefinitionsQuery struct {
	Status       *string                            `json:"status,omitzero"`
	ScheduleType *string                            `json:"schedule_type,omitzero"`
	ReferenceID  *string                            `json:"reference_id,omitzero"`
	DateCreated  *ReadEventChannelsQueryDateCreated `json:"date_created,omitzero"`
	Cursor       *ReadBroadcastChannelsQueryCursor  `json:"cursor,omitzero"`
	Sort         map[string]string                  `json:"sort,omitzero"`
	Limit        any                                `json:"limit,omitzero"`
}

type ReadSchedulerDefinitionsItem struct {
	ScheduleID              string                              `json:"schedule_id"`
	ConjoinAccountID        string                              `json:"conjoin_account_id"`
	ConjoinProjectID        string                              `json:"conjoin_project_id"`
	ReferenceID             conjoin.Nullable[string]            `json:"reference_id,omitzero"`
	LiveMode                bool                                `json:"live_mode"`
	Name                    string                              `json:"name"`
	ScheduleType            string                              `json:"schedule_type"`
	CronExpression          conjoin.Nullable[string]            `json:"cron_expression,omitzero"`
	Timezone                conjoin.Nullable[string]            `json:"timezone,omitzero"`
	OneTimeAt               conjoin.Nullable[string]            `json:"one_time_at,omitzero"`
	TargetURL               string                              `json:"target_url"`
	Payload                 map[string]any                      `json:"payload,omitzero"`
	Status                  string                              `json:"status"`
	NextRunAt               conjoin.Nullable[string]            `json:"next_run_at,omitzero"`
	LastRunAt               conjoin.Nullable[string]            `json:"last_run_at,omitzero"`
	Description             conjoin.Nullable[string]            `json:"description,omitzero"`
	MaxRetries              float64                             `json:"max_retries"`
	RetryBackoffStrategy    string                              `json:"retry_backoff_strategy"`
	RetryBackoffBaseSeconds float64                             `json:"retry_backoff_base_seconds"`
	TimeoutSeconds          float64                             `json:"timeout_seconds"`
	GraceWindowSeconds      float64                             `json:"grace_window_seconds"`
	DlqEnabled              bool                                `json:"dlq_enabled"`
	DlqRetentionDays        conjoin.Nullable[float64]           `json:"dlq_retention_days,omitzero"`
	Headers                 conjoin.Nullable[map[string]string] `json:"headers,omitzero"`
	OnSuccess               conjoin.Nullable[[]map[string]any]  `json:"on_success,omitzero"`
	OnFailure               conjoin.Nullable[[]map[string]any]  `json:"on_failure,omitzero"`
	Metadata                map[string]any                      `json:"metadata,omitzero"`
	DateCreated             string                              `json:"date_created"`
	DateUpdated             string                              `json:"date_updated"`
	DateDeleted             conjoin.Nullable[string]            `json:"date_deleted,omitzero"`
}

type CreateSchedulerDefinitionRequest struct {
	Name                    string                                                          `json:"name"`
	ScheduleType            string                                                          `json:"schedule_type"`
	CronExpression          *string                                                         `json:"cron_expression,omitzero"`
	Timezone                *string                                                         `json:"timezone,omitzero"`
	OneTimeAt               *string                                                         `json:"one_time_at,omitzero"`
	TargetURL               string                                                          `json:"target_url"`
	Payload                 map[string]any                                                  `json:"payload,omitzero"`
	Description             *string                                                         `json:"description,omitzero"`
	MaxRetries              *int64                                                          `json:"max_retries,omitzero"`
	RetryBackoffStrategy    *string                                                         `json:"retry_backoff_strategy,omitzero"`
	RetryBackoffBaseSeconds *int64                                                          `json:"retry_backoff_base_seconds,omitzero"`
	TimeoutSeconds          *int64                                                          `json:"timeout_seconds,omitzero"`
	GraceWindowSeconds      *int64                                                          `json:"grace_window_seconds,omitzero"`
	DlqEnabled              *bool                                                           `json:"dlq_enabled,omitzero"`
	DlqRetentionDays        *int64                                                          `json:"dlq_retention_days,omitzero"`
	ReferenceID             *string                                                         `json:"reference_id,omitzero"`
	Headers                 conjoin.Nullable[map[string]string]                             `json:"headers,omitzero"`
	OnSuccess               conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_success,omitzero"`
	OnFailure               conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_failure,omitzero"`
}

type CreateSchedulerDefinitionResponse = ReadSchedulerDefinitionsItem

type ReadSchedulerExecutionsQuery struct {
	Status           *string                           `json:"status,omitzero"`
	ReferenceID      *string                           `json:"reference_id,omitzero"`
	ConjoinRequestID *string                           `json:"conjoin_request_id,omitzero"`
	Cursor           *ReadBroadcastChannelsQueryCursor `json:"cursor,omitzero"`
	Sort             map[string]string                 `json:"sort,omitzero"`
	Limit            any                               `json:"limit,omitzero"`
}

type ReadSchedulerExecutionsItemAttemptHistoryItem struct {
	Attempt      float64                   `json:"attempt"`
	Status       string                    `json:"status"`
	ResponseCode conjoin.Nullable[float64] `json:"response_code,omitzero"`
	DurationMs   float64                   `json:"duration_ms"`
	Error        conjoin.Nullable[string]  `json:"error,omitzero"`
	AttemptedAt  string                    `json:"attempted_at"`
}

type ReadSchedulerExecutionsItem struct {
	ExecutionID      string                                          `json:"execution_id"`
	ScheduleID       string                                          `json:"schedule_id"`
	ConjoinAccountID string                                          `json:"conjoin_account_id"`
	ConjoinProjectID string                                          `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string]                        `json:"reference_id,omitzero"`
	LiveMode         bool                                            `json:"live_mode"`
	Status           string                                          `json:"status"`
	ConjoinRequestID string                                          `json:"conjoin_request_id"`
	TraceSource      conjoin.Nullable[string]                        `json:"trace_source,omitzero"`
	ResponseCode     conjoin.Nullable[float64]                       `json:"response_code,omitzero"`
	ResponseBody     conjoin.Nullable[string]                        `json:"response_body,omitzero"`
	Error            conjoin.Nullable[map[string]any]                `json:"error,omitzero"`
	ExecutedAt       string                                          `json:"executed_at"`
	ScheduledFor     string                                          `json:"scheduled_for"`
	NextAttemptAt    conjoin.Nullable[string]                        `json:"next_attempt_at,omitzero"`
	CompletedAt      conjoin.Nullable[string]                        `json:"completed_at,omitzero"`
	DurationMs       conjoin.Nullable[float64]                       `json:"duration_ms,omitzero"`
	Attempts         float64                                         `json:"attempts"`
	MaxAttempts      float64                                         `json:"max_attempts"`
	LastAttemptAt    conjoin.Nullable[string]                        `json:"last_attempt_at,omitzero"`
	AttemptHistory   []ReadSchedulerExecutionsItemAttemptHistoryItem `json:"attempt_history,omitzero"`
	DateCreated      string                                          `json:"date_created"`
}

type ReadSchedulerDeadLetterEntriesQuery struct {
	Replayed         any                               `json:"replayed,omitzero"`
	ReferenceID      *string                           `json:"reference_id,omitzero"`
	ConjoinRequestID *string                           `json:"conjoin_request_id,omitzero"`
	Cursor           *ReadBroadcastChannelsQueryCursor `json:"cursor,omitzero"`
	Sort             map[string]string                 `json:"sort,omitzero"`
	Limit            any                               `json:"limit,omitzero"`
}

type ReadSchedulerDeadLetterEntriesItem struct {
	DlqEntryID       string                   `json:"dlq_entry_id"`
	ScheduleID       string                   `json:"schedule_id"`
	ExecutionID      string                   `json:"execution_id"`
	TargetURL        string                   `json:"target_url"`
	Payload          map[string]any           `json:"payload"`
	FailureReason    string                   `json:"failure_reason"`
	Attempts         float64                  `json:"attempts"`
	FailedAt         string                   `json:"failed_at"`
	Replayed         bool                     `json:"replayed"`
	ReplayedAt       conjoin.Nullable[string] `json:"replayed_at,omitzero"`
	ConjoinRequestID string                   `json:"conjoin_request_id"`
	TraceSource      conjoin.Nullable[string] `json:"trace_source,omitzero"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	LiveMode         bool                     `json:"live_mode"`
	DateCreated      string                   `json:"date_created"`
}

type ReadSchedulerDefinitionsCountQuery = ReadSchedulerDefinitionsQuery

type ReadSchedulerDefinitionsCountResponse = ReadBroadcastChannelsCountResponse

type UpdateSchedulerDefinitionRequest struct {
	Name                    *string                                                         `json:"name,omitzero"`
	CronExpression          *string                                                         `json:"cron_expression,omitzero"`
	Timezone                *string                                                         `json:"timezone,omitzero"`
	OneTimeAt               *string                                                         `json:"one_time_at,omitzero"`
	TargetURL               *string                                                         `json:"target_url,omitzero"`
	Payload                 map[string]any                                                  `json:"payload,omitzero"`
	Description             *string                                                         `json:"description,omitzero"`
	MaxRetries              *int64                                                          `json:"max_retries,omitzero"`
	RetryBackoffStrategy    *string                                                         `json:"retry_backoff_strategy,omitzero"`
	RetryBackoffBaseSeconds *int64                                                          `json:"retry_backoff_base_seconds,omitzero"`
	TimeoutSeconds          *int64                                                          `json:"timeout_seconds,omitzero"`
	GraceWindowSeconds      *int64                                                          `json:"grace_window_seconds,omitzero"`
	DlqEnabled              *bool                                                           `json:"dlq_enabled,omitzero"`
	DlqRetentionDays        conjoin.Nullable[int64]                                         `json:"dlq_retention_days,omitzero"`
	Headers                 conjoin.Nullable[map[string]string]                             `json:"headers,omitzero"`
	OnSuccess               conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_success,omitzero"`
	OnFailure               conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_failure,omitzero"`
}

type UpdateSchedulerDefinitionResponse = ReadSchedulerDefinitionsItem

type PauseSchedulerResponse = ReadSchedulerDefinitionsItem

type ResumeSchedulerResponse = ReadSchedulerDefinitionsItem

type CancelSchedulerResponse = ReadSchedulerDefinitionsItem

type TriggerSchedulerExecutionResponse = ReadSchedulerExecutionsItem

type ReadSchedulerExecutionsCountQuery = ReadSchedulerExecutionsQuery

type ReadSchedulerExecutionsCountResponse = ReadBroadcastChannelsCountResponse

type ReadSchedulerDeadLetterEntriesCountQuery = ReadSchedulerDeadLetterEntriesQuery

type ReadSchedulerDeadLetterEntriesCountResponse = ReadBroadcastChannelsCountResponse

type ReplaySchedulerDeadLetterEntryResponse = ReadSchedulerDeadLetterEntriesItem
