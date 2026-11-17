package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationMembershipsService struct {
	client *conjoin.Client
}

func (s *OrganizationMembershipsService) ListMemberships(ctx context.Context, organizationID string, query *ListMembershipsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListMembershipsItem], error) {
	return conjoin.List[ListMembershipsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/memberships/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationMembershipsService) CreateMembership(ctx context.Context, organizationID string, body *CreateMembershipRequest, opts ...conjoin.CallOption) (*CreateMembershipResponse, error) {
	var out CreateMembershipResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/memberships/",
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

func (s *OrganizationMembershipsService) ListMembershipsCount(ctx context.Context, organizationID string, query *ListMembershipsCountQuery, opts ...conjoin.CallOption) (*ListMembershipsCountResponse, error) {
	var out ListMembershipsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/memberships/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationMembershipsService) UpdateMembership(ctx context.Context, organizationID string, membershipID string, body *UpdateMembershipRequest, opts ...conjoin.CallOption) (*UpdateMembershipResponse, error) {
	var out UpdateMembershipResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/memberships/{membership_id}",
		PathParams:   []string{organizationID, membershipID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationMembershipsService) DeleteMembership(ctx context.Context, organizationID string, membershipID string, opts ...conjoin.CallOption) (*DeleteMembershipResponse, error) {
	var out DeleteMembershipResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}/memberships/{membership_id}",
		PathParams: []string{organizationID, membershipID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationMembershipsService) GrantOrgAccountRole(ctx context.Context, organizationID string, membershipID string, body *GrantOrgAccountRoleRequest, opts ...conjoin.CallOption) (*GrantOrgAccountRoleResponse, error) {
	var out GrantOrgAccountRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/memberships/{membership_id}/grant-role",
		PathParams:            []string{organizationID, membershipID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationMembershipsService) RevokeOrgAccountRole(ctx context.Context, organizationID string, membershipID string, body *RevokeOrgAccountRoleRequest, opts ...conjoin.CallOption) (*RevokeOrgAccountRoleResponse, error) {
	var out RevokeOrgAccountRoleResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/memberships/{membership_id}/revoke-role",
		PathParams:            []string{organizationID, membershipID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
