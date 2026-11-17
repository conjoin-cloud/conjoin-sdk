from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._wire import wire_names
from conjoin_cloud.generated._models import (
    CloudAuditReadLogsCountQuery,
    CloudAuditReadLogsCountResponse,
    CloudAuditReadLogsItem,
    CloudAuditReadLogsQuery,
    CloudAuditReadStatsQuery,
    CloudAuditReadStatsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


_READ_LOGS_QUERY_ALIASES = {
    'from_': 'from',
}
_READ_LOGS_COUNT_QUERY_ALIASES = {
    'from_': 'from',
}
_READ_STATS_QUERY_ALIASES = {
    'from_': 'from',
}


class CloudAuditsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_logs(
        self,
        query: CloudAuditReadLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudAuditReadLogsItem]:
        return self._client.request(
            'GET',
            'cloud/audit-logs/',
            query=wire_names(query, _READ_LOGS_QUERY_ALIASES),
            cast_to=Page[CloudAuditReadLogsItem],
            request_options=request_options,
        )

    def read_logs_count(
        self,
        query: CloudAuditReadLogsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAuditReadLogsCountResponse:
        return self._client.request(
            'GET',
            'cloud/audit-logs/count',
            query=wire_names(query, _READ_LOGS_COUNT_QUERY_ALIASES),
            cast_to=CloudAuditReadLogsCountResponse,
            request_options=request_options,
        )

    def read_stats(
        self,
        query: CloudAuditReadStatsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAuditReadStatsResponse:
        return self._client.request(
            'GET',
            'cloud/audit-logs/stats',
            query=wire_names(query, _READ_STATS_QUERY_ALIASES),
            cast_to=CloudAuditReadStatsResponse,
            request_options=request_options,
        )


class AsyncCloudAuditsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_logs(
        self,
        query: CloudAuditReadLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudAuditReadLogsItem]:
        return await self._client.request(
            'GET',
            'cloud/audit-logs/',
            query=wire_names(query, _READ_LOGS_QUERY_ALIASES),
            cast_to=AsyncPage[CloudAuditReadLogsItem],
            request_options=request_options,
        )

    async def read_logs_count(
        self,
        query: CloudAuditReadLogsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAuditReadLogsCountResponse:
        return await self._client.request(
            'GET',
            'cloud/audit-logs/count',
            query=wire_names(query, _READ_LOGS_COUNT_QUERY_ALIASES),
            cast_to=CloudAuditReadLogsCountResponse,
            request_options=request_options,
        )

    async def read_stats(
        self,
        query: CloudAuditReadStatsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAuditReadStatsResponse:
        return await self._client.request(
            'GET',
            'cloud/audit-logs/stats',
            query=wire_names(query, _READ_STATS_QUERY_ALIASES),
            cast_to=CloudAuditReadStatsResponse,
            request_options=request_options,
        )
