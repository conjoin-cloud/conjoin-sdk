from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    BillingRefundCreateRequest,
    BillingRefundCreateResponse,
    BillingRefundListCountQuery,
    BillingRefundListCountResponse,
    BillingRefundListItem,
    BillingRefundListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingRefundsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingRefundListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingRefundListItem]:
        return self._client.request(
            'GET',
            'billing/refunds/',
            query=query,
            cast_to=Page[BillingRefundListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingRefundCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingRefundCreateResponse:
        return self._client.request(
            'POST',
            'billing/refunds/',
            body=data,
            cast_to=BillingRefundCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingRefundListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingRefundListCountResponse:
        return self._client.request(
            'GET',
            'billing/refunds/count',
            query=query,
            cast_to=BillingRefundListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingRefundsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingRefundListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingRefundListItem]:
        return await self._client.request(
            'GET',
            'billing/refunds/',
            query=query,
            cast_to=AsyncPage[BillingRefundListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingRefundCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingRefundCreateResponse:
        return await self._client.request(
            'POST',
            'billing/refunds/',
            body=data,
            cast_to=BillingRefundCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingRefundListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingRefundListCountResponse:
        return await self._client.request(
            'GET',
            'billing/refunds/count',
            query=query,
            cast_to=BillingRefundListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
