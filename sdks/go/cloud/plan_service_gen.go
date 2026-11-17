package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PlansService struct {
	client *conjoin.Client
}

func (s *PlansService) ReadAccount(ctx context.Context, opts ...conjoin.CallOption) (*ReadAccountPlanResponse, error) {
	var out ReadAccountPlanResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/account/plan",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PlansService) List(ctx context.Context, query *ReadPlansQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadPlansItem], error) {
	return conjoin.List[ReadPlansItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/plans/",
		Query:  query,
	}, opts...)
}

func (s *PlansService) ReadCount(ctx context.Context, query *ReadPlansCountQuery, opts ...conjoin.CallOption) (*ReadPlansCountResponse, error) {
	var out ReadPlansCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/plans/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PlansService) Read(ctx context.Context, planID string, opts ...conjoin.CallOption) (*ReadPlanResponse, error) {
	var out ReadPlanResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "cloud/plans/{plan_id}",
		PathParams: []string{planID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
