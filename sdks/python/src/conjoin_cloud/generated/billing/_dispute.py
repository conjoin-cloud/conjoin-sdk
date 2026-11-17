from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingDisputeGetResponse,
    BillingDisputeListCountQuery,
    BillingDisputeListCountResponse,
    BillingDisputeListItem,
    BillingDisputeListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingDisputesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingDisputeListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingDisputeListItem]:
        return self._client.request(
            'GET',
            'billing/disputes/',
            query=query,
            cast_to=Page[BillingDisputeListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingDisputeListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDisputeListCountResponse:
        return self._client.request(
            'GET',
            'billing/disputes/count',
            query=query,
            cast_to=BillingDisputeListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def get(
        self,
        dispute_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDisputeGetResponse:
        return self._client.request(
            'GET',
            f'billing/disputes/{encode_path_param(dispute_id)}',
            cast_to=BillingDisputeGetResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingDisputesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingDisputeListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingDisputeListItem]:
        return await self._client.request(
            'GET',
            'billing/disputes/',
            query=query,
            cast_to=AsyncPage[BillingDisputeListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingDisputeListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDisputeListCountResponse:
        return await self._client.request(
            'GET',
            'billing/disputes/count',
            query=query,
            cast_to=BillingDisputeListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def get(
        self,
        dispute_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDisputeGetResponse:
        return await self._client.request(
            'GET',
            f'billing/disputes/{encode_path_param(dispute_id)}',
            cast_to=BillingDisputeGetResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
