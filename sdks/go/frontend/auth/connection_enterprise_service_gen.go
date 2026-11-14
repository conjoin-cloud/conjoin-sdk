package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ConnectionEnterprisesService struct {
	client *conjoin.Client
}

func (s *ConnectionEnterprisesService) ConfigureSsoPortalConnection(ctx context.Context, body *ConfigureSsoPortalConnectionRequest, opts ...conjoin.CallOption) (*ConfigureSsoPortalConnectionResponse, error) {
	var out ConfigureSsoPortalConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/connections",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) UpdateSsoPortalConnection(ctx context.Context, connectionID string, body *UpdateSsoPortalConnectionRequest, opts ...conjoin.CallOption) (*UpdateSsoPortalConnectionResponse, error) {
	var out UpdateSsoPortalConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/portal/connections/{connection_id}",
		PathParams:   []string{connectionID},
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) ImportSsoPortalMetadata(ctx context.Context, connectionID string, body *ImportSsoPortalMetadataRequest, opts ...conjoin.CallOption) (*ImportSsoPortalMetadataResponse, error) {
	var out ImportSsoPortalMetadataResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/portal/connections/{connection_id}/import-metadata",
		PathParams:   []string{connectionID},
		Body:         body,
		BodyRequired: true,
		Multipart:    true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) ReadSsoPortalProviderConfig(ctx context.Context, connectionID string, opts ...conjoin.CallOption) (*ReadSsoPortalProviderConfigResponse, error) {
	var out ReadSsoPortalProviderConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/portal/connections/{connection_id}/service-provider-settings",
		PathParams: []string{connectionID},
		Auth:       conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
