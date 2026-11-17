from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    BillingChargeListCountQuery,
    BillingChargeListCountResponse,
    BillingChargeListItem,
    BillingChargeListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingChargesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingChargeListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingChargeListItem]:
        return self._client.request(
            'GET',
            'billing/charges/',
            query=query,
            cast_to=Page[BillingChargeListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingChargeListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingChargeListCountResponse:
        return self._client.request(
            'GET',
            'billing/charges/count',
            query=query,
            cast_to=BillingChargeListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingChargesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingChargeListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingChargeListItem]:
        return await self._client.request(
            'GET',
            'billing/charges/',
            query=query,
            cast_to=AsyncPage[BillingChargeListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingChargeListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingChargeListCountResponse:
        return await self._client.request(
            'GET',
            'billing/charges/count',
            query=query,
            cast_to=BillingChargeListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
