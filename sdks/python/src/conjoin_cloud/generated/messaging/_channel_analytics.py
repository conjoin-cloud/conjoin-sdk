from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingChannelAnalyticsCreateReportResponse,
    MessagingChannelAnalyticsGenerateSummariesResponse,
    MessagingChannelAnalyticsListItem,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingChannelAnalyticsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingChannelAnalyticsListItem]:
        return self._client.request(
            'POST',
            'messaging/analytics/',
            cast_to=Page[MessagingChannelAnalyticsListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def generate_summaries(
        self,
        channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsGenerateSummariesResponse:
        return self._client.request(
            'POST',
            f'messaging/analytics/channels/{encode_path_param(channel_id)}/generate',
            cast_to=MessagingChannelAnalyticsGenerateSummariesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create_report(
        self,
        message_id: str,
        channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsCreateReportResponse:
        return self._client.request(
            'POST',
            (
                f'messaging/analytics/messages/{encode_path_param(message_id)}/channels'
                f'/{encode_path_param(channel_id)}/reports'
            ),
            cast_to=MessagingChannelAnalyticsCreateReportResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_opens(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/opens',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_clicks(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/clicks',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_deliveries(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/deliveries',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_subscribes(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/subscribes',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def increment_unsubscribes(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/unsubscribes',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingChannelAnalyticsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingChannelAnalyticsListItem]:
        return await self._client.request(
            'POST',
            'messaging/analytics/',
            cast_to=AsyncPage[MessagingChannelAnalyticsListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def generate_summaries(
        self,
        channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsGenerateSummariesResponse:
        return await self._client.request(
            'POST',
            f'messaging/analytics/channels/{encode_path_param(channel_id)}/generate',
            cast_to=MessagingChannelAnalyticsGenerateSummariesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create_report(
        self,
        message_id: str,
        channel_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingChannelAnalyticsCreateReportResponse:
        return await self._client.request(
            'POST',
            (
                f'messaging/analytics/messages/{encode_path_param(message_id)}/channels'
                f'/{encode_path_param(channel_id)}/reports'
            ),
            cast_to=MessagingChannelAnalyticsCreateReportResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_opens(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/opens',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_clicks(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/clicks',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_deliveries(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/deliveries',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_subscribes(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/subscribes',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def increment_unsubscribes(
        self,
        analytics_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'PATCH',
            f'messaging/analytics/{encode_path_param(analytics_id)}/unsubscribes',
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
