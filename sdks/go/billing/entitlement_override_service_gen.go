package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EntitlementOverridesService struct {
	client *conjoin.Client
}

func (s *EntitlementOverridesService) List(ctx context.Context, query *ListEntitlementOverridesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListEntitlementOverridesItem], error) {
	return conjoin.List[ListEntitlementOverridesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/entitlement-overrides/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *EntitlementOverridesService) Create(ctx context.Context, body *CreateEntitlementOverrideRequest, opts ...conjoin.CallOption) (*CreateEntitlementOverrideResponse, error) {
	var out CreateEntitlementOverrideResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/entitlement-overrides/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitlementOverridesService) ListCount(ctx context.Context, query *ListEntitlementOverridesCountQuery, opts ...conjoin.CallOption) (*ListEntitlementOverridesCountResponse, error) {
	var out ListEntitlementOverridesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/entitlement-overrides/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitlementOverridesService) Update(ctx context.Context, entitlementOverrideID string, body *UpdateEntitlementOverrideRequest, opts ...conjoin.CallOption) (*UpdateEntitlementOverrideResponse, error) {
	var out UpdateEntitlementOverrideResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/entitlement-overrides/{entitlement_override_id}",
		PathParams:   []string{entitlementOverrideID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitlementOverridesService) Delete(ctx context.Context, entitlementOverrideID string, opts ...conjoin.CallOption) (*DeleteEntitlementOverrideResponse, error) {
	var out DeleteEntitlementOverrideResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "billing/entitlement-overrides/{entitlement_override_id}",
		PathParams: []string{entitlementOverrideID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
