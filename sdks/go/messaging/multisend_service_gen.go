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
		Path:                  "messaging/multisend/send",
		Body:                  body,
		BodyRequired:          true,
		Scopes:                []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *MultisendsService) Read(ctx context.Context, messageID string, opts ...conjoin.CallOption) (*ReadMultisendResponse, error) {
	var out ReadMultisendResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "messaging/multisend/{message_id}",
		PathParams: []string{messageID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
