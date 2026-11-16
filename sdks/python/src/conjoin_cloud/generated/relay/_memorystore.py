from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    RelayMemorystoreCreateClusterRequest,
    RelayMemorystoreCreateClusterResponse,
    RelayMemorystoreDeleteClusterResponse,
    RelayMemorystoreExecuteCommandRequest,
    RelayMemorystoreExecuteCommandResponse,
    RelayMemorystoreReadClusterResponse,
    RelayMemorystoreReadClustersCountQuery,
    RelayMemorystoreReadClustersCountResponse,
    RelayMemorystoreReadClustersItem,
    RelayMemorystoreReadClustersQuery,
    RelayMemorystoreSuspendClusterResponse,
    RelayMemorystoreUpdateClusterRequest,
    RelayMemorystoreUpdateClusterResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelayMemorystoresResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_clusters(
        self,
        query: RelayMemorystoreReadClustersQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayMemorystoreReadClustersItem]:
        return self._client.request(
            'GET',
            'relay/memorystore-clusters/',
            query=query,
            cast_to=Page[RelayMemorystoreReadClustersItem],
            request_options=request_options,
        )

    def create_cluster(
        self,
        data: RelayMemorystoreCreateClusterRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreCreateClusterResponse:
        return self._client.request(
            'POST',
            'relay/memorystore-clusters/',
            body=data,
            cast_to=RelayMemorystoreCreateClusterResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_clusters_count(
        self,
        query: RelayMemorystoreReadClustersCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreReadClustersCountResponse:
        return self._client.request(
            'GET',
            'relay/memorystore-clusters/count',
            query=query,
            cast_to=RelayMemorystoreReadClustersCountResponse,
            request_options=request_options,
        )

    def read_cluster(
        self,
        memorystore_cluster_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreReadClusterResponse:
        return self._client.request(
            'GET',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}',
            cast_to=RelayMemorystoreReadClusterResponse,
            request_options=request_options,
        )

    def update_cluster(
        self,
        memorystore_cluster_id: str,
        data: RelayMemorystoreUpdateClusterRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreUpdateClusterResponse:
        return self._client.request(
            'PATCH',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}',
            body=data,
            cast_to=RelayMemorystoreUpdateClusterResponse,
            request_options=request_options,
        )

    def delete_cluster(
        self,
        memorystore_cluster_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreDeleteClusterResponse:
        return self._client.request(
            'DELETE',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}',
            cast_to=RelayMemorystoreDeleteClusterResponse,
            request_options=request_options,
        )

    def suspend_cluster(
        self,
        memorystore_cluster_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreSuspendClusterResponse:
        return self._client.request(
            'POST',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}/suspend',
            cast_to=RelayMemorystoreSuspendClusterResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def execute_command(
        self,
        memorystore_cluster_id: str,
        data: RelayMemorystoreExecuteCommandRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreExecuteCommandResponse:
        return self._client.request(
            'POST',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}/execute',
            body=data,
            cast_to=RelayMemorystoreExecuteCommandResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )


class AsyncRelayMemorystoresResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_clusters(
        self,
        query: RelayMemorystoreReadClustersQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayMemorystoreReadClustersItem]:
        return await self._client.request(
            'GET',
            'relay/memorystore-clusters/',
            query=query,
            cast_to=AsyncPage[RelayMemorystoreReadClustersItem],
            request_options=request_options,
        )

    async def create_cluster(
        self,
        data: RelayMemorystoreCreateClusterRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreCreateClusterResponse:
        return await self._client.request(
            'POST',
            'relay/memorystore-clusters/',
            body=data,
            cast_to=RelayMemorystoreCreateClusterResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_clusters_count(
        self,
        query: RelayMemorystoreReadClustersCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreReadClustersCountResponse:
        return await self._client.request(
            'GET',
            'relay/memorystore-clusters/count',
            query=query,
            cast_to=RelayMemorystoreReadClustersCountResponse,
            request_options=request_options,
        )

    async def read_cluster(
        self,
        memorystore_cluster_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreReadClusterResponse:
        return await self._client.request(
            'GET',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}',
            cast_to=RelayMemorystoreReadClusterResponse,
            request_options=request_options,
        )

    async def update_cluster(
        self,
        memorystore_cluster_id: str,
        data: RelayMemorystoreUpdateClusterRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreUpdateClusterResponse:
        return await self._client.request(
            'PATCH',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}',
            body=data,
            cast_to=RelayMemorystoreUpdateClusterResponse,
            request_options=request_options,
        )

    async def delete_cluster(
        self,
        memorystore_cluster_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreDeleteClusterResponse:
        return await self._client.request(
            'DELETE',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}',
            cast_to=RelayMemorystoreDeleteClusterResponse,
            request_options=request_options,
        )

    async def suspend_cluster(
        self,
        memorystore_cluster_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreSuspendClusterResponse:
        return await self._client.request(
            'POST',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}/suspend',
            cast_to=RelayMemorystoreSuspendClusterResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def execute_command(
        self,
        memorystore_cluster_id: str,
        data: RelayMemorystoreExecuteCommandRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayMemorystoreExecuteCommandResponse:
        return await self._client.request(
            'POST',
            f'relay/memorystore-clusters/{encode_path_param(memorystore_cluster_id)}/execute',
            body=data,
            cast_to=RelayMemorystoreExecuteCommandResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )
