package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type FeatureAccessesService struct {
	client *conjoin.Client
}

func (s *FeatureAccessesService) CheckEntitlement(ctx context.Context, body *CheckEntitlementRequest, opts ...conjoin.CallOption) (*CheckEntitlementResponse, error) {
	var out CheckEntitlementResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entitlements/check",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *FeatureAccessesService) TrackFeatureUsage(ctx context.Context, body *TrackFeatureUsageRequest, opts ...conjoin.CallOption) (*TrackFeatureUsageResponse, error) {
	var out TrackFeatureUsageResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entitlements/track",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
