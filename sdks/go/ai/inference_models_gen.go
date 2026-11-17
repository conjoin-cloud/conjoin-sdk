package ai

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type CreateChatCompletionRequestMessagesItem struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type CreateChatCompletionRequestToolsItem struct {
	Name        string         `json:"name"`
	Description string         `json:"description"`
	Parameters  map[string]any `json:"parameters"`
}

type CreateChatCompletionRequestContextAgentic struct {
	Enabled  bool   `json:"enabled"`
	MaxSteps *int64 `json:"max_steps,omitzero"`
}

type CreateChatCompletionRequestContext struct {
	Containers []string                                   `json:"containers"`
	Modes      []string                                   `json:"modes,omitzero"`
	Agentic    *CreateChatCompletionRequestContextAgentic `json:"agentic,omitzero"`
}

type CreateChatCompletionRequest struct {
	Model          string                                    `json:"model"`
	Messages       []CreateChatCompletionRequestMessagesItem `json:"messages"`
	Temperature    *float64                                  `json:"temperature,omitzero"`
	MaxTokens      *int64                                    `json:"max_tokens,omitzero"`
	TopP           *float64                                  `json:"top_p,omitzero"`
	Stream         *bool                                     `json:"stream,omitzero"`
	Stop           []string                                  `json:"stop,omitzero"`
	Tools          []CreateChatCompletionRequestToolsItem    `json:"tools,omitzero"`
	ResponseFormat map[string]any                            `json:"response_format,omitzero"`
	Metadata       map[string]any                            `json:"metadata,omitzero"`
	Context        *CreateChatCompletionRequestContext       `json:"context,omitzero"`
}

type CreateChatCompletionResponseChoicesItemMessage struct {
	Role      string `json:"role"`
	Content   string `json:"content"`
	ToolCalls []any  `json:"tool_calls,omitzero"`
}

type CreateChatCompletionResponseChoicesItem struct {
	Index        float64                                        `json:"index"`
	Message      CreateChatCompletionResponseChoicesItemMessage `json:"message"`
	FinishReason string                                         `json:"finish_reason"`
}

type CreateChatCompletionResponseUsage struct {
	PromptTokens     float64 `json:"prompt_tokens"`
	CompletionTokens float64 `json:"completion_tokens"`
	TotalTokens      float64 `json:"total_tokens"`
}

type CreateChatCompletionResponseConjoin struct {
	CostUsd     float64 `json:"cost_usd"`
	LatencyMs   float64 `json:"latency_ms"`
	IsByok      bool    `json:"is_byok"`
	ContextUsed bool    `json:"context_used"`
}

type CreateChatCompletionResponse struct {
	ID      string                                    `json:"id"`
	Object  string                                    `json:"object"`
	Created float64                                   `json:"created"`
	Model   string                                    `json:"model"`
	Choices []CreateChatCompletionResponseChoicesItem `json:"choices"`
	Usage   CreateChatCompletionResponseUsage         `json:"usage"`
	Conjoin CreateChatCompletionResponseConjoin       `json:"_conjoin"`
}

type CreateMultiModelInferenceRequest struct {
	Models      []string                                  `json:"models"`
	Messages    []CreateChatCompletionRequestMessagesItem `json:"messages"`
	Temperature *float64                                  `json:"temperature,omitzero"`
	MaxTokens   *int64                                    `json:"max_tokens,omitzero"`
	Synthesize  *bool                                     `json:"synthesize,omitzero"`
	JudgeModel  *string                                   `json:"judge_model,omitzero"`
}

type CreateMultiModelInferenceResponseResultsItemOutput struct {
	Content      string `json:"content"`
	FinishReason string `json:"finish_reason"`
}

type CreateMultiModelInferenceResponseResultsItemTokenUsage struct {
	InputTokens  float64 `json:"input_tokens"`
	OutputTokens float64 `json:"output_tokens"`
	TotalTokens  float64 `json:"total_tokens"`
}

type CreateMultiModelInferenceResponseResultsItem struct {
	Model      string                                                 `json:"model"`
	Provider   string                                                 `json:"provider"`
	Output     CreateMultiModelInferenceResponseResultsItemOutput     `json:"output"`
	TokenUsage CreateMultiModelInferenceResponseResultsItemTokenUsage `json:"token_usage"`
	CostUsd    float64                                                `json:"cost_usd"`
	LatencyMs  float64                                                `json:"latency_ms"`
}

type CreateMultiModelInferenceResponse struct {
	RequestID   string                                                 `json:"request_id"`
	RequestType string                                                 `json:"request_type"`
	Models      []string                                               `json:"models"`
	Results     []CreateMultiModelInferenceResponseResultsItem         `json:"results"`
	Synthesis   map[string]any                                         `json:"synthesis"`
	TokenUsage  CreateMultiModelInferenceResponseResultsItemTokenUsage `json:"token_usage"`
	CostUsd     float64                                                `json:"cost_usd"`
	LatencyMs   float64                                                `json:"latency_ms"`
}

type CreateBestOfNInferenceRequest struct {
	Model             string                                    `json:"model"`
	Messages          []CreateChatCompletionRequestMessagesItem `json:"messages"`
	N                 int64                                     `json:"n"`
	Temperature       *float64                                  `json:"temperature,omitzero"`
	MaxTokens         *int64                                    `json:"max_tokens,omitzero"`
	SelectionCriteria *string                                   `json:"selection_criteria,omitzero"`
}

type CreateBestOfNInferenceResponseSelected struct {
	Content      string                                                 `json:"content"`
	FinishReason string                                                 `json:"finish_reason"`
	Model        string                                                 `json:"model"`
	Usage        CreateMultiModelInferenceResponseResultsItemTokenUsage `json:"usage"`
	CostUsd      float64                                                `json:"cost_usd"`
}

type CreateBestOfNInferenceResponseCandidatesItem struct {
	Content      string                                                 `json:"content"`
	FinishReason string                                                 `json:"finish_reason"`
	Usage        CreateMultiModelInferenceResponseResultsItemTokenUsage `json:"usage"`
	CostUsd      float64                                                `json:"cost_usd"`
	LatencyMs    float64                                                `json:"latency_ms"`
}

type CreateBestOfNInferenceResponse struct {
	RequestID   string                                                 `json:"request_id"`
	RequestType string                                                 `json:"request_type"`
	Model       string                                                 `json:"model"`
	N           float64                                                `json:"n"`
	Selected    CreateBestOfNInferenceResponseSelected                 `json:"selected"`
	Candidates  []CreateBestOfNInferenceResponseCandidatesItem         `json:"candidates"`
	TokenUsage  CreateMultiModelInferenceResponseResultsItemTokenUsage `json:"token_usage"`
	CostUsd     float64                                                `json:"cost_usd"`
	LatencyMs   float64                                                `json:"latency_ms"`
}

type ListInferenceRequestsQuery struct {
	Model            *string                          `json:"model,omitzero"`
	Status           *string                          `json:"status,omitzero"`
	RequestType      *string                          `json:"request_type,omitzero"`
	ConjoinRequestID *string                          `json:"conjoin_request_id,omitzero"`
	TraceSource      *string                          `json:"trace_source,omitzero"`
	DateCreated      *ListByokConfigsQueryDateCreated `json:"date_created,omitzero"`
	Cursor           *ListByokConfigsQueryCursor      `json:"cursor,omitzero"`
	Sort             map[string]string                `json:"sort,omitzero"`
	Limit            any                              `json:"limit,omitzero"`
}

type ListInferenceRequestsItem struct {
	RequestID        string                                                 `json:"request_id"`
	ConjoinAccountID string                                                 `json:"conjoin_account_id"`
	ConjoinProjectID string                                                 `json:"conjoin_project_id"`
	LiveMode         bool                                                   `json:"live_mode"`
	ConjoinRequestID string                                                 `json:"conjoin_request_id"`
	TraceSource      conjoin.Nullable[string]                               `json:"trace_source,omitzero"`
	Model            string                                                 `json:"model"`
	Provider         string                                                 `json:"provider"`
	RequestType      string                                                 `json:"request_type"`
	Status           string                                                 `json:"status"`
	TokenUsage       CreateMultiModelInferenceResponseResultsItemTokenUsage `json:"token_usage"`
	CostUsd          float64                                                `json:"cost_usd"`
	LatencyMs        float64                                                `json:"latency_ms"`
	StreamingEnabled bool                                                   `json:"streaming_enabled"`
	PolicyApplied    bool                                                   `json:"policy_applied"`
	IsByok           bool                                                   `json:"is_byok"`
	ContextUsed      bool                                                   `json:"context_used"`
	DateCreated      string                                                 `json:"date_created"`
	DateUpdated      string                                                 `json:"date_updated"`
}

type ListInferenceRequestsCountQuery = ListInferenceRequestsQuery

type ListInferenceRequestsCountResponse = ListByokConfigsCountResponse

type ReadInferenceRequestResponse = ListInferenceRequestsItem
