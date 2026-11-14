from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingPaymentIntentCreateRequest,
    BillingPaymentIntentListCountQuery,
    BillingPaymentIntentListCountResponse,
    BillingPaymentIntentListItem,
    BillingPaymentIntentListQuery,
    BillingPaymentIntentVerifyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingPaymentIntentsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingPaymentIntentListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingPaymentIntentListItem]:
        return self._client.request(
            'GET',
            'billing/payment-intents/',
            query=query,
            cast_to=Page[BillingPaymentIntentListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingPaymentIntentCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            'billing/payment-intents/',
            body=data,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingPaymentIntentListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentIntentListCountResponse:
        return self._client.request(
            'GET',
            'billing/payment-intents/count',
            query=query,
            cast_to=BillingPaymentIntentListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def verify(
        self,
        payment_intent_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentIntentVerifyResponse:
        return self._client.request(
            'POST',
            f'billing/payment-intents/{encode_path_param(payment_intent_id)}/verify',
            cast_to=BillingPaymentIntentVerifyResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingPaymentIntentsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingPaymentIntentListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingPaymentIntentListItem]:
        return await self._client.request(
            'GET',
            'billing/payment-intents/',
            query=query,
            cast_to=AsyncPage[BillingPaymentIntentListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingPaymentIntentCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            'billing/payment-intents/',
            body=data,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingPaymentIntentListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentIntentListCountResponse:
        return await self._client.request(
            'GET',
            'billing/payment-intents/count',
            query=query,
            cast_to=BillingPaymentIntentListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def verify(
        self,
        payment_intent_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPaymentIntentVerifyResponse:
        return await self._client.request(
            'POST',
            f'billing/payment-intents/{encode_path_param(payment_intent_id)}/verify',
            cast_to=BillingPaymentIntentVerifyResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
