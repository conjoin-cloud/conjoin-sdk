package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type APIKeysService struct {
	client *conjoin.Client
}

func (s *APIKeysService) ReadApiKeys(ctx context.Context, query *ReadApiKeysQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadApiKeysItem], error) {
	return conjoin.List[ReadApiKeysItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/api-keys/",
		Query:  query,
	}, opts...)
}

func (s *APIKeysService) CreateApiKey(ctx context.Context, body *CreateApiKeyRequest, opts ...conjoin.CallOption) (string, error) {
	var out string
	err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "cloud/api-keys/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...)
	return out, err
}

func (s *APIKeysService) ReadApiKeysCount(ctx context.Context, query *ReadApiKeysCountQuery, opts ...conjoin.CallOption) (*ReadApiKeysCountResponse, error) {
	var out ReadApiKeysCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/api-keys/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *APIKeysService) RegenerateApiKey(ctx context.Context, apiKeyID string, body *RegenerateApiKeyRequest, opts ...conjoin.CallOption) (string, error) {
	var out string
	err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "cloud/api-keys/{api_key_id}/regenerate",
		PathParams:   []string{apiKeyID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...)
	return out, err
}

func (s *APIKeysService) UpdateApiKey(ctx context.Context, apiKeyID string, body *UpdateApiKeyRequest, opts ...conjoin.CallOption) (*UpdateApiKeyResponse, error) {
	var out UpdateApiKeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/api-keys/{api_key_id}",
		PathParams:   []string{apiKeyID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *APIKeysService) DeleteApiKey(ctx context.Context, apiKeyID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "cloud/api-keys/{api_key_id}",
		PathParams: []string{apiKeyID},
	}, &out, opts...)
	return out, err
}
