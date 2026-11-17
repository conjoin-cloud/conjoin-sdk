package relay

import (
	"context"

	conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
)

type EventsService struct {
	client *conjoin.Client
}

func (s *EventsService) ReadEventChannels(ctx context.Context, query *ReadEventChannelsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadEventChannelsItem], error) {
	return conjoin.List[ReadEventChannelsItem](ctx, s.client, conjoin.Operation{
		Method: "GET",
		Path:   "relay/event-channels/",
		Query:  query,
	}, opts...)
}

func (s *EventsService) CreateEventChannel(ctx context.Context, body *CreateEventChannelRequest, opts ...conjoin.CallOption) (*CreateEventChannelResponse, error) {
	var out CreateEventChannelResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/event-channels/",
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) ReadEventSubscriptions(ctx context.Context, eventChannelID string, query *ReadEventSubscriptionsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadEventSubscriptionsItem], error) {
	return conjoin.List[ReadEventSubscriptionsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/event-channels/{event_channel_id}/subscriptions",
		PathParams: []string{eventChannelID},
		Query:      query,
	}, opts...)
}

func (s *EventsService) CreateEventSubscription(ctx context.Context, eventChannelID string, body *CreateEventSubscriptionRequest, opts ...conjoin.CallOption) (*CreateEventSubscriptionResponse, error) {
	var out CreateEventSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/event-channels/{event_channel_id}/subscriptions",
		PathParams:            []string{eventChannelID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) Read(ctx context.Context, eventChannelID string, query *ReadEventsQuery, opts ...conjoin.CallOption) (*conjoin.Page[ReadEventsItem], error) {
	return conjoin.List[ReadEventsItem](ctx, s.client, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/event-channels/{event_channel_id}/events",
		PathParams: []string{eventChannelID},
		Query:      query,
	}, opts...)
}

func (s *EventsService) ReadEventChannelsCount(ctx context.Context, query *ReadEventChannelsCountQuery, opts ...conjoin.CallOption) (*ReadEventChannelsCountResponse, error) {
	var out ReadEventChannelsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method: "GET",
		Path:   "relay/event-channels/count",
		Query:  query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) UpdateEventChannel(ctx context.Context, eventChannelID string, body *UpdateEventChannelRequest, opts ...conjoin.CallOption) (*UpdateEventChannelResponse, error) {
	var out UpdateEventChannelResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/event-channels/{event_channel_id}",
		PathParams:   []string{eventChannelID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) DeleteEventChannel(ctx context.Context, eventChannelID string, opts ...conjoin.CallOption) (*DeleteEventChannelResponse, error) {
	var out DeleteEventChannelResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/event-channels/{event_channel_id}",
		PathParams: []string{eventChannelID},
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) ReadEventSubscriptionsCount(ctx context.Context, eventChannelID string, query *ReadEventSubscriptionsCountQuery, opts ...conjoin.CallOption) (*ReadEventSubscriptionsCountResponse, error) {
	var out ReadEventSubscriptionsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/event-channels/{event_channel_id}/subscriptions/count",
		PathParams: []string{eventChannelID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) UpdateEventSubscription(ctx context.Context, eventChannelID string, subscriptionID string, body *UpdateEventSubscriptionRequest, opts ...conjoin.CallOption) (*UpdateEventSubscriptionResponse, error) {
	var out UpdateEventSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:       "PATCH",
		Path:         "relay/event-channels/{event_channel_id}/subscriptions/{subscription_id}",
		PathParams:   []string{eventChannelID, subscriptionID},
		Body:         body,
		BodyRequired: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) DeleteEventSubscription(ctx context.Context, eventChannelID string, subscriptionID string, opts ...conjoin.CallOption) (*DeleteEventSubscriptionResponse, error) {
	var out DeleteEventSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "DELETE",
		Path:       "relay/event-channels/{event_channel_id}/subscriptions/{subscription_id}",
		PathParams: []string{eventChannelID, subscriptionID},
		Response:   conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) PauseEventSubscription(ctx context.Context, eventChannelID string, subscriptionID string, opts ...conjoin.CallOption) (*PauseEventSubscriptionResponse, error) {
	var out PauseEventSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/event-channels/{event_channel_id}/subscriptions/{subscription_id}/pause",
		PathParams:            []string{eventChannelID, subscriptionID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) ResumeEventSubscription(ctx context.Context, eventChannelID string, subscriptionID string, opts ...conjoin.CallOption) (*ResumeEventSubscriptionResponse, error) {
	var out ResumeEventSubscriptionResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/event-channels/{event_channel_id}/subscriptions/{subscription_id}/resume",
		PathParams:            []string{eventChannelID, subscriptionID},
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) PublishEvent(ctx context.Context, eventChannelID string, body *PublishEventRequest, opts ...conjoin.CallOption) (*PublishEventResponse, error) {
	var out PublishEventResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/event-channels/{event_channel_id}/publish",
		PathParams:            []string{eventChannelID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) ReadCount(ctx context.Context, eventChannelID string, query *ReadEventsCountQuery, opts ...conjoin.CallOption) (*ReadEventsCountResponse, error) {
	var out ReadEventsCountResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:     "GET",
		Path:       "relay/event-channels/{event_channel_id}/events/count",
		PathParams: []string{eventChannelID},
		Query:      query,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}

func (s *EventsService) Replay(ctx context.Context, eventChannelID string, body *ReplayEventsRequest, opts ...conjoin.CallOption) (*ReplayEventsResponse, error) {
	var out ReplayEventsResponse
	if err := s.client.Do(ctx, conjoin.Operation{
		Method:                "POST",
		Path:                  "relay/event-channels/{event_channel_id}/replay",
		PathParams:            []string{eventChannelID},
		Body:                  body,
		BodyRequired:          true,
		AcceptsIdempotencyKey: true,
		Response:              conjoin.ResponseBody,
	}, &out, opts...); err != nil {
		return nil, err
	}
	return &out, nil
}
