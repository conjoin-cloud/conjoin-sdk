package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type AuditsService struct {
	client *conjoin.Client
}

func (s *AuditsService) ReadLogs(ctx context.Context, query *ReadAuditLogsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadAuditLogsItem], error) {
	return conjoin.List[ReadAuditLogsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/audit-logs/",
		Query:  query,
	}, opts...)
}

func (s *AuditsService) ReadLogsCount(ctx context.Context, query *ReadAuditLogsCountQuery, opts ...conjoin.CallOption) (*ReadAuditLogsCountResponse, error) {
	var out ReadAuditLogsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/audit-logs/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *AuditsService) ReadStats(ctx context.Context, query *ReadAuditStatsQuery, opts ...conjoin.CallOption) (*ReadAuditStatsResponse, error) {
	var out ReadAuditStatsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:        "GET",
		Path:          "cloud/audit-logs/stats",
		Query:         query,
		QueryRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
