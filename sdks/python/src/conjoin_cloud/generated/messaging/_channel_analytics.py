from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingChannelAnalyticsCreateReportRequest,
    MessagingChannelAnalyticsCreateReportResponse,
    MessagingChannelAnalyticsGenerateSummariesRequest,
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
    MessagingChannelAnalyticsListItem,
    MessagingChannelAnalyticsListRequest,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingChannelAnalyticsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        data: MessagingChannelAnalyticsListRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingChannelAnalyticsListItem]:
        return self._client.request(
            'POST',
            'messaging/email/analytics/',
            body=data,
            cast_to=Page[MessagingChannelAnalyticsListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def generate_summaries(
        self,
        channel_id: str,
        data: MessagingChannelAnalyticsGenerateSummariesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsGenerateSummariesResponse:
        return self._client.request(
            'POST',
            f'messaging/email/analytics/channels/{encode_path_param(channel_id)}/generate',
            body=data,
            cast_to=MessagingChannelAnalyticsGenerateSummariesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def create_report(
        self,
        message_id: str,
        channel_id: str,
        data: MessagingChannelAnalyticsCreateReportRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsCreateReportResponse:
        return self._client.request(
            'POST',
            (
                f'messaging/email/analytics/messages/{encode_path_param(message_id)}/channels'
                f'/{encode_path_param(channel_id)}/reports'
            ),
            body=data,
            cast_to=MessagingChannelAnalyticsCreateReportResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def increment_opens(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementOpensRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementOpensResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/opens',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementOpensResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_clicks(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementClicksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementClicksResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/clicks',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementClicksResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_deliveries(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementDeliveriesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementDeliveriesResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/deliveries',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementDeliveriesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_subscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementSubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementSubscribesResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/subscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementSubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_unsubscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementUnsubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementUnsubscribesResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/unsubscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementUnsubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingChannelAnalyticsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        data: MessagingChannelAnalyticsListRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingChannelAnalyticsListItem]:
        return await self._client.request(
            'POST',
            'messaging/email/analytics/',
            body=data,
            cast_to=AsyncPage[MessagingChannelAnalyticsListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def generate_summaries(
        self,
        channel_id: str,
        data: MessagingChannelAnalyticsGenerateSummariesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsGenerateSummariesResponse:
        return await self._client.request(
            'POST',
            f'messaging/email/analytics/channels/{encode_path_param(channel_id)}/generate',
            body=data,
            cast_to=MessagingChannelAnalyticsGenerateSummariesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def create_report(
        self,
        message_id: str,
        channel_id: str,
        data: MessagingChannelAnalyticsCreateReportRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsCreateReportResponse:
        return await self._client.request(
            'POST',
            (
                f'messaging/email/analytics/messages/{encode_path_param(message_id)}/channels'
                f'/{encode_path_param(channel_id)}/reports'
            ),
            body=data,
            cast_to=MessagingChannelAnalyticsCreateReportResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def increment_opens(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementOpensRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementOpensResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/opens',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementOpensResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_clicks(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementClicksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementClicksResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/clicks',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementClicksResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_deliveries(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementDeliveriesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementDeliveriesResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/deliveries',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementDeliveriesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_subscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementSubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementSubscribesResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/subscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementSubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_unsubscribes(
        self,
        analytics_id: str,
        data: MessagingChannelAnalyticsIncrementUnsubscribesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsIncrementUnsubscribesResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/analytics/{encode_path_param(analytics_id)}/unsubscribes',
            body=data,
            cast_to=MessagingChannelAnalyticsIncrementUnsubscribesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
