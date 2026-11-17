package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type RefundsService struct {
	client *conjoin.Client
}

func (s *RefundsService) List(ctx context.Context, query *ListRefundsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListRefundsItem], error) {
	return conjoin.List[ListRefundsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/refunds/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *RefundsService) Create(ctx context.Context, body *CreateRefundRequest, opts ...conjoin.CallOption) (*CreateRefundResponse, error) {
	var out CreateRefundResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/refunds/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *RefundsService) ListCount(ctx context.Context, query *ListRefundsCountQuery, opts ...conjoin.CallOption) (*ListRefundsCountResponse, error) {
	var out ListRefundsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/refunds/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
