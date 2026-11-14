from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudZoneCreateRequest,
    CloudZoneCreateResponse,
    CloudZoneListItem,
    CloudZoneListQuery,
    CloudZoneReadCountQuery,
    CloudZoneReadCountResponse,
    CloudZoneReadResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudZonesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: CloudZoneListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudZoneListItem]:
        return self._client.request(
            'GET',
            'cloud/zones/',
            query=query,
            cast_to=Page[CloudZoneListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: CloudZoneCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudZoneCreateResponse:
        return self._client.request(
            'POST',
            'cloud/zones/',
            body=data,
            cast_to=CloudZoneCreateResponse,
            request_options=request_options,
        )

    def read_count(
        self,
        query: CloudZoneReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudZoneReadCountResponse:
        return self._client.request(
            'GET',
            'cloud/zones/count',
            query=query,
            cast_to=CloudZoneReadCountResponse,
            request_options=request_options,
        )

    def read(
        self,
        zone_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudZoneReadResponse:
        return self._client.request(
            'GET',
            f'cloud/zones/{encode_path_param(zone_id)}',
            cast_to=CloudZoneReadResponse,
            request_options=request_options,
        )

    def delete(
        self,
        zone_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'DELETE',
            f'cloud/zones/{encode_path_param(zone_id)}',
            request_options=request_options,
        )

    def verify_dns(
        self,
        zone_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            f'cloud/zones/{encode_path_param(zone_id)}/verify',
            request_options=request_options,
        )


class AsyncCloudZonesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: CloudZoneListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudZoneListItem]:
        return await self._client.request(
            'GET',
            'cloud/zones/',
            query=query,
            cast_to=AsyncPage[CloudZoneListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: CloudZoneCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudZoneCreateResponse:
        return await self._client.request(
            'POST',
            'cloud/zones/',
            body=data,
            cast_to=CloudZoneCreateResponse,
            request_options=request_options,
        )

    async def read_count(
        self,
        query: CloudZoneReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudZoneReadCountResponse:
        return await self._client.request(
            'GET',
            'cloud/zones/count',
            query=query,
            cast_to=CloudZoneReadCountResponse,
            request_options=request_options,
        )

    async def read(
        self,
        zone_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudZoneReadResponse:
        return await self._client.request(
            'GET',
            f'cloud/zones/{encode_path_param(zone_id)}',
            cast_to=CloudZoneReadResponse,
            request_options=request_options,
        )

    async def delete(
        self,
        zone_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'DELETE',
            f'cloud/zones/{encode_path_param(zone_id)}',
            request_options=request_options,
        )

    async def verify_dns(
        self,
        zone_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            f'cloud/zones/{encode_path_param(zone_id)}/verify',
            request_options=request_options,
        )
