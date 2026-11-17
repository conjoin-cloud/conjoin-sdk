package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMsService struct {
	client *conjoin.Client
}

func (s *SMsService) ListSmsMessages(ctx context.Context, query *ListSmsMessagesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSmsMessagesItem], error) {
	return conjoin.List[ListSmsMessagesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-messages/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *SMsService) SendSms(ctx context.Context, body *SendSmsRequest, opts ...conjoin.CallOption) (*SendSmsResponse, error) {
	var out SendSmsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-messages/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMsService) ListSmsMessagesCount(ctx context.Context, query *ListSmsMessagesCountQuery, opts ...conjoin.CallOption) (*ListSmsMessagesCountResponse, error) {
	var out ListSmsMessagesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms-messages/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMsService) ReadSmsMessage(ctx context.Context, smsMessageID string, opts ...conjoin.CallOption) (*ReadSmsMessageResponse, error) {
	var out ReadSmsMessageResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/sms-messages/{sms_message_id}",
		PathParams: []string{smsMessageID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMsService) GenerateSmsSummary(ctx context.Context, body *GenerateSmsSummaryRequest, opts ...conjoin.CallOption) (*GenerateSmsSummaryResponse, error) {
	var out GenerateSmsSummaryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/sms-message-previews/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
