package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type TemplatesService struct {
	client *conjoin.Client
}

func (s *TemplatesService) CreateMessage(ctx context.Context, body *CreateMessageTemplateRequest, opts ...conjoin.CallOption) (*CreateMessageTemplateResponse, error) {
	var out CreateMessageTemplateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/templates/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *TemplatesService) ListMessage(ctx context.Context, body *ListMessageTemplatesRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListMessageTemplatesItem], error) {
	return conjoin.List[ListMessageTemplatesItem](ctx, s.client, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/templates/retrieve",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, opts...)
}

func (s *TemplatesService) ReadMessage(ctx context.Context, templateID string, opts ...conjoin.CallOption) (*ReadMessageTemplateResponse, error) {
	var out ReadMessageTemplateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/templates/{template_id}",
		PathParams: []string{templateID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *TemplatesService) DeleteMessage(ctx context.Context, templateID string, opts ...conjoin.CallOption) (*DeleteMessageTemplateResponse, error) {
	var out DeleteMessageTemplateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/templates/{template_id}",
		PathParams: []string{templateID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *TemplatesService) UpdateMessage(ctx context.Context, templateID string, body *UpdateMessageTemplateRequest, opts ...conjoin.CallOption) (*UpdateMessageTemplateResponse, error) {
	var out UpdateMessageTemplateResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/templates/{template_id}",
		PathParams:   []string{templateID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *TemplatesService) DeleteMessages(ctx context.Context, body *DeleteMessageTemplatesRequest, opts ...conjoin.CallOption) (*DeleteMessageTemplatesResponse, error) {
	var out DeleteMessageTemplatesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/templates/wipe",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		Response:     conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
