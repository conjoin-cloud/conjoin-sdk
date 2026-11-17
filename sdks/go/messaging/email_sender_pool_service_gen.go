package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EmailSenderPoolsService struct {
	client *conjoin.Client
}

func (s *EmailSenderPoolsService) ListMany(ctx context.Context, query *ListManyEmailSenderPoolsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListManyEmailSenderPoolsItem], error) {
	return conjoin.List[ListManyEmailSenderPoolsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/email-sender-pools/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *EmailSenderPoolsService) Create(ctx context.Context, body *CreateEmailSenderPoolRequest, opts ...conjoin.CallOption) (*CreateEmailSenderPoolResponse, error) {
	var out CreateEmailSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-sender-pools/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSenderPoolsService) ListManyCount(ctx context.Context, query *ListManyEmailSenderPoolsCountQuery, opts ...conjoin.CallOption) (*ListManyEmailSenderPoolsCountResponse, error) {
	var out ListManyEmailSenderPoolsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/email-sender-pools/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSenderPoolsService) AddEmailSendersToPool(ctx context.Context, emailSenderPoolID string, body *AddEmailSendersToPoolRequest, opts ...conjoin.CallOption) (*AddEmailSendersToPoolResponse, error) {
	var out AddEmailSendersToPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-sender-pools/{email_sender_pool_id}/senders",
		PathParams:            []string{emailSenderPoolID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSenderPoolsService) Get(ctx context.Context, emailSenderPoolID string, opts ...conjoin.CallOption) (*GetEmailSenderPoolResponse, error) {
	var out GetEmailSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/email-sender-pools/{email_sender_pool_id}",
		PathParams: []string{emailSenderPoolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailSenderPoolsService) Delete(ctx context.Context, emailSenderPoolID string, opts ...conjoin.CallOption) (*DeleteEmailSenderPoolResponse, error) {
	var out DeleteEmailSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/email-sender-pools/{email_sender_pool_id}",
		PathParams: []string{emailSenderPoolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
