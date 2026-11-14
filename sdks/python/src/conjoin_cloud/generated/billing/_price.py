from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingPriceArchiveResponse,
    BillingPriceCreateRequest,
    BillingPriceCreateResponse,
    BillingPriceDeleteResponse,
    BillingPriceListCountQuery,
    BillingPriceListCountResponse,
    BillingPriceListItem,
    BillingPriceListQuery,
    BillingPriceReadResponse,
    BillingPriceRestoreResponse,
    BillingPriceUpdateRequest,
    BillingPriceUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingPricesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingPriceListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingPriceListItem]:
        return self._client.request(
            'GET',
            'billing/prices/',
            query=query,
            cast_to=Page[BillingPriceListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingPriceCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceCreateResponse:
        return self._client.request(
            'POST',
            'billing/prices/',
            body=data,
            cast_to=BillingPriceCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingPriceListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceListCountResponse:
        return self._client.request(
            'GET',
            'billing/prices/count',
            query=query,
            cast_to=BillingPriceListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def read(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceReadResponse:
        return self._client.request(
            'GET',
            f'billing/prices/{encode_path_param(price_id)}',
            cast_to=BillingPriceReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        price_id: str,
        data: BillingPriceUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/prices/{encode_path_param(price_id)}',
            body=data,
            cast_to=BillingPriceUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def delete(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceDeleteResponse:
        return self._client.request(
            'DELETE',
            f'billing/prices/{encode_path_param(price_id)}',
            cast_to=BillingPriceDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            unwrap_data=False,
        )

    def archive(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceArchiveResponse:
        return self._client.request(
            'POST',
            f'billing/prices/{encode_path_param(price_id)}/archive',
            cast_to=BillingPriceArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def restore(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceRestoreResponse:
        return self._client.request(
            'POST',
            f'billing/prices/{encode_path_param(price_id)}/restore',
            cast_to=BillingPriceRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingPricesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingPriceListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingPriceListItem]:
        return await self._client.request(
            'GET',
            'billing/prices/',
            query=query,
            cast_to=AsyncPage[BillingPriceListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingPriceCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceCreateResponse:
        return await self._client.request(
            'POST',
            'billing/prices/',
            body=data,
            cast_to=BillingPriceCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingPriceListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceListCountResponse:
        return await self._client.request(
            'GET',
            'billing/prices/count',
            query=query,
            cast_to=BillingPriceListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def read(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceReadResponse:
        return await self._client.request(
            'GET',
            f'billing/prices/{encode_path_param(price_id)}',
            cast_to=BillingPriceReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        price_id: str,
        data: BillingPriceUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/prices/{encode_path_param(price_id)}',
            body=data,
            cast_to=BillingPriceUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def delete(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'billing/prices/{encode_path_param(price_id)}',
            cast_to=BillingPriceDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            unwrap_data=False,
        )

    async def archive(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceArchiveResponse:
        return await self._client.request(
            'POST',
            f'billing/prices/{encode_path_param(price_id)}/archive',
            cast_to=BillingPriceArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def restore(
        self,
        price_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceRestoreResponse:
        return await self._client.request(
            'POST',
            f'billing/prices/{encode_path_param(price_id)}/restore',
            cast_to=BillingPriceRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
