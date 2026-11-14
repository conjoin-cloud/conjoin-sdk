from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudSKUCatalogReadSingleSkuCatalogResponse,
    CloudSKUCatalogReadSkuCatalogCountQuery,
    CloudSKUCatalogReadSkuCatalogCountResponse,
    CloudSKUCatalogReadSkuCatalogItem,
    CloudSKUCatalogReadSkuCatalogQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudSKUCatalogsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_sku_catalog(
        self,
        query: CloudSKUCatalogReadSkuCatalogQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudSKUCatalogReadSkuCatalogItem]:
        return self._client.request(
            'GET',
            'cloud/skus/',
            query=query,
            cast_to=Page[CloudSKUCatalogReadSkuCatalogItem],
            request_options=request_options,
        )

    def read_sku_catalog_count(
        self,
        query: CloudSKUCatalogReadSkuCatalogCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSKUCatalogReadSkuCatalogCountResponse:
        return self._client.request(
            'GET',
            'cloud/skus/count',
            query=query,
            cast_to=CloudSKUCatalogReadSkuCatalogCountResponse,
            request_options=request_options,
        )

    def read_single_sku_catalog(
        self,
        sku_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSKUCatalogReadSingleSkuCatalogResponse:
        return self._client.request(
            'GET',
            f'cloud/skus/{encode_path_param(sku_id)}',
            cast_to=CloudSKUCatalogReadSingleSkuCatalogResponse,
            request_options=request_options,
        )


class AsyncCloudSKUCatalogsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_sku_catalog(
        self,
        query: CloudSKUCatalogReadSkuCatalogQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudSKUCatalogReadSkuCatalogItem]:
        return await self._client.request(
            'GET',
            'cloud/skus/',
            query=query,
            cast_to=AsyncPage[CloudSKUCatalogReadSkuCatalogItem],
            request_options=request_options,
        )

    async def read_sku_catalog_count(
        self,
        query: CloudSKUCatalogReadSkuCatalogCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSKUCatalogReadSkuCatalogCountResponse:
        return await self._client.request(
            'GET',
            'cloud/skus/count',
            query=query,
            cast_to=CloudSKUCatalogReadSkuCatalogCountResponse,
            request_options=request_options,
        )

    async def read_single_sku_catalog(
        self,
        sku_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSKUCatalogReadSingleSkuCatalogResponse:
        return await self._client.request(
            'GET',
            f'cloud/skus/{encode_path_param(sku_id)}',
            cast_to=CloudSKUCatalogReadSingleSkuCatalogResponse,
            request_options=request_options,
        )
