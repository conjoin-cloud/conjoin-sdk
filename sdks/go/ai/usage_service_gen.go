package ai

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type UsagesService struct {
	client *conjoin.Client
}

func (s *UsagesService) ListRecords(ctx context.Context, query *ListUsageRecordsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListUsageRecordsItem], error) {
	return conjoin.List[ListUsageRecordsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/usage/records",
		Query:  query,
	}, opts...)
}

func (s *UsagesService) ReadSummary(ctx context.Context, query *ReadUsageSummaryQuery, opts ...conjoin.CallOption) (*ReadUsageSummaryResponse, error) {
	var out ReadUsageSummaryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "ai/usage/summary",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
