package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type CredentialsService struct {
	client *conjoin.Client
}

func (s *CredentialsService) UpdateApiKey(ctx context.Context, accountID string, credentialID string, body *UpdateApiKeyCredentialRequest, opts ...conjoin.CallOption) (*UpdateApiKeyCredentialResponse, error) {
	var out UpdateApiKeyCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/accounts/{account_id}/credentials/{credential_id}",
		PathParams:   []string{accountID, credentialID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) CreatePassword(ctx context.Context, accountID string, body *CreatePasswordCredentialRequest, opts ...conjoin.CallOption) (*CreatePasswordCredentialResponse, error) {
	var out CreatePasswordCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/password-credentials",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) RotatePassword(ctx context.Context, accountID string, body *RotatePasswordCredentialRequest, opts ...conjoin.CallOption) (*RotatePasswordCredentialResponse, error) {
	var out RotatePasswordCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/password-credentials/rotate",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) EnrollTotp(ctx context.Context, accountID string, body *EnrollTotpCredentialRequest, opts ...conjoin.CallOption) (*EnrollTotpCredentialResponse, error) {
	var out EnrollTotpCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/totp-credentials/enroll",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) ActivateTotp(ctx context.Context, accountID string, body *ActivateTotpCredentialRequest, opts ...conjoin.CallOption) (*ActivateTotpCredentialResponse, error) {
	var out ActivateTotpCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/totp-credentials/activate",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) RotateTotpRecoveryCodes(ctx context.Context, accountID string, body *RotateTotpRecoveryCodesRequest, opts ...conjoin.CallOption) (*RotateTotpRecoveryCodesResponse, error) {
	var out RotateTotpRecoveryCodesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/totp-recovery-codes/rotate",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) ConsumeTotpRecoveryCode(ctx context.Context, accountID string, body *ConsumeTotpRecoveryCodeRequest, opts ...conjoin.CallOption) (*ConsumeTotpRecoveryCodeResponse, error) {
	var out ConsumeTotpRecoveryCodeResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/totp-recovery-codes/consume",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) EnrollSmsMfa(ctx context.Context, accountID string, body *EnrollSmsMfaCredentialRequest, opts ...conjoin.CallOption) (*EnrollSmsMfaCredentialResponse, error) {
	var out EnrollSmsMfaCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/sms-credentials/enroll",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) SendSmsMfaActivationCode(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*SendSmsMfaActivationCodeResponse, error) {
	var out SendSmsMfaActivationCodeResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/sms-credentials/send-activation-code",
		PathParams:            []string{accountID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) ActivateSmsMfa(ctx context.Context, accountID string, body *ActivateSmsMfaCredentialRequest, opts ...conjoin.CallOption) (*ActivateSmsMfaCredentialResponse, error) {
	var out ActivateSmsMfaCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/sms-credentials/activate",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) VerifySmsMfa(ctx context.Context, accountID string, body *VerifySmsMfaCredentialRequest, opts ...conjoin.CallOption) (*VerifySmsMfaCredentialResponse, error) {
	var out VerifySmsMfaCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/sms-credentials/verify",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) SendSmsMfaChallenge(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*SendSmsMfaChallengeResponse, error) {
	var out SendSmsMfaChallengeResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/sms-credentials/send-challenge",
		PathParams:            []string{accountID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) ReadApiKeyUsage(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*ReadApiKeyUsageResponse, error) {
	var out ReadApiKeyUsageResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/api-key-credentials/usage-stats",
		PathParams: []string{accountID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) IssueApiKey(ctx context.Context, accountID string, body *IssueApiKeyCredentialRequest, opts ...conjoin.CallOption) (*IssueApiKeyCredentialResponse, error) {
	var out IssueApiKeyCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/api-key-credentials",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) RotateApiKey(ctx context.Context, accountID string, credentialID string, body *RotateApiKeyCredentialRequest, opts ...conjoin.CallOption) (*RotateApiKeyCredentialResponse, error) {
	var out RotateApiKeyCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/credentials/{credential_id}/rotate",
		PathParams:            []string{accountID, credentialID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) RevokeApiKey(ctx context.Context, accountID string, credentialID string, body *RevokeApiKeyCredentialRequest, opts ...conjoin.CallOption) (*RevokeApiKeyCredentialResponse, error) {
	var out RevokeApiKeyCredentialResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/credentials/{credential_id}/revoke",
		PathParams:            []string{accountID, credentialID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) StartPasskeyRegistration(ctx context.Context, accountID string, body *StartPasskeyRegistrationRequest, opts ...conjoin.CallOption) (*StartPasskeyRegistrationResponse, error) {
	var out StartPasskeyRegistrationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/passkey-registrations/start",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) VerifyPasskeyRegistration(ctx context.Context, accountID string, body *VerifyPasskeyRegistrationRequest, opts ...conjoin.CallOption) (*VerifyPasskeyRegistrationResponse, error) {
	var out VerifyPasskeyRegistrationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/passkey-registrations/verify",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) StartPasskeyentication(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*StartPasskeyenticationResponse, error) {
	var out StartPasskeyenticationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/passkey-authentications/start",
		PathParams:            []string{accountID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CredentialsService) VerifyPasskeyentication(ctx context.Context, accountID string, body *VerifyPasskeyenticationRequest, opts ...conjoin.CallOption) (*VerifyPasskeyenticationResponse, error) {
	var out VerifyPasskeyenticationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/passkey-authentications/verify",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
