package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationGroupsService struct {
	client *conjoin.Client
}

func (s *OrganizationGroupsService) ListGroups(ctx context.Context, organizationID string, query *ListGroupsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListGroupsItem], error) {
	return conjoin.List[ListGroupsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/groups/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationGroupsService) CreateGroup(ctx context.Context, organizationID string, body *CreateGroupRequest, opts ...conjoin.CallOption) (*CreateGroupResponse, error) {
	var out CreateGroupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/groups/",
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

func (s *OrganizationGroupsService) ListGroupMembers(ctx context.Context, groupID string, query *ListGroupMembersQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListGroupMembersItem], error) {
	return conjoin.List[ListGroupMembersItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/groups/{group_id}/members",
		PathParams: []string{groupID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationGroupsService) ListGroupMembersCount(ctx context.Context, groupID string, query *ListGroupMembersCountQuery, opts ...conjoin.CallOption) (*ListGroupMembersCountResponse, error) {
	var out ListGroupMembersCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/groups/{group_id}/members/count",
		PathParams: []string{groupID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationGroupsService) ListGroupsCount(ctx context.Context, organizationID string, query *ListGroupsCountQuery, opts ...conjoin.CallOption) (*ListGroupsCountResponse, error) {
	var out ListGroupsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/groups/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationGroupsService) UpdateGroup(ctx context.Context, organizationID string, groupID string, body *UpdateGroupRequest, opts ...conjoin.CallOption) (*UpdateGroupResponse, error) {
	var out UpdateGroupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/groups/{group_id}",
		PathParams:   []string{organizationID, groupID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationGroupsService) DeleteGroup(ctx context.Context, organizationID string, groupID string, opts ...conjoin.CallOption) (*DeleteGroupResponse, error) {
	var out DeleteGroupResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}/groups/{group_id}",
		PathParams: []string{organizationID, groupID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationGroupsService) AddGroupMember(ctx context.Context, organizationID string, groupID string, body *AddGroupMemberRequest, opts ...conjoin.CallOption) (*AddGroupMemberResponse, error) {
	var out AddGroupMemberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/groups/{group_id}/add-members",
		PathParams:            []string{organizationID, groupID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationGroupsService) RemoveGroupMember(ctx context.Context, organizationID string, groupID string, body *RemoveGroupMemberRequest, opts ...conjoin.CallOption) (*RemoveGroupMemberResponse, error) {
	var out RemoveGroupMemberResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/groups/{group_id}/remove-members",
		PathParams:            []string{organizationID, groupID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationGroupsService) BulkSyncGroupMembers(ctx context.Context, organizationID string, groupID string, body *BulkSyncGroupMembersRequest, opts ...conjoin.CallOption) (*BulkSyncGroupMembersResponse, error) {
	var out BulkSyncGroupMembersResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/groups/{group_id}/sync-members",
		PathParams:            []string{organizationID, groupID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
