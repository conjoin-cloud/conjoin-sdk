from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AiContextCreateIndexRequest,
    AiContextCreateIndexResponse,
    AiContextDeleteIndexResponse,
    AiContextListIndexesItem,
    AiContextListIndexesQuery,
    AiContextListQueryLogsItem,
    AiContextListQueryLogsQuery,
    AiContextQueryRequest,
    AiContextQueryResponse,
    AiContextReadIndexResponse,
    AiContextSyncIndexResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AiContextsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_indexes(
        self,
        query: AiContextListIndexesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiContextListIndexesItem]:
        return self._client.request(
            'GET',
            'ai/context/indexes',
            query=query,
            cast_to=Page[AiContextListIndexesItem],
            request_options=request_options,
        )

    def create_index(
        self,
        data: AiContextCreateIndexRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextCreateIndexResponse:
        return self._client.request(
            'POST',
            'ai/context/indexes',
            body=data,
            cast_to=AiContextCreateIndexResponse,
            request_options=request_options,
        )

    def read_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextReadIndexResponse:
        return self._client.request(
            'GET',
            f'ai/context/indexes/{encode_path_param(index_id)}',
            cast_to=AiContextReadIndexResponse,
            request_options=request_options,
        )

    def delete_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextDeleteIndexResponse:
        return self._client.request(
            'DELETE',
            f'ai/context/indexes/{encode_path_param(index_id)}',
            cast_to=AiContextDeleteIndexResponse,
            request_options=request_options,
        )

    def sync_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextSyncIndexResponse:
        return self._client.request(
            'POST',
            f'ai/context/indexes/{encode_path_param(index_id)}/sync',
            cast_to=AiContextSyncIndexResponse,
            request_options=request_options,
        )

    def query(
        self,
        data: AiContextQueryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextQueryResponse:
        return self._client.request(
            'POST',
            'ai/context/query',
            body=data,
            cast_to=AiContextQueryResponse,
            request_options=request_options,
        )

    def list_query_logs(
        self,
        query: AiContextListQueryLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiContextListQueryLogsItem]:
        return self._client.request(
            'GET',
            'ai/context/query-logs',
            query=query,
            cast_to=Page[AiContextListQueryLogsItem],
            request_options=request_options,
        )


class AsyncAiContextsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_indexes(
        self,
        query: AiContextListIndexesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiContextListIndexesItem]:
        return await self._client.request(
            'GET',
            'ai/context/indexes',
            query=query,
            cast_to=AsyncPage[AiContextListIndexesItem],
            request_options=request_options,
        )

    async def create_index(
        self,
        data: AiContextCreateIndexRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextCreateIndexResponse:
        return await self._client.request(
            'POST',
            'ai/context/indexes',
            body=data,
            cast_to=AiContextCreateIndexResponse,
            request_options=request_options,
        )

    async def read_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextReadIndexResponse:
        return await self._client.request(
            'GET',
            f'ai/context/indexes/{encode_path_param(index_id)}',
            cast_to=AiContextReadIndexResponse,
            request_options=request_options,
        )

    async def delete_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextDeleteIndexResponse:
        return await self._client.request(
            'DELETE',
            f'ai/context/indexes/{encode_path_param(index_id)}',
            cast_to=AiContextDeleteIndexResponse,
            request_options=request_options,
        )

    async def sync_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextSyncIndexResponse:
        return await self._client.request(
            'POST',
            f'ai/context/indexes/{encode_path_param(index_id)}/sync',
            cast_to=AiContextSyncIndexResponse,
            request_options=request_options,
        )

    async def query(
        self,
        data: AiContextQueryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextQueryResponse:
        return await self._client.request(
            'POST',
            'ai/context/query',
            body=data,
            cast_to=AiContextQueryResponse,
            request_options=request_options,
        )

    async def list_query_logs(
        self,
        query: AiContextListQueryLogsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiContextListQueryLogsItem]:
        return await self._client.request(
            'GET',
            'ai/context/query-logs',
            query=query,
            cast_to=AsyncPage[AiContextListQueryLogsItem],
            request_options=request_options,
        )
