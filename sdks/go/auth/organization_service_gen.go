package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationsService struct {
	client *conjoin.Client
}

func (s *OrganizationsService) List(ctx context.Context, query *ListOrganizationsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListOrganizationsItem], error) {
	return conjoin.List[ListOrganizationsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "auth/organizations/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationsService) Create(ctx context.Context, body *CreateOrganizationRequest, opts ...conjoin.CallOption) (*CreateOrganizationResponse, error) {
	var out CreateOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) ListCount(ctx context.Context, query *ListOrganizationsCountQuery, opts ...conjoin.CallOption) (*ListOrganizationsCountResponse, error) {
	var out ListOrganizationsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/organizations/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) Read(ctx context.Context, organizationID string, opts ...conjoin.CallOption) (*ReadOrganizationResponse, error) {
	var out ReadOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}",
		PathParams: []string{organizationID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) Update(ctx context.Context, organizationID string, body *UpdateOrganizationRequest, opts ...conjoin.CallOption) (*UpdateOrganizationResponse, error) {
	var out UpdateOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) Delete(ctx context.Context, organizationID string, query *DeleteOrganizationQuery, opts ...conjoin.CallOption) (*DeleteOrganizationResponse, error) {
	var out DeleteOrganizationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationsService) UpdateSettings(ctx context.Context, organizationID string, body *UpdateOrganizationSettingsRequest, opts ...conjoin.CallOption) (*UpdateOrganizationSettingsResponse, error) {
	var out UpdateOrganizationSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/settings",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
