package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type CreditWalletsService struct {
	client *conjoin.Client
}

func (s *CreditWalletsService) List(ctx context.Context, query *ListCreditWalletsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListCreditWalletsItem], error) {
	return conjoin.List[ListCreditWalletsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/credit-wallets/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *CreditWalletsService) Create(ctx context.Context, body *CreateCreditWalletRequest, opts ...conjoin.CallOption) (*CreateCreditWalletResponse, error) {
	var out CreateCreditWalletResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/credit-wallets/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CreditWalletsService) ListCount(ctx context.Context, query *ListCreditWalletsCountQuery, opts ...conjoin.CallOption) (*ListCreditWalletsCountResponse, error) {
	var out ListCreditWalletsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/credit-wallets/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CreditWalletsService) Update(ctx context.Context, creditWalletID string, body *UpdateCreditWalletRequest, opts ...conjoin.CallOption) (*UpdateCreditWalletResponse, error) {
	var out UpdateCreditWalletResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/credit-wallets/{credit_wallet_id}",
		PathParams:   []string{creditWalletID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CreditWalletsService) GrantCredits(ctx context.Context, creditWalletID string, body *GrantCreditsRequest, opts ...conjoin.CallOption) (*GrantCreditsResponse, error) {
	var out GrantCreditsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "billing/credit-wallets/{credit_wallet_id}/grant",
		PathParams:   []string{creditWalletID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
