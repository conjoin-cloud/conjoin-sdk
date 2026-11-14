package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EmailsService struct {
	client *conjoin.Client
}

func (s *EmailsService) Send(ctx context.Context, body *SendEmailRequest, opts ...conjoin.CallOption) (*SendEmailResponse, error) {
	var out SendEmailResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/email/send",
		Body:         body,
		BodyRequired: true,
		Multipart:    true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailsService) ReadMessages(ctx context.Context, messageID string, body *ReadEmailMessagesRequest, opts ...conjoin.CallOption) (*conjoin.Page[ReadEmailMessagesItem], error) {
	return conjoin.List[ReadEmailMessagesItem](ctx, s.client, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/email/messages/{message_id}",
		PathParams:   []string{messageID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *EmailsService) GetSummary(ctx context.Context, opts ...conjoin.CallOption) (*GetEmailSummaryResponse, error) {
	var out GetEmailSummaryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/email/summary",
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
