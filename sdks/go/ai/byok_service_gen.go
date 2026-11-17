package ai

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type BYOKsService struct {
	client *conjoin.Client
}

func (s *BYOKsService) ListByokConfigs(ctx context.Context, query *ListByokConfigsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListByokConfigsItem], error) {
	return conjoin.List[ListByokConfigsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "ai/byok-configs/",
		Query:  query,
	}, opts...)
}

func (s *BYOKsService) CreateByokConfig(ctx context.Context, body *CreateByokConfigRequest, opts ...conjoin.CallOption) (*CreateByokConfigResponse, error) {
	var out CreateByokConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/byok-configs/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BYOKsService) ListByokConfigsCount(ctx context.Context, query *ListByokConfigsCountQuery, opts ...conjoin.CallOption) (*ListByokConfigsCountResponse, error) {
	var out ListByokConfigsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "ai/byok-configs/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BYOKsService) ReadByokConfig(ctx context.Context, byokConfigID string, opts ...conjoin.CallOption) (*ReadByokConfigResponse, error) {
	var out ReadByokConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "ai/byok-configs/{byok_config_id}",
		PathParams: []string{byokConfigID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BYOKsService) UpdateByokConfig(ctx context.Context, byokConfigID string, body *UpdateByokConfigRequest, opts ...conjoin.CallOption) (*UpdateByokConfigResponse, error) {
	var out UpdateByokConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "ai/byok-configs/{byok_config_id}",
		PathParams:   []string{byokConfigID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BYOKsService) DeleteByokConfig(ctx context.Context, byokConfigID string, opts ...conjoin.CallOption) (*DeleteByokConfigResponse, error) {
	var out DeleteByokConfigResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "ai/byok-configs/{byok_config_id}",
		PathParams: []string{byokConfigID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BYOKsService) TestByokConnection(ctx context.Context, byokConfigID string, opts ...conjoin.CallOption) (*TestByokConnectionResponse, error) {
	var out TestByokConnectionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "ai/byok-configs/{byok_config_id}/test",
		PathParams:            []string{byokConfigID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
