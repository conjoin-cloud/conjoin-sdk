package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationRolePermissionsService struct {
	client *conjoin.Client
}

func (s *OrganizationRolePermissionsService) ListOrgRolePermissions(ctx context.Context, roleID string, query *ListOrgRolePermissionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListOrgRolePermissionsItem], error) {
	return conjoin.List[ListOrgRolePermissionsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/roles/{role_id}/permissions",
		PathParams: []string{roleID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationRolePermissionsService) ListOrgRolePermissionsCount(ctx context.Context, roleID string, query *ListOrgRolePermissionsCountQuery, opts ...conjoin.CallOption) (*ListOrgRolePermissionsCountResponse, error) {
	var out ListOrgRolePermissionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/roles/{role_id}/permissions/count",
		PathParams: []string{roleID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationRolePermissionsService) AssignOrgRolePermission(ctx context.Context, organizationID string, roleID string, body *AssignOrgRolePermissionRequest, opts ...conjoin.CallOption) ([]AssignOrgRolePermissionResponseItem, error) {
	var out []AssignOrgRolePermissionResponseItem
	err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/roles/{role_id}/assign-permissions",
		PathParams:            []string{organizationID, roleID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...)
	return out, err
}

func (s *OrganizationRolePermissionsService) RemoveRolePermission(ctx context.Context, organizationID string, roleID string, body *RemoveRolePermissionRequest, opts ...conjoin.CallOption) (*RemoveRolePermissionResponse, error) {
	var out RemoveRolePermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/roles/{role_id}/remove-permissions",
		PathParams:            []string{organizationID, roleID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
