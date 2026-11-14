package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMSSendersService struct {
	client *conjoin.Client
}

func (s *SMSSendersService) CreateSmsSender(ctx context.Context, body *CreateSmsSenderRequest, opts ...conjoin.CallOption) (*CreateSmsSenderResponse, error) {
	var out CreateSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/sms/senders/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) EnableSmsSender(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*EnableSmsSenderResponse, error) {
	var out EnableSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/sms/senders/{sender_id}/enable",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) DisableSmsSender(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*DisableSmsSenderResponse, error) {
	var out DisableSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/sms/senders/{sender_id}/disable",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) ListSmsSender(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*ListSmsSenderResponse, error) {
	var out ListSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms/senders/{sender_id}",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) DeleteSmsSender(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*DeleteSmsSenderResponse, error) {
	var out DeleteSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/sms/senders/{sender_id}",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) UpdateOneSmsSender(ctx context.Context, senderID string, opts ...conjoin.CallOption) (*UpdateOneSmsSenderResponse, error) {
	var out UpdateOneSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/sms/senders/{sender_id}",
		PathParams: []string{senderID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMSSendersService) TransferSmsSender(ctx context.Context, senderID string, projectID string, opts ...conjoin.CallOption) (*TransferSmsSenderResponse, error) {
	var out TransferSmsSenderResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/sms/senders/transfers/{sender_id}/{project_id}",
		PathParams: []string{senderID, projectID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
