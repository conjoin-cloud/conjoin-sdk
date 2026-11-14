from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    BillingSettingsReadResponse,
    BillingSettingsUpdateRequest,
    BillingSettingsUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingSettingsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSettingsReadResponse:
        return self._client.request(
            'GET',
            'billing/settings/',
            cast_to=BillingSettingsReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        data: BillingSettingsUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSettingsUpdateResponse:
        return self._client.request(
            'PATCH',
            'billing/settings/',
            body=data,
            cast_to=BillingSettingsUpdateResponse,
            request_options=request_options,
        )


class AsyncBillingSettingsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSettingsReadResponse:
        return await self._client.request(
            'GET',
            'billing/settings/',
            cast_to=BillingSettingsReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        data: BillingSettingsUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSettingsUpdateResponse:
        return await self._client.request(
            'PATCH',
            'billing/settings/',
            body=data,
            cast_to=BillingSettingsUpdateResponse,
            request_options=request_options,
        )
