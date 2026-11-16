package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ConnectionEnterprisesService struct {
	client *conjoin.Client
}

type ConfigureSsoPortalConnectionHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *ConnectionEnterprisesService) ConfigureSsoPortalConnection(ctx context.Context, body *ConfigureSsoPortalConnectionRequest, headers ConfigureSsoPortalConnectionHeaders, opts ...conjoin.CallOption) (*ConfigureSsoPortalConnectionResponse, error) {
	var out ConfigureSsoPortalConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/connections",
		Body:         body,
		BodyRequired: true,
		Headers:      []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

type UpdateSsoPortalConnectionHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *ConnectionEnterprisesService) UpdateSsoPortalConnection(ctx context.Context, connectionID string, body *UpdateSsoPortalConnectionRequest, headers UpdateSsoPortalConnectionHeaders, opts ...conjoin.CallOption) (*UpdateSsoPortalConnectionResponse, error) {
	var out UpdateSsoPortalConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/portal/connections/{connection_id}",
		PathParams:   []string{connectionID},
		Body:         body,
		BodyRequired: true,
		Headers:      []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

type ImportSsoPortalMetadataHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *ConnectionEnterprisesService) ImportSsoPortalMetadata(ctx context.Context, connectionID string, body *ImportSsoPortalMetadataRequest, headers ImportSsoPortalMetadataHeaders, opts ...conjoin.CallOption) (*ImportSsoPortalMetadataResponse, error) {
	var out ImportSsoPortalMetadataResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/connections/{connection_id}/import-metadata",
		PathParams:   []string{connectionID},
		Body:         body,
		BodyRequired: true,
		Multipart:    true,
		Headers:      []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

type ReadSsoPortalProviderConfigHeaders struct {
	PortalTicket conjoin.Credential `header:"x-portal-ticket"`
}

func (s *ConnectionEnterprisesService) ReadSsoPortalProviderConfig(ctx context.Context, connectionID string, headers ReadSsoPortalProviderConfigHeaders, opts ...conjoin.CallOption) (*ReadSsoPortalProviderConfigResponse, error) {
	var out ReadSsoPortalProviderConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/portal/connections/{connection_id}/service-provider-settings",
		PathParams: []string{connectionID},
		Headers:    []conjoin.DeclaredHeader{{Name: "x-portal-ticket", Argument: "PortalTicket", Value: headers.PortalTicket, Required: true}},
		Auth:       conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
