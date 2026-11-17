package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ChannelAnalyticsService struct {
	client *conjoin.Client
}

func (s *ChannelAnalyticsService) List(ctx context.Context, body *ListChannelAnalyticsRequest, opts ...conjoin.CallOption) (*conjoin.Page[ListChannelAnalyticsItem], error) {
	return conjoin.List[ListChannelAnalyticsItem](ctx, s.client, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email/analytics/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, opts...)
}

func (s *ChannelAnalyticsService) GenerateSummaries(ctx context.Context, channelID string, body *GenerateChannelAnalyticsSummariesRequest, opts ...conjoin.CallOption) (*GenerateChannelAnalyticsSummariesResponse, error) {
	var out GenerateChannelAnalyticsSummariesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email/analytics/channels/{channel_id}/generate",
		PathParams:            []string{channelID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) CreateReport(ctx context.Context, messageID string, channelID string, body *CreateChannelAnalyticsReportRequest, opts ...conjoin.CallOption) (*CreateChannelAnalyticsReportResponse, error) {
	var out CreateChannelAnalyticsReportResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/email/analytics/messages/{message_id}/channels/{channel_id}/reports",
		PathParams:            []string{messageID, channelID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementOpens(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsOpensRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsOpensResponse, error) {
	var out IncrementChannelAnalyticsOpensResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/email/analytics/{analytics_id}/opens",
		PathParams:   []string{analyticsID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementClicks(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsClicksRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsClicksResponse, error) {
	var out IncrementChannelAnalyticsClicksResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/email/analytics/{analytics_id}/clicks",
		PathParams:   []string{analyticsID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementDeliveries(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsDeliveriesRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsDeliveriesResponse, error) {
	var out IncrementChannelAnalyticsDeliveriesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/email/analytics/{analytics_id}/deliveries",
		PathParams:   []string{analyticsID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementSubscribes(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsSubscribesRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsSubscribesResponse, error) {
	var out IncrementChannelAnalyticsSubscribesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/email/analytics/{analytics_id}/subscribes",
		PathParams:   []string{analyticsID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementUnsubscribes(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsUnsubscribesRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsUnsubscribesResponse, error) {
	var out IncrementChannelAnalyticsUnsubscribesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/email/analytics/{analytics_id}/unsubscribes",
		PathParams:   []string{analyticsID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
