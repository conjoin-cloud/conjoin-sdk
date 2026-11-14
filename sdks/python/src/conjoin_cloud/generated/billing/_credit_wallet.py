from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingCreditWalletCreateRequest,
    BillingCreditWalletCreateResponse,
    BillingCreditWalletGrantCreditsRequest,
    BillingCreditWalletGrantCreditsResponse,
    BillingCreditWalletListCountQuery,
    BillingCreditWalletListCountResponse,
    BillingCreditWalletListItem,
    BillingCreditWalletListQuery,
    BillingCreditWalletUpdateRequest,
    BillingCreditWalletUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingCreditWalletsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingCreditWalletListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingCreditWalletListItem]:
        return self._client.request(
            'GET',
            'billing/credit-wallets/',
            query=query,
            cast_to=Page[BillingCreditWalletListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingCreditWalletCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletCreateResponse:
        return self._client.request(
            'POST',
            'billing/credit-wallets/',
            body=data,
            cast_to=BillingCreditWalletCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingCreditWalletListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletListCountResponse:
        return self._client.request(
            'GET',
            'billing/credit-wallets/count',
            query=query,
            cast_to=BillingCreditWalletListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        credit_wallet_id: str,
        data: BillingCreditWalletUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/credit-wallets/{encode_path_param(credit_wallet_id)}',
            body=data,
            cast_to=BillingCreditWalletUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def grant_credits(
        self,
        credit_wallet_id: str,
        data: BillingCreditWalletGrantCreditsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletGrantCreditsResponse:
        return self._client.request(
            'POST',
            f'billing/credit-wallets/{encode_path_param(credit_wallet_id)}/grant',
            body=data,
            cast_to=BillingCreditWalletGrantCreditsResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingCreditWalletsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingCreditWalletListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingCreditWalletListItem]:
        return await self._client.request(
            'GET',
            'billing/credit-wallets/',
            query=query,
            cast_to=AsyncPage[BillingCreditWalletListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingCreditWalletCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletCreateResponse:
        return await self._client.request(
            'POST',
            'billing/credit-wallets/',
            body=data,
            cast_to=BillingCreditWalletCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingCreditWalletListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletListCountResponse:
        return await self._client.request(
            'GET',
            'billing/credit-wallets/count',
            query=query,
            cast_to=BillingCreditWalletListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        credit_wallet_id: str,
        data: BillingCreditWalletUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/credit-wallets/{encode_path_param(credit_wallet_id)}',
            body=data,
            cast_to=BillingCreditWalletUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def grant_credits(
        self,
        credit_wallet_id: str,
        data: BillingCreditWalletGrantCreditsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditWalletGrantCreditsResponse:
        return await self._client.request(
            'POST',
            f'billing/credit-wallets/{encode_path_param(credit_wallet_id)}/grant',
            body=data,
            cast_to=BillingCreditWalletGrantCreditsResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
