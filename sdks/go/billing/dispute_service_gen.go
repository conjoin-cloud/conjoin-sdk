package billing

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type DisputesService struct {
	client *conjoin.Client
}

func (s *DisputesService) List(ctx context.Context, query *ListDisputesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListDisputesItem], error) {
	return conjoin.List[ListDisputesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "billing/disputes/",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, opts...)
}

func (s *DisputesService) ListCount(ctx context.Context, query *ListDisputesCountQuery, opts ...conjoin.CallOption) (*ListDisputesCountResponse, error) {
	var out ListDisputesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "billing/disputes/count",
		Query:  query,
		Scopes: []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *DisputesService) Get(ctx context.Context, disputeID string, opts ...conjoin.CallOption) (*GetDisputeResponse, error) {
	var out GetDisputeResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "billing/disputes/{dispute_id}",
		PathParams: []string{disputeID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeBillingEntity},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
