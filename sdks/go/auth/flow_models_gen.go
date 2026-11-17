package auth

type StartSignupRequest struct {
	Email              *string `json:"email,omitzero"`
	Phone              *string `json:"phone,omitzero"`
	ProviderKey        *string `json:"provider_key,omitzero"`
	VerificationOption *string `json:"verification_option,omitzero"`
	Password           *string `json:"password,omitzero"`
}

type StartSignupResponseMFA struct {
	Method string `json:"method"`
}

type StartSignupResponseStepUp struct {
	AvailableMethods []string `json:"available_methods"`
	ChallengeID      string   `json:"challenge_id"`
}

type StartSignupResponse struct {
	Status             *string                    `json:"status,omitzero"`
	AccountID          *string                    `json:"account_id,omitzero"`
	SessionID          *string                    `json:"session_id,omitzero"`
	State              *string                    `json:"state,omitzero"`
	VerificationMethod *string                    `json:"verification_method,omitzero"`
	RedirectURL        *string                    `json:"redirect_url,omitzero"`
	MFA                *StartSignupResponseMFA    `json:"mfa,omitzero"`
	Verification       map[string]any             `json:"verification,omitzero"`
	TrustedDeviceToken *string                    `json:"trusted_device_token,omitzero"`
	StepUp             *StartSignupResponseStepUp `json:"step_up,omitzero"`
}

type CompleteSignupRequestVerificationResult struct {
	PinCode        *string `json:"pin_code,omitzero"`
	MagicLinkToken *string `json:"magic_link_token,omitzero"`
	OauthToken     *string `json:"oauth_token,omitzero"`
}

type CompleteSignupRequest struct {
	VerificationResult CompleteSignupRequestVerificationResult `json:"verification_result"`
	Password           *string                                 `json:"password,omitzero"`
}

type CompleteSignupResponse = StartSignupResponse

type ConfirmLinkSignupRequestStepUp struct {
	ChallengeID       string  `json:"challenge_id"`
	Method            string  `json:"method"`
	Code              *string `json:"code,omitzero"`
	Password          *string `json:"password,omitzero"`
	AssertionResponse any     `json:"assertion_response,omitzero"`
}

type ConfirmLinkSignupRequest struct {
	Confirm bool                            `json:"confirm"`
	StepUp  *ConfirmLinkSignupRequestStepUp `json:"step_up,omitzero"`
}

type ConfirmLinkSignupResponse = StartSignupResponse

type StartSigninRequest struct {
	Email              *string `json:"email,omitzero"`
	Phone              *string `json:"phone,omitzero"`
	ProviderKey        *string `json:"provider_key,omitzero"`
	VerificationOption *string `json:"verification_option,omitzero"`
	Password           *string `json:"password,omitzero"`
	TrustedDeviceToken *string `json:"trusted_device_token,omitzero"`
	RememberDevice     *bool   `json:"remember_device,omitzero"`
}

type StartSigninResponse = StartSignupResponse

type CompleteSigninRequestMFA struct {
	Method            *string `json:"method,omitzero"`
	TotpCode          *string `json:"totp_code,omitzero"`
	PhoneCode         *string `json:"phone_code,omitzero"`
	AssertionResponse any     `json:"assertion_response,omitzero"`
	CredentialID      *string `json:"credential_id,omitzero"`
}

type CompleteSigninRequest struct {
	VerificationResult CompleteSignupRequestVerificationResult `json:"verification_result"`
	MFA                *CompleteSigninRequestMFA               `json:"mfa,omitzero"`
	TrustedDeviceToken *string                                 `json:"trusted_device_token,omitzero"`
	RememberDevice     *bool                                   `json:"remember_device,omitzero"`
}

type CompleteSigninResponse = StartSignupResponse

type StartPasswordResetRequest struct {
	Email string  `json:"email"`
	Phone *string `json:"phone,omitzero"`
}

type StartPasswordResetResponse = StartSignupResponse

type CompletePasswordResetRequest struct {
	ResetToken  string `json:"reset_token"`
	NewPassword string `json:"new_password"`
}

type CompletePasswordResetResponse = StartSignupResponse
