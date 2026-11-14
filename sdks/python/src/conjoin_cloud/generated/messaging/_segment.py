from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingSegmentsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_one(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            'messaging/segments/',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def update_one(
        self,
        segment_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'PATCH',
            f'messaging/segments/{encode_path_param(segment_id)}',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_one(
        self,
        segment_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'DELETE',
            f'messaging/segments/{encode_path_param(segment_id)}',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_many(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            'messaging/segments/retrieve',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingSegmentsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_one(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            'messaging/segments/',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def update_one(
        self,
        segment_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'PATCH',
            f'messaging/segments/{encode_path_param(segment_id)}',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_one(
        self,
        segment_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'DELETE',
            f'messaging/segments/{encode_path_param(segment_id)}',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_many(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            'messaging/segments/retrieve',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
