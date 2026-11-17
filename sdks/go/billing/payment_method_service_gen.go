package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PaymentMethodsService struct {
	client *conjoin.Client
}

func (s *PaymentMethodsService) List(ctx context.Context, query *ListPaymentMethodsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPaymentMethodsItem], error) {
	return conjoin.List[ListPaymentMethodsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/payment-methods/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *PaymentMethodsService) Create(ctx context.Context, body *CreatePaymentMethodRequest, opts ...conjoin.CallOption) (string, error) {
	var out string
	err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/payment-methods/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...)
	return out, err
}

func (s *PaymentMethodsService) ListCount(ctx context.Context, query *ListPaymentMethodsCountQuery, opts ...conjoin.CallOption) (*ListPaymentMethodsCountResponse, error) {
	var out ListPaymentMethodsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/payment-methods/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PaymentMethodsService) Delete(ctx context.Context, paymentMethodID string, opts ...conjoin.CallOption) (*DeletePaymentMethodResponse, error) {
	var out DeletePaymentMethodResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "billing/payment-methods/{payment_method_id}",
		PathParams: []string{paymentMethodID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
