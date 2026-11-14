package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PriceBundlesService struct {
	client *conjoin.Client
}

func (s *PriceBundlesService) ListActivations(ctx context.Context, query *ListPriceBundleActivationsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPriceBundleActivationsItem], error) {
	return conjoin.List[ListPriceBundleActivationsItem](ctx, s.client, conjoin.Operation{
		Method:        "GET",
		Path:          "billing/price-bundle-activations/",
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *PriceBundlesService) Activate(ctx context.Context, body *ActivatePriceBundleRequest, opts ...conjoin.CallOption) (*ActivatePriceBundleResponse, error) {
	var out ActivatePriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/price-bundle-activations/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) ListActivationsCount(ctx context.Context, query *ListPriceBundleActivationsCountQuery, opts ...conjoin.CallOption) (*ListPriceBundleActivationsCountResponse, error) {
	var out ListPriceBundleActivationsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "billing/price-bundle-activations/count",
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) Deactivate(ctx context.Context, priceBundleActivationID string, body *DeactivatePriceBundleRequest, opts ...conjoin.CallOption) (*DeactivatePriceBundleResponse, error) {
	var out DeactivatePriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/price-bundle-activations/{price_bundle_activation_id}/deactivate",
		PathParams:   []string{priceBundleActivationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) ReadAvailableBundleTransitions(ctx context.Context, query *ReadAvailableBundleTransitionsQuery, opts ...conjoin.CallOption) (*ReadAvailableBundleTransitionsResponse, error) {
	var out ReadAvailableBundleTransitionsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "billing/price-bundle-transitions/",
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) List(ctx context.Context, query *ListPriceBundlesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPriceBundlesItem], error) {
	return conjoin.List[ListPriceBundlesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/price-bundles/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *PriceBundlesService) Create(ctx context.Context, body *CreatePriceBundleRequest, opts ...conjoin.CallOption) (*CreatePriceBundleResponse, error) {
	var out CreatePriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/price-bundles/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) ListCount(ctx context.Context, query *ListPriceBundlesCountQuery, opts ...conjoin.CallOption) (*ListPriceBundlesCountResponse, error) {
	var out ListPriceBundlesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/price-bundles/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) Read(ctx context.Context, priceBundleID string, opts ...conjoin.CallOption) (*ReadPriceBundleResponse, error) {
	var out ReadPriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/price-bundles/{price_bundle_id}",
		PathParams: []string{priceBundleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) Update(ctx context.Context, priceBundleID string, body *UpdatePriceBundleRequest, opts ...conjoin.CallOption) (*UpdatePriceBundleResponse, error) {
	var out UpdatePriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/price-bundles/{price_bundle_id}",
		PathParams:   []string{priceBundleID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) Archive(ctx context.Context, priceBundleID string, opts ...conjoin.CallOption) (*ArchivePriceBundleResponse, error) {
	var out ArchivePriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/price-bundles/{price_bundle_id}/archive",
		PathParams: []string{priceBundleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) Restore(ctx context.Context, priceBundleID string, opts ...conjoin.CallOption) (*RestorePriceBundleResponse, error) {
	var out RestorePriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/price-bundles/{price_bundle_id}/restore",
		PathParams: []string{priceBundleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PriceBundlesService) Publish(ctx context.Context, priceBundleID string, opts ...conjoin.CallOption) (*PublishPriceBundleResponse, error) {
	var out PublishPriceBundleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "billing/price-bundles/{price_bundle_id}/publish",
		PathParams: []string{priceBundleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
