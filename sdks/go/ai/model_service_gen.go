package ai

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type ModelsService struct {
	client *conjoin.Client
}

func (s *ModelsService) List(ctx context.Context, query *ListModelsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListModelsItem], error) {
	return conjoin.List[ListModelsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/model/models",
		Query:  query,
	}, opts...)
}

func (s *ModelsService) Read(ctx context.Context, modelID string, opts ...conjoin.CallOption) (*ReadModelResponse, error) {
	var out ReadModelResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "ai/model/models/{model_id}",
		PathParams: []string{modelID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
