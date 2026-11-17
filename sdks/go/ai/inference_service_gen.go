package ai

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type InferencesService struct {
	client *conjoin.Client
}

func (s *InferencesService) CreateChatCompletion(ctx context.Context, body *CreateChatCompletionRequest, opts ...conjoin.CallOption) (*CreateChatCompletionResponse, error) {
	var out CreateChatCompletionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/inference/chat/completions",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InferencesService) CreateAiMultiModel(ctx context.Context, body *CreateMultiModelInferenceRequest, opts ...conjoin.CallOption) (*CreateMultiModelInferenceResponse, error) {
	var out CreateMultiModelInferenceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/multi-model-inferences/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InferencesService) CreateAiBestOfN(ctx context.Context, body *CreateBestOfNInferenceRequest, opts ...conjoin.CallOption) (*CreateBestOfNInferenceResponse, error) {
	var out CreateBestOfNInferenceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/best-of-n-inferences/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InferencesService) ListRequests(ctx context.Context, query *ListInferenceRequestsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListInferenceRequestsItem], error) {
	return conjoin.List[ListInferenceRequestsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/inference-requests/",
		Query:  query,
	}, opts...)
}

func (s *InferencesService) ListRequestsCount(ctx context.Context, query *ListInferenceRequestsCountQuery, opts ...conjoin.CallOption) (*ListInferenceRequestsCountResponse, error) {
	var out ListInferenceRequestsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "ai/inference-requests/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *InferencesService) ReadRequest(ctx context.Context, inferenceRequestID string, opts ...conjoin.CallOption) (*ReadInferenceRequestResponse, error) {
	var out ReadInferenceRequestResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "ai/inference-requests/{inference_request_id}",
		PathParams: []string{inferenceRequestID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
