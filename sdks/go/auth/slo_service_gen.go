package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SLOsService struct {
	client *conjoin.Client
}

func (s *SLOsService) OidcLogout(ctx context.Context, accountID string, body *OidcLogoutRequest, opts ...conjoin.CallOption) (*OidcLogoutResponse, error) {
	var out OidcLogoutResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/logout-oidc",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SLOsService) SamlSpLogout(ctx context.Context, accountID string, body *SamlSpLogoutRequest, opts ...conjoin.CallOption) (*SamlSpLogoutResponse, error) {
	var out SamlSpLogoutResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/accounts/{account_id}/logout-saml",
		PathParams:            []string{accountID},
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SLOsService) SamlIdpLogout(ctx context.Context, body *SamlIdpLogoutRequest, opts ...conjoin.CallOption) (*SamlIdpLogoutResponse, error) {
	var out SamlIdpLogoutResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "auth/saml-logout-requests",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeAuthApp},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
