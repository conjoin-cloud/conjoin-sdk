package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SMsService struct {
	client *conjoin.Client
}

func (s *SMsService) SendSms(ctx context.Context, body *SendSmsRequest, opts ...conjoin.CallOption) (*SendSmsResponse, error) {
	var out SendSmsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/sms/send",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SMsService) ReadSmsMessages(ctx context.Context, messageID string, body *ReadSmsMessagesRequest, opts ...conjoin.CallOption) (*conjoin.Page[ReadSmsMessagesItem], error) {
	return conjoin.List[ReadSmsMessagesItem](ctx, s.client, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/sms/messages/{message_id}",
		PathParams:   []string{messageID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *SMsService) GetSmsSummary(ctx context.Context, opts ...conjoin.CallOption) (*GetSmsSummaryResponse, error) {
	var out GetSmsSummaryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/sms/summary",
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
