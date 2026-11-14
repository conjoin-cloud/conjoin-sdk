package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type IdentitiesService struct {
	client *conjoin.Client
}

func (s *IdentitiesService) DiscoverAccount(ctx context.Context, body *DiscoverAccountRequest, opts ...conjoin.CallOption) (*DiscoverAccountResponse, error) {
	var out DiscoverAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/discover",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *IdentitiesService) Link(ctx context.Context, accountID string, body *LinkIdentityRequest, opts ...conjoin.CallOption) (*LinkIdentityResponse, error) {
	var out LinkIdentityResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/identities/link",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *IdentitiesService) Unlink(ctx context.Context, accountID string, body *UnlinkIdentityRequest, opts ...conjoin.CallOption) error {
	return s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/identities/unlink",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, nil, opts...)
}
