package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ChannelAnalyticsService struct {
	client *conjoin.Client
}

func (s *ChannelAnalyticsService) List(ctx context.Context, query *ListChannelAnalyticsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListChannelAnalyticsItem], error) {
	return conjoin.List[ListChannelAnalyticsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/analytics/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *ChannelAnalyticsService) CreateReport(ctx context.Context, body *CreateChannelAnalyticsReportRequest, opts ...conjoin.CallOption) (*CreateChannelAnalyticsReportResponse, error) {
	var out CreateChannelAnalyticsReportResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/analytics-reports/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) ListCount(ctx context.Context, query *ListChannelAnalyticsCountQuery, opts ...conjoin.CallOption) (*ListChannelAnalyticsCountResponse, error) {
	var out ListChannelAnalyticsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "messaging/analytics/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) GenerateSummaries(ctx context.Context, query *GenerateChannelAnalyticsSummariesQuery, opts ...conjoin.CallOption) (*GenerateChannelAnalyticsSummariesResponse, error) {
	var out GenerateChannelAnalyticsSummariesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "messaging/analytics/stats",
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementOpens(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsOpensRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsOpensResponse, error) {
	var out IncrementChannelAnalyticsOpensResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/analytics/{analytics_id}/opens",
		PathParams:            []string{analyticsID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementClicks(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsClicksRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsClicksResponse, error) {
	var out IncrementChannelAnalyticsClicksResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/analytics/{analytics_id}/clicks",
		PathParams:            []string{analyticsID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementDeliveries(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsDeliveriesRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsDeliveriesResponse, error) {
	var out IncrementChannelAnalyticsDeliveriesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/analytics/{analytics_id}/deliveries",
		PathParams:            []string{analyticsID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementSubscribes(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsSubscribesRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsSubscribesResponse, error) {
	var out IncrementChannelAnalyticsSubscribesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/analytics/{analytics_id}/subscribes",
		PathParams:            []string{analyticsID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementUnsubscribes(ctx context.Context, analyticsID string, body *IncrementChannelAnalyticsUnsubscribesRequest, opts ...conjoin.CallOption) (*IncrementChannelAnalyticsUnsubscribesResponse, error) {
	var out IncrementChannelAnalyticsUnsubscribesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/analytics/{analytics_id}/unsubscribes",
		PathParams:            []string{analyticsID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
