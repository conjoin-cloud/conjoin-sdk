package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type NativesService struct {
	client *conjoin.Client
}

func (s *NativesService) StartSignup(ctx context.Context, body *StartNativeSignupRequest, opts ...conjoin.CallOption) (*StartNativeSignupResponse, error) {
	var out StartNativeSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/native/sign-ups/start",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *NativesService) CompleteSignup(ctx context.Context, body *CompleteNativeSignupRequest, opts ...conjoin.CallOption) (*CompleteNativeSignupResponse, error) {
	var out CompleteNativeSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/native/sign-ups/complete",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *NativesService) ConfirmLinkSignup(ctx context.Context, body *ConfirmLinkNativeSignupRequest, opts ...conjoin.CallOption) (*ConfirmLinkNativeSignupResponse, error) {
	var out ConfirmLinkNativeSignupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/native/sign-ups/confirm-link",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *NativesService) StartSignin(ctx context.Context, body *StartNativeSigninRequest, opts ...conjoin.CallOption) (*StartNativeSigninResponse, error) {
	var out StartNativeSigninResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/native/sign-ins/start",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *NativesService) CompleteSignin(ctx context.Context, body *CompleteNativeSigninRequest, opts ...conjoin.CallOption) (*CompleteNativeSigninResponse, error) {
	var out CompleteNativeSigninResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/native/sign-ins/complete",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *NativesService) ProcessTokenMint(ctx context.Context, opts ...conjoin.CallOption) (*ProcessNativeTokenMintResponse, error) {
	var out ProcessNativeTokenMintResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "POST",
		Path:   "auth/client/native/tokens",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *NativesService) RefreshSession(ctx context.Context, body *RefreshNativeSessionRequest, opts ...conjoin.CallOption) (*RefreshNativeSessionResponse, error) {
	var out RefreshNativeSessionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/native/tokens/refresh",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *NativesService) ProcessLogout(ctx context.Context, opts ...conjoin.CallOption) (*ProcessNativeLogoutResponse, error) {
	var out ProcessNativeLogoutResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "POST",
		Path:   "auth/client/native/logout",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
