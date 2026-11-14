package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SSOPortalsService struct {
	client *conjoin.Client
}

func (s *SSOPortalsService) ReadSsoPortalSettings(ctx context.Context, opts ...conjoin.CallOption) (*ReadSsoPortalSettingsResponse, error) {
	var out ReadSsoPortalSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/portal/settings",
		Scopes: []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SSOPortalsService) UpdateSsoPortalSettings(ctx context.Context, body *UpdateSsoPortalSettingsRequest, opts ...conjoin.CallOption) (*UpdateSsoPortalSettingsResponse, error) {
	var out UpdateSsoPortalSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/portal/settings",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SSOPortalsService) MintSsoPortalTicket(ctx context.Context, organizationID string, body map[string]any, opts ...conjoin.CallOption) (*MintSsoPortalTicketResponse, error) {
	var out MintSsoPortalTicketResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/portal-tickets/",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SSOPortalsService) RevokeSsoPortalTicket(ctx context.Context, organizationID string, portalTicketID string, opts ...conjoin.CallOption) (*RevokeSsoPortalTicketResponse, error) {
	var out RevokeSsoPortalTicketResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/portal-tickets/{portal_ticket_id}/revoke",
		PathParams: []string{organizationID, portalTicketID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
