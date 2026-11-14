package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SubscriptionsService struct {
	client *conjoin.Client
}

func (s *SubscriptionsService) List(ctx context.Context, query *ListSubscriptionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSubscriptionsItem], error) {
	return conjoin.List[ListSubscriptionsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/subscriptions/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *SubscriptionsService) Create(ctx context.Context, body *CreateSubscriptionRequest, opts ...conjoin.CallOption) (*CreateSubscriptionResponse, error) {
	var out CreateSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/subscriptions/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) ListCycles(ctx context.Context, subscriptionID string, query *ListSubscriptionCyclesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListSubscriptionCyclesItem], error) {
	return conjoin.List[ListSubscriptionCyclesItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/subscriptions/{subscription_id}/cycles",
		PathParams: []string{subscriptionID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *SubscriptionsService) ListCount(ctx context.Context, query *ListSubscriptionsCountQuery, opts ...conjoin.CallOption) (*ListSubscriptionsCountResponse, error) {
	var out ListSubscriptionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/subscriptions/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) Read(ctx context.Context, subscriptionID string, opts ...conjoin.CallOption) (*ReadSubscriptionResponse, error) {
	var out ReadSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/subscriptions/{subscription_id}",
		PathParams: []string{subscriptionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) Update(ctx context.Context, subscriptionID string, body *UpdateSubscriptionRequest, opts ...conjoin.CallOption) (*UpdateSubscriptionResponse, error) {
	var out UpdateSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/subscriptions/{subscription_id}",
		PathParams:   []string{subscriptionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) CreatePlanChange(ctx context.Context, subscriptionID string, body *CreateSubscriptionPlanChangeRequest, opts ...conjoin.CallOption) (*CreateSubscriptionPlanChangeResponse, error) {
	var out CreateSubscriptionPlanChangeResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/subscriptions/{subscription_id}/plan-changes",
		PathParams:   []string{subscriptionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) Cancel(ctx context.Context, subscriptionID string, body *CancelSubscriptionRequest, opts ...conjoin.CallOption) (*CancelSubscriptionResponse, error) {
	var out CancelSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/subscriptions/{subscription_id}/cancel",
		PathParams:   []string{subscriptionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) Pause(ctx context.Context, subscriptionID string, body *PauseSubscriptionRequest, opts ...conjoin.CallOption) (*PauseSubscriptionResponse, error) {
	var out PauseSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/subscriptions/{subscription_id}/pause",
		PathParams:   []string{subscriptionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) Resume(ctx context.Context, subscriptionID string, opts ...conjoin.CallOption) (*ResumeSubscriptionResponse, error) {
	var out ResumeSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/subscriptions/{subscription_id}/resume",
		PathParams: []string{subscriptionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SubscriptionsService) RecordUsage(ctx context.Context, subscriptionID string, body *RecordSubscriptionUsageRequest, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/subscriptions/{subscription_id}/usage-records",
		PathParams:   []string{subscriptionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...)
	return out, err
}

func (s *SubscriptionsService) ReadUsageSummary(ctx context.Context, subscriptionID string, query *ReadSubscriptionUsageSummaryQuery, opts ...conjoin.CallOption) ([]ReadSubscriptionUsageSummaryResponseItem, error) {
	var out []ReadSubscriptionUsageSummaryResponseItem
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/subscriptions/{subscription_id}/usage-summaries",
		PathParams: []string{subscriptionID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...)
	return out, err
}

func (s *SubscriptionsService) ListCyclesCount(ctx context.Context, subscriptionID string, query *ListSubscriptionCyclesCountQuery, opts ...conjoin.CallOption) (*ListSubscriptionCyclesCountResponse, error) {
	var out ListSubscriptionCyclesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/subscriptions/{subscription_id}/cycles/count",
		PathParams: []string{subscriptionID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
