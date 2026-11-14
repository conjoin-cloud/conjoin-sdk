package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SubscriptionSchedulesService struct {
	client *conjoin.Client
}

func (s *SubscriptionSchedulesService) List(ctx context.Context, subscriptionID string, query *ListSubscriptionSchedulesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSubscriptionSchedulesItem], error) {
	return conjoin.List[ListSubscriptionSchedulesItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/subscriptions/{subscription_id}/schedules",
		PathParams: []string{subscriptionID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *SubscriptionSchedulesService) Create(ctx context.Context, subscriptionID string, body *CreateSubscriptionScheduleRequest, opts ...conjoin.CallOption) (*CreateSubscriptionScheduleResponse, error) {
	var out CreateSubscriptionScheduleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/subscriptions/{subscription_id}/schedules",
		PathParams:   []string{subscriptionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionSchedulesService) ListCount(ctx context.Context, subscriptionID string, query *ListSubscriptionSchedulesCountQuery, opts ...conjoin.CallOption) (*ListSubscriptionSchedulesCountResponse, error) {
	var out ListSubscriptionSchedulesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/subscriptions/{subscription_id}/schedules/count",
		PathParams: []string{subscriptionID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionSchedulesService) Get(ctx context.Context, subscriptionScheduleID string, opts ...conjoin.CallOption) (*GetSubscriptionScheduleResponse, error) {
	var out GetSubscriptionScheduleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/subscription-schedules/{subscription_schedule_id}",
		PathParams: []string{subscriptionScheduleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionSchedulesService) Cancel(ctx context.Context, subscriptionScheduleID string, opts ...conjoin.CallOption) (*CancelSubscriptionScheduleResponse, error) {
	var out CancelSubscriptionScheduleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/subscription-schedules/{subscription_schedule_id}/cancel",
		PathParams: []string{subscriptionScheduleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionSchedulesService) Release(ctx context.Context, subscriptionScheduleID string, opts ...conjoin.CallOption) (*ReleaseSubscriptionScheduleResponse, error) {
	var out ReleaseSubscriptionScheduleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/subscription-schedules/{subscription_schedule_id}/release",
		PathParams: []string{subscriptionScheduleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
