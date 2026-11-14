package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type BroadcastsService struct {
	client *conjoin.Client
}

func (s *BroadcastsService) GenerateConnectionToken(ctx context.Context, opts ...conjoin.CallOption) (*GenerateBroadcastConnectionTokenResponse, error) {
	var out GenerateBroadcastConnectionTokenResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "POST",
		Path:   "relay/broadcast-connection-tokens/",
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BroadcastsService) ReadChannels(ctx context.Context, query *ReadBroadcastChannelsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadBroadcastChannelsItem], error) {
	return conjoin.List[ReadBroadcastChannelsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/broadcast-channels/",
		Query:  query,
	}, opts...)
}

func (s *BroadcastsService) CreateChannel(ctx context.Context, body *CreateBroadcastChannelRequest, opts ...conjoin.CallOption) (*CreateBroadcastChannelResponse, error) {
	var out CreateBroadcastChannelResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "relay/broadcast-channels/",
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BroadcastsService) ReadChannelsCount(ctx context.Context, query *ReadBroadcastChannelsCountQuery, opts ...conjoin.CallOption) (*ReadBroadcastChannelsCountResponse, error) {
	var out ReadBroadcastChannelsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/broadcast-channels/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BroadcastsService) UpdateChannel(ctx context.Context, broadcastChannelID string, body *UpdateBroadcastChannelRequest, opts ...conjoin.CallOption) (*UpdateBroadcastChannelResponse, error) {
	var out UpdateBroadcastChannelResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/broadcast-channels/{broadcast_channel_id}",
		PathParams:   []string{broadcastChannelID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BroadcastsService) DeleteChannel(ctx context.Context, broadcastChannelID string, opts ...conjoin.CallOption) (*DeleteBroadcastChannelResponse, error) {
	var out DeleteBroadcastChannelResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/broadcast-channels/{broadcast_channel_id}",
		PathParams: []string{broadcastChannelID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BroadcastsService) GenerateAuthToken(ctx context.Context, broadcastChannelID string, body *GenerateBroadcastAuthTokenRequest, opts ...conjoin.CallOption) (*GenerateBroadcastAuthTokenResponse, error) {
	var out GenerateBroadcastAuthTokenResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "relay/broadcast-channels/{broadcast_channel_id}/auth-tokens",
		PathParams:   []string{broadcastChannelID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BroadcastsService) PublishTo(ctx context.Context, broadcastChannelID string, body *PublishToBroadcastRequest, opts ...conjoin.CallOption) (*PublishToBroadcastResponse, error) {
	var out PublishToBroadcastResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "POST",
		Path:         "relay/broadcast-channels/{broadcast_channel_id}/publish",
		PathParams:   []string{broadcastChannelID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *BroadcastsService) ReadPresence(ctx context.Context, broadcastChannelID string, opts ...conjoin.CallOption) (*ReadBroadcastPresenceResponse, error) {
	var out ReadBroadcastPresenceResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/broadcast-channels/{broadcast_channel_id}/presence-members",
		PathParams: []string{broadcastChannelID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
