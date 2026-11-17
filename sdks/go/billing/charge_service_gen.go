package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ChargesService struct {
	client *conjoin.Client
}

func (s *ChargesService) List(ctx context.Context, query *ListChargesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListChargesItem], error) {
	return conjoin.List[ListChargesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/charges/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *ChargesService) ListCount(ctx context.Context, query *ListChargesCountQuery, opts ...conjoin.CallOption) (*ListChargesCountResponse, error) {
	var out ListChargesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/charges/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
