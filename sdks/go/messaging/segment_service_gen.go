package messaging

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type SegmentsService struct {
	client *conjoin.Client
}

func (s *SegmentsService) CreateOne(ctx context.Context, body any, opts ...conjoin.CallOption) (any, error) {
	var out any
	err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/segments/",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}

func (s *SegmentsService) UpdateOne(ctx context.Context, segmentID string, body any, opts ...conjoin.CallOption) (any, error) {
	var out any
	err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "messaging/segments/{segment_id}",
		PathParams:   []string{segmentID},
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}

func (s *SegmentsService) DeleteOne(ctx context.Context, segmentID string, opts ...conjoin.CallOption) (any, error) {
	var out any
	err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "messaging/segments/{segment_id}",
		PathParams: []string{segmentID},
		Scopes:     []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}

func (s *SegmentsService) ListMany(ctx context.Context, body any, opts ...conjoin.CallOption) (any, error) {
	var out any
	err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "messaging/segments/retrieve",
		Body:         body,
		BodyRequired: true,
		Scopes:       []conjoin.ScopeName{conjoin.ScopeMessagingProfile},
	}, &out, opts...)
	return out, err
}
