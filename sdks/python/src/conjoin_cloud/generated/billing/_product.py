from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingProductArchiveResponse,
    BillingProductCreateRequest,
    BillingProductCreateResponse,
    BillingProductDeleteResponse,
    BillingProductListCountQuery,
    BillingProductListCountResponse,
    BillingProductListItem,
    BillingProductListQuery,
    BillingProductReadResponse,
    BillingProductRestoreResponse,
    BillingProductUpdateRequest,
    BillingProductUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingProductsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingProductListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingProductListItem]:
        return self._client.request(
            'GET',
            'billing/products/',
            query=query,
            cast_to=Page[BillingProductListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingProductCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductCreateResponse:
        return self._client.request(
            'POST',
            'billing/products/',
            body=data,
            cast_to=BillingProductCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingProductListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductListCountResponse:
        return self._client.request(
            'GET',
            'billing/products/count',
            query=query,
            cast_to=BillingProductListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def read(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductReadResponse:
        return self._client.request(
            'GET',
            f'billing/products/{encode_path_param(product_id)}',
            cast_to=BillingProductReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        product_id: str,
        data: BillingProductUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/products/{encode_path_param(product_id)}',
            body=data,
            cast_to=BillingProductUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def delete(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductDeleteResponse:
        return self._client.request(
            'DELETE',
            f'billing/products/{encode_path_param(product_id)}',
            cast_to=BillingProductDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            unwrap_data=False,
        )

    def archive(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductArchiveResponse:
        return self._client.request(
            'POST',
            f'billing/products/{encode_path_param(product_id)}/archive',
            cast_to=BillingProductArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def restore(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductRestoreResponse:
        return self._client.request(
            'POST',
            f'billing/products/{encode_path_param(product_id)}/restore',
            cast_to=BillingProductRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingProductsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingProductListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingProductListItem]:
        return await self._client.request(
            'GET',
            'billing/products/',
            query=query,
            cast_to=AsyncPage[BillingProductListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingProductCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductCreateResponse:
        return await self._client.request(
            'POST',
            'billing/products/',
            body=data,
            cast_to=BillingProductCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingProductListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductListCountResponse:
        return await self._client.request(
            'GET',
            'billing/products/count',
            query=query,
            cast_to=BillingProductListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def read(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductReadResponse:
        return await self._client.request(
            'GET',
            f'billing/products/{encode_path_param(product_id)}',
            cast_to=BillingProductReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        product_id: str,
        data: BillingProductUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/products/{encode_path_param(product_id)}',
            body=data,
            cast_to=BillingProductUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def delete(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'billing/products/{encode_path_param(product_id)}',
            cast_to=BillingProductDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            unwrap_data=False,
        )

    async def archive(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductArchiveResponse:
        return await self._client.request(
            'POST',
            f'billing/products/{encode_path_param(product_id)}/archive',
            cast_to=BillingProductArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def restore(
        self,
        product_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingProductRestoreResponse:
        return await self._client.request(
            'POST',
            f'billing/products/{encode_path_param(product_id)}/restore',
            cast_to=BillingProductRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
