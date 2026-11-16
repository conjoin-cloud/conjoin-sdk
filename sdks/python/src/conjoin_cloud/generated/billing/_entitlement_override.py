from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingEntitlementOverrideCreateRequest,
    BillingEntitlementOverrideCreateResponse,
    BillingEntitlementOverrideDeleteResponse,
    BillingEntitlementOverrideListCountQuery,
    BillingEntitlementOverrideListCountResponse,
    BillingEntitlementOverrideListItem,
    BillingEntitlementOverrideListQuery,
    BillingEntitlementOverrideUpdateRequest,
    BillingEntitlementOverrideUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingEntitlementOverridesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingEntitlementOverrideListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingEntitlementOverrideListItem]:
        return self._client.request(
            'GET',
            'billing/entitlement-overrides/',
            query=query,
            cast_to=Page[BillingEntitlementOverrideListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingEntitlementOverrideCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideCreateResponse:
        return self._client.request(
            'POST',
            'billing/entitlement-overrides/',
            body=data,
            cast_to=BillingEntitlementOverrideCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: BillingEntitlementOverrideListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideListCountResponse:
        return self._client.request(
            'GET',
            'billing/entitlement-overrides/count',
            query=query,
            cast_to=BillingEntitlementOverrideListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        entitlement_override_id: str,
        data: BillingEntitlementOverrideUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/entitlement-overrides/{encode_path_param(entitlement_override_id)}',
            body=data,
            cast_to=BillingEntitlementOverrideUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def delete(
        self,
        entitlement_override_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideDeleteResponse:
        return self._client.request(
            'DELETE',
            f'billing/entitlement-overrides/{encode_path_param(entitlement_override_id)}',
            cast_to=BillingEntitlementOverrideDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            unwrap_data=False,
        )


class AsyncBillingEntitlementOverridesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingEntitlementOverrideListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingEntitlementOverrideListItem]:
        return await self._client.request(
            'GET',
            'billing/entitlement-overrides/',
            query=query,
            cast_to=AsyncPage[BillingEntitlementOverrideListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingEntitlementOverrideCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideCreateResponse:
        return await self._client.request(
            'POST',
            'billing/entitlement-overrides/',
            body=data,
            cast_to=BillingEntitlementOverrideCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: BillingEntitlementOverrideListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideListCountResponse:
        return await self._client.request(
            'GET',
            'billing/entitlement-overrides/count',
            query=query,
            cast_to=BillingEntitlementOverrideListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        entitlement_override_id: str,
        data: BillingEntitlementOverrideUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/entitlement-overrides/{encode_path_param(entitlement_override_id)}',
            body=data,
            cast_to=BillingEntitlementOverrideUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def delete(
        self,
        entitlement_override_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementOverrideDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'billing/entitlement-overrides/{encode_path_param(entitlement_override_id)}',
            cast_to=BillingEntitlementOverrideDeleteResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            unwrap_data=False,
        )
