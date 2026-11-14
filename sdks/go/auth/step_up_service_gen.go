package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type StepUpsService struct {
	client *conjoin.Client
}

func (s *StepUpsService) Request(ctx context.Context, accountID string, body *RequestStepUpRequest, opts ...conjoin.CallOption) (*RequestStepUpResponse, error) {
	var out RequestStepUpResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/step-ups/start",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *StepUpsService) Verify(ctx context.Context, accountID string, body *VerifyStepUpRequest, opts ...conjoin.CallOption) (*VerifyStepUpResponse, error) {
	var out VerifyStepUpResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/step-ups/verify",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *StepUpsService) Validate(ctx context.Context, accountID string, body *ValidateStepUpRequest, opts ...conjoin.CallOption) (*ValidateStepUpResponse, error) {
	var out ValidateStepUpResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/step-ups/validate",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
