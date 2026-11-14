package auth

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type AccountsService struct {
	client *conjoin.Client
}

func (s *AccountsService) BatchLookup(ctx context.Context, body *BatchLookupAccountsRequest, opts ...conjoin.CallOption) ([]BatchLookupAccountsResponseItem, error) {
	var out []BatchLookupAccountsResponseItem
	err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "auth/client/account-lookups/",
		Body:         body,
		BodyRequired: true,
		Auth:         conjoin.AuthNone,
	}, &out, opts...)
	return out, err
}
