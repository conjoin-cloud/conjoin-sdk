package ai

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ContextsService struct {
	client *conjoin.Client
}

func (s *ContextsService) CreateIndex(ctx context.Context, body *CreateContextIndexRequest, opts ...conjoin.CallOption) (*CreateContextIndexResponse, error) {
	var out CreateContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/context/indexes",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) ListIndexes(ctx context.Context, query *ListContextIndexesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListContextIndexesItem], error) {
	return conjoin.List[ListContextIndexesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/context/indexes",
		Query:  query,
	}, opts...)
}

func (s *ContextsService) ReadIndex(ctx context.Context, indexID string, opts ...conjoin.CallOption) (*ReadContextIndexResponse, error) {
	var out ReadContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "ai/context/indexes/{index_id}",
		PathParams: []string{indexID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) DeleteIndex(ctx context.Context, indexID string, opts ...conjoin.CallOption) (*DeleteContextIndexResponse, error) {
	var out DeleteContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "ai/context/indexes/{index_id}",
		PathParams: []string{indexID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) SyncIndex(ctx context.Context, indexID string, opts ...conjoin.CallOption) (*SyncContextIndexResponse, error) {
	var out SyncContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/context/indexes/{index_id}/sync",
		PathParams:            []string{indexID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) Query(ctx context.Context, body *QueryContextRequest, opts ...conjoin.CallOption) (*QueryContextResponse, error) {
	var out QueryContextResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/context/query",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) ListQueryLogs(ctx context.Context, query *ListContextQueryLogsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListContextQueryLogsItem], error) {
	return conjoin.List[ListContextQueryLogsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/context/query-logs",
		Query:  query,
	}, opts...)
}
