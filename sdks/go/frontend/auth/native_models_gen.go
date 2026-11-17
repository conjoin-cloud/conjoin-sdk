package auth

type StartNativeSignupRequest = StartSignupRequest

type StartNativeSignupResponseClientHandle struct {
	ClientID    string `json:"client_id"`
	ReferenceID string `json:"reference_id"`
}

type StartNativeSignupResponse struct {
	Status             *string                                `json:"status,omitzero"`
	AccountID          *string                                `json:"account_id,omitzero"`
	SessionID          *string                                `json:"session_id,omitzero"`
	State              *string                                `json:"state,omitzero"`
	VerificationMethod *string                                `json:"verification_method,omitzero"`
	RedirectURL        *string                                `json:"redirect_url,omitzero"`
	MFA                *StartSignupResponseMFA                `json:"mfa,omitzero"`
	Verification       map[string]any                         `json:"verification,omitzero"`
	TrustedDeviceToken *string                                `json:"trusted_device_token,omitzero"`
	StepUp             *StartSignupResponseStepUp             `json:"step_up,omitzero"`
	ClientHandle       *StartNativeSignupResponseClientHandle `json:"client_handle,omitzero"`
}

type CompleteNativeSignupRequest = CompleteSignupRequest

type CompleteNativeSignupResponse = StartNativeSignupResponse

type ConfirmLinkNativeSignupRequest = ConfirmLinkSignupRequest

type ConfirmLinkNativeSignupResponse = StartNativeSignupResponse

type StartNativeSigninRequest = StartSigninRequest

type StartNativeSigninResponse = StartNativeSignupResponse

type CompleteNativeSigninRequest = CompleteSigninRequest

type CompleteNativeSigninResponse = StartNativeSignupResponse

type ProcessNativeTokenMintResponse struct {
	AccessToken  string  `json:"access_token"`
	TokenType    string  `json:"token_type"`
	ExpiresIn    float64 `json:"expires_in"`
	RefreshToken string  `json:"refresh_token"`
	SessionID    string  `json:"session_id"`
	AccountID    string  `json:"account_id"`
}

type RefreshNativeSessionRequest struct {
	RefreshToken *string `json:"refresh_token,omitzero"`
}

type RefreshNativeSessionResponse = ProcessNativeTokenMintResponse

type ProcessNativeLogoutResponse = ProcessLogoutResponse
