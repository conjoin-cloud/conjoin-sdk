package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type AccountRecoveriesService struct {
	client *conjoin.Client
}

func (s *AccountRecoveriesService) StartRecovery(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*StartRecoveryResponse, error) {
	var out StartRecoveryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/recoveries/start",
		PathParams:            []string{accountID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AccountRecoveriesService) VerifyRecovery(ctx context.Context, accountID string, body *VerifyRecoveryRequest, opts ...conjoin.CallOption) (*VerifyRecoveryResponse, error) {
	var out VerifyRecoveryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/recoveries/verify",
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

func (s *AccountRecoveriesService) CompleteRecovery(ctx context.Context, accountID string, body *CompleteRecoveryRequest, opts ...conjoin.CallOption) (*CompleteRecoveryResponse, error) {
	var out CompleteRecoveryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/recoveries/complete",
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

func (s *AccountRecoveriesService) AdminResetAccount(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*AdminResetAccountResponse, error) {
	var out AdminResetAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/reset-mfa",
		PathParams:            []string{accountID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
