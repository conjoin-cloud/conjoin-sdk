package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ClientsService struct {
	client *conjoin.Client
}

func (s *ClientsService) GetOidcDiscovery(ctx context.Context, opts ...conjoin.CallOption) (*GetOidcDiscoveryResponse, error) {
	var out GetOidcDiscoveryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/client/.well-known/openid-configuration",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ClientsService) ProcessHandshake(ctx context.Context, opts ...conjoin.CallOption) (*ProcessHandshakeResponse, error) {
	var out ProcessHandshakeResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "POST",
		Path:   "auth/client/handshakes",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ClientsService) ProcessLogout(ctx context.Context, opts ...conjoin.CallOption) (*ProcessLogoutResponse, error) {
	var out ProcessLogoutResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "POST",
		Path:   "auth/client/logout",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ClientsService) GetJwks(ctx context.Context, opts ...conjoin.CallOption) (*GetJwksResponse, error) {
	var out GetJwksResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "auth/client/.well-known/jwks.json",
		Auth:   conjoin.AuthNone,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
