package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationRolesService struct {
	client *conjoin.Client
}

func (s *OrganizationRolesService) ListOrgRoles(ctx context.Context, organizationID string, query *ListOrgRolesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListOrgRolesItem], error) {
	return conjoin.List[ListOrgRolesItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/roles/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationRolesService) CreateOrgRole(ctx context.Context, organizationID string, body *CreateOrgRoleRequest, opts ...conjoin.CallOption) (*CreateOrgRoleResponse, error) {
	var out CreateOrgRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/roles/",
		PathParams:            []string{organizationID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationRolesService) ListOrgRolesCount(ctx context.Context, organizationID string, query *ListOrgRolesCountQuery, opts ...conjoin.CallOption) (*ListOrgRolesCountResponse, error) {
	var out ListOrgRolesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/roles/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationRolesService) ReadOrgRole(ctx context.Context, organizationID string, roleID string, opts ...conjoin.CallOption) (*ReadOrgRoleResponse, error) {
	var out ReadOrgRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/roles/{role_id}",
		PathParams: []string{organizationID, roleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationRolesService) UpdateOrgRole(ctx context.Context, organizationID string, roleID string, body *UpdateOrgRoleRequest, opts ...conjoin.CallOption) (*UpdateOrgRoleResponse, error) {
	var out UpdateOrgRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/roles/{role_id}",
		PathParams:   []string{organizationID, roleID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationRolesService) DeleteOrgRole(ctx context.Context, organizationID string, roleID string, opts ...conjoin.CallOption) (*DeleteOrgRoleResponse, error) {
	var out DeleteOrgRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}/roles/{role_id}",
		PathParams: []string{organizationID, roleID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationRolesService) ArchiveOrgRole(ctx context.Context, organizationID string, roleID string, opts ...conjoin.CallOption) (*ArchiveOrgRoleResponse, error) {
	var out ArchiveOrgRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/roles/{role_id}/archive",
		PathParams:            []string{organizationID, roleID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationRolesService) RestoreOrgRole(ctx context.Context, organizationID string, roleID string, opts ...conjoin.CallOption) (*RestoreOrgRoleResponse, error) {
	var out RestoreOrgRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/roles/{role_id}/restore",
		PathParams:            []string{organizationID, roleID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
