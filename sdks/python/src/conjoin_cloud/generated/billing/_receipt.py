from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingReceiptListCountQuery,
    BillingReceiptListCountResponse,
    BillingReceiptListItem,
    BillingReceiptListQuery,
    BillingReceiptReadResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingReceiptsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingReceiptListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingReceiptListItem]:
        return self._client.request(
            'GET',
            'billing/receipts/',
            query=query,
            cast_to=Page[BillingReceiptListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingReceiptListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingReceiptListCountResponse:
        return self._client.request(
            'GET',
            'billing/receipts/count',
            query=query,
            cast_to=BillingReceiptListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def read(
        self,
        receipt_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingReceiptReadResponse:
        return self._client.request(
            'GET',
            f'billing/receipts/{encode_path_param(receipt_id)}',
            cast_to=BillingReceiptReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingReceiptsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingReceiptListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingReceiptListItem]:
        return await self._client.request(
            'GET',
            'billing/receipts/',
            query=query,
            cast_to=AsyncPage[BillingReceiptListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingReceiptListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingReceiptListCountResponse:
        return await self._client.request(
            'GET',
            'billing/receipts/count',
            query=query,
            cast_to=BillingReceiptListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def read(
        self,
        receipt_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingReceiptReadResponse:
        return await self._client.request(
            'GET',
            f'billing/receipts/{encode_path_param(receipt_id)}',
            cast_to=BillingReceiptReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
