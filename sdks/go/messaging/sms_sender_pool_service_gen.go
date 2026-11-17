package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMSSenderPoolsService struct {
	client *conjoin.Client
}

func (s *SMSSenderPoolsService) ListManySmsSenderPools(ctx context.Context, query *ListManySmsSenderPoolsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListManySmsSenderPoolsItem], error) {
	return conjoin.List[ListManySmsSenderPoolsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-sender-pools/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *SMSSenderPoolsService) CreateSmsSenderPool(ctx context.Context, body *CreateSmsSenderPoolRequest, opts ...conjoin.CallOption) (*CreateSmsSenderPoolResponse, error) {
	var out CreateSmsSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-sender-pools/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSenderPoolsService) ListManySmsSenderPoolsCount(ctx context.Context, query *ListManySmsSenderPoolsCountQuery, opts ...conjoin.CallOption) (*ListManySmsSenderPoolsCountResponse, error) {
	var out ListManySmsSenderPoolsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-sender-pools/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSenderPoolsService) AddSmsSendersToPool(ctx context.Context, smsSenderPoolID string, body *AddSmsSendersToPoolRequest, opts ...conjoin.CallOption) (*AddSmsSendersToPoolResponse, error) {
	var out AddSmsSendersToPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-sender-pools/{sms_sender_pool_id}/senders",
		PathParams:            []string{smsSenderPoolID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSenderPoolsService) GetSmsSenderPool(ctx context.Context, smsSenderPoolID string, opts ...conjoin.CallOption) (*GetSmsSenderPoolResponse, error) {
	var out GetSmsSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms-sender-pools/{sms_sender_pool_id}",
		PathParams: []string{smsSenderPoolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSenderPoolsService) DeleteSmsSenderPool(ctx context.Context, smsSenderPoolID string, opts ...conjoin.CallOption) (*DeleteSmsSenderPoolResponse, error) {
	var out DeleteSmsSenderPoolResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/sms-sender-pools/{sms_sender_pool_id}",
		PathParams: []string{smsSenderPoolID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
