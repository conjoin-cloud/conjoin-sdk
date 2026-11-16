from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingSubscriptionCancelRequest,
    BillingSubscriptionCancelResponse,
    BillingSubscriptionCreatePlanChangeRequest,
    BillingSubscriptionCreatePlanChangeResponse,
    BillingSubscriptionCreateRequest,
    BillingSubscriptionCreateResponse,
    BillingSubscriptionListCountQuery,
    BillingSubscriptionListCountResponse,
    BillingSubscriptionListCyclesCountQuery,
    BillingSubscriptionListCyclesCountResponse,
    BillingSubscriptionListCyclesItem,
    BillingSubscriptionListCyclesQuery,
    BillingSubscriptionListItem,
    BillingSubscriptionListQuery,
    BillingSubscriptionPauseRequest,
    BillingSubscriptionPauseResponse,
    BillingSubscriptionReadResponse,
    BillingSubscriptionReadUsageSummaryItem,
    BillingSubscriptionReadUsageSummaryQuery,
    BillingSubscriptionRecordUsageRequest,
    BillingSubscriptionResumeResponse,
    BillingSubscriptionUpdateRequest,
    BillingSubscriptionUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingSubscriptionsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingSubscriptionListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingSubscriptionListItem]:
        return self._client.request(
            'GET',
            'billing/subscriptions/',
            query=query,
            cast_to=Page[BillingSubscriptionListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create(
        self,
        data: BillingSubscriptionCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionCreateResponse:
        return self._client.request(
            'POST',
            'billing/subscriptions/',
            body=data,
            cast_to=BillingSubscriptionCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def list_cycles(
        self,
        subscription_id: str,
        query: BillingSubscriptionListCyclesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingSubscriptionListCyclesItem]:
        return self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/cycles',
            query=query,
            cast_to=Page[BillingSubscriptionListCyclesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_count(
        self,
        query: BillingSubscriptionListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionListCountResponse:
        return self._client.request(
            'GET',
            'billing/subscriptions/count',
            query=query,
            cast_to=BillingSubscriptionListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def read(
        self,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionReadResponse:
        return self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}',
            cast_to=BillingSubscriptionReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def update(
        self,
        subscription_id: str,
        data: BillingSubscriptionUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/subscriptions/{encode_path_param(subscription_id)}',
            body=data,
            cast_to=BillingSubscriptionUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def create_plan_change(
        self,
        subscription_id: str,
        data: BillingSubscriptionCreatePlanChangeRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionCreatePlanChangeResponse:
        return self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/plan-changes',
            body=data,
            cast_to=BillingSubscriptionCreatePlanChangeResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def cancel(
        self,
        subscription_id: str,
        data: BillingSubscriptionCancelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionCancelResponse:
        return self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/cancel',
            body=data,
            cast_to=BillingSubscriptionCancelResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def pause(
        self,
        subscription_id: str,
        data: BillingSubscriptionPauseRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionPauseResponse:
        return self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/pause',
            body=data,
            cast_to=BillingSubscriptionPauseResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def resume(
        self,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionResumeResponse:
        return self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/resume',
            cast_to=BillingSubscriptionResumeResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def record_usage(
        self,
        subscription_id: str,
        data: BillingSubscriptionRecordUsageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/usage-records',
            body=data,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    def read_usage_summary(
        self,
        subscription_id: str,
        query: BillingSubscriptionReadUsageSummaryQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> list[BillingSubscriptionReadUsageSummaryItem]:
        return self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/usage-summaries',
            query=query,
            cast_to=list[BillingSubscriptionReadUsageSummaryItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    def list_cycles_count(
        self,
        subscription_id: str,
        query: BillingSubscriptionListCyclesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionListCyclesCountResponse:
        return self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/cycles/count',
            query=query,
            cast_to=BillingSubscriptionListCyclesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )


class AsyncBillingSubscriptionsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingSubscriptionListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingSubscriptionListItem]:
        return await self._client.request(
            'GET',
            'billing/subscriptions/',
            query=query,
            cast_to=AsyncPage[BillingSubscriptionListItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create(
        self,
        data: BillingSubscriptionCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionCreateResponse:
        return await self._client.request(
            'POST',
            'billing/subscriptions/',
            body=data,
            cast_to=BillingSubscriptionCreateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def list_cycles(
        self,
        subscription_id: str,
        query: BillingSubscriptionListCyclesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingSubscriptionListCyclesItem]:
        return await self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/cycles',
            query=query,
            cast_to=AsyncPage[BillingSubscriptionListCyclesItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_count(
        self,
        query: BillingSubscriptionListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionListCountResponse:
        return await self._client.request(
            'GET',
            'billing/subscriptions/count',
            query=query,
            cast_to=BillingSubscriptionListCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def read(
        self,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionReadResponse:
        return await self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}',
            cast_to=BillingSubscriptionReadResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def update(
        self,
        subscription_id: str,
        data: BillingSubscriptionUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/subscriptions/{encode_path_param(subscription_id)}',
            body=data,
            cast_to=BillingSubscriptionUpdateResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def create_plan_change(
        self,
        subscription_id: str,
        data: BillingSubscriptionCreatePlanChangeRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionCreatePlanChangeResponse:
        return await self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/plan-changes',
            body=data,
            cast_to=BillingSubscriptionCreatePlanChangeResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def cancel(
        self,
        subscription_id: str,
        data: BillingSubscriptionCancelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionCancelResponse:
        return await self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/cancel',
            body=data,
            cast_to=BillingSubscriptionCancelResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def pause(
        self,
        subscription_id: str,
        data: BillingSubscriptionPauseRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionPauseResponse:
        return await self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/pause',
            body=data,
            cast_to=BillingSubscriptionPauseResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def resume(
        self,
        subscription_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionResumeResponse:
        return await self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/resume',
            cast_to=BillingSubscriptionResumeResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def record_usage(
        self,
        subscription_id: str,
        data: BillingSubscriptionRecordUsageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/usage-records',
            body=data,
            request_options=request_options,
            scopes=('billing_entity_id',),
            accepts_idempotency_key=True,
        )

    async def read_usage_summary(
        self,
        subscription_id: str,
        query: BillingSubscriptionReadUsageSummaryQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> list[BillingSubscriptionReadUsageSummaryItem]:
        return await self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/usage-summaries',
            query=query,
            cast_to=list[BillingSubscriptionReadUsageSummaryItem],
            request_options=request_options,
            scopes=('billing_entity_id',),
        )

    async def list_cycles_count(
        self,
        subscription_id: str,
        query: BillingSubscriptionListCyclesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingSubscriptionListCyclesCountResponse:
        return await self._client.request(
            'GET',
            f'billing/subscriptions/{encode_path_param(subscription_id)}/cycles/count',
            query=query,
            cast_to=BillingSubscriptionListCyclesCountResponse,
            request_options=request_options,
            scopes=('billing_entity_id',),
        )
