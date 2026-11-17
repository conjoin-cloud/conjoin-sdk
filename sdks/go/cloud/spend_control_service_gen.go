package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SpendControlsService struct {
	client *conjoin.Client
}

func (s *SpendControlsService) Read(ctx context.Context, opts ...conjoin.CallOption) (*ReadSpendControlResponse, error) {
	var out ReadSpendControlResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/spend-control/",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SpendControlsService) Update(ctx context.Context, body *UpdateSpendControlRequest, opts ...conjoin.CallOption) (*UpdateSpendControlResponse, error) {
	var out UpdateSpendControlResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/spend-control/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SpendControlsService) ReadUsage(ctx context.Context, opts ...conjoin.CallOption) (*ReadSpendControlUsageResponse, error) {
	var out ReadSpendControlUsageResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/spend-control/usage",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
