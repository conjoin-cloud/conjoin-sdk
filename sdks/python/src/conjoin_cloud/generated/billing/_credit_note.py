from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingCreditNoteCreateRequest,
    BillingCreditNoteCreateResponse,
    BillingCreditNoteListCountQuery,
    BillingCreditNoteListCountResponse,
    BillingCreditNoteListCustomerCreditBalancesCountQuery,
    BillingCreditNoteListCustomerCreditBalancesCountResponse,
    BillingCreditNoteListCustomerCreditBalancesItem,
    BillingCreditNoteListCustomerCreditBalancesQuery,
    BillingCreditNoteListItem,
    BillingCreditNoteListQuery,
    BillingCreditNoteVoidResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingCreditNotesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingCreditNoteListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingCreditNoteListItem]:
        return self._client.request(
            'GET',
            'billing/credit-notes/',
            query=query,
            cast_to=Page[BillingCreditNoteListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingCreditNoteCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteCreateResponse:
        return self._client.request(
            'POST',
            'billing/credit-notes/',
            body=data,
            cast_to=BillingCreditNoteCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_customer_credit_balances(
        self,
        customer_id: str,
        query: BillingCreditNoteListCustomerCreditBalancesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingCreditNoteListCustomerCreditBalancesItem]:
        return self._client.request(
            'GET',
            f'billing/credit-notes/{encode_path_param(customer_id)}/credit-balances',
            query=query,
            cast_to=Page[BillingCreditNoteListCustomerCreditBalancesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingCreditNoteListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteListCountResponse:
        return self._client.request(
            'GET',
            'billing/credit-notes/count',
            query=query,
            cast_to=BillingCreditNoteListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def void(
        self,
        credit_note_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteVoidResponse:
        return self._client.request(
            'POST',
            f'billing/credit-notes/{encode_path_param(credit_note_id)}/void',
            cast_to=BillingCreditNoteVoidResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_customer_credit_balances_count(
        self,
        customer_id: str,
        query: BillingCreditNoteListCustomerCreditBalancesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteListCustomerCreditBalancesCountResponse:
        return self._client.request(
            'GET',
            f'billing/credit-notes/{encode_path_param(customer_id)}/credit-balances/count',
            query=query,
            cast_to=BillingCreditNoteListCustomerCreditBalancesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingCreditNotesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingCreditNoteListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingCreditNoteListItem]:
        return await self._client.request(
            'GET',
            'billing/credit-notes/',
            query=query,
            cast_to=AsyncPage[BillingCreditNoteListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingCreditNoteCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteCreateResponse:
        return await self._client.request(
            'POST',
            'billing/credit-notes/',
            body=data,
            cast_to=BillingCreditNoteCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_customer_credit_balances(
        self,
        customer_id: str,
        query: BillingCreditNoteListCustomerCreditBalancesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingCreditNoteListCustomerCreditBalancesItem]:
        return await self._client.request(
            'GET',
            f'billing/credit-notes/{encode_path_param(customer_id)}/credit-balances',
            query=query,
            cast_to=AsyncPage[BillingCreditNoteListCustomerCreditBalancesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingCreditNoteListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteListCountResponse:
        return await self._client.request(
            'GET',
            'billing/credit-notes/count',
            query=query,
            cast_to=BillingCreditNoteListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def void(
        self,
        credit_note_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteVoidResponse:
        return await self._client.request(
            'POST',
            f'billing/credit-notes/{encode_path_param(credit_note_id)}/void',
            cast_to=BillingCreditNoteVoidResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_customer_credit_balances_count(
        self,
        customer_id: str,
        query: BillingCreditNoteListCustomerCreditBalancesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCreditNoteListCustomerCreditBalancesCountResponse:
        return await self._client.request(
            'GET',
            f'billing/credit-notes/{encode_path_param(customer_id)}/credit-balances/count',
            query=query,
            cast_to=BillingCreditNoteListCustomerCreditBalancesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
