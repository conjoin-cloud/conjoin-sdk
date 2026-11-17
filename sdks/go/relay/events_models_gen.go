package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadEventChannelsQueryDateCreated struct {
	Equals    *string `json:"equals,omitzero"`
	NotEquals *string `json:"not_equals,omitzero"`
	Gt        *string `json:"gt,omitzero"`
	Lt        *string `json:"lt,omitzero"`
	Gte       *string `json:"gte,omitzero"`
	Lte       *string `json:"lte,omitzero"`
}

type ReadEventChannelsQuery struct {
	Status      *string                            `json:"status,omitzero"`
	ReferenceID *string                            `json:"reference_id,omitzero"`
	DateCreated *ReadEventChannelsQueryDateCreated `json:"date_created,omitzero"`
	Cursor      *ReadBroadcastChannelsQueryCursor  `json:"cursor,omitzero"`
	Sort        map[string]string                  `json:"sort,omitzero"`
	Limit       any                                `json:"limit,omitzero"`
}

type ReadEventChannelsItem struct {
	ChannelID        string                   `json:"channel_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	LiveMode         bool                     `json:"live_mode"`
	Name             string                   `json:"name"`
	RetentionHours   *float64                 `json:"retention_hours,omitzero"`
	Status           string                   `json:"status"`
	Description      conjoin.Nullable[string] `json:"description,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreateEventChannelRequest struct {
	Name           string  `json:"name"`
	ReferenceID    *string `json:"reference_id,omitzero"`
	RetentionHours *int64  `json:"retention_hours,omitzero"`
	Description    *string `json:"description,omitzero"`
}

type CreateEventChannelResponse = ReadEventChannelsItem

type ReadEventSubscriptionsQuery = ReadEventChannelsQuery

type ReadEventSubscriptionsItemFilterRulesPropertyFiltersItem struct {
	Field    string `json:"field"`
	Operator string `json:"operator"`
	Value    any    `json:"value"`
}

type ReadEventSubscriptionsItemFilterRules struct {
	EventTypes      []string                                                   `json:"event_types,omitzero"`
	PropertyFilters []ReadEventSubscriptionsItemFilterRulesPropertyFiltersItem `json:"property_filters,omitzero"`
}

type ReadEventSubscriptionsItemRetryPolicy struct {
	MaxRetries         *float64 `json:"max_retries,omitzero"`
	BackoffStrategy    *string  `json:"backoff_strategy,omitzero"`
	BackoffBaseSeconds *float64 `json:"backoff_base_seconds,omitzero"`
}

type ReadEventSubscriptionsItem struct {
	SubscriptionID   string                                 `json:"subscription_id"`
	ChannelID        string                                 `json:"channel_id"`
	ConjoinAccountID string                                 `json:"conjoin_account_id"`
	ConjoinProjectID string                                 `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string]               `json:"reference_id,omitzero"`
	LiveMode         bool                                   `json:"live_mode"`
	EndpointURL      string                                 `json:"endpoint_url"`
	FilterRules      *ReadEventSubscriptionsItemFilterRules `json:"filter_rules,omitzero"`
	RetryPolicy      *ReadEventSubscriptionsItemRetryPolicy `json:"retry_policy,omitzero"`
	Status           string                                 `json:"status"`
	PausedReason     conjoin.Nullable[string]               `json:"paused_reason,omitzero"`
	Description      conjoin.Nullable[string]               `json:"description,omitzero"`
	Headers          conjoin.Nullable[map[string]string]    `json:"headers,omitzero"`
	OnSuccess        conjoin.Nullable[[]map[string]any]     `json:"on_success,omitzero"`
	OnFailure        conjoin.Nullable[[]map[string]any]     `json:"on_failure,omitzero"`
	DateCreated      string                                 `json:"date_created"`
	DateUpdated      string                                 `json:"date_updated"`
}

type CreateEventSubscriptionRequestFilterRulesPropertyFiltersItem struct {
	Field    *string `json:"field,omitzero"`
	Operator *string `json:"operator,omitzero"`
	Value    any     `json:"value,omitzero"`
}

type CreateEventSubscriptionRequestFilterRules struct {
	EventTypes      []string                                                       `json:"event_types,omitzero"`
	PropertyFilters []CreateEventSubscriptionRequestFilterRulesPropertyFiltersItem `json:"property_filters,omitzero"`
}

type CreateEventSubscriptionRequestRetryPolicy struct {
	MaxRetries         *int64  `json:"max_retries,omitzero"`
	BackoffStrategy    *string `json:"backoff_strategy,omitzero"`
	BackoffBaseSeconds *int64  `json:"backoff_base_seconds,omitzero"`
}

type CreateEventSubscriptionRequestOnSuccessItem struct {
	Type       *string           `json:"type,omitzero"`
	ChannelID  *string           `json:"channel_id,omitzero"`
	EventType  *string           `json:"event_type,omitzero"`
	QueueID    *string           `json:"queue_id,omitzero"`
	PipelineID *string           `json:"pipeline_id,omitzero"`
	URL        *string           `json:"url,omitzero"`
	Headers    map[string]string `json:"headers,omitzero"`
}

type CreateEventSubscriptionRequest struct {
	EndpointURL string                                                          `json:"endpoint_url"`
	ReferenceID *string                                                         `json:"reference_id,omitzero"`
	FilterRules *CreateEventSubscriptionRequestFilterRules                      `json:"filter_rules,omitzero"`
	RetryPolicy *CreateEventSubscriptionRequestRetryPolicy                      `json:"retry_policy,omitzero"`
	Description *string                                                         `json:"description,omitzero"`
	Headers     conjoin.Nullable[map[string]string]                             `json:"headers,omitzero"`
	OnSuccess   conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_success,omitzero"`
	OnFailure   conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_failure,omitzero"`
}

type CreateEventSubscriptionResponse = ReadEventSubscriptionsItem

type ReadEventsQuery struct {
	ReferenceID *string                           `json:"reference_id,omitzero"`
	Cursor      *ReadBroadcastChannelsQueryCursor `json:"cursor,omitzero"`
	Sort        map[string]string                 `json:"sort,omitzero"`
	Limit       any                               `json:"limit,omitzero"`
}

type ReadEventsItem struct {
	EventID          string                   `json:"event_id"`
	ChannelID        string                   `json:"channel_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string] `json:"reference_id,omitzero"`
	LiveMode         bool                     `json:"live_mode"`
	EventType        string                   `json:"event_type"`
	Payload          map[string]any           `json:"payload,omitzero"`
	Status           string                   `json:"status"`
	DateCreated      string                   `json:"date_created"`
}

type ReadEventChannelsCountQuery = ReadEventChannelsQuery

type ReadEventChannelsCountResponse = ReadBroadcastChannelsCountResponse

type UpdateEventChannelRequest struct {
	Name           *string `json:"name,omitzero"`
	RetentionHours *int64  `json:"retention_hours,omitzero"`
	Description    *string `json:"description,omitzero"`
}

type UpdateEventChannelResponse = ReadEventChannelsItem

type DeleteEventChannelResponse = ReadEventChannelsItem

type ReadEventSubscriptionsCountQuery = ReadEventChannelsQuery

type ReadEventSubscriptionsCountResponse = ReadBroadcastChannelsCountResponse

type UpdateEventSubscriptionRequest struct {
	EndpointURL *string                                                         `json:"endpoint_url,omitzero"`
	FilterRules *CreateEventSubscriptionRequestFilterRules                      `json:"filter_rules,omitzero"`
	RetryPolicy *CreateEventSubscriptionRequestRetryPolicy                      `json:"retry_policy,omitzero"`
	Description *string                                                         `json:"description,omitzero"`
	Headers     conjoin.Nullable[map[string]string]                             `json:"headers,omitzero"`
	OnSuccess   conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_success,omitzero"`
	OnFailure   conjoin.Nullable[[]CreateEventSubscriptionRequestOnSuccessItem] `json:"on_failure,omitzero"`
}

type UpdateEventSubscriptionResponse = ReadEventSubscriptionsItem

type DeleteEventSubscriptionResponseResponse struct {
	Type    string `json:"type"`
	Code    int64  `json:"code"`
	Message string `json:"message"`
}

type DeleteEventSubscriptionResponse struct {
	Response *DeleteEventSubscriptionResponseResponse `json:"response,omitzero"`
}

type PauseEventSubscriptionResponse = ReadEventSubscriptionsItem

type ResumeEventSubscriptionResponse = ReadEventSubscriptionsItem

type PublishEventRequest struct {
	EventType   string         `json:"event_type"`
	ReferenceID *string        `json:"reference_id,omitzero"`
	Payload     map[string]any `json:"payload,omitzero"`
}

type PublishEventResponse = ReadEventsItem

type ReadEventsCountQuery = ReadEventsQuery

type ReadEventsCountResponse = ReadBroadcastChannelsCountResponse

type ReplayEventsRequest struct {
	FromTimestamp  *string `json:"from_timestamp,omitzero"`
	ToTimestamp    *string `json:"to_timestamp,omitzero"`
	SubscriptionID *string `json:"subscription_id,omitzero"`
}

type ReplayEventsResponse = DeleteEventSubscriptionResponse
