from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingProfileCloseResponse,
    MessagingProfileCreateRequest,
    MessagingProfileCreateResponse,
    MessagingProfileDeleteResponse,
    MessagingProfileDisableChannelsRequest,
    MessagingProfileDisableChannelsResponse,
    MessagingProfileDisableResponse,
    MessagingProfileEnableChannelsRequest,
    MessagingProfileEnableChannelsResponse,
    MessagingProfileEnableResponse,
    MessagingProfileListCountQuery,
    MessagingProfileListCountResponse,
    MessagingProfileListItem,
    MessagingProfileListQuery,
    MessagingProfileReadResponse,
    MessagingProfileUpdateRequest,
    MessagingProfileUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingProfilesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: MessagingProfileListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingProfileListItem]:
        return self._client.request(
            'GET',
            'messaging/profiles/',
            query=query,
            cast_to=Page[MessagingProfileListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: MessagingProfileCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCreateResponse:
        return self._client.request(
            'POST',
            'messaging/profiles/',
            body=data,
            cast_to=MessagingProfileCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: MessagingProfileListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileListCountResponse:
        return self._client.request(
            'GET',
            'messaging/profiles/count',
            query=query,
            cast_to=MessagingProfileListCountResponse,
            request_options=request_options,
        )

    def enable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileEnableResponse:
        return self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/enable',
            cast_to=MessagingProfileEnableResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def disable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDisableResponse:
        return self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/disable',
            cast_to=MessagingProfileDisableResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def enable_channels(
        self,
        profile_id: str,
        data: MessagingProfileEnableChannelsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileEnableChannelsResponse:
        return self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/enable-channels',
            body=data,
            cast_to=MessagingProfileEnableChannelsResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def disable_channels(
        self,
        profile_id: str,
        data: MessagingProfileDisableChannelsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDisableChannelsResponse:
        return self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/disable-channels',
            body=data,
            cast_to=MessagingProfileDisableChannelsResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def close(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCloseResponse:
        return self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/close',
            cast_to=MessagingProfileCloseResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileReadResponse:
        return self._client.request(
            'GET',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        profile_id: str,
        data: MessagingProfileUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            body=data,
            cast_to=MessagingProfileUpdateResponse,
            request_options=request_options,
        )

    def delete(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileDeleteResponse,
            request_options=request_options,
        )


class AsyncMessagingProfilesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: MessagingProfileListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingProfileListItem]:
        return await self._client.request(
            'GET',
            'messaging/profiles/',
            query=query,
            cast_to=AsyncPage[MessagingProfileListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: MessagingProfileCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/profiles/',
            body=data,
            cast_to=MessagingProfileCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: MessagingProfileListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileListCountResponse:
        return await self._client.request(
            'GET',
            'messaging/profiles/count',
            query=query,
            cast_to=MessagingProfileListCountResponse,
            request_options=request_options,
        )

    async def enable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileEnableResponse:
        return await self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/enable',
            cast_to=MessagingProfileEnableResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def disable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDisableResponse:
        return await self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/disable',
            cast_to=MessagingProfileDisableResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def enable_channels(
        self,
        profile_id: str,
        data: MessagingProfileEnableChannelsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileEnableChannelsResponse:
        return await self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/enable-channels',
            body=data,
            cast_to=MessagingProfileEnableChannelsResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def disable_channels(
        self,
        profile_id: str,
        data: MessagingProfileDisableChannelsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDisableChannelsResponse:
        return await self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/disable-channels',
            body=data,
            cast_to=MessagingProfileDisableChannelsResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def close(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCloseResponse:
        return await self._client.request(
            'POST',
            f'messaging/profiles/{encode_path_param(profile_id)}/close',
            cast_to=MessagingProfileCloseResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileReadResponse:
        return await self._client.request(
            'GET',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        profile_id: str,
        data: MessagingProfileUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            body=data,
            cast_to=MessagingProfileUpdateResponse,
            request_options=request_options,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileDeleteResponse,
            request_options=request_options,
        )
