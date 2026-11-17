package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type MultisendsService struct {
	client *conjoin.Client
}

func (s *MultisendsService) Create(ctx context.Context, body *CreateMultisendRequest, opts ...conjoin.CallOption) (*CreateMultisendResponse, error) {
	var out CreateMultisendResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "messaging/broadcasts/",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MultisendsService) Read(ctx context.Context, broadcastID string, opts ...conjoin.CallOption) (*ReadMultisendResponse, error) {
	var out ReadMultisendResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/broadcasts/{broadcast_id}",
		PathParams: []string{broadcastID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
