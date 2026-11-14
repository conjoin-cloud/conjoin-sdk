package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EmailSenderPoolsService struct {
	client *conjoin.Client
}

func (s *EmailSenderPoolsService) Create(ctx context.Context, body *CreateEmailSenderPoolRequest, opts ...conjoin.CallOption) (*CreateEmailSenderPoolResponse, error) {
	var out CreateEmailSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/email/sender-pools/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSenderPoolsService) AddEmailSendersToPool(ctx context.Context, poolID string, body *AddEmailSendersToPoolRequest, opts ...conjoin.CallOption) (*AddEmailSendersToPoolResponse, error) {
	var out AddEmailSendersToPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/email/sender-pools/{pool_id}/senders",
		PathParams:   []string{poolID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSenderPoolsService) Get(ctx context.Context, poolID string, opts ...conjoin.CallOption) (*GetEmailSenderPoolResponse, error) {
	var out GetEmailSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/email/sender-pools/{pool_id}",
		PathParams: []string{poolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSenderPoolsService) Delete(ctx context.Context, poolID string, opts ...conjoin.CallOption) (*DeleteEmailSenderPoolResponse, error) {
	var out DeleteEmailSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/email/sender-pools/{pool_id}",
		PathParams: []string{poolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
