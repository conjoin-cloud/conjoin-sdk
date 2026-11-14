package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SCIMManagementsService struct {
	client *conjoin.Client
}

func (s *SCIMManagementsService) ReadScimSettings(ctx context.Context, organizationID string, opts ...conjoin.CallOption) (*ReadScimSettingsResponse, error) {
	var out ReadScimSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/scim-settings",
		PathParams: []string{organizationID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMManagementsService) UpdateScimSettings(ctx context.Context, organizationID string, body *UpdateScimSettingsRequest, opts ...conjoin.CallOption) (*UpdateScimSettingsResponse, error) {
	var out UpdateScimSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/scim-settings",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMManagementsService) SyncScimRolesForMember(ctx context.Context, organizationID string, membershipID string, opts ...conjoin.CallOption) (*SyncScimRolesForMemberResponse, error) {
	var out SyncScimRolesForMemberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/memberships/{membership_id}/sync-scim-roles",
		PathParams: []string{organizationID, membershipID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMManagementsService) SyncScimRolesForGroup(ctx context.Context, organizationID string, groupID string, opts ...conjoin.CallOption) (*SyncScimRolesForGroupResponse, error) {
	var out SyncScimRolesForGroupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/groups/{group_id}/sync-scim-roles",
		PathParams: []string{organizationID, groupID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMManagementsService) ReconcileScimUsers(ctx context.Context, organizationID string, body *ReconcileScimUsersRequest, opts ...conjoin.CallOption) (*ReconcileScimUsersResponse, error) {
	var out ReconcileScimUsersResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/reconcile-scim-users",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMManagementsService) ReconcileScimGroups(ctx context.Context, organizationID string, body *ReconcileScimGroupsRequest, opts ...conjoin.CallOption) (*ReconcileScimGroupsResponse, error) {
	var out ReconcileScimGroupsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/reconcile-scim-groups",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SCIMManagementsService) ReconcileScimGroupMembers(ctx context.Context, organizationID string, body *ReconcileScimGroupMembersRequest, opts ...conjoin.CallOption) (*ReconcileScimGroupMembersResponse, error) {
	var out ReconcileScimGroupMembersResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/reconcile-scim-group-members",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
