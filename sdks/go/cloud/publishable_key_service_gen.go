package cloud

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type PublishableKeysService struct {
	client *conjoin.Client
}

func (s *PublishableKeysService) List(ctx context.Context, query *ListPublishableKeysQuery, opts ...conjoin.CallOption) (*conjoin.Page[ListPublishableKeysItem], error) {
	return conjoin.List[ListPublishableKeysItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/publishable-keys/",
		Query:  query,
	}, opts...)
}

func (s *PublishableKeysService) Create(ctx context.Context, opts ...conjoin.CallOption) (string, error) {
	var out string
	err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "cloud/publishable-keys/",
		AcceptsIdempotencyKey: true,
	}, &out, opts...)
	return out, err
}

func (s *PublishableKeysService) ListCount(ctx context.Context, query *ListPublishableKeysCountQuery, opts ...conjoin.CallOption) (*ListPublishableKeysCountResponse, error) {
	var out ListPublishableKeysCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "cloud/publishable-keys/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PublishableKeysService) Rotate(ctx context.Context, publishableKeyID string, opts ...conjoin.CallOption) (string, error) {
	var out string
	err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "cloud/publishable-keys/{publishable_key_id}/rotate",
		PathParams:            []string{publishableKeyID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...)
	return out, err
}

func (s *PublishableKeysService) Update(ctx context.Context, publishableKeyID string, body *UpdatePublishableKeyRequest, opts ...conjoin.CallOption) (*UpdatePublishableKeyResponse, error) {
	var out UpdatePublishableKeyResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "cloud/publishable-keys/{publishable_key_id}",
		PathParams:   []string{publishableKeyID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *PublishableKeysService) Revoke(ctx context.Context, publishableKeyID string, opts ...conjoin.CallOption) (bool, error) {
	var out bool
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "cloud/publishable-keys/{publishable_key_id}",
		PathParams: []string{publishableKeyID},
	}, &out, opts...)
	return out, err
}
