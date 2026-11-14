package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type TrustedDevicesService struct {
	client *conjoin.Client
}

func (s *TrustedDevicesService) List(ctx context.Context, accountID string, query *ListTrustedDevicesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListTrustedDevicesItem], error) {
	return conjoin.List[ListTrustedDevicesItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/trusted-devices/",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, opts...)
}

func (s *TrustedDevicesService) ListCount(ctx context.Context, accountID string, query *ListTrustedDevicesCountQuery, opts ...conjoin.CallOption) (*ListTrustedDevicesCountResponse, error) {
	var out ListTrustedDevicesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "auth/accounts/{account_id}/trusted-devices/count",
		PathParams: []string{accountID},
		Query:      query,
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *TrustedDevicesService) RevokeAll(ctx context.Context, accountID string, opts ...conjoin.CallOption) (*RevokeAllTrustedDevicesResponse, error) {
	var out RevokeAllTrustedDevicesResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/accounts/{account_id}/trusted-devices/revoke-all",
		PathParams: []string{accountID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *TrustedDevicesService) Revoke(ctx context.Context, accountID string, trustedDeviceID string, opts ...conjoin.CallOption) (*RevokeTrustedDeviceResponse, error) {
	var out RevokeTrustedDeviceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "POST",
		Path:       "auth/accounts/{account_id}/trusted-devices/{trusted_device_id}/revoke",
		PathParams: []string{accountID, trustedDeviceID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
