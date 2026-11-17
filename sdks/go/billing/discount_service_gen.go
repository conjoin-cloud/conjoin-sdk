package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type DiscountsService struct {
	client *conjoin.Client
}

func (s *DiscountsService) List(ctx context.Context, query *ListDiscountsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListDiscountsItem], error) {
	return conjoin.List[ListDiscountsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/discounts/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *DiscountsService) Create(ctx context.Context, body *CreateDiscountRequest, opts ...conjoin.CallOption) (*CreateDiscountResponse, error) {
	var out CreateDiscountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/discounts/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *DiscountsService) ListCount(ctx context.Context, query *ListDiscountsCountQuery, opts ...conjoin.CallOption) (*ListDiscountsCountResponse, error) {
	var out ListDiscountsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/discounts/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *DiscountsService) Delete(ctx context.Context, discountID string, opts ...conjoin.CallOption) (*DeleteDiscountResponse, error) {
	var out DeleteDiscountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "billing/discounts/{discount_id}",
		PathParams: []string{discountID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
