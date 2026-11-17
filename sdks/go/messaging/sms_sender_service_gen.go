package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMSSendersService struct {
	client *conjoin.Client
}

func (s *SMSSendersService) ListManySmsSenders(ctx context.Context, query *ListManySmsSendersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListManySmsSendersItem], error) {
	return conjoin.List[ListManySmsSendersItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-senders/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *SMSSendersService) CreateSmsSender(ctx context.Context, body *CreateSmsSenderRequest, opts ...conjoin.CallOption) (*CreateSmsSenderResponse, error) {
	var out CreateSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-senders/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) ListManySmsSendersCount(ctx context.Context, query *ListManySmsSendersCountQuery, opts ...conjoin.CallOption) (*ListManySmsSendersCountResponse, error) {
	var out ListManySmsSendersCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-senders/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) ReadSmsSender(ctx context.Context, smsSenderID string, opts ...conjoin.CallOption) (*ReadSmsSenderResponse, error) {
	var out ReadSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms-senders/{sms_sender_id}",
		PathParams: []string{smsSenderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) UpdateOneSmsSender(ctx context.Context, smsSenderID string, body *UpdateOneSmsSenderRequest, opts ...conjoin.CallOption) (*UpdateOneSmsSenderResponse, error) {
	var out UpdateOneSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/sms-senders/{sms_sender_id}",
		PathParams:   []string{smsSenderID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) DeleteSmsSender(ctx context.Context, smsSenderID string, opts ...conjoin.CallOption) (*DeleteSmsSenderResponse, error) {
	var out DeleteSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/sms-senders/{sms_sender_id}",
		PathParams: []string{smsSenderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) EnableSmsSender(ctx context.Context, smsSenderID string, opts ...conjoin.CallOption) (*EnableSmsSenderResponse, error) {
	var out EnableSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-senders/{sms_sender_id}/enable",
		PathParams:            []string{smsSenderID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) DisableSmsSender(ctx context.Context, smsSenderID string, opts ...conjoin.CallOption) (*DisableSmsSenderResponse, error) {
	var out DisableSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-senders/{sms_sender_id}/disable",
		PathParams:            []string{smsSenderID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) TransferSmsSender(ctx context.Context, smsSenderID string, body *TransferSmsSenderRequest, opts ...conjoin.CallOption) (*TransferSmsSenderResponse, error) {
	var out TransferSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-senders/{sms_sender_id}/transfer",
		PathParams:            []string{smsSenderID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
