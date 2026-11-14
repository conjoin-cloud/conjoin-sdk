package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ChannelAnalyticsService struct {
	client *conjoin.Client
}

func (s *ChannelAnalyticsService) List(ctx context.Context, opts ...conjoin.CallOption) (*conjoin.Page[ListChannelAnalyticsItem], error) {
	return conjoin.List[ListChannelAnalyticsItem](ctx, s.client, conjoin.Operation{
		Method: "POST",
		Path:   "messaging/analytics/",
		Scopes: []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, opts...)
}

func (s *ChannelAnalyticsService) GenerateSummaries(ctx context.Context, channelID string, opts ...conjoin.CallOption) (*GenerateChannelAnalyticsSummariesResponse, error) {
	var out GenerateChannelAnalyticsSummariesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "messaging/analytics/channels/{channel_id}/generate",
		PathParams: []string{channelID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) CreateReport(ctx context.Context, messageID string, channelID string, opts ...conjoin.CallOption) (*CreateChannelAnalyticsReportResponse, error) {
	var out CreateChannelAnalyticsReportResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "messaging/analytics/messages/{message_id}/channels/{channel_id}/reports",
		PathParams: []string{messageID, channelID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ChannelAnalyticsService) IncrementOpens(ctx context.Context, analyticsID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/analytics/{analytics_id}/opens",
		PathParams: []string{analyticsID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}

func (s *ChannelAnalyticsService) IncrementClicks(ctx context.Context, analyticsID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/analytics/{analytics_id}/clicks",
		PathParams: []string{analyticsID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}

func (s *ChannelAnalyticsService) IncrementDeliveries(ctx context.Context, analyticsID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/analytics/{analytics_id}/deliveries",
		PathParams: []string{analyticsID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}

func (s *ChannelAnalyticsService) IncrementSubscribes(ctx context.Context, analyticsID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/analytics/{analytics_id}/subscribes",
		PathParams: []string{analyticsID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}

func (s *ChannelAnalyticsService) IncrementUnsubscribes(ctx context.Context, analyticsID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "PATCH",
		Path:       "messaging/analytics/{analytics_id}/unsubscribes",
		PathParams: []string{analyticsID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}
