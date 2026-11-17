from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    BillingFeatureAccessCheckEntitlementRequest,
    BillingFeatureAccessCheckEntitlementResponse,
    BillingFeatureAccessTrackFeatureUsageRequest,
    BillingFeatureAccessTrackFeatureUsageResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingFeatureAccessesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def check_entitlement(
        self,
        data: BillingFeatureAccessCheckEntitlementRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingFeatureAccessCheckEntitlementResponse:
        return self._client.request(
            'POST',
            'billing/entitlements/check',
            body=data,
            cast_to=BillingFeatureAccessCheckEntitlementResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def track_feature_usage(
        self,
        data: BillingFeatureAccessTrackFeatureUsageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingFeatureAccessTrackFeatureUsageResponse:
        return self._client.request(
            'POST',
            'billing/entitlements/track',
            body=data,
            cast_to=BillingFeatureAccessTrackFeatureUsageResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )


class AsyncBillingFeatureAccessesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def check_entitlement(
        self,
        data: BillingFeatureAccessCheckEntitlementRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingFeatureAccessCheckEntitlementResponse:
        return await self._client.request(
            'POST',
            'billing/entitlements/check',
            body=data,
            cast_to=BillingFeatureAccessCheckEntitlementResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def track_feature_usage(
        self,
        data: BillingFeatureAccessTrackFeatureUsageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingFeatureAccessTrackFeatureUsageResponse:
        return await self._client.request(
            'POST',
            'billing/entitlements/track',
            body=data,
            cast_to=BillingFeatureAccessTrackFeatureUsageResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )
