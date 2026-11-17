package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type WebhooksService struct {
	client *conjoin.Client
}

func (s *WebhooksService) List(ctx context.Context, query *ReadWebhooksQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadWebhooksItem], error) {
	return conjoin.List[ReadWebhooksItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/webhooks/",
		Query:  query,
	}, opts...)
}

func (s *WebhooksService) Register(ctx context.Context, body *RegisterWebhookRequest, opts ...conjoin.CallOption) (*RegisterWebhookResponse, error) {
	var out RegisterWebhookResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "cloud/webhooks/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *WebhooksService) ReadCount(ctx context.Context, query *ReadWebhooksCountQuery, opts ...conjoin.CallOption) (*ReadWebhooksCountResponse, error) {
	var out ReadWebhooksCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/webhooks/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *WebhooksService) Read(ctx context.Context, webhookID string, opts ...conjoin.CallOption) (*ReadWebhookResponse, error) {
	var out ReadWebhookResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/webhooks/{webhook_id}",
		PathParams: []string{webhookID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *WebhooksService) Update(ctx context.Context, webhookID string, body *UpdateWebhookRequest, opts ...conjoin.CallOption) (*UpdateWebhookResponse, error) {
	var out UpdateWebhookResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/webhooks/{webhook_id}",
		PathParams:   []string{webhookID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *WebhooksService) Delete(ctx context.Context, webhookID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "cloud/webhooks/{webhook_id}",
		PathParams: []string{webhookID},
	}, &out, opts...)
	return out, err
}

func (s *WebhooksService) ReadEvents(ctx context.Context, query *ReadWebhookEventsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadWebhookEventsItem], error) {
	return conjoin.List[ReadWebhookEventsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/webhook-events/",
		Query:  query,
	}, opts...)
}

func (s *WebhooksService) ReadEventsCount(ctx context.Context, query *ReadWebhookEventsCountQuery, opts ...conjoin.CallOption) (*ReadWebhookEventsCountResponse, error) {
	var out ReadWebhookEventsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/webhook-events/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
