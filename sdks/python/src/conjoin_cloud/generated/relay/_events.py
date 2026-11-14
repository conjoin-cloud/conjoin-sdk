from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    RelayEventsCreateEventChannelRequest,
    RelayEventsCreateEventChannelResponse,
    RelayEventsCreateEventSubscriptionRequest,
    RelayEventsCreateEventSubscriptionResponse,
    RelayEventsDeleteEventChannelResponse,
    RelayEventsDeleteEventSubscriptionResponse,
    RelayEventsPauseEventSubscriptionResponse,
    RelayEventsPublishEventRequest,
    RelayEventsPublishEventResponse,
    RelayEventsReadCountQuery,
    RelayEventsReadCountResponse,
    RelayEventsReadEventChannelsCountQuery,
    RelayEventsReadEventChannelsCountResponse,
    RelayEventsReadEventChannelsItem,
    RelayEventsReadEventChannelsQuery,
    RelayEventsReadEventSubscriptionsCountQuery,
    RelayEventsReadEventSubscriptionsCountResponse,
    RelayEventsReadEventSubscriptionsItem,
    RelayEventsReadEventSubscriptionsQuery,
    RelayEventsReadItem,
    RelayEventsReadQuery,
    RelayEventsReplayRequest,
    RelayEventsReplayResponse,
    RelayEventsResumeEventSubscriptionResponse,
    RelayEventsUpdateEventChannelRequest,
    RelayEventsUpdateEventChannelResponse,
    RelayEventsUpdateEventSubscriptionRequest,
    RelayEventsUpdateEventSubscriptionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelayEventsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_event_channels(
        self,
        query: RelayEventsReadEventChannelsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayEventsReadEventChannelsItem]:
        return self._client.request(
            'GET',
            'relay/event-channels/',
            query=query,
            cast_to=Page[RelayEventsReadEventChannelsItem],
            request_options=request_options,
        )

    def create_event_channel(
        self,
        data: RelayEventsCreateEventChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsCreateEventChannelResponse:
        return self._client.request(
            'POST',
            'relay/event-channels/',
            body=data,
            cast_to=RelayEventsCreateEventChannelResponse,
            request_options=request_options,
        )

    def read_event_subscriptions(
        self,
        event_channel_id: str,
        query: RelayEventsReadEventSubscriptionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayEventsReadEventSubscriptionsItem]:
        return self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions',
            query=query,
            cast_to=Page[RelayEventsReadEventSubscriptionsItem],
            request_options=request_options,
        )

    def create_event_subscription(
        self,
        event_channel_id: str,
        data: RelayEventsCreateEventSubscriptionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsCreateEventSubscriptionResponse:
        return self._client.request(
            'POST',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions',
            body=data,
            cast_to=RelayEventsCreateEventSubscriptionResponse,
            request_options=request_options,
        )

    def read(
        self,
        event_channel_id: str,
        query: RelayEventsReadQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayEventsReadItem]:
        return self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/events',
            query=query,
            cast_to=Page[RelayEventsReadItem],
            request_options=request_options,
        )

    def read_event_channels_count(
        self,
        query: RelayEventsReadEventChannelsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReadEventChannelsCountResponse:
        return self._client.request(
            'GET',
            'relay/event-channels/count',
            query=query,
            cast_to=RelayEventsReadEventChannelsCountResponse,
            request_options=request_options,
        )

    def update_event_channel(
        self,
        event_channel_id: str,
        data: RelayEventsUpdateEventChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsUpdateEventChannelResponse:
        return self._client.request(
            'PATCH',
            f'relay/event-channels/{encode_path_param(event_channel_id)}',
            body=data,
            cast_to=RelayEventsUpdateEventChannelResponse,
            request_options=request_options,
        )

    def delete_event_channel(
        self,
        event_channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsDeleteEventChannelResponse:
        return self._client.request(
            'DELETE',
            f'relay/event-channels/{encode_path_param(event_channel_id)}',
            cast_to=RelayEventsDeleteEventChannelResponse,
            request_options=request_options,
        )

    def read_event_subscriptions_count(
        self,
        event_channel_id: str,
        query: RelayEventsReadEventSubscriptionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReadEventSubscriptionsCountResponse:
        return self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions/count',
            query=query,
            cast_to=RelayEventsReadEventSubscriptionsCountResponse,
            request_options=request_options,
        )

    def update_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        data: RelayEventsUpdateEventSubscriptionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsUpdateEventSubscriptionResponse:
        return self._client.request(
            'PATCH',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}'
            ),
            body=data,
            cast_to=RelayEventsUpdateEventSubscriptionResponse,
            request_options=request_options,
        )

    def delete_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsDeleteEventSubscriptionResponse:
        return self._client.request(
            'DELETE',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}'
            ),
            cast_to=RelayEventsDeleteEventSubscriptionResponse,
            request_options=request_options,
            unwrap_data=False,
        )

    def pause_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsPauseEventSubscriptionResponse:
        return self._client.request(
            'POST',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}/pause'
            ),
            cast_to=RelayEventsPauseEventSubscriptionResponse,
            request_options=request_options,
        )

    def resume_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsResumeEventSubscriptionResponse:
        return self._client.request(
            'POST',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}/resume'
            ),
            cast_to=RelayEventsResumeEventSubscriptionResponse,
            request_options=request_options,
        )

    def publish_event(
        self,
        event_channel_id: str,
        data: RelayEventsPublishEventRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsPublishEventResponse:
        return self._client.request(
            'POST',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/publish',
            body=data,
            cast_to=RelayEventsPublishEventResponse,
            request_options=request_options,
        )

    def read_count(
        self,
        event_channel_id: str,
        query: RelayEventsReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReadCountResponse:
        return self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/events/count',
            query=query,
            cast_to=RelayEventsReadCountResponse,
            request_options=request_options,
        )

    def replay(
        self,
        event_channel_id: str,
        data: RelayEventsReplayRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReplayResponse:
        return self._client.request(
            'POST',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/replay',
            body=data,
            cast_to=RelayEventsReplayResponse,
            request_options=request_options,
            unwrap_data=False,
        )


class AsyncRelayEventsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_event_channels(
        self,
        query: RelayEventsReadEventChannelsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayEventsReadEventChannelsItem]:
        return await self._client.request(
            'GET',
            'relay/event-channels/',
            query=query,
            cast_to=AsyncPage[RelayEventsReadEventChannelsItem],
            request_options=request_options,
        )

    async def create_event_channel(
        self,
        data: RelayEventsCreateEventChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsCreateEventChannelResponse:
        return await self._client.request(
            'POST',
            'relay/event-channels/',
            body=data,
            cast_to=RelayEventsCreateEventChannelResponse,
            request_options=request_options,
        )

    async def read_event_subscriptions(
        self,
        event_channel_id: str,
        query: RelayEventsReadEventSubscriptionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayEventsReadEventSubscriptionsItem]:
        return await self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions',
            query=query,
            cast_to=AsyncPage[RelayEventsReadEventSubscriptionsItem],
            request_options=request_options,
        )

    async def create_event_subscription(
        self,
        event_channel_id: str,
        data: RelayEventsCreateEventSubscriptionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsCreateEventSubscriptionResponse:
        return await self._client.request(
            'POST',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions',
            body=data,
            cast_to=RelayEventsCreateEventSubscriptionResponse,
            request_options=request_options,
        )

    async def read(
        self,
        event_channel_id: str,
        query: RelayEventsReadQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayEventsReadItem]:
        return await self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/events',
            query=query,
            cast_to=AsyncPage[RelayEventsReadItem],
            request_options=request_options,
        )

    async def read_event_channels_count(
        self,
        query: RelayEventsReadEventChannelsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReadEventChannelsCountResponse:
        return await self._client.request(
            'GET',
            'relay/event-channels/count',
            query=query,
            cast_to=RelayEventsReadEventChannelsCountResponse,
            request_options=request_options,
        )

    async def update_event_channel(
        self,
        event_channel_id: str,
        data: RelayEventsUpdateEventChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsUpdateEventChannelResponse:
        return await self._client.request(
            'PATCH',
            f'relay/event-channels/{encode_path_param(event_channel_id)}',
            body=data,
            cast_to=RelayEventsUpdateEventChannelResponse,
            request_options=request_options,
        )

    async def delete_event_channel(
        self,
        event_channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsDeleteEventChannelResponse:
        return await self._client.request(
            'DELETE',
            f'relay/event-channels/{encode_path_param(event_channel_id)}',
            cast_to=RelayEventsDeleteEventChannelResponse,
            request_options=request_options,
        )

    async def read_event_subscriptions_count(
        self,
        event_channel_id: str,
        query: RelayEventsReadEventSubscriptionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReadEventSubscriptionsCountResponse:
        return await self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions/count',
            query=query,
            cast_to=RelayEventsReadEventSubscriptionsCountResponse,
            request_options=request_options,
        )

    async def update_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        data: RelayEventsUpdateEventSubscriptionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsUpdateEventSubscriptionResponse:
        return await self._client.request(
            'PATCH',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}'
            ),
            body=data,
            cast_to=RelayEventsUpdateEventSubscriptionResponse,
            request_options=request_options,
        )

    async def delete_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsDeleteEventSubscriptionResponse:
        return await self._client.request(
            'DELETE',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}'
            ),
            cast_to=RelayEventsDeleteEventSubscriptionResponse,
            request_options=request_options,
            unwrap_data=False,
        )

    async def pause_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsPauseEventSubscriptionResponse:
        return await self._client.request(
            'POST',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}/pause'
            ),
            cast_to=RelayEventsPauseEventSubscriptionResponse,
            request_options=request_options,
        )

    async def resume_event_subscription(
        self,
        event_channel_id: str,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsResumeEventSubscriptionResponse:
        return await self._client.request(
            'POST',
            (
                f'relay/event-channels/{encode_path_param(event_channel_id)}/subscriptions'
                f'/{encode_path_param(subscription_id)}/resume'
            ),
            cast_to=RelayEventsResumeEventSubscriptionResponse,
            request_options=request_options,
        )

    async def publish_event(
        self,
        event_channel_id: str,
        data: RelayEventsPublishEventRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsPublishEventResponse:
        return await self._client.request(
            'POST',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/publish',
            body=data,
            cast_to=RelayEventsPublishEventResponse,
            request_options=request_options,
        )

    async def read_count(
        self,
        event_channel_id: str,
        query: RelayEventsReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReadCountResponse:
        return await self._client.request(
            'GET',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/events/count',
            query=query,
            cast_to=RelayEventsReadCountResponse,
            request_options=request_options,
        )

    async def replay(
        self,
        event_channel_id: str,
        data: RelayEventsReplayRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayEventsReplayResponse:
        return await self._client.request(
            'POST',
            f'relay/event-channels/{encode_path_param(event_channel_id)}/replay',
            body=data,
            cast_to=RelayEventsReplayResponse,
            request_options=request_options,
            unwrap_data=False,
        )
