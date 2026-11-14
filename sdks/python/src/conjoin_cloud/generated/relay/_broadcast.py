from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    RelayBroadcastCreateChannelRequest,
    RelayBroadcastCreateChannelResponse,
    RelayBroadcastDeleteChannelResponse,
    RelayBroadcastGenerateAuthTokenRequest,
    RelayBroadcastGenerateAuthTokenResponse,
    RelayBroadcastGenerateConnectionTokenResponse,
    RelayBroadcastPublishToRequest,
    RelayBroadcastPublishToResponse,
    RelayBroadcastReadChannelsCountQuery,
    RelayBroadcastReadChannelsCountResponse,
    RelayBroadcastReadChannelsItem,
    RelayBroadcastReadChannelsQuery,
    RelayBroadcastReadPresenceResponse,
    RelayBroadcastUpdateChannelRequest,
    RelayBroadcastUpdateChannelResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelayBroadcastsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def generate_connection_token(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastGenerateConnectionTokenResponse:
        return self._client.request(
            'POST',
            'relay/broadcast-connection-tokens/',
            cast_to=RelayBroadcastGenerateConnectionTokenResponse,
            request_options=request_options,
        )

    def read_channels(
        self,
        query: RelayBroadcastReadChannelsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayBroadcastReadChannelsItem]:
        return self._client.request(
            'GET',
            'relay/broadcast-channels/',
            query=query,
            cast_to=Page[RelayBroadcastReadChannelsItem],
            request_options=request_options,
        )

    def create_channel(
        self,
        data: RelayBroadcastCreateChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastCreateChannelResponse:
        return self._client.request(
            'POST',
            'relay/broadcast-channels/',
            body=data,
            cast_to=RelayBroadcastCreateChannelResponse,
            request_options=request_options,
        )

    def read_channels_count(
        self,
        query: RelayBroadcastReadChannelsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastReadChannelsCountResponse:
        return self._client.request(
            'GET',
            'relay/broadcast-channels/count',
            query=query,
            cast_to=RelayBroadcastReadChannelsCountResponse,
            request_options=request_options,
        )

    def update_channel(
        self,
        broadcast_channel_id: str,
        data: RelayBroadcastUpdateChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastUpdateChannelResponse:
        return self._client.request(
            'PATCH',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}',
            body=data,
            cast_to=RelayBroadcastUpdateChannelResponse,
            request_options=request_options,
        )

    def delete_channel(
        self,
        broadcast_channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastDeleteChannelResponse:
        return self._client.request(
            'DELETE',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}',
            cast_to=RelayBroadcastDeleteChannelResponse,
            request_options=request_options,
        )

    def generate_auth_token(
        self,
        broadcast_channel_id: str,
        data: RelayBroadcastGenerateAuthTokenRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastGenerateAuthTokenResponse:
        return self._client.request(
            'POST',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}/auth-tokens',
            body=data,
            cast_to=RelayBroadcastGenerateAuthTokenResponse,
            request_options=request_options,
        )

    def publish_to(
        self,
        broadcast_channel_id: str,
        data: RelayBroadcastPublishToRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastPublishToResponse:
        return self._client.request(
            'POST',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}/publish',
            body=data,
            cast_to=RelayBroadcastPublishToResponse,
            request_options=request_options,
        )

    def read_presence(
        self,
        broadcast_channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastReadPresenceResponse:
        return self._client.request(
            'GET',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}/presence-members',
            cast_to=RelayBroadcastReadPresenceResponse,
            request_options=request_options,
        )


class AsyncRelayBroadcastsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def generate_connection_token(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastGenerateConnectionTokenResponse:
        return await self._client.request(
            'POST',
            'relay/broadcast-connection-tokens/',
            cast_to=RelayBroadcastGenerateConnectionTokenResponse,
            request_options=request_options,
        )

    async def read_channels(
        self,
        query: RelayBroadcastReadChannelsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayBroadcastReadChannelsItem]:
        return await self._client.request(
            'GET',
            'relay/broadcast-channels/',
            query=query,
            cast_to=AsyncPage[RelayBroadcastReadChannelsItem],
            request_options=request_options,
        )

    async def create_channel(
        self,
        data: RelayBroadcastCreateChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastCreateChannelResponse:
        return await self._client.request(
            'POST',
            'relay/broadcast-channels/',
            body=data,
            cast_to=RelayBroadcastCreateChannelResponse,
            request_options=request_options,
        )

    async def read_channels_count(
        self,
        query: RelayBroadcastReadChannelsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastReadChannelsCountResponse:
        return await self._client.request(
            'GET',
            'relay/broadcast-channels/count',
            query=query,
            cast_to=RelayBroadcastReadChannelsCountResponse,
            request_options=request_options,
        )

    async def update_channel(
        self,
        broadcast_channel_id: str,
        data: RelayBroadcastUpdateChannelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastUpdateChannelResponse:
        return await self._client.request(
            'PATCH',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}',
            body=data,
            cast_to=RelayBroadcastUpdateChannelResponse,
            request_options=request_options,
        )

    async def delete_channel(
        self,
        broadcast_channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastDeleteChannelResponse:
        return await self._client.request(
            'DELETE',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}',
            cast_to=RelayBroadcastDeleteChannelResponse,
            request_options=request_options,
        )

    async def generate_auth_token(
        self,
        broadcast_channel_id: str,
        data: RelayBroadcastGenerateAuthTokenRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastGenerateAuthTokenResponse:
        return await self._client.request(
            'POST',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}/auth-tokens',
            body=data,
            cast_to=RelayBroadcastGenerateAuthTokenResponse,
            request_options=request_options,
        )

    async def publish_to(
        self,
        broadcast_channel_id: str,
        data: RelayBroadcastPublishToRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastPublishToResponse:
        return await self._client.request(
            'POST',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}/publish',
            body=data,
            cast_to=RelayBroadcastPublishToResponse,
            request_options=request_options,
        )

    async def read_presence(
        self,
        broadcast_channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayBroadcastReadPresenceResponse:
        return await self._client.request(
            'GET',
            f'relay/broadcast-channels/{encode_path_param(broadcast_channel_id)}/presence-members',
            cast_to=RelayBroadcastReadPresenceResponse,
            request_options=request_options,
        )
