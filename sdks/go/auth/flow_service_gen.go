package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type FlowsService struct {
	client *conjoin.Client
}

func (s *FlowsService) StartSignup(ctx context.Context, clientID string, body *StartSignupRequest, opts ...conjoin.CallOption) (*StartSignupResponse, error) {
	var out StartSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/sign-ups/start",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) CompleteSignup(ctx context.Context, clientID string, body *CompleteSignupRequest, opts ...conjoin.CallOption) (*CompleteSignupResponse, error) {
	var out CompleteSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/sign-ups/complete",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) ConfirmLinkSignup(ctx context.Context, clientID string, body *ConfirmLinkSignupRequest, opts ...conjoin.CallOption) (*ConfirmLinkSignupResponse, error) {
	var out ConfirmLinkSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/sign-ups/confirm-link",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) StartSignin(ctx context.Context, clientID string, body *StartSigninRequest, opts ...conjoin.CallOption) (*StartSigninResponse, error) {
	var out StartSigninResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/sign-ins/start",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) CompleteSignin(ctx context.Context, clientID string, body *CompleteSigninRequest, opts ...conjoin.CallOption) (*CompleteSigninResponse, error) {
	var out CompleteSigninResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/sign-ins/complete",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) StartPasswordReset(ctx context.Context, clientID string, body *StartPasswordResetRequest, opts ...conjoin.CallOption) (*StartPasswordResetResponse, error) {
	var out StartPasswordResetResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/password-resets/start",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) CompletePasswordReset(ctx context.Context, clientID string, body *CompletePasswordResetRequest, opts ...conjoin.CallOption) (*CompletePasswordResetResponse, error) {
	var out CompletePasswordResetResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/clients/{client_id}/password-resets/complete",
		PathParams:   []string{clientID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
