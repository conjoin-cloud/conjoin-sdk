from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    AiUsageListRecordsCountQuery,
    AiUsageListRecordsCountResponse,
    AiUsageListRecordsItem,
    AiUsageListRecordsQuery,
    AiUsageReadSummaryQuery,
    AiUsageReadSummaryResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AiUsagesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_records(
        self,
        query: AiUsageListRecordsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiUsageListRecordsItem]:
        return self._client.request(
            'GET',
            'ai/usage-records/',
            query=query,
            cast_to=Page[AiUsageListRecordsItem],
            request_options=request_options,
        )

    def list_records_count(
        self,
        query: AiUsageListRecordsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiUsageListRecordsCountResponse:
        return self._client.request(
            'GET',
            'ai/usage-records/count',
            query=query,
            cast_to=AiUsageListRecordsCountResponse,
            request_options=request_options,
        )

    def read_summary(
        self,
        query: AiUsageReadSummaryQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiUsageReadSummaryResponse:
        return self._client.request(
            'GET',
            'ai/usage/',
            query=query,
            cast_to=AiUsageReadSummaryResponse,
            request_options=request_options,
        )


class AsyncAiUsagesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_records(
        self,
        query: AiUsageListRecordsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiUsageListRecordsItem]:
        return await self._client.request(
            'GET',
            'ai/usage-records/',
            query=query,
            cast_to=AsyncPage[AiUsageListRecordsItem],
            request_options=request_options,
        )

    async def list_records_count(
        self,
        query: AiUsageListRecordsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiUsageListRecordsCountResponse:
        return await self._client.request(
            'GET',
            'ai/usage-records/count',
            query=query,
            cast_to=AiUsageListRecordsCountResponse,
            request_options=request_options,
        )

    async def read_summary(
        self,
        query: AiUsageReadSummaryQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiUsageReadSummaryResponse:
        return await self._client.request(
            'GET',
            'ai/usage/',
            query=query,
            cast_to=AiUsageReadSummaryResponse,
            request_options=request_options,
        )
