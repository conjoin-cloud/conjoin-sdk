package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EmailsService struct {
	client *conjoin.Client
}

func (s *EmailsService) ListMessages(ctx context.Context, query *ListEmailMessagesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListEmailMessagesItem], error) {
	return conjoin.List[ListEmailMessagesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/email-messages/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *EmailsService) Send(ctx context.Context, body *SendEmailRequest, opts ...conjoin.CallOption) (*SendEmailResponse, error) {
	var out SendEmailResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-messages/",
		Body:                  body,
		BodyRequired:          true,
		Multipart:             true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailsService) ListMessagesCount(ctx context.Context, query *ListEmailMessagesCountQuery, opts ...conjoin.CallOption) (*ListEmailMessagesCountResponse, error) {
	var out ListEmailMessagesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/email-messages/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailsService) ReadMessage(ctx context.Context, emailMessageID string, opts ...conjoin.CallOption) (*ReadEmailMessageResponse, error) {
	var out ReadEmailMessageResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/email-messages/{email_message_id}",
		PathParams: []string{emailMessageID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EmailsService) GenerateSummary(ctx context.Context, body *GenerateEmailSummaryRequest, opts ...conjoin.CallOption) (*GenerateEmailSummaryResponse, error) {
	var out GenerateEmailSummaryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email-message-previews/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
