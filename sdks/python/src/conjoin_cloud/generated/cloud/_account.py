from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    CloudAccountReadResponse,
    CloudAccountUpdateRequest,
    CloudAccountUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudAccountsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAccountReadResponse:
        return self._client.request(
            'GET',
            'cloud/account/',
            cast_to=CloudAccountReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        data: CloudAccountUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAccountUpdateResponse:
        return self._client.request(
            'PATCH',
            'cloud/account/',
            body=data,
            cast_to=CloudAccountUpdateResponse,
            request_options=request_options,
        )


class AsyncCloudAccountsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAccountReadResponse:
        return await self._client.request(
            'GET',
            'cloud/account/',
            cast_to=CloudAccountReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        data: CloudAccountUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAccountUpdateResponse:
        return await self._client.request(
            'PATCH',
            'cloud/account/',
            body=data,
            cast_to=CloudAccountUpdateResponse,
            request_options=request_options,
        )
