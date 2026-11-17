package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type CouponsService struct {
	client *conjoin.Client
}

func (s *CouponsService) List(ctx context.Context, query *ListCouponsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListCouponsItem], error) {
	return conjoin.List[ListCouponsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/coupons/",
		Query:  query,
	}, opts...)
}

func (s *CouponsService) Create(ctx context.Context, body *CreateCouponRequest, opts ...conjoin.CallOption) (*CreateCouponResponse, error) {
	var out CreateCouponResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/coupons/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CouponsService) ListCount(ctx context.Context, query *ListCouponsCountQuery, opts ...conjoin.CallOption) (*ListCouponsCountResponse, error) {
	var out ListCouponsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/coupons/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CouponsService) Update(ctx context.Context, couponID string, body *UpdateCouponRequest, opts ...conjoin.CallOption) (*UpdateCouponResponse, error) {
	var out UpdateCouponResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "billing/coupons/{coupon_id}",
		PathParams:   []string{couponID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *CouponsService) Delete(ctx context.Context, couponID string, opts ...conjoin.CallOption) (*DeleteCouponResponse, error) {
	var out DeleteCouponResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "billing/coupons/{coupon_id}",
		PathParams: []string{couponID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
