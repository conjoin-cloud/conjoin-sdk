package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type RoleAssignmentLogsService struct {
	client *conjoin.Client
}

func (s *RoleAssignmentLogsService) List(ctx context.Context, organizationID string, query *ListRoleAssignmentLogsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListRoleAssignmentLogsItem], error) {
	return conjoin.List[ListRoleAssignmentLogsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/role-assignment-logs/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *RoleAssignmentLogsService) ListCount(ctx context.Context, organizationID string, query *ListRoleAssignmentLogsCountQuery, opts ...conjoin.CallOption) (*ListRoleAssignmentLogsCountResponse, error) {
	var out ListRoleAssignmentLogsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/role-assignment-logs/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
