package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EmailSendersService struct {
	client *conjoin.Client
}

func (s *EmailSendersService) ListMany(ctx context.Context, query *ListManyEmailSendersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListManyEmailSendersItem], error) {
	return conjoin.List[ListManyEmailSendersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/email-senders/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *EmailSendersService) Create(ctx context.Context, body *CreateEmailSenderRequest, opts ...conjoin.CallOption) (*CreateEmailSenderResponse, error) {
	var out CreateEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-senders/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) ListManyCount(ctx context.Context, query *ListManyEmailSendersCountQuery, opts ...conjoin.CallOption) (*ListManyEmailSendersCountResponse, error) {
	var out ListManyEmailSendersCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/email-senders/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Read(ctx context.Context, emailSenderID string, opts ...conjoin.CallOption) (*ReadEmailSenderResponse, error) {
	var out ReadEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/email-senders/{email_sender_id}",
		PathParams: []string{emailSenderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Delete(ctx context.Context, emailSenderID string, opts ...conjoin.CallOption) (*DeleteEmailSenderResponse, error) {
	var out DeleteEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/email-senders/{email_sender_id}",
		PathParams: []string{emailSenderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Verify(ctx context.Context, emailSenderID string, opts ...conjoin.CallOption) (*VerifyEmailSenderResponse, error) {
	var out VerifyEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-senders/{email_sender_id}/verify",
		PathParams:            []string{emailSenderID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Enable(ctx context.Context, emailSenderID string, opts ...conjoin.CallOption) (*EnableEmailSenderResponse, error) {
	var out EnableEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-senders/{email_sender_id}/enable",
		PathParams:            []string{emailSenderID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Disable(ctx context.Context, emailSenderID string, opts ...conjoin.CallOption) (*DisableEmailSenderResponse, error) {
	var out DisableEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-senders/{email_sender_id}/disable",
		PathParams:            []string{emailSenderID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Transfer(ctx context.Context, emailSenderID string, body *TransferEmailSenderRequest, opts ...conjoin.CallOption) (*TransferEmailSenderResponse, error) {
	var out TransferEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-senders/{email_sender_id}/transfer",
		PathParams:            []string{emailSenderID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
