package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SearchesService struct {
	client *conjoin.Client
}

func (s *SearchesService) CreateIndex(ctx context.Context, body *CreateSearchIndexRequest, opts ...conjoin.CallOption) (*CreateSearchIndexResponse, error) {
	var out CreateSearchIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/search/indexes",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SearchesService) ReadIndexes(ctx context.Context, query *ReadSearchIndexesQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadSearchIndexesItem], error) {
	return conjoin.List[ReadSearchIndexesItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/search/indexes",
		Query:  query,
	}, opts...)
}

func (s *SearchesService) DeleteIndex(ctx context.Context, indexID string, opts ...conjoin.CallOption) (*DeleteSearchIndexResponse, error) {
	var out DeleteSearchIndexResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/search/indexes/{index_id}",
		PathParams: []string{indexID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SearchesService) IndexDocument(ctx context.Context, indexID string, body *IndexSearchDocumentRequest, opts ...conjoin.CallOption) (*IndexSearchDocumentResponse, error) {
	var out IndexSearchDocumentResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/search/indexes/{index_id}/documents",
		PathParams:            []string{indexID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SearchesService) IndexDocumentBatch(ctx context.Context, indexID string, body *IndexSearchDocumentBatchRequest, opts ...conjoin.CallOption) (*IndexSearchDocumentBatchResponse, error) {
	var out IndexSearchDocumentBatchResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/search/indexes/{index_id}/documents/batch",
		PathParams:            []string{indexID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SearchesService) RemoveDocument(ctx context.Context, indexID string, documentID string, opts ...conjoin.CallOption) (*RemoveSearchDocumentResponse, error) {
	var out RemoveSearchDocumentResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/search/indexes/{index_id}/documents/{document_id}",
		PathParams: []string{indexID, documentID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SearchesService) SearchQuery(ctx context.Context, indexID string, body *SearchQueryRequest, opts ...conjoin.CallOption) (*SearchQueryResponse, error) {
	var out SearchQueryResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/search/indexes/{index_id}/query",
		PathParams:            []string{indexID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *SearchesService) AutoSuggest(ctx context.Context, indexID string, body *AutoSuggestSearchRequest, opts ...conjoin.CallOption) (*AutoSuggestSearchResponse, error) {
	var out AutoSuggestSearchResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/search/indexes/{index_id}/suggest",
		PathParams:            []string{indexID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
