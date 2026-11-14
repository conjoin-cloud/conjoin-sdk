package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type BrandingsService struct {
	client *conjoin.Client
}

func (s *BrandingsService) GetProject(ctx context.Context, opts ...conjoin.CallOption) (*GetProjectBrandingResponse, error) {
	var out GetProjectBrandingResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/branding/",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BrandingsService) PatchProject(ctx context.Context, body *PatchProjectBrandingRequest, opts ...conjoin.CallOption) (*PatchProjectBrandingResponse, error) {
	var out PatchProjectBrandingResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/branding/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BrandingsService) GetOrgOverride(ctx context.Context, organizationID string, opts ...conjoin.CallOption) (*GetOrgBrandingOverrideResponse, error) {
	var out GetOrgBrandingOverrideResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/branding/organizations/{organization_id}",
		PathParams: []string{organizationID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BrandingsService) PatchOrgOverride(ctx context.Context, organizationID string, body *PatchOrgBrandingOverrideRequest, opts ...conjoin.CallOption) (*PatchOrgBrandingOverrideResponse, error) {
	var out PatchOrgBrandingOverrideResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/branding/organizations/{organization_id}",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
