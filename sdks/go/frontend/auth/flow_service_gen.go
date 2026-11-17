package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type FlowsService struct {
	client *conjoin.Client
}

func (s *FlowsService) StartSignup(ctx context.Context, body *StartSignupRequest, opts ...conjoin.CallOption) (*StartSignupResponse, error) {
	var out StartSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/sign-ups/start",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) CompleteSignup(ctx context.Context, body *CompleteSignupRequest, opts ...conjoin.CallOption) (*CompleteSignupResponse, error) {
	var out CompleteSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/sign-ups/complete",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) ConfirmLinkSignup(ctx context.Context, body *ConfirmLinkSignupRequest, opts ...conjoin.CallOption) (*ConfirmLinkSignupResponse, error) {
	var out ConfirmLinkSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/sign-ups/confirm-link",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) StartSignin(ctx context.Context, body *StartSigninRequest, opts ...conjoin.CallOption) (*StartSigninResponse, error) {
	var out StartSigninResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/sign-ins/start",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) CompleteSignin(ctx context.Context, body *CompleteSigninRequest, opts ...conjoin.CallOption) (*CompleteSigninResponse, error) {
	var out CompleteSigninResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/sign-ins/complete",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) StartPasswordReset(ctx context.Context, body *StartPasswordResetRequest, opts ...conjoin.CallOption) (*StartPasswordResetResponse, error) {
	var out StartPasswordResetResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/password-resets/start",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FlowsService) CompletePasswordReset(ctx context.Context, body *CompletePasswordResetRequest, opts ...conjoin.CallOption) (*CompletePasswordResetResponse, error) {
	var out CompletePasswordResetResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/password-resets/complete",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
