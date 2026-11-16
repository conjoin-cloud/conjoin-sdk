from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingSubscriptionScheduleCancelResponse,
    BillingSubscriptionScheduleCreateRequest,
    BillingSubscriptionScheduleCreateResponse,
    BillingSubscriptionScheduleGetResponse,
    BillingSubscriptionScheduleListCountQuery,
    BillingSubscriptionScheduleListCountResponse,
    BillingSubscriptionScheduleListItem,
    BillingSubscriptionScheduleListQuery,
    BillingSubscriptionScheduleReleaseResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingSubscriptionSchedulesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        subscription_id: str,
        query: BillingSubscriptionScheduleListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingSubscriptionScheduleListItem]:
        return self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/schedules',
            query=query,
            cast_to=Page[BillingSubscriptionScheduleListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        subscription_id: str,
        data: BillingSubscriptionScheduleCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleCreateResponse:
        return self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/schedules',
            body=data,
            cast_to=BillingSubscriptionScheduleCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        subscription_id: str,
        query: BillingSubscriptionScheduleListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleListCountResponse:
        return self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/schedules/count',
            query=query,
            cast_to=BillingSubscriptionScheduleListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def get(
        self,
        subscription_schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleGetResponse:
        return self._client.request(
            'GET',
            f'billing/subscription-schedules/{encode_path_param(subscription_schedule_id)}',
            cast_to=BillingSubscriptionScheduleGetResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def cancel(
        self,
        subscription_schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleCancelResponse:
        return self._client.request(
            'POST',
            f'billing/subscription-schedules/{encode_path_param(subscription_schedule_id)}/cancel',
            cast_to=BillingSubscriptionScheduleCancelResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def release(
        self,
        subscription_schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleReleaseResponse:
        return self._client.request(
            'POST',
            f'billing/subscription-schedules/{encode_path_param(subscription_schedule_id)}/release',
            cast_to=BillingSubscriptionScheduleReleaseResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )


class AsyncBillingSubscriptionSchedulesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        subscription_id: str,
        query: BillingSubscriptionScheduleListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingSubscriptionScheduleListItem]:
        return await self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/schedules',
            query=query,
            cast_to=AsyncPage[BillingSubscriptionScheduleListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        subscription_id: str,
        data: BillingSubscriptionScheduleCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleCreateResponse:
        return await self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/schedules',
            body=data,
            cast_to=BillingSubscriptionScheduleCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        subscription_id: str,
        query: BillingSubscriptionScheduleListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleListCountResponse:
        return await self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/schedules/count',
            query=query,
            cast_to=BillingSubscriptionScheduleListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def get(
        self,
        subscription_schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleGetResponse:
        return await self._client.request(
            'GET',
            f'billing/subscription-schedules/{encode_path_param(subscription_schedule_id)}',
            cast_to=BillingSubscriptionScheduleGetResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def cancel(
        self,
        subscription_schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleCancelResponse:
        return await self._client.request(
            'POST',
            f'billing/subscription-schedules/{encode_path_param(subscription_schedule_id)}/cancel',
            cast_to=BillingSubscriptionScheduleCancelResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def release(
        self,
        subscription_schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionScheduleReleaseResponse:
        return await self._client.request(
            'POST',
            f'billing/subscription-schedules/{encode_path_param(subscription_schedule_id)}/release',
            cast_to=BillingSubscriptionScheduleReleaseResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )
