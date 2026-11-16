package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type OrganizationInvitationsService struct {
	client *conjoin.Client
}

func (s *OrganizationInvitationsService) ListInvitations(ctx context.Context, organizationID string, query *ListInvitationsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListInvitationsItem], error) {
	return conjoin.List[ListInvitationsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/invitations/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *OrganizationInvitationsService) CreateInvitation(ctx context.Context, organizationID string, body *CreateInvitationRequest, opts ...conjoin.CallOption) (*CreateInvitationResponse, error) {
	var out CreateInvitationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/invitations/",
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

func (s *OrganizationInvitationsService) ListInvitationsCount(ctx context.Context, organizationID string, query *ListInvitationsCountQuery, opts ...conjoin.CallOption) (*ListInvitationsCountResponse, error) {
	var out ListInvitationsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/invitations/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationInvitationsService) RevokeInvitation(ctx context.Context, organizationID string, invitationID string, opts ...conjoin.CallOption) (*RevokeInvitationResponse, error) {
	var out RevokeInvitationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/invitations/{invitation_id}/revoke",
		PathParams:            []string{organizationID, invitationID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *OrganizationInvitationsService) ResendInvitation(ctx context.Context, organizationID string, invitationID string, body *ResendInvitationRequest, opts ...conjoin.CallOption) (*ResendInvitationResponse, error) {
	var out ResendInvitationResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/organizations/{organization_id}/invitations/{invitation_id}/resend",
		PathParams:            []string{organizationID, invitationID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
