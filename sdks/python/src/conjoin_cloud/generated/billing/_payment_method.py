from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingPaymentMethodCreateRequest,
    BillingPaymentMethodDeleteResponse,
    BillingPaymentMethodListCountQuery,
    BillingPaymentMethodListCountResponse,
    BillingPaymentMethodListItem,
    BillingPaymentMethodListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingPaymentMethodsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingPaymentMethodListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingPaymentMethodListItem]:
        return self._client.request(
            'GET',
            'billing/payment-methods/',
            query=query,
            cast_to=Page[BillingPaymentMethodListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingPaymentMethodCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            'billing/payment-methods/',
            body=data,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingPaymentMethodListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentMethodListCountResponse:
        return self._client.request(
            'GET',
            'billing/payment-methods/count',
            query=query,
            cast_to=BillingPaymentMethodListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def delete(
        self,
        payment_method_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentMethodDeleteResponse:
        return self._client.request(
            'DELETE',
            f'billing/payment-methods/{encode_path_param(payment_method_id)}',
            cast_to=BillingPaymentMethodDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingPaymentMethodsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingPaymentMethodListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingPaymentMethodListItem]:
        return await self._client.request(
            'GET',
            'billing/payment-methods/',
            query=query,
            cast_to=AsyncPage[BillingPaymentMethodListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingPaymentMethodCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            'billing/payment-methods/',
            body=data,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingPaymentMethodListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentMethodListCountResponse:
        return await self._client.request(
            'GET',
            'billing/payment-methods/count',
            query=query,
            cast_to=BillingPaymentMethodListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def delete(
        self,
        payment_method_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentMethodDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'billing/payment-methods/{encode_path_param(payment_method_id)}',
            cast_to=BillingPaymentMethodDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
