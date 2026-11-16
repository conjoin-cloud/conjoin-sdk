package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type AuthorizationsService struct {
	client *conjoin.Client
}

func (s *AuthorizationsService) AuthorizeAction(ctx context.Context, organizationID string, body *AuthorizeActionRequest, opts ...conjoin.CallOption) (*AuthorizeActionResponse, error) {
	var out AuthorizeActionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/authorize",
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

func (s *AuthorizationsService) CheckRole(ctx context.Context, organizationID string, body *CheckRoleRequest, opts ...conjoin.CallOption) (*CheckRoleResponse, error) {
	var out CheckRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/check-role",
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

func (s *AuthorizationsService) ReadEffectivePermissions(ctx context.Context, organizationID string, query *ReadEffectivePermissionsQuery, opts ...conjoin.CallOption) (*ReadEffectivePermissionsResponse, error) {
	var out ReadEffectivePermissionsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "auth/organizations/{organization_id}/effective-permissions",
		PathParams:    []string{organizationID},
		Query:         query,
		QueryRequired: true,
		Scopes:        []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
