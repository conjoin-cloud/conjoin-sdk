package auth

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type UpdateApiKeyCredentialRequestRateLimit struct {
	MaxRequests   int64 `json:"max_requests"`
	WindowSeconds int64 `json:"window_seconds"`
}

type UpdateApiKeyCredentialRequest struct {
	AllowedIps    []string                                                 `json:"allowed_ips,omitzero"`
	Label         conjoin.Nullable[string]                                 `json:"label,omitzero"`
	Environment   conjoin.Nullable[string]                                 `json:"environment,omitzero"`
	TokenMetadata conjoin.Nullable[map[string]any]                         `json:"token_metadata,omitzero"`
	RateLimit     conjoin.Nullable[UpdateApiKeyCredentialRequestRateLimit] `json:"rate_limit,omitzero"`
}

type UpdateApiKeyCredentialResponse struct {
	CredentialID     string                   `json:"credential_id"`
	AccountID        string                   `json:"account_id"`
	Kind             string                   `json:"kind"`
	AppID            string                   `json:"app_id"`
	ConjoinAccountID string                   `json:"conjoin_account_id"`
	ConjoinProjectID string                   `json:"conjoin_project_id"`
	LiveMode         bool                     `json:"live_mode"`
	Data             map[string]any           `json:"data,omitzero"`
	Metadata         map[string]any           `json:"metadata,omitzero"`
	DateCreated      string                   `json:"date_created"`
	DateUpdated      string                   `json:"date_updated"`
	DateDeleted      conjoin.Nullable[string] `json:"date_deleted,omitzero"`
}

type CreatePasswordCredentialRequest struct {
	Password string `json:"password"`
}

type CreatePasswordCredentialResponse = UpdateApiKeyCredentialResponse

type RotatePasswordCredentialRequest struct {
	NewPassword     string  `json:"new_password"`
	CurrentPassword *string `json:"current_password,omitzero"`
	SessionID       *string `json:"session_id,omitzero"`
	StepUpToken     *string `json:"step_up_token,omitzero"`
}

type RotatePasswordCredentialResponse = UpdateApiKeyCredentialResponse

type EnrollTotpCredentialRequest struct {
	RecoveryCodeCount  *int64  `json:"recovery_code_count,omitzero"`
	RecoveryCodeLength *int64  `json:"recovery_code_length,omitzero"`
	Issuer             *string `json:"issuer,omitzero"`
	AccountLabel       *string `json:"account_label,omitzero"`
	SessionID          *string `json:"session_id,omitzero"`
	StepUpToken        *string `json:"step_up_token,omitzero"`
}

type EnrollTotpCredentialResponse = UpdateApiKeyCredentialResponse

type ActivateTotpCredentialRequest = VerifyCredentialMfaTotpRequest

type ActivateTotpCredentialResponse = UpdateApiKeyCredentialResponse

type RotateTotpRecoveryCodesRequest struct {
	RecoveryCodeCount  *int64  `json:"recovery_code_count,omitzero"`
	RecoveryCodeLength *int64  `json:"recovery_code_length,omitzero"`
	SessionID          *string `json:"session_id,omitzero"`
	StepUpToken        *string `json:"step_up_token,omitzero"`
}

type RotateTotpRecoveryCodesResponse = UpdateApiKeyCredentialResponse

type ConsumeTotpRecoveryCodeRequest = VerifyCredentialMfaTotpRequest

type ConsumeTotpRecoveryCodeResponse = UpdateApiKeyCredentialResponse

type EnrollSmsMfaCredentialRequest struct {
	Phone       string  `json:"phone"`
	SessionID   *string `json:"session_id,omitzero"`
	StepUpToken *string `json:"step_up_token,omitzero"`
}

type EnrollSmsMfaCredentialResponse struct {
	CredentialID string `json:"credential_id"`
}

type SendSmsMfaActivationCodeResponse = UpdateApiKeyCredentialResponse

type ActivateSmsMfaCredentialRequest = VerifyCredentialMfaTotpRequest

type ActivateSmsMfaCredentialResponse = UpdateApiKeyCredentialResponse

type VerifySmsMfaCredentialRequest = VerifyCredentialMfaTotpRequest

type VerifySmsMfaCredentialResponse = UpdateApiKeyCredentialResponse

type SendSmsMfaChallengeResponse = UpdateApiKeyCredentialResponse

type ReadApiKeyUsageResponse = UpdateApiKeyCredentialResponse

type IssueApiKeyCredentialRequest struct {
	Prefix        *string                                                  `json:"prefix,omitzero"`
	Scopes        []string                                                 `json:"scopes,omitzero"`
	ExpireAt      *string                                                  `json:"expire_at,omitzero"`
	TestMode      *bool                                                    `json:"test_mode,omitzero"`
	AllowedIps    []string                                                 `json:"allowed_ips,omitzero"`
	Label         conjoin.Nullable[string]                                 `json:"label,omitzero"`
	Environment   conjoin.Nullable[string]                                 `json:"environment,omitzero"`
	TokenMetadata conjoin.Nullable[map[string]any]                         `json:"token_metadata,omitzero"`
	RateLimit     conjoin.Nullable[UpdateApiKeyCredentialRequestRateLimit] `json:"rate_limit,omitzero"`
	SessionID     *string                                                  `json:"session_id,omitzero"`
	StepUpToken   *string                                                  `json:"step_up_token,omitzero"`
}

type IssueApiKeyCredentialResponse struct {
	APIKey     string                         `json:"api_key"`
	Credential UpdateApiKeyCredentialResponse `json:"credential"`
}

type RotateApiKeyCredentialRequest struct {
	Prefix      *string  `json:"prefix,omitzero"`
	Scopes      []string `json:"scopes,omitzero"`
	ExpireAt    *string  `json:"expire_at,omitzero"`
	TestMode    *bool    `json:"test_mode,omitzero"`
	OverlapDays *int64   `json:"overlap_days,omitzero"`
	SessionID   *string  `json:"session_id,omitzero"`
	StepUpToken *string  `json:"step_up_token,omitzero"`
}

type RotateApiKeyCredentialResponse struct {
	APIKey       string `json:"api_key"`
	CredentialID string `json:"credential_id"`
}

type RevokeApiKeyCredentialRequest struct {
	SessionID   *string `json:"session_id,omitzero"`
	StepUpToken *string `json:"step_up_token,omitzero"`
}

type RevokeApiKeyCredentialResponse = UpdateApiKeyCredentialResponse

type StartPasskeyRegistrationRequest struct {
	UserHandle  string  `json:"user_handle"`
	SessionID   *string `json:"session_id,omitzero"`
	StepUpToken *string `json:"step_up_token,omitzero"`
}

type StartPasskeyRegistrationResponse = UpdateApiKeyCredentialResponse

type VerifyPasskeyRegistrationRequest struct {
	AttestationResponse any     `json:"attestation_response"`
	SessionID           *string `json:"session_id,omitzero"`
	StepUpToken         *string `json:"step_up_token,omitzero"`
}

type VerifyPasskeyRegistrationResponse = EnrollSmsMfaCredentialResponse

type StartPasskeyenticationResponse = UpdateApiKeyCredentialResponse

type VerifyPasskeyenticationRequest struct {
	AssertionResponse any `json:"assertion_response"`
}

type VerifyPasskeyenticationResponse = UpdateApiKeyCredentialResponse
