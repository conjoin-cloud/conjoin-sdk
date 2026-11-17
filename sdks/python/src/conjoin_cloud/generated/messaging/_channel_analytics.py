from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingChannelAnalyticsCreateReportRequest,
    MessagingChannelAnalyticsCreateReportResponse,
    MessagingChannelAnalyticsGenerateSummariesQuery,
    MessagingChannelAnalyticsGenerateSummariesResponse,
    MessagingChannelAnalyticsIncrementClicksRequest,
    MessagingChannelAnalyticsIncrementClicksResponse,
    MessagingChannelAnalyticsIncrementDeliveriesRequest,
    MessagingChannelAnalyticsIncrementDeliveriesResponse,
    MessagingChannelAnalyticsIncrementOpensRequest,
    MessagingChannelAnalyticsIncrementOpensResponse,
    MessagingChannelAnalyticsIncrementSubscribesRequest,
    MessagingChannelAnalyticsIncrementSubscribesResponse,
    MessagingChannelAnalyticsIncrementUnsubscribesRequest,
    MessagingChannelAnalyticsIncrementUnsubscribesResponse,
    MessagingChannelAnalyticsListCountQuery,
    MessagingChannelAnalyticsListCountResponse,
    MessagingChannelAnalyticsListItem,
    MessagingChannelAnalyticsListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingChannelAnalyticsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: MessagingChannelAnalyticsListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingChannelAnalyticsListItem]:
        return self._client.request(
            'GET',
            'messaging/analytics/',
            query=query,
            cast_to=Page[MessagingChannelAnalyticsListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create_report(
        self,
        data: MessagingChannelAnalyticsCreateReportRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsCreateReportResponse:
        return self._client.request(
            'POST',
            'messaging/analytics-reports/',
            body=data,
            cast_to=MessagingChannelAnalyticsCreateReportResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: MessagingChannelAnalyticsListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsListCountResponse:
        return self._client.request(
            'GET',
            'messaging/analytics/count',
            query=query,
            cast_to=MessagingChannelAnalyticsListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def generate_summaries(
        self,
        query: MessagingChannelAnalyticsGenerateSummariesQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsGenerateSummariesResponse:
        return self._client.request(
            'GET',
            'messaging/analytics/stats',
            query=query,
            cast_to=MessagingChannelAnalyticsGenerateSummariesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_opens(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementOpensRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementOpensResponse:
        return self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/opens',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementOpensResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def increment_clicks(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementClicksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementClicksResponse:
        return self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/clicks',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementClicksResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def increment_deliveries(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementDeliveriesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementDeliveriesResponse:
        return self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/deliveries',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementDeliveriesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def increment_subscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementSubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementSubscribesResponse:
        return self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/subscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementSubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def increment_unsubscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementUnsubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementUnsubscribesResponse:
        return self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/unsubscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementUnsubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingChannelAnalyticsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: MessagingChannelAnalyticsListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingChannelAnalyticsListItem]:
        return await self._client.request(
            'GET',
            'messaging/analytics/',
            query=query,
            cast_to=AsyncPage[MessagingChannelAnalyticsListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create_report(
        self,
        data: MessagingChannelAnalyticsCreateReportRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsCreateReportResponse:
        return await self._client.request(
            'POST',
            'messaging/analytics-reports/',
            body=data,
            cast_to=MessagingChannelAnalyticsCreateReportResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: MessagingChannelAnalyticsListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsListCountResponse:
        return await self._client.request(
            'GET',
            'messaging/analytics/count',
            query=query,
            cast_to=MessagingChannelAnalyticsListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def generate_summaries(
        self,
        query: MessagingChannelAnalyticsGenerateSummariesQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsGenerateSummariesResponse:
        return await self._client.request(
            'GET',
            'messaging/analytics/stats',
            query=query,
            cast_to=MessagingChannelAnalyticsGenerateSummariesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_opens(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementOpensRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementOpensResponse:
        return await self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/opens',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementOpensResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def increment_clicks(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementClicksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementClicksResponse:
        return await self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/clicks',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementClicksResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def increment_deliveries(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementDeliveriesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementDeliveriesResponse:
        return await self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/deliveries',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementDeliveriesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def increment_subscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementSubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementSubscribesResponse:
        return await self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/subscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementSubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def increment_unsubscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementUnsubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementUnsubscribesResponse:
        return await self._client.request(
            'POST',
            f'messaging/analytics/{encode_path_param(analytics_id)}/unsubscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementUnsubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
