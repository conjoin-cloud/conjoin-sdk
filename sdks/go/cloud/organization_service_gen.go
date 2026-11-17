package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationsService struct {
	client *conjoin.Client
}

func (s *OrganizationsService) List(ctx context.Context, query *ReadOrganizationsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadOrganizationsItem], error) {
	return conjoin.List[ReadOrganizationsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/organizations/",
		Query:  query,
	}, opts...)
}

func (s *OrganizationsService) Create(ctx context.Context, body *CreateOrganizationRequest, opts ...conjoin.CallOption) (*CreateOrganizationResponse, error) {
	var out CreateOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "cloud/organizations/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) ReadCount(ctx context.Context, query *ReadOrganizationsCountQuery, opts ...conjoin.CallOption) (*ReadOrganizationsCountResponse, error) {
	var out ReadOrganizationsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/organizations/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) Read(ctx context.Context, organizationID string, opts ...conjoin.CallOption) (*ReadOrganizationResponse, error) {
	var out ReadOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/organizations/{organization_id}",
		PathParams: []string{organizationID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) Update(ctx context.Context, organizationID string, body *UpdateOrganizationRequest, opts ...conjoin.CallOption) (*UpdateOrganizationResponse, error) {
	var out UpdateOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/organizations/{organization_id}",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
