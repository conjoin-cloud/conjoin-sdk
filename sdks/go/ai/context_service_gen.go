package ai

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ContextsService struct {
	client *conjoin.Client
}

func (s *ContextsService) ListIndexes(ctx context.Context, query *ListContextIndexesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListContextIndexesItem], error) {
	return conjoin.List[ListContextIndexesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/context-indexes/",
		Query:  query,
	}, opts...)
}

func (s *ContextsService) CreateIndex(ctx context.Context, body *CreateContextIndexRequest, opts ...conjoin.CallOption) (*CreateContextIndexResponse, error) {
	var out CreateContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/context-indexes/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) ListIndexesCount(ctx context.Context, query *ListContextIndexesCountQuery, opts ...conjoin.CallOption) (*ListContextIndexesCountResponse, error) {
	var out ListContextIndexesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "ai/context-indexes/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) ReadIndex(ctx context.Context, contextIndexID string, opts ...conjoin.CallOption) (*ReadContextIndexResponse, error) {
	var out ReadContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "ai/context-indexes/{context_index_id}",
		PathParams: []string{contextIndexID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) DeleteIndex(ctx context.Context, contextIndexID string, opts ...conjoin.CallOption) (*DeleteContextIndexResponse, error) {
	var out DeleteContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "ai/context-indexes/{context_index_id}",
		PathParams: []string{contextIndexID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) SyncIndex(ctx context.Context, contextIndexID string, opts ...conjoin.CallOption) (*SyncContextIndexResponse, error) {
	var out SyncContextIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/context-indexes/{context_index_id}/sync",
		PathParams:            []string{contextIndexID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) ListQueries(ctx context.Context, query *ListContextQueriesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListContextQueriesItem], error) {
	return conjoin.List[ListContextQueriesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/context-queries/",
		Query:  query,
	}, opts...)
}

func (s *ContextsService) CreateQuery(ctx context.Context, body *CreateContextQueryRequest, opts ...conjoin.CallOption) (*CreateContextQueryResponse, error) {
	var out CreateContextQueryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/context-queries/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *ContextsService) ListQueriesCount(ctx context.Context, query *ListContextQueriesCountQuery, opts ...conjoin.CallOption) (*ListContextQueriesCountResponse, error) {
	var out ListContextQueriesCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "ai/context-queries/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
