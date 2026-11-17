package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationPermissionsService struct {
	client *conjoin.Client
}

func (s *OrganizationPermissionsService) ListOrgPermissions(ctx context.Context, organizationID string, query *ListOrgPermissionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListOrgPermissionsItem], error) {
	return conjoin.List[ListOrgPermissionsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/permissions/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationPermissionsService) CreateOrgPermission(ctx context.Context, organizationID string, body *CreateOrgPermissionRequest, opts ...conjoin.CallOption) (*CreateOrgPermissionResponse, error) {
	var out CreateOrgPermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/permissions/",
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

func (s *OrganizationPermissionsService) ListOrgPermissionsCount(ctx context.Context, organizationID string, query *ListOrgPermissionsCountQuery, opts ...conjoin.CallOption) (*ListOrgPermissionsCountResponse, error) {
	var out ListOrgPermissionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/permissions/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationPermissionsService) ReadOrgPermission(ctx context.Context, organizationID string, permissionID string, opts ...conjoin.CallOption) (*ReadOrgPermissionResponse, error) {
	var out ReadOrgPermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/permissions/{permission_id}",
		PathParams: []string{organizationID, permissionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationPermissionsService) UpdateOrgPermission(ctx context.Context, organizationID string, permissionID string, body *UpdateOrgPermissionRequest, opts ...conjoin.CallOption) (*UpdateOrgPermissionResponse, error) {
	var out UpdateOrgPermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/permissions/{permission_id}",
		PathParams:   []string{organizationID, permissionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationPermissionsService) DeleteOrgPermission(ctx context.Context, organizationID string, permissionID string, opts ...conjoin.CallOption) (*DeleteOrgPermissionResponse, error) {
	var out DeleteOrgPermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}/permissions/{permission_id}",
		PathParams: []string{organizationID, permissionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationPermissionsService) ArchiveOrgPermission(ctx context.Context, organizationID string, permissionID string, opts ...conjoin.CallOption) (*ArchiveOrgPermissionResponse, error) {
	var out ArchiveOrgPermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/permissions/{permission_id}/archive",
		PathParams:            []string{organizationID, permissionID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationPermissionsService) RestoreOrgPermission(ctx context.Context, organizationID string, permissionID string, opts ...conjoin.CallOption) (*RestoreOrgPermissionResponse, error) {
	var out RestoreOrgPermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/permissions/{permission_id}/restore",
		PathParams:            []string{organizationID, permissionID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
