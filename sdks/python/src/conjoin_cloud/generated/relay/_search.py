from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    RelaySearchAutoSuggestRequest,
    RelaySearchAutoSuggestResponse,
    RelaySearchCreateIndexRequest,
    RelaySearchCreateIndexResponse,
    RelaySearchDeleteIndexResponse,
    RelaySearchIndexDocumentBatchRequest,
    RelaySearchIndexDocumentBatchResponse,
    RelaySearchIndexDocumentRequest,
    RelaySearchIndexDocumentResponse,
    RelaySearchReadIndexesItem,
    RelaySearchReadIndexesQuery,
    RelaySearchRemoveDocumentResponse,
    RelaySearchSearchQueryRequest,
    RelaySearchSearchQueryResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelaySearchesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_indexes(
        self,
        query: RelaySearchReadIndexesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelaySearchReadIndexesItem]:
        return self._client.request(
            'GET',
            'relay/search/indexes',
            query=query,
            cast_to=Page[RelaySearchReadIndexesItem],
            request_options=request_options,
        )

    def create_index(
        self,
        data: RelaySearchCreateIndexRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchCreateIndexResponse:
        return self._client.request(
            'POST',
            'relay/search/indexes',
            body=data,
            cast_to=RelaySearchCreateIndexResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def delete_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchDeleteIndexResponse:
        return self._client.request(
            'DELETE',
            f'relay/search/indexes/{encode_path_param(index_id)}',
            cast_to=RelaySearchDeleteIndexResponse,
            request_options=request_options,
        )

    def index_document(
        self,
        index_id: str,
        data: RelaySearchIndexDocumentRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchIndexDocumentResponse:
        return self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/documents',
            body=data,
            cast_to=RelaySearchIndexDocumentResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def index_document_batch(
        self,
        index_id: str,
        data: RelaySearchIndexDocumentBatchRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchIndexDocumentBatchResponse:
        return self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/documents/batch',
            body=data,
            cast_to=RelaySearchIndexDocumentBatchResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def remove_document(
        self,
        index_id: str,
        document_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchRemoveDocumentResponse:
        return self._client.request(
            'DELETE',
            (
                f'relay/search/indexes/{encode_path_param(index_id)}/documents'
                f'/{encode_path_param(document_id)}'
            ),
            cast_to=RelaySearchRemoveDocumentResponse,
            request_options=request_options,
        )

    def search_query(
        self,
        index_id: str,
        data: RelaySearchSearchQueryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchSearchQueryResponse:
        return self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/query',
            body=data,
            cast_to=RelaySearchSearchQueryResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def auto_suggest(
        self,
        index_id: str,
        data: RelaySearchAutoSuggestRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchAutoSuggestResponse:
        return self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/suggest',
            body=data,
            cast_to=RelaySearchAutoSuggestResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )


class AsyncRelaySearchesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_indexes(
        self,
        query: RelaySearchReadIndexesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelaySearchReadIndexesItem]:
        return await self._client.request(
            'GET',
            'relay/search/indexes',
            query=query,
            cast_to=AsyncPage[RelaySearchReadIndexesItem],
            request_options=request_options,
        )

    async def create_index(
        self,
        data: RelaySearchCreateIndexRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchCreateIndexResponse:
        return await self._client.request(
            'POST',
            'relay/search/indexes',
            body=data,
            cast_to=RelaySearchCreateIndexResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def delete_index(
        self,
        index_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchDeleteIndexResponse:
        return await self._client.request(
            'DELETE',
            f'relay/search/indexes/{encode_path_param(index_id)}',
            cast_to=RelaySearchDeleteIndexResponse,
            request_options=request_options,
        )

    async def index_document(
        self,
        index_id: str,
        data: RelaySearchIndexDocumentRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchIndexDocumentResponse:
        return await self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/documents',
            body=data,
            cast_to=RelaySearchIndexDocumentResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def index_document_batch(
        self,
        index_id: str,
        data: RelaySearchIndexDocumentBatchRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchIndexDocumentBatchResponse:
        return await self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/documents/batch',
            body=data,
            cast_to=RelaySearchIndexDocumentBatchResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def remove_document(
        self,
        index_id: str,
        document_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchRemoveDocumentResponse:
        return await self._client.request(
            'DELETE',
            (
                f'relay/search/indexes/{encode_path_param(index_id)}/documents'
                f'/{encode_path_param(document_id)}'
            ),
            cast_to=RelaySearchRemoveDocumentResponse,
            request_options=request_options,
        )

    async def search_query(
        self,
        index_id: str,
        data: RelaySearchSearchQueryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchSearchQueryResponse:
        return await self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/query',
            body=data,
            cast_to=RelaySearchSearchQueryResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def auto_suggest(
        self,
        index_id: str,
        data: RelaySearchAutoSuggestRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySearchAutoSuggestResponse:
        return await self._client.request(
            'POST',
            f'relay/search/indexes/{encode_path_param(index_id)}/suggest',
            body=data,
            cast_to=RelaySearchAutoSuggestResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )
