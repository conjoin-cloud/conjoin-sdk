package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SelvesService struct {
	client *conjoin.Client
}

func (s *SelvesService) ListEntitlementOverrides(ctx context.Context, query *ListSelfEntitlementOverridesQuery, sessionToken conjoin.Credential, opts ...conjoin.CallOption) (*conjoin.Page[ListSelfEntitlementOverridesItem], error) {
	return conjoin.List[ListSelfEntitlementOverridesItem](ctx, s.client, conjoin.Operation{
		Method:       "GET",
		Path:         "billing/self/entitlement-overrides/",
		Query:        query,
		SessionToken: sessionToken,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		Auth:         conjoin.AuthSession,
	}, opts...)
}

func (s *SelvesService) ListPriceBundles(ctx context.Context, query *ListSelfPriceBundlesQuery, sessionToken conjoin.Credential, opts ...conjoin.CallOption) (*conjoin.Page[ListSelfPriceBundlesItem], error) {
	return conjoin.List[ListSelfPriceBundlesItem](ctx, s.client, conjoin.Operation{
		Method:       "GET",
		Path:         "billing/self/price-bundles/",
		Query:        query,
		SessionToken: sessionToken,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		Auth:         conjoin.AuthSession,
	}, opts...)
}

func (s *SelvesService) ListEntitlementOverridesCount(ctx context.Context, query *ListSelfEntitlementOverridesCountQuery, sessionToken conjoin.Credential, opts ...conjoin.CallOption) (*ListSelfEntitlementOverridesCountResponse, error) {
	var out ListSelfEntitlementOverridesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "GET",
		Path:         "billing/self/entitlement-overrides/count",
		Query:        query,
		SessionToken: sessionToken,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		Auth:         conjoin.AuthSession,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SelvesService) ListPriceBundlesCount(ctx context.Context, query *ListSelfPriceBundlesCountQuery, sessionToken conjoin.Credential, opts ...conjoin.CallOption) (*ListSelfPriceBundlesCountResponse, error) {
	var out ListSelfPriceBundlesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "GET",
		Path:         "billing/self/price-bundles/count",
		Query:        query,
		SessionToken: sessionToken,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		Auth:         conjoin.AuthSession,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
