from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AiContextCreateIndexRequest,
    AiContextCreateIndexResponse,
    AiContextCreateQueryRequest,
    AiContextCreateQueryResponse,
    AiContextDeleteIndexResponse,
    AiContextListIndexesCountQuery,
    AiContextListIndexesCountResponse,
    AiContextListIndexesItem,
    AiContextListIndexesQuery,
    AiContextListQueriesCountQuery,
    AiContextListQueriesCountResponse,
    AiContextListQueriesItem,
    AiContextListQueriesQuery,
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
            'ai/context-indexes/',
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
            'ai/context-indexes/',
            body=data,
            cast_to=AiContextCreateIndexResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_indexes_count(
        self,
        query: AiContextListIndexesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextListIndexesCountResponse:
        return self._client.request(
            'GET',
            'ai/context-indexes/count',
            query=query,
            cast_to=AiContextListIndexesCountResponse,
            request_options=request_options,
        )

    def read_index(
        self,
        context_index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextReadIndexResponse:
        return self._client.request(
            'GET',
            f'ai/context-indexes/{encode_path_param(context_index_id)}',
            cast_to=AiContextReadIndexResponse,
            request_options=request_options,
        )

    def delete_index(
        self,
        context_index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextDeleteIndexResponse:
        return self._client.request(
            'DELETE',
            f'ai/context-indexes/{encode_path_param(context_index_id)}',
            cast_to=AiContextDeleteIndexResponse,
            request_options=request_options,
        )

    def sync_index(
        self,
        context_index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextSyncIndexResponse:
        return self._client.request(
            'POST',
            f'ai/context-indexes/{encode_path_param(context_index_id)}/sync',
            cast_to=AiContextSyncIndexResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_queries(
        self,
        query: AiContextListQueriesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiContextListQueriesItem]:
        return self._client.request(
            'GET',
            'ai/context-queries/',
            query=query,
            cast_to=Page[AiContextListQueriesItem],
            request_options=request_options,
        )

    def create_query(
        self,
        data: AiContextCreateQueryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextCreateQueryResponse:
        return self._client.request(
            'POST',
            'ai/context-queries/',
            body=data,
            cast_to=AiContextCreateQueryResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_queries_count(
        self,
        query: AiContextListQueriesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextListQueriesCountResponse:
        return self._client.request(
            'GET',
            'ai/context-queries/count',
            query=query,
            cast_to=AiContextListQueriesCountResponse,
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
            'ai/context-indexes/',
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
            'ai/context-indexes/',
            body=data,
            cast_to=AiContextCreateIndexResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_indexes_count(
        self,
        query: AiContextListIndexesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextListIndexesCountResponse:
        return await self._client.request(
            'GET',
            'ai/context-indexes/count',
            query=query,
            cast_to=AiContextListIndexesCountResponse,
            request_options=request_options,
        )

    async def read_index(
        self,
        context_index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextReadIndexResponse:
        return await self._client.request(
            'GET',
            f'ai/context-indexes/{encode_path_param(context_index_id)}',
            cast_to=AiContextReadIndexResponse,
            request_options=request_options,
        )

    async def delete_index(
        self,
        context_index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextDeleteIndexResponse:
        return await self._client.request(
            'DELETE',
            f'ai/context-indexes/{encode_path_param(context_index_id)}',
            cast_to=AiContextDeleteIndexResponse,
            request_options=request_options,
        )

    async def sync_index(
        self,
        context_index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextSyncIndexResponse:
        return await self._client.request(
            'POST',
            f'ai/context-indexes/{encode_path_param(context_index_id)}/sync',
            cast_to=AiContextSyncIndexResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_queries(
        self,
        query: AiContextListQueriesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiContextListQueriesItem]:
        return await self._client.request(
            'GET',
            'ai/context-queries/',
            query=query,
            cast_to=AsyncPage[AiContextListQueriesItem],
            request_options=request_options,
        )

    async def create_query(
        self,
        data: AiContextCreateQueryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextCreateQueryResponse:
        return await self._client.request(
            'POST',
            'ai/context-queries/',
            body=data,
            cast_to=AiContextCreateQueryResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_queries_count(
        self,
        query: AiContextListQueriesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiContextListQueriesCountResponse:
        return await self._client.request(
            'GET',
            'ai/context-queries/count',
            query=query,
            cast_to=AiContextListQueriesCountResponse,
            request_options=request_options,
        )
