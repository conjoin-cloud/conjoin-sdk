package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type GetSettingsResponse struct {
	SettingsID             string                           `json:"settings_id"`
	ConjoinAccountID       string                           `json:"conjoin_account_id"`
	ConjoinProjectID       string                           `json:"conjoin_project_id"`
	LiveMode               bool                             `json:"live_mode"`
	SigningSecretMasked    string                           `json:"signing_secret_masked"`
	SigningSecretRotatedAt conjoin.Nullable[string]         `json:"signing_secret_rotated_at,omitzero"`
	Scheduler              conjoin.Nullable[map[string]any] `json:"scheduler,omitzero"`
	Queues                 conjoin.Nullable[map[string]any] `json:"queues,omitzero"`
	Events                 conjoin.Nullable[map[string]any] `json:"events,omitzero"`
	Pipelines              conjoin.Nullable[map[string]any] `json:"pipelines,omitzero"`
	DateCreated            string                           `json:"date_created"`
	DateUpdated            conjoin.Nullable[string]         `json:"date_updated,omitzero"`
}

type UpdateSettingsRequestScheduler struct {
	TimeoutSeconds          conjoin.Nullable[int64]             `json:"timeout_seconds,omitzero"`
	MaxRetries              conjoin.Nullable[int64]             `json:"max_retries,omitzero"`
	RetryBackoffStrategy    conjoin.Nullable[string]            `json:"retry_backoff_strategy,omitzero"`
	RetryBackoffBaseSeconds conjoin.Nullable[int64]             `json:"retry_backoff_base_seconds,omitzero"`
	DlqRetentionDays        conjoin.Nullable[int64]             `json:"dlq_retention_days,omitzero"`
	Headers                 conjoin.Nullable[map[string]string] `json:"headers,omitzero"`
}

type UpdateSettingsRequestQueues struct {
	MaxRetries              conjoin.Nullable[int64]             `json:"max_retries,omitzero"`
	RetryBackoffStrategy    conjoin.Nullable[string]            `json:"retry_backoff_strategy,omitzero"`
	RetryBackoffBaseSeconds conjoin.Nullable[int64]             `json:"retry_backoff_base_seconds,omitzero"`
	Headers                 conjoin.Nullable[map[string]string] `json:"headers,omitzero"`
}

type UpdateSettingsRequestPipelines struct {
	Headers conjoin.Nullable[map[string]string] `json:"headers,omitzero"`
}

type UpdateSettingsRequest struct {
	Scheduler *UpdateSettingsRequestScheduler `json:"scheduler,omitzero"`
	Queues    *UpdateSettingsRequestQueues    `json:"queues,omitzero"`
	Events    *UpdateSettingsRequestQueues    `json:"events,omitzero"`
	Pipelines *UpdateSettingsRequestPipelines `json:"pipelines,omitzero"`
}

type UpdateSettingsResponse = GetSettingsResponse

type RotateSigningSecretResponse = GetSettingsResponse

type RevealSigningSecretResponse struct {
	SigningSecret string `json:"signing_secret"`
}
