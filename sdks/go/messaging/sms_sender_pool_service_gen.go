package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMSSenderPoolsService struct {
	client *conjoin.Client
}

func (s *SMSSenderPoolsService) CreateSmsSenderPool(ctx context.Context, body *CreateSmsSenderPoolRequest, opts ...conjoin.CallOption) (*CreateSmsSenderPoolResponse, error) {
	var out CreateSmsSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms/sender-pools/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSenderPoolsService) AddSmsSendersToPool(ctx context.Context, poolID string, body *AddSmsSendersToPoolRequest, opts ...conjoin.CallOption) (*AddSmsSendersToPoolResponse, error) {
	var out AddSmsSendersToPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms/sender-pools/{pool_id}/senders",
		PathParams:            []string{poolID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSenderPoolsService) GetSmsSenderPool(ctx context.Context, poolID string, opts ...conjoin.CallOption) (*GetSmsSenderPoolResponse, error) {
	var out GetSmsSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms/sender-pools/{pool_id}",
		PathParams: []string{poolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSenderPoolsService) DeleteSmsSenderPool(ctx context.Context, poolID string, opts ...conjoin.CallOption) (*DeleteSmsSenderPoolResponse, error) {
	var out DeleteSmsSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/sms/sender-pools/{pool_id}",
		PathParams: []string{poolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
