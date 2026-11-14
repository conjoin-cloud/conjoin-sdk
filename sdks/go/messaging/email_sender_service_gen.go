package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EmailSendersService struct {
	client *conjoin.Client
}

func (s *EmailSendersService) Verify(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*VerifyEmailSenderResponse, error) {
	var out VerifyEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/email/senders/{sender_id}/verify",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) ListMany(ctx context.Context, body *ListManyEmailSendersRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListManyEmailSendersItem], error) {
	return conjoin.List[ListManyEmailSendersItem](ctx, s.client, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/email/senders/retrieve",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *EmailSendersService) ListOne(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*ListOneEmailSenderResponse, error) {
	var out ListOneEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/email/senders/{sender_id}",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Delete(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*DeleteEmailSenderResponse, error) {
	var out DeleteEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/email/senders/{sender_id}",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Create(ctx context.Context, body *CreateEmailSenderRequest, opts ...conjoin.CallOption) (*CreateEmailSenderResponse, error) {
	var out CreateEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/email/senders/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Enable(ctx context.Context, senderID string, body *EnableEmailSenderRequest, opts ...conjoin.CallOption) (*EnableEmailSenderResponse, error) {
	var out EnableEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/email/senders/{sender_id}/enable",
		PathParams:   []string{senderID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Disable(ctx context.Context, senderID string, body *DisableEmailSenderRequest, opts ...conjoin.CallOption) (*DisableEmailSenderResponse, error) {
	var out DisableEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/email/senders/{sender_id}/disable",
		PathParams:   []string{senderID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSendersService) Transfer(ctx context.Context, senderID string, projectID string, opts ...conjoin.CallOption) (*TransferEmailSenderResponse, error) {
	var out TransferEmailSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/email/senders/transfers/{sender_id}/{project_id}",
		PathParams: []string{senderID, projectID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
