from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingCustomerArchiveResponse,
    BillingCustomerCreateRequest,
    BillingCustomerCreateResponse,
    BillingCustomerListCountQuery,
    BillingCustomerListCountResponse,
    BillingCustomerListItem,
    BillingCustomerListQuery,
    BillingCustomerReadResponse,
    BillingCustomerRestoreResponse,
    BillingCustomerUpdateRequest,
    BillingCustomerUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingCustomersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingCustomerListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingCustomerListItem]:
        return self._client.request(
            'GET',
            'billing/customers/',
            query=query,
            cast_to=Page[BillingCustomerListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingCustomerCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerCreateResponse:
        return self._client.request(
            'POST',
            'billing/customers/',
            body=data,
            cast_to=BillingCustomerCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: BillingCustomerListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerListCountResponse:
        return self._client.request(
            'GET',
            'billing/customers/count',
            query=query,
            cast_to=BillingCustomerListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def read(
        self,
        customer_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerReadResponse:
        return self._client.request(
            'GET',
            f'billing/customers/{encode_path_param(customer_id)}',
            cast_to=BillingCustomerReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        customer_id: str,
        data: BillingCustomerUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/customers/{encode_path_param(customer_id)}',
            body=data,
            cast_to=BillingCustomerUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def archive(
        self,
        customer_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerArchiveResponse:
        return self._client.request(
            'POST',
            f'billing/customers/{encode_path_param(customer_id)}/archive',
            cast_to=BillingCustomerArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def restore(
        self,
        customer_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerRestoreResponse:
        return self._client.request(
            'POST',
            f'billing/customers/{encode_path_param(customer_id)}/restore',
            cast_to=BillingCustomerRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )


class AsyncBillingCustomersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingCustomerListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingCustomerListItem]:
        return await self._client.request(
            'GET',
            'billing/customers/',
            query=query,
            cast_to=AsyncPage[BillingCustomerListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingCustomerCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerCreateResponse:
        return await self._client.request(
            'POST',
            'billing/customers/',
            body=data,
            cast_to=BillingCustomerCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: BillingCustomerListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerListCountResponse:
        return await self._client.request(
            'GET',
            'billing/customers/count',
            query=query,
            cast_to=BillingCustomerListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def read(
        self,
        customer_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerReadResponse:
        return await self._client.request(
            'GET',
            f'billing/customers/{encode_path_param(customer_id)}',
            cast_to=BillingCustomerReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        customer_id: str,
        data: BillingCustomerUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/customers/{encode_path_param(customer_id)}',
            body=data,
            cast_to=BillingCustomerUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def archive(
        self,
        customer_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerArchiveResponse:
        return await self._client.request(
            'POST',
            f'billing/customers/{encode_path_param(customer_id)}/archive',
            cast_to=BillingCustomerArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def restore(
        self,
        customer_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCustomerRestoreResponse:
        return await self._client.request(
            'POST',
            f'billing/customers/{encode_path_param(customer_id)}/restore',
            cast_to=BillingCustomerRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )
