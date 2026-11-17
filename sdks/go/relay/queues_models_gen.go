package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadQueueDefinitionsQuery = ReadEventChannelsQuery

type ReadQueueDefinitionsItem struct {
	QueueID                    string                              `json:"queue_id"`
	ConjoinAccountID           string                              `json:"conjoin_account_id"`
	ConjoinProjectID           string                              `json:"conjoin_project_id"`
	ReferenceID                conjoin.Nullable[string]            `json:"reference_id,omitzero"`
	LiveMode                   bool                                `json:"live_mode"`
	Name                       string                              `json:"name"`
	TargetURL                  string                              `json:"target_url"`
	RateLimitPerMinute         conjoin.Nullable[float64]           `json:"rate_limit_per_minute,omitzero"`
	MaxRetries                 *float64                            `json:"max_retries,omitzero"`
	RetryBackoffStrategy       conjoin.Nullable[string]            `json:"retry_backoff_strategy,omitzero"`
	RetryBackoffBaseSeconds    conjoin.Nullable[float64]           `json:"retry_backoff_base_seconds,omitzero"`
	Priority                   *float64                            `json:"priority,omitzero"`
	DefaultDelaySeconds        *float64                            `json:"default_delay_seconds,omitzero"`
	Status                     string                              `json:"status"`
	Description                conjoin.Nullable[string]            `json:"description,omitzero"`
	TimeoutSeconds             *float64                            `json:"timeout_seconds,omitzero"`
	VisibilityTimeoutSeconds   *float64                            `json:"visibility_timeout_seconds,omitzero"`
	MaxConcurrentDeliveries    conjoin.Nullable[float64]           `json:"max_concurrent_deliveries,omitzero"`
	DlqEnabled                 *bool                               `json:"dlq_enabled,omitzero"`
	TaskRetentionDays          conjoin.Nullable[float64]           `json:"task_retention_days,omitzero"`
	DlqRetentionDays           conjoin.Nullable[float64]           `json:"dlq_retention_days,omitzero"`
	Headers                    conjoin.Nullable[map[string]string] `json:"headers,omitzero"`
	OnSuccess                  conjoin.Nullable[[]map[string]any]  `json:"on_success,omitzero"`
	OnFailure                  conjoin.Nullable[[]map[string]any]  `json:"on_failure,omitzero"`
	StatusBroadcastEnabled     *bool                               `json:"status_broadcast_enabled,omitzero"`
	StatusEventsEnabled        *bool                               `json:"status_events_enabled,omitzero"`
	StatusBroadcastChannelID   conjoin.Nullable[string]            `json:"status_broadcast_channel_id,omitzero"`
	StatusEventChannelID       conjoin.Nullable[string]            `json:"status_event_channel_id,omitzero"`
	StatusBatchIntervalSeconds *float64                            `json:"status_batch_interval_seconds,omitzero"`
	StatusBatchMaxSize         *float64                            `json:"status_batch_max_size,omitzero"`
	ResponseForwardFields      conjoin.Nullable[[]string]          `json:"response_forward_fields,omitzero"`
	Metadata                   map[string]any                      `json:"metadata,omitzero"`
	DateCreated                string                              `json:"date_created"`
	DateUpdated                string                              `json:"date_updated"`
	DateDeleted                conjoin.Nullable[string]            `json:"date_deleted,omitzero"`
}

type CreateQueueDefinitionRequest struct {
	Name                       string                                                          `json:"name"`
	ReferenceID                *string                                                         `json:"reference_id,omitzero"`
	TargetURL                  string                                                          `json:"target_url"`
	RateLimitPerMinute         *int64                                                          `json:"rate_limit_per_minute,omitzero"`
	MaxRetries                 *int64                                                          `json:"max_retries,omitzero"`
	RetryBackoffStrategy       *string                                                         `json:"retry_backoff_strategy,omitzero"`
	RetryBackoffBaseSeconds    *int64                                                          `json:"retry_backoff_base_seconds,omitzero"`
	Priority                   *int64                                                          `json:"priority,omitzero"`
	DefaultDelaySeconds        *int64                                                          `json:"default_delay_seconds,omitzero"`
	Description                *string                                                         `json:"description,omitzero"`
	TimeoutSeconds             *int64                                                          `json:"timeout_seconds,omitzero"`
	VisibilityTimeoutSeconds   *int64                                                          `json:"visibility_timeout_seconds,omitzero"`
	MaxConcurrentDeliveries    conjoin.Nullable[int64]                                         `json:"max_concurrent_deliveries,omitzero"`
	DlqEnabled                 *bool                                                           `json:"dlq_enabled,omitzero"`
	TaskRetentionDays          *int64                                                          `json:"task_retention_days,omitzero"`
	DlqRetentionDays           *int64                                                          `json:"dlq_retention_days,omitzero"`
	Headers                    conjoin.Nullable[map[string]string]                             `json:"headers,omitzero"`
	OnSuccess                  conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_success,omitzero"`
	OnFailure                  conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_failure,omitzero"`
	StatusBroadcastEnabled     *bool                                                           `json:"status_broadcast_enabled,omitzero"`
	StatusEventsEnabled        *bool                                                           `json:"status_events_enabled,omitzero"`
	StatusBroadcastChannelID   conjoin.Nullable[string]                                        `json:"status_broadcast_channel_id,omitzero"`
	StatusEventChannelID       conjoin.Nullable[string]                                        `json:"status_event_channel_id,omitzero"`
	StatusBatchIntervalSeconds *int64                                                          `json:"status_batch_interval_seconds,omitzero"`
	StatusBatchMaxSize         *int64                                                          `json:"status_batch_max_size,omitzero"`
	ResponseForwardFields      conjoin.Nullable[[]string]                                      `json:"response_forward_fields,omitzero"`
}

type CreateQueueDefinitionResponse = ReadQueueDefinitionsItem

type ReadQueueTasksQuery struct {
	Status           *string                            `json:"status,omitzero"`
	TaskIDs          *string                            `json:"task_ids,omitzero"`
	ReferenceID      *string                            `json:"reference_id,omitzero"`
	ConjoinRequestID *string                            `json:"conjoin_request_id,omitzero"`
	DateCreated      *ReadEventChannelsQueryDateCreated `json:"date_created,omitzero"`
	Cursor           *ReadBroadcastChannelsQueryCursor  `json:"cursor,omitzero"`
	Sort             map[string]string                  `json:"sort,omitzero"`
	Limit            any                                `json:"limit,omitzero"`
}

type ReadQueueTasksItem struct {
	TaskID             string                    `json:"task_id"`
	QueueID            string                    `json:"queue_id"`
	ConjoinAccountID   string                    `json:"conjoin_account_id"`
	ConjoinProjectID   string                    `json:"conjoin_project_id"`
	LiveMode           bool                      `json:"live_mode"`
	ReferenceID        conjoin.Nullable[string]  `json:"reference_id,omitzero"`
	ConjoinRequestID   string                    `json:"conjoin_request_id"`
	TraceSource        conjoin.Nullable[string]  `json:"trace_source,omitzero"`
	Payload            map[string]any            `json:"payload,omitzero"`
	TargetURL          *string                   `json:"target_url,omitzero"`
	Status             string                    `json:"status"`
	AttemptCount       *float64                  `json:"attempt_count,omitzero"`
	ScheduledAt        conjoin.Nullable[string]  `json:"scheduled_at,omitzero"`
	CompletedAt        conjoin.Nullable[string]  `json:"completed_at,omitzero"`
	ResponseStatusCode conjoin.Nullable[float64] `json:"response_status_code,omitzero"`
	ResponseBody       conjoin.Nullable[string]  `json:"response_body,omitzero"`
	DateCreated        string                    `json:"date_created"`
	DateUpdated        string                    `json:"date_updated"`
}

type EnqueueTaskRequestScheduledFor struct {
	Datetime string  `json:"datetime"`
	Timezone *string `json:"timezone,omitzero"`
}

type EnqueueTaskRequest struct {
	Payload      map[string]any                      `json:"payload,omitzero"`
	ReferenceID  *string                             `json:"reference_id,omitzero"`
	DelaySeconds *int64                              `json:"delay_seconds,omitzero"`
	ScheduledFor *EnqueueTaskRequestScheduledFor     `json:"scheduled_for,omitzero"`
	TargetURL    *string                             `json:"target_url,omitzero"`
	Headers      conjoin.Nullable[map[string]string] `json:"headers,omitzero"`
}

type EnqueueTaskResponse = ReadQueueTasksItem

type ReadDeadLetterTasksQuery struct {
	ReferenceID      *string                            `json:"reference_id,omitzero"`
	ConjoinRequestID *string                            `json:"conjoin_request_id,omitzero"`
	DateCreated      *ReadEventChannelsQueryDateCreated `json:"date_created,omitzero"`
	Cursor           *ReadBroadcastChannelsQueryCursor  `json:"cursor,omitzero"`
	Sort             map[string]string                  `json:"sort,omitzero"`
	Limit            any                                `json:"limit,omitzero"`
}

type ReadDeadLetterTasksItem struct {
	DlqEntryID           string                    `json:"dlq_entry_id"`
	TaskID               string                    `json:"task_id"`
	QueueID              string                    `json:"queue_id"`
	ConjoinAccountID     string                    `json:"conjoin_account_id"`
	ConjoinProjectID     string                    `json:"conjoin_project_id"`
	LiveMode             bool                      `json:"live_mode"`
	ReferenceID          conjoin.Nullable[string]  `json:"reference_id,omitzero"`
	ConjoinRequestID     string                    `json:"conjoin_request_id"`
	TraceSource          conjoin.Nullable[string]  `json:"trace_source,omitzero"`
	Payload              map[string]any            `json:"payload,omitzero"`
	Error                map[string]any            `json:"error,omitzero"`
	OriginalAttemptCount *float64                  `json:"original_attempt_count,omitzero"`
	ResponseStatusCode   conjoin.Nullable[float64] `json:"response_status_code,omitzero"`
	ResponseBody         conjoin.Nullable[string]  `json:"response_body,omitzero"`
	DateCreated          string                    `json:"date_created"`
}

type ReadQueueDefinitionsCountQuery = ReadEventChannelsQuery

type ReadQueueDefinitionsCountResponse = ReadBroadcastChannelsCountResponse

type UpdateQueueDefinitionRequest struct {
	Name                       *string                                                         `json:"name,omitzero"`
	TargetURL                  *string                                                         `json:"target_url,omitzero"`
	RateLimitPerMinute         conjoin.Nullable[int64]                                         `json:"rate_limit_per_minute,omitzero"`
	MaxRetries                 *int64                                                          `json:"max_retries,omitzero"`
	RetryBackoffStrategy       *string                                                         `json:"retry_backoff_strategy,omitzero"`
	RetryBackoffBaseSeconds    *int64                                                          `json:"retry_backoff_base_seconds,omitzero"`
	Priority                   *int64                                                          `json:"priority,omitzero"`
	DefaultDelaySeconds        *int64                                                          `json:"default_delay_seconds,omitzero"`
	Description                *string                                                         `json:"description,omitzero"`
	TimeoutSeconds             *int64                                                          `json:"timeout_seconds,omitzero"`
	VisibilityTimeoutSeconds   *int64                                                          `json:"visibility_timeout_seconds,omitzero"`
	MaxConcurrentDeliveries    conjoin.Nullable[int64]                                         `json:"max_concurrent_deliveries,omitzero"`
	DlqEnabled                 *bool                                                           `json:"dlq_enabled,omitzero"`
	TaskRetentionDays          *int64                                                          `json:"task_retention_days,omitzero"`
	DlqRetentionDays           *int64                                                          `json:"dlq_retention_days,omitzero"`
	Headers                    conjoin.Nullable[map[string]string]                             `json:"headers,omitzero"`
	OnSuccess                  conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_success,omitzero"`
	OnFailure                  conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_failure,omitzero"`
	StatusBroadcastEnabled     *bool                                                           `json:"status_broadcast_enabled,omitzero"`
	StatusEventsEnabled        *bool                                                           `json:"status_events_enabled,omitzero"`
	StatusBroadcastChannelID   conjoin.Nullable[string]                                        `json:"status_broadcast_channel_id,omitzero"`
	StatusEventChannelID       conjoin.Nullable[string]                                        `json:"status_event_channel_id,omitzero"`
	StatusBatchIntervalSeconds *int64                                                          `json:"status_batch_interval_seconds,omitzero"`
	StatusBatchMaxSize         *int64                                                          `json:"status_batch_max_size,omitzero"`
	ResponseForwardFields      conjoin.Nullable[[]string]                                      `json:"response_forward_fields,omitzero"`
}

type UpdateQueueDefinitionResponse = ReadQueueDefinitionsItem

type DeleteQueueDefinitionResponse = ReadQueueDefinitionsItem

type PauseQueueResponse = ReadQueueDefinitionsItem

type ResumeQueueResponse = ReadQueueDefinitionsItem

type BatchEnqueueTasksRequestDefaults struct {
	ReferenceID  *string                             `json:"reference_id,omitzero"`
	DelaySeconds *int64                              `json:"delay_seconds,omitzero"`
	ScheduledFor *EnqueueTaskRequestScheduledFor     `json:"scheduled_for,omitzero"`
	TargetURL    *string                             `json:"target_url,omitzero"`
	Headers      conjoin.Nullable[map[string]string] `json:"headers,omitzero"`
}

type BatchEnqueueTasksRequest struct {
	Defaults *BatchEnqueueTasksRequestDefaults `json:"defaults,omitzero"`
	Tasks    []EnqueueTaskRequest              `json:"tasks"`
}

type BatchEnqueueTasksResponseTasksItem struct {
	TaskID      string                   `json:"task_id"`
	ReferenceID conjoin.Nullable[string] `json:"reference_id,omitzero"`
}

type BatchEnqueueTasksResponse struct {
	TasksCreated float64                              `json:"tasks_created"`
	Tasks        []BatchEnqueueTasksResponseTasksItem `json:"tasks"`
}

type ReadQueueTasksCountQuery = ReadQueueTasksQuery

type ReadQueueTasksCountResponse = ReadBroadcastChannelsCountResponse

type ReadDeadLetterTasksCountQuery = ReadDeadLetterTasksQuery

type ReadDeadLetterTasksCountResponse = ReadBroadcastChannelsCountResponse

type ReplayDeadLetterTaskResponse = ReadQueueTasksItem

type PurgeQueueTasksRequest struct {
	Status *string `json:"status,omitzero"`
}

type PurgeQueueTasksResponse struct {
	TasksDeleted       float64 `json:"tasks_deleted"`
	DeadLettersDeleted float64 `json:"dead_letters_deleted"`
}
