package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type VerificationsService struct {
	client *conjoin.Client
}

func (s *VerificationsService) Create(ctx context.Context, body *CreateVerificationRequest, opts ...conjoin.CallOption) (*CreateVerificationResponse, error) {
	var out CreateVerificationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/otps/send",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *VerificationsService) Check(ctx context.Context, token string, body *CheckVerificationRequest, opts ...conjoin.CallOption) (*CheckVerificationResponse, error) {
	var out CheckVerificationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/otps/verify/{token}",
		PathParams:   []string{token},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *VerificationsService) Resend(ctx context.Context, verificationID string, body *ResendVerificationRequest, opts ...conjoin.CallOption) (*ResendVerificationResponse, error) {
	var out ResendVerificationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/otps/resend/{verification_id}",
		PathParams:   []string{verificationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *VerificationsService) ListMessages(ctx context.Context, body *ListVerificationMessagesRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListVerificationMessagesItem], error) {
	return conjoin.List[ListVerificationMessagesItem](ctx, s.client, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/otps/messages",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}
