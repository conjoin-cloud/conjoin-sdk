package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type VerificationsService struct {
	client *conjoin.Client
}

func (s *VerificationsService) ListMessages(ctx context.Context, query *ListVerificationMessagesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListVerificationMessagesItem], error) {
	return conjoin.List[ListVerificationMessagesItem](ctx, s.client, conjoin.Operation{
		Method:        "GET",
		Path:          "messaging/verifications/",
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *VerificationsService) Create(ctx context.Context, body *CreateVerificationRequest, opts ...conjoin.CallOption) (*CreateVerificationResponse, error) {
	var out CreateVerificationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/verifications/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *VerificationsService) ListMessagesCount(ctx context.Context, query *ListVerificationMessagesCountQuery, opts ...conjoin.CallOption) (*ListVerificationMessagesCountResponse, error) {
	var out ListVerificationMessagesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "messaging/verifications/count",
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *VerificationsService) Check(ctx context.Context, verificationID string, body *CheckVerificationRequest, opts ...conjoin.CallOption) (*CheckVerificationResponse, error) {
	var out CheckVerificationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/verifications/{verification_id}/check",
		PathParams:            []string{verificationID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *VerificationsService) Resend(ctx context.Context, verificationID string, opts ...conjoin.CallOption) (*ResendVerificationResponse, error) {
	var out ResendVerificationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/verifications/{verification_id}/resend",
		PathParams:            []string{verificationID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
