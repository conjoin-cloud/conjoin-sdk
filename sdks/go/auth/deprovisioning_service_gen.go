package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type DeprovisioningsService struct {
	client *conjoin.Client
}

func (s *DeprovisioningsService) DeprovisionAccount(ctx context.Context, accountID string, body *DeprovisionAccountRequest, opts ...conjoin.CallOption) (*DeprovisionAccountResponse, error) {
	var out DeprovisionAccountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/accounts/{account_id}/deprovision",
		PathParams:   []string{accountID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeAuthApp},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
