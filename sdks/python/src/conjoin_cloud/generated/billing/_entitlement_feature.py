from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingEntitlementFeatureArchiveResponse,
    BillingEntitlementFeatureCreateRequest,
    BillingEntitlementFeatureCreateResponse,
    BillingEntitlementFeatureListCountQuery,
    BillingEntitlementFeatureListCountResponse,
    BillingEntitlementFeatureListItem,
    BillingEntitlementFeatureListQuery,
    BillingEntitlementFeatureReadResponse,
    BillingEntitlementFeatureUpdateRequest,
    BillingEntitlementFeatureUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingEntitlementFeaturesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingEntitlementFeatureListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingEntitlementFeatureListItem]:
        return self._client.request(
            'GET',
            'billing/entitlement-features/',
            query=query,
            cast_to=Page[BillingEntitlementFeatureListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: BillingEntitlementFeatureCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureCreateResponse:
        return self._client.request(
            'POST',
            'billing/entitlement-features/',
            body=data,
            cast_to=BillingEntitlementFeatureCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: BillingEntitlementFeatureListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureListCountResponse:
        return self._client.request(
            'GET',
            'billing/entitlement-features/count',
            query=query,
            cast_to=BillingEntitlementFeatureListCountResponse,
            request_options=request_options,
        )

    def read(
        self,
        entitlement_feature_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureReadResponse:
        return self._client.request(
            'GET',
            f'billing/entitlement-features/{encode_path_param(entitlement_feature_id)}',
            cast_to=BillingEntitlementFeatureReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        entitlement_feature_id: str,
        data: BillingEntitlementFeatureUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/entitlement-features/{encode_path_param(entitlement_feature_id)}',
            body=data,
            cast_to=BillingEntitlementFeatureUpdateResponse,
            request_options=request_options,
        )

    def archive(
        self,
        entitlement_feature_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureArchiveResponse:
        return self._client.request(
            'POST',
            f'billing/entitlement-features/{encode_path_param(entitlement_feature_id)}/archive',
            cast_to=BillingEntitlementFeatureArchiveResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )


class AsyncBillingEntitlementFeaturesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingEntitlementFeatureListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingEntitlementFeatureListItem]:
        return await self._client.request(
            'GET',
            'billing/entitlement-features/',
            query=query,
            cast_to=AsyncPage[BillingEntitlementFeatureListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: BillingEntitlementFeatureCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureCreateResponse:
        return await self._client.request(
            'POST',
            'billing/entitlement-features/',
            body=data,
            cast_to=BillingEntitlementFeatureCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: BillingEntitlementFeatureListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureListCountResponse:
        return await self._client.request(
            'GET',
            'billing/entitlement-features/count',
            query=query,
            cast_to=BillingEntitlementFeatureListCountResponse,
            request_options=request_options,
        )

    async def read(
        self,
        entitlement_feature_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureReadResponse:
        return await self._client.request(
            'GET',
            f'billing/entitlement-features/{encode_path_param(entitlement_feature_id)}',
            cast_to=BillingEntitlementFeatureReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        entitlement_feature_id: str,
        data: BillingEntitlementFeatureUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/entitlement-features/{encode_path_param(entitlement_feature_id)}',
            body=data,
            cast_to=BillingEntitlementFeatureUpdateResponse,
            request_options=request_options,
        )

    async def archive(
        self,
        entitlement_feature_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingEntitlementFeatureArchiveResponse:
        return await self._client.request(
            'POST',
            f'billing/entitlement-features/{encode_path_param(entitlement_feature_id)}/archive',
            cast_to=BillingEntitlementFeatureArchiveResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )
