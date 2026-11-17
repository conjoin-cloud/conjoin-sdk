package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ReceiptsService struct {
	client *conjoin.Client
}

func (s *ReceiptsService) List(ctx context.Context, query *ListReceiptsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListReceiptsItem], error) {
	return conjoin.List[ListReceiptsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/receipts/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *ReceiptsService) ListCount(ctx context.Context, query *ListReceiptsCountQuery, opts ...conjoin.CallOption) (*ListReceiptsCountResponse, error) {
	var out ListReceiptsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/receipts/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ReceiptsService) Read(ctx context.Context, receiptID string, opts ...conjoin.CallOption) (*ReadReceiptResponse, error) {
	var out ReadReceiptResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/receipts/{receipt_id}",
		PathParams: []string{receiptID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
