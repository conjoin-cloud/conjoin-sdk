from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingDiscountCreateRequest,
    BillingDiscountCreateResponse,
    BillingDiscountDeleteResponse,
    BillingDiscountListCountQuery,
    BillingDiscountListCountResponse,
    BillingDiscountListItem,
    BillingDiscountListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingDiscountsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingDiscountListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingDiscountListItem]:
        return self._client.request(
            'GET',
            'billing/discounts/',
            query=query,
            cast_to=Page[BillingDiscountListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingDiscountCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDiscountCreateResponse:
        return self._client.request(
            'POST',
            'billing/discounts/',
            body=data,
            cast_to=BillingDiscountCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: BillingDiscountListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDiscountListCountResponse:
        return self._client.request(
            'GET',
            'billing/discounts/count',
            query=query,
            cast_to=BillingDiscountListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def delete(
        self,
        discount_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDiscountDeleteResponse:
        return self._client.request(
            'DELETE',
            f'billing/discounts/{encode_path_param(discount_id)}',
            cast_to=BillingDiscountDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingDiscountsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingDiscountListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingDiscountListItem]:
        return await self._client.request(
            'GET',
            'billing/discounts/',
            query=query,
            cast_to=AsyncPage[BillingDiscountListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingDiscountCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDiscountCreateResponse:
        return await self._client.request(
            'POST',
            'billing/discounts/',
            body=data,
            cast_to=BillingDiscountCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: BillingDiscountListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDiscountListCountResponse:
        return await self._client.request(
            'GET',
            'billing/discounts/count',
            query=query,
            cast_to=BillingDiscountListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def delete(
        self,
        discount_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingDiscountDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'billing/discounts/{encode_path_param(discount_id)}',
            cast_to=BillingDiscountDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
