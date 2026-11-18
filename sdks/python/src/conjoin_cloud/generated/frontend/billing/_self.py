from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._credential import Credential
from conjoin_cloud._request_options import RequestOptions, session_auth
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated.frontend._models import (
    BillingSelfActivatePriceBundlesRequest,
    BillingSelfActivatePriceBundlesResponse,
    BillingSelfCreatePaymentMethodRequest,
    BillingSelfCreatePaymentMethodResponse,
    BillingSelfDeactivatePriceBundleRequest,
    BillingSelfDeactivatePriceBundleResponse,
    BillingSelfListEntitlementOverridesCountQuery,
    BillingSelfListEntitlementOverridesCountResponse,
    BillingSelfListEntitlementOverridesItem,
    BillingSelfListEntitlementOverridesQuery,
    BillingSelfListPaymentMethodsCountQuery,
    BillingSelfListPaymentMethodsCountResponse,
    BillingSelfListPaymentMethodsItem,
    BillingSelfListPaymentMethodsQuery,
    BillingSelfListPriceBundlesCountQuery,
    BillingSelfListPriceBundlesCountResponse,
    BillingSelfListPriceBundlesItem,
    BillingSelfListPriceBundlesQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingSelvesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_payment_methods(
        self,
        query: BillingSelfListPaymentMethodsQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingSelfListPaymentMethodsItem]:
        return self._client.request(
            'GET',
            'billing/self/payment-methods/',
            query=query,
            cast_to=Page[BillingSelfListPaymentMethodsItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def create_payment_method(
        self,
        data: BillingSelfCreatePaymentMethodRequest,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfCreatePaymentMethodResponse:
        return self._client.request(
            'POST',
            'billing/self/payment-methods/',
            body=data,
            cast_to=BillingSelfCreatePaymentMethodResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def list_payment_methods_count(
        self,
        query: BillingSelfListPaymentMethodsCountQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfListPaymentMethodsCountResponse:
        return self._client.request(
            'GET',
            'billing/self/payment-methods/count',
            query=query,
            cast_to=BillingSelfListPaymentMethodsCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def list_entitlement_overrides(
        self,
        query: BillingSelfListEntitlementOverridesQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingSelfListEntitlementOverridesItem]:
        return self._client.request(
            'GET',
            'billing/self/entitlement-overrides/',
            query=query,
            cast_to=Page[BillingSelfListEntitlementOverridesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def list_price_bundles(
        self,
        query: BillingSelfListPriceBundlesQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingSelfListPriceBundlesItem]:
        return self._client.request(
            'GET',
            'billing/self/price-bundles/',
            query=query,
            cast_to=Page[BillingSelfListPriceBundlesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def list_entitlement_overrides_count(
        self,
        query: BillingSelfListEntitlementOverridesCountQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfListEntitlementOverridesCountResponse:
        return self._client.request(
            'GET',
            'billing/self/entitlement-overrides/count',
            query=query,
            cast_to=BillingSelfListEntitlementOverridesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def list_price_bundles_count(
        self,
        query: BillingSelfListPriceBundlesCountQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfListPriceBundlesCountResponse:
        return self._client.request(
            'GET',
            'billing/self/price-bundles/count',
            query=query,
            cast_to=BillingSelfListPriceBundlesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def activate_price_bundles(
        self,
        data: BillingSelfActivatePriceBundlesRequest,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfActivatePriceBundlesResponse:
        return self._client.request(
            'POST',
            'billing/self/price-bundle-activations/',
            body=data,
            cast_to=BillingSelfActivatePriceBundlesResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    def deactivate_price_bundle(
        self,
        price_bundle_activation_id: str,
        data: BillingSelfDeactivatePriceBundleRequest,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfDeactivatePriceBundleResponse:
        return self._client.request(
            'POST',
            (
                'billing/self/price-bundle-activations'
                f'/{encode_path_param(price_bundle_activation_id)}/deactivate'
            ),
            body=data,
            cast_to=BillingSelfDeactivatePriceBundleResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )


class AsyncBillingSelvesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_payment_methods(
        self,
        query: BillingSelfListPaymentMethodsQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingSelfListPaymentMethodsItem]:
        return await self._client.request(
            'GET',
            'billing/self/payment-methods/',
            query=query,
            cast_to=AsyncPage[BillingSelfListPaymentMethodsItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def create_payment_method(
        self,
        data: BillingSelfCreatePaymentMethodRequest,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfCreatePaymentMethodResponse:
        return await self._client.request(
            'POST',
            'billing/self/payment-methods/',
            body=data,
            cast_to=BillingSelfCreatePaymentMethodResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def list_payment_methods_count(
        self,
        query: BillingSelfListPaymentMethodsCountQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfListPaymentMethodsCountResponse:
        return await self._client.request(
            'GET',
            'billing/self/payment-methods/count',
            query=query,
            cast_to=BillingSelfListPaymentMethodsCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def list_entitlement_overrides(
        self,
        query: BillingSelfListEntitlementOverridesQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingSelfListEntitlementOverridesItem]:
        return await self._client.request(
            'GET',
            'billing/self/entitlement-overrides/',
            query=query,
            cast_to=AsyncPage[BillingSelfListEntitlementOverridesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def list_price_bundles(
        self,
        query: BillingSelfListPriceBundlesQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingSelfListPriceBundlesItem]:
        return await self._client.request(
            'GET',
            'billing/self/price-bundles/',
            query=query,
            cast_to=AsyncPage[BillingSelfListPriceBundlesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def list_entitlement_overrides_count(
        self,
        query: BillingSelfListEntitlementOverridesCountQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfListEntitlementOverridesCountResponse:
        return await self._client.request(
            'GET',
            'billing/self/entitlement-overrides/count',
            query=query,
            cast_to=BillingSelfListEntitlementOverridesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def list_price_bundles_count(
        self,
        query: BillingSelfListPriceBundlesCountQuery | None = None,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfListPriceBundlesCountResponse:
        return await self._client.request(
            'GET',
            'billing/self/price-bundles/count',
            query=query,
            cast_to=BillingSelfListPriceBundlesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def activate_price_bundles(
        self,
        data: BillingSelfActivatePriceBundlesRequest,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfActivatePriceBundlesResponse:
        return await self._client.request(
            'POST',
            'billing/self/price-bundle-activations/',
            body=data,
            cast_to=BillingSelfActivatePriceBundlesResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )

    async def deactivate_price_bundle(
        self,
        price_bundle_activation_id: str,
        data: BillingSelfDeactivatePriceBundleRequest,
        *,
        session_token: Credential,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSelfDeactivatePriceBundleResponse:
        return await self._client.request(
            'POST',
            (
                'billing/self/price-bundle-activations'
                f'/{encode_path_param(price_bundle_activation_id)}/deactivate'
            ),
            body=data,
            cast_to=BillingSelfDeactivatePriceBundleResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            default_auth=session_auth(session_token),
        )
