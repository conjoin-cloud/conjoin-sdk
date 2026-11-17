package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type ReadPipelineDefinitionsQuery = ReadEventChannelsQuery

type ReadPipelineDefinitionsItem struct {
	PipelineID       string                                 `json:"pipeline_id"`
	ConjoinAccountID string                                 `json:"conjoin_account_id"`
	ConjoinProjectID string                                 `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string]               `json:"reference_id,omitzero"`
	LiveMode         bool                                   `json:"live_mode"`
	Name             string                                 `json:"name"`
	EndpointURL      string                                 `json:"endpoint_url"`
	RetryPolicy      *ReadEventSubscriptionsItemRetryPolicy `json:"retry_policy,omitzero"`
	TimeoutSeconds   conjoin.Nullable[float64]              `json:"timeout_seconds,omitzero"`
	Status           string                                 `json:"status"`
	Description      conjoin.Nullable[string]               `json:"description,omitzero"`
	Metadata         map[string]any                         `json:"metadata,omitzero"`
	DateCreated      string                                 `json:"date_created"`
	DateUpdated      string                                 `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string]               `json:"date_deleted,omitzero"`
}

type CreatePipelineDefinitionRequest struct {
	Name           string                                     `json:"name"`
	ReferenceID    *string                                    `json:"reference_id,omitzero"`
	EndpointURL    string                                     `json:"endpoint_url"`
	RetryPolicy    *CreateEventSubscriptionRequestRetryPolicy `json:"retry_policy,omitzero"`
	TimeoutSeconds *int64                                     `json:"timeout_seconds,omitzero"`
	Description    *string                                    `json:"description,omitzero"`
}

type CreatePipelineDefinitionResponse = ReadPipelineDefinitionsItem

type ReadPipelineDefinitionsCountQuery = ReadEventChannelsQuery

type ReadPipelineDefinitionsCountResponse = ReadBroadcastChannelsCountResponse

type UpdatePipelineDefinitionRequest struct {
	Name           *string                                    `json:"name,omitzero"`
	EndpointURL    *string                                    `json:"endpoint_url,omitzero"`
	RetryPolicy    *CreateEventSubscriptionRequestRetryPolicy `json:"retry_policy,omitzero"`
	TimeoutSeconds *int64                                     `json:"timeout_seconds,omitzero"`
	Description    *string                                    `json:"description,omitzero"`
}

type UpdatePipelineDefinitionResponse = ReadPipelineDefinitionsItem

type DeletePipelineDefinitionResponse = ReadPipelineDefinitionsItem

type TriggerPipelineRunRequest struct {
	ReferenceID *string        `json:"reference_id,omitzero"`
	Payload     map[string]any `json:"payload,omitzero"`
}

type TriggerPipelineRunResponse struct {
	RunID            string                           `json:"run_id"`
	PipelineID       string                           `json:"pipeline_id"`
	ConjoinAccountID string                           `json:"conjoin_account_id"`
	ConjoinProjectID string                           `json:"conjoin_project_id"`
	ReferenceID      conjoin.Nullable[string]         `json:"reference_id,omitzero"`
	LiveMode         bool                             `json:"live_mode"`
	ConjoinRequestID string                           `json:"conjoin_request_id"`
	TraceSource      conjoin.Nullable[string]         `json:"trace_source,omitzero"`
	Status           string                           `json:"status"`
	Payload          map[string]any                   `json:"payload,omitzero"`
	Steps            []map[string]any                 `json:"steps,omitzero"`
	StartedAt        conjoin.Nullable[string]         `json:"started_at,omitzero"`
	CompletedAt      conjoin.Nullable[string]         `json:"completed_at,omitzero"`
	Error            conjoin.Nullable[map[string]any] `json:"error,omitzero"`
	DateCreated      string                           `json:"date_created"`
	DateUpdated      string                           `json:"date_updated"`
}

type ReadPipelineRunsQuery struct {
	PipelineID       *string                           `json:"pipeline_id,omitzero"`
	Status           *string                           `json:"status,omitzero"`
	ReferenceID      *string                           `json:"reference_id,omitzero"`
	ConjoinRequestID *string                           `json:"conjoin_request_id,omitzero"`
	Cursor           *ReadBroadcastChannelsQueryCursor `json:"cursor,omitzero"`
	Sort             map[string]string                 `json:"sort,omitzero"`
	Limit            any                               `json:"limit,omitzero"`
}

type ReadPipelineRunsItem = TriggerPipelineRunResponse

type ReadPipelineRunsCountQuery = ReadPipelineRunsQuery

type ReadPipelineRunsCountResponse = ReadBroadcastChannelsCountResponse

type ReadPipelineRunResponse = TriggerPipelineRunResponse

type CancelPipelineRunResponse = TriggerPipelineRunResponse

type ApprovePipelineGateRequest struct {
	ApproverData map[string]any `json:"approver_data,omitzero"`
}

type ApprovePipelineGateResponse struct {
	StepID           string                           `json:"step_id"`
	RunID            string                           `json:"run_id"`
	PipelineID       string                           `json:"pipeline_id"`
	ConjoinAccountID string                           `json:"conjoin_account_id"`
	ConjoinProjectID string                           `json:"conjoin_project_id"`
	LiveMode         bool                             `json:"live_mode"`
	StepIndex        float64                          `json:"step_index"`
	StepName         string                           `json:"step_name"`
	StepType         string                           `json:"step_type"`
	Status           string                           `json:"status"`
	Input            any                              `json:"input,omitzero"`
	Output           any                              `json:"output,omitzero"`
	AttemptCount     float64                          `json:"attempt_count"`
	Error            conjoin.Nullable[string]         `json:"error,omitzero"`
	StartedAt        conjoin.Nullable[string]         `json:"started_at,omitzero"`
	CompletedAt      conjoin.Nullable[string]         `json:"completed_at,omitzero"`
	GateMetadata     conjoin.Nullable[map[string]any] `json:"gate_metadata,omitzero"`
	DateCreated      string                           `json:"date_created"`
	DateUpdated      string                           `json:"date_updated"`
}

type RejectPipelineGateRequest struct {
	Reason *string `json:"reason,omitzero"`
}

type RejectPipelineGateResponse = ApprovePipelineGateResponse
