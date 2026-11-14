from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingPriceBundleActivateRequest,
    BillingPriceBundleActivateResponse,
    BillingPriceBundleArchiveResponse,
    BillingPriceBundleCreateRequest,
    BillingPriceBundleCreateResponse,
    BillingPriceBundleDeactivateRequest,
    BillingPriceBundleDeactivateResponse,
    BillingPriceBundleListActivationsCountQuery,
    BillingPriceBundleListActivationsCountResponse,
    BillingPriceBundleListActivationsItem,
    BillingPriceBundleListActivationsQuery,
    BillingPriceBundleListCountQuery,
    BillingPriceBundleListCountResponse,
    BillingPriceBundleListItem,
    BillingPriceBundleListQuery,
    BillingPriceBundlePublishResponse,
    BillingPriceBundleReadAvailableBundleTransitionsQuery,
    BillingPriceBundleReadAvailableBundleTransitionsResponse,
    BillingPriceBundleReadResponse,
    BillingPriceBundleRestoreResponse,
    BillingPriceBundleUpdateRequest,
    BillingPriceBundleUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingPriceBundlesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_activations(
        self,
        query: BillingPriceBundleListActivationsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingPriceBundleListActivationsItem]:
        return self._client.request(
            'GET',
            'billing/price-bundle-activations/',
            query=query,
            cast_to=Page[BillingPriceBundleListActivationsItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def activate(
        self,
        data: BillingPriceBundleActivateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleActivateResponse:
        return self._client.request(
            'POST',
            'billing/price-bundle-activations/',
            body=data,
            cast_to=BillingPriceBundleActivateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_activations_count(
        self,
        query: BillingPriceBundleListActivationsCountQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleListActivationsCountResponse:
        return self._client.request(
            'GET',
            'billing/price-bundle-activations/count',
            query=query,
            cast_to=BillingPriceBundleListActivationsCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def deactivate(
        self,
        price_bundle_activation_id: str,
        data: BillingPriceBundleDeactivateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleDeactivateResponse:
        return self._client.request(
            'POST',
            (
                f'billing/price-bundle-activations/{encode_path_param(price_bundle_activation_id)}'
                '/deactivate'
            ),
            body=data,
            cast_to=BillingPriceBundleDeactivateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def read_available_bundle_transitions(
        self,
        query: BillingPriceBundleReadAvailableBundleTransitionsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleReadAvailableBundleTransitionsResponse:
        return self._client.request(
            'GET',
            'billing/price-bundle-transitions/',
            query=query,
            cast_to=BillingPriceBundleReadAvailableBundleTransitionsResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list(
        self,
        query: BillingPriceBundleListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingPriceBundleListItem]:
        return self._client.request(
            'GET',
            'billing/price-bundles/',
            query=query,
            cast_to=Page[BillingPriceBundleListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingPriceBundleCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleCreateResponse:
        return self._client.request(
            'POST',
            'billing/price-bundles/',
            body=data,
            cast_to=BillingPriceBundleCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingPriceBundleListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleListCountResponse:
        return self._client.request(
            'GET',
            'billing/price-bundles/count',
            query=query,
            cast_to=BillingPriceBundleListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def read(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleReadResponse:
        return self._client.request(
            'GET',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}',
            cast_to=BillingPriceBundleReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        price_bundle_id: str,
        data: BillingPriceBundleUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}',
            body=data,
            cast_to=BillingPriceBundleUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def archive(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleArchiveResponse:
        return self._client.request(
            'POST',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}/archive',
            cast_to=BillingPriceBundleArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def restore(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleRestoreResponse:
        return self._client.request(
            'POST',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}/restore',
            cast_to=BillingPriceBundleRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def publish(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundlePublishResponse:
        return self._client.request(
            'POST',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}/publish',
            cast_to=BillingPriceBundlePublishResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingPriceBundlesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_activations(
        self,
        query: BillingPriceBundleListActivationsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingPriceBundleListActivationsItem]:
        return await self._client.request(
            'GET',
            'billing/price-bundle-activations/',
            query=query,
            cast_to=AsyncPage[BillingPriceBundleListActivationsItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def activate(
        self,
        data: BillingPriceBundleActivateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleActivateResponse:
        return await self._client.request(
            'POST',
            'billing/price-bundle-activations/',
            body=data,
            cast_to=BillingPriceBundleActivateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_activations_count(
        self,
        query: BillingPriceBundleListActivationsCountQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleListActivationsCountResponse:
        return await self._client.request(
            'GET',
            'billing/price-bundle-activations/count',
            query=query,
            cast_to=BillingPriceBundleListActivationsCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def deactivate(
        self,
        price_bundle_activation_id: str,
        data: BillingPriceBundleDeactivateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleDeactivateResponse:
        return await self._client.request(
            'POST',
            (
                f'billing/price-bundle-activations/{encode_path_param(price_bundle_activation_id)}'
                '/deactivate'
            ),
            body=data,
            cast_to=BillingPriceBundleDeactivateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def read_available_bundle_transitions(
        self,
        query: BillingPriceBundleReadAvailableBundleTransitionsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleReadAvailableBundleTransitionsResponse:
        return await self._client.request(
            'GET',
            'billing/price-bundle-transitions/',
            query=query,
            cast_to=BillingPriceBundleReadAvailableBundleTransitionsResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list(
        self,
        query: BillingPriceBundleListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingPriceBundleListItem]:
        return await self._client.request(
            'GET',
            'billing/price-bundles/',
            query=query,
            cast_to=AsyncPage[BillingPriceBundleListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingPriceBundleCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleCreateResponse:
        return await self._client.request(
            'POST',
            'billing/price-bundles/',
            body=data,
            cast_to=BillingPriceBundleCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingPriceBundleListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleListCountResponse:
        return await self._client.request(
            'GET',
            'billing/price-bundles/count',
            query=query,
            cast_to=BillingPriceBundleListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def read(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleReadResponse:
        return await self._client.request(
            'GET',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}',
            cast_to=BillingPriceBundleReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        price_bundle_id: str,
        data: BillingPriceBundleUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}',
            body=data,
            cast_to=BillingPriceBundleUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def archive(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleArchiveResponse:
        return await self._client.request(
            'POST',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}/archive',
            cast_to=BillingPriceBundleArchiveResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def restore(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundleRestoreResponse:
        return await self._client.request(
            'POST',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}/restore',
            cast_to=BillingPriceBundleRestoreResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def publish(
        self,
        price_bundle_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingPriceBundlePublishResponse:
        return await self._client.request(
            'POST',
            f'billing/price-bundles/{encode_path_param(price_bundle_id)}/publish',
            cast_to=BillingPriceBundlePublishResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
