package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ConnectionEnterprisesService struct {
	client *conjoin.Client
}

func (s *ConnectionEnterprisesService) ListEnterpriseConnections(ctx context.Context, organizationID string, query *ListEnterpriseConnectionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListEnterpriseConnectionsItem], error) {
	return conjoin.List[ListEnterpriseConnectionsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/connections/",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *ConnectionEnterprisesService) CreateEnterpriseConnection(ctx context.Context, organizationID string, body *CreateEnterpriseConnectionRequest, opts ...conjoin.CallOption) (*CreateEnterpriseConnectionResponse, error) {
	var out CreateEnterpriseConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/connections/",
		PathParams:   []string{organizationID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) ListEnterpriseConnectionsCount(ctx context.Context, organizationID string, query *ListEnterpriseConnectionsCountQuery, opts ...conjoin.CallOption) (*ListEnterpriseConnectionsCountResponse, error) {
	var out ListEnterpriseConnectionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/connections/count",
		PathParams: []string{organizationID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) ReadEnterpriseConnection(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*ReadEnterpriseConnectionResponse, error) {
	var out ReadEnterpriseConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) UpdateEnterpriseConnection(ctx context.Context, organizationID string, connectionID string, body *UpdateEnterpriseConnectionRequest, opts ...conjoin.CallOption) (*UpdateEnterpriseConnectionResponse, error) {
	var out UpdateEnterpriseConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "auth/organizations/{organization_id}/connections/{connection_id}",
		PathParams:   []string{organizationID, connectionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) DeleteEnterpriseConnection(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*DeleteEnterpriseConnectionResponse, error) {
	var out DeleteEnterpriseConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) EnableEnterpriseConnection(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*EnableEnterpriseConnectionResponse, error) {
	var out EnableEnterpriseConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}/enable",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) DisableEnterpriseConnection(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*DisableEnterpriseConnectionResponse, error) {
	var out DisableEnterpriseConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}/disable",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) RotateEnterpriseConnectionSigningKey(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*RotateEnterpriseConnectionSigningKeyResponse, error) {
	var out RotateEnterpriseConnectionSigningKeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}/signing-keys/rotate",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) ActivateEnterpriseConnectionSigningKey(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*ActivateEnterpriseConnectionSigningKeyResponse, error) {
	var out ActivateEnterpriseConnectionSigningKeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}/signing-keys/activate",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) CancelEnterpriseConnectionSigningKey(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*CancelEnterpriseConnectionSigningKeyResponse, error) {
	var out CancelEnterpriseConnectionSigningKeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}/signing-keys/cancel",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) RevokeEnterpriseConnectionSigningKey(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*RevokeEnterpriseConnectionSigningKeyResponse, error) {
	var out RevokeEnterpriseConnectionSigningKeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}/signing-keys/revoke",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) ReadEnterpriseProviderSettings(ctx context.Context, organizationID string, connectionID string, opts ...conjoin.CallOption) (*ReadEnterpriseProviderSettingsResponse, error) {
	var out ReadEnterpriseProviderSettingsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/organizations/{organization_id}/connections/{connection_id}/provider-settings",
		PathParams: []string{organizationID, connectionID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) ImportEnterpriseSamlMetadata(ctx context.Context, organizationID string, connectionID string, body *ImportEnterpriseSamlMetadataRequest, opts ...conjoin.CallOption) (*ImportEnterpriseSamlMetadataResponse, error) {
	var out ImportEnterpriseSamlMetadataResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/connections/{connection_id}/import-metadata",
		PathParams:   []string{organizationID, connectionID},
		Body:         body,
		BodyRequired: true,
		Multipart:    true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ConnectionEnterprisesService) SyncEnterpriseSamlMetadata(ctx context.Context, organizationID string, connectionID string, body *SyncEnterpriseSamlMetadataRequest, opts ...conjoin.CallOption) (*SyncEnterpriseSamlMetadataResponse, error) {
	var out SyncEnterpriseSamlMetadataResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/organizations/{organization_id}/connections/{connection_id}/sync-metadata",
		PathParams:   []string{organizationID, connectionID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
