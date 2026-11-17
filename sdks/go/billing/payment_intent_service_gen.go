package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PaymentIntentsService struct {
	client *conjoin.Client
}

func (s *PaymentIntentsService) List(ctx context.Context, query *ListPaymentIntentsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPaymentIntentsItem], error) {
	return conjoin.List[ListPaymentIntentsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/payment-intents/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *PaymentIntentsService) Create(ctx context.Context, body *CreatePaymentIntentRequest, opts ...conjoin.CallOption) (string, error) {
	var out string
	err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/payment-intents/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...)
	return out, err
}

func (s *PaymentIntentsService) ListCount(ctx context.Context, query *ListPaymentIntentsCountQuery, opts ...conjoin.CallOption) (*ListPaymentIntentsCountResponse, error) {
	var out ListPaymentIntentsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/payment-intents/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PaymentIntentsService) Verify(ctx context.Context, paymentIntentID string, opts ...conjoin.CallOption) (*VerifyPaymentIntentResponse, error) {
	var out VerifyPaymentIntentResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "billing/payment-intents/{payment_intent_id}/verify",
		PathParams:            []string{paymentIntentID},
		Scopes:                []conjoin.ScopeName{conjoin.ScopeBillingEntity},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
