from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    CloudSpendControlReadResponse,
    CloudSpendControlReadUsageResponse,
    CloudSpendControlUpdateRequest,
    CloudSpendControlUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudSpendControlsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSpendControlReadResponse:
        return self._client.request(
            'GET',
            'cloud/spend-control/',
            cast_to=CloudSpendControlReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        data: CloudSpendControlUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSpendControlUpdateResponse:
        return self._client.request(
            'PATCH',
            'cloud/spend-control/',
            body=data,
            cast_to=CloudSpendControlUpdateResponse,
            request_options=request_options,
        )

    def read_usage(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSpendControlReadUsageResponse:
        return self._client.request(
            'GET',
            'cloud/spend-control/usage',
            cast_to=CloudSpendControlReadUsageResponse,
            request_options=request_options,
        )


class AsyncCloudSpendControlsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSpendControlReadResponse:
        return await self._client.request(
            'GET',
            'cloud/spend-control/',
            cast_to=CloudSpendControlReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        data: CloudSpendControlUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSpendControlUpdateResponse:
        return await self._client.request(
            'PATCH',
            'cloud/spend-control/',
            body=data,
            cast_to=CloudSpendControlUpdateResponse,
            request_options=request_options,
        )

    async def read_usage(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSpendControlReadUsageResponse:
        return await self._client.request(
            'GET',
            'cloud/spend-control/usage',
            cast_to=CloudSpendControlReadUsageResponse,
            request_options=request_options,
        )
