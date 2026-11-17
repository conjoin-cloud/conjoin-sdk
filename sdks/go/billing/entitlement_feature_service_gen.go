package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EntitlementFeaturesService struct {
	client *conjoin.Client
}

func (s *EntitlementFeaturesService) List(ctx context.Context, query *ListEntitlementFeaturesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListEntitlementFeaturesItem], error) {
	return conjoin.List[ListEntitlementFeaturesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/entitlement-features/",
		Query:  query,
	}, opts...)
}

func (s *EntitlementFeaturesService) Create(ctx context.Context, body *CreateEntitlementFeatureRequest, opts ...conjoin.CallOption) (*CreateEntitlementFeatureResponse, error) {
	var out CreateEntitlementFeatureResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entitlement-features/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitlementFeaturesService) ListCount(ctx context.Context, query *ListEntitlementFeaturesCountQuery, opts ...conjoin.CallOption) (*ListEntitlementFeaturesCountResponse, error) {
	var out ListEntitlementFeaturesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/entitlement-features/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitlementFeaturesService) Read(ctx context.Context, entitlementFeatureID string, opts ...conjoin.CallOption) (*ReadEntitlementFeatureResponse, error) {
	var out ReadEntitlementFeatureResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/entitlement-features/{entitlement_feature_id}",
		PathParams: []string{entitlementFeatureID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitlementFeaturesService) Update(ctx context.Context, entitlementFeatureID string, body *UpdateEntitlementFeatureRequest, opts ...conjoin.CallOption) (*UpdateEntitlementFeatureResponse, error) {
	var out UpdateEntitlementFeatureResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/entitlement-features/{entitlement_feature_id}",
		PathParams:   []string{entitlementFeatureID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EntitlementFeaturesService) Archive(ctx context.Context, entitlementFeatureID string, opts ...conjoin.CallOption) (*ArchiveEntitlementFeatureResponse, error) {
	var out ArchiveEntitlementFeatureResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/entitlement-features/{entitlement_feature_id}/archive",
		PathParams:            []string{entitlementFeatureID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
