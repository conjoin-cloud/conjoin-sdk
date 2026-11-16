package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ResourceGrantsService struct {
	client *conjoin.Client
}

func (s *ResourceGrantsService) List(ctx context.Context, organizationID string, query *ListResourceGrantsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListResourceGrantsItem], error) {
	return conjoin.List[ListResourceGrantsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/resource-grants/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *ResourceGrantsService) GrantResourcePermission(ctx context.Context, organizationID string, body *GrantResourcePermissionRequest, opts ...conjoin.CallOption) (*GrantResourcePermissionResponse, error) {
	var out GrantResourcePermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/resource-grants/",
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

func (s *ResourceGrantsService) CheckResourcePermission(ctx context.Context, organizationID string, body *CheckResourcePermissionRequest, opts ...conjoin.CallOption) (*CheckResourcePermissionResponse, error) {
	var out CheckResourcePermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/check-resource-permission",
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

func (s *ResourceGrantsService) ListCount(ctx context.Context, organizationID string, query *ListResourceGrantsCountQuery, opts ...conjoin.CallOption) (*ListResourceGrantsCountResponse, error) {
	var out ListResourceGrantsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/resource-grants/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ResourceGrantsService) RevokeResourcePermission(ctx context.Context, organizationID string, resourceGrantID string, body *RevokeResourcePermissionRequest, opts ...conjoin.CallOption) (*RevokeResourcePermissionResponse, error) {
	var out RevokeResourcePermissionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/resource-grants/{resource_grant_id}/revoke",
		PathParams:            []string{organizationID, resourceGrantID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
