from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    StorageContainerArchiveResponse,
    StorageContainerCancelDeletionResponse,
    StorageContainerChangeClassRequest,
    StorageContainerChangeClassResponse,
    StorageContainerCreateRequest,
    StorageContainerCreateResponse,
    StorageContainerListItem,
    StorageContainerListQuery,
    StorageContainerReadResponse,
    StorageContainerRequestDeletionQuery,
    StorageContainerRequestDeletionResponse,
    StorageContainerRestoreResponse,
    StorageContainerUpdateLifecyclePolicyRequest,
    StorageContainerUpdateLifecyclePolicyResponse,
    StorageContainerUpdateSettingsRequest,
    StorageContainerUpdateSettingsResponse,
    StorageContainerUpdateTransitionPolicyRequest,
    StorageContainerUpdateTransitionPolicyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class StorageContainersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: StorageContainerListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[StorageContainerListItem]:
        return self._client.request(
            'GET',
            'storage/storage-container/',
            query=query,
            cast_to=Page[StorageContainerListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: StorageContainerCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerCreateResponse:
        return self._client.request(
            'POST',
            'storage/storage-container/',
            body=data,
            cast_to=StorageContainerCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerReadResponse:
        return self._client.request(
            'GET',
            f'storage/storage-container/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerReadResponse,
            request_options=request_options,
        )

    def request_deletion(
        self,
        container_name_or_id: str,
        query: StorageContainerRequestDeletionQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerRequestDeletionResponse:
        return self._client.request(
            'DELETE',
            f'storage/storage-container/{encode_path_param(container_name_or_id)}',
            query=query,
            cast_to=StorageContainerRequestDeletionResponse,
            request_options=request_options,
        )

    def archive(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerArchiveResponse:
        return self._client.request(
            'PATCH',
            f'storage/storage-container/archive/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerArchiveResponse,
            request_options=request_options,
        )

    def restore(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerRestoreResponse:
        return self._client.request(
            'PATCH',
            f'storage/storage-container/restore/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerRestoreResponse,
            request_options=request_options,
        )

    def update_lifecycle_policy(
        self,
        container_name_or_id: str,
        data: StorageContainerUpdateLifecyclePolicyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerUpdateLifecyclePolicyResponse:
        return self._client.request(
            'PATCH',
            f'storage/storage-container/lifecycle-policy/{encode_path_param(container_name_or_id)}',
            body=data,
            cast_to=StorageContainerUpdateLifecyclePolicyResponse,
            request_options=request_options,
        )

    def update_settings(
        self,
        container_name_or_id: str,
        data: StorageContainerUpdateSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerUpdateSettingsResponse:
        return self._client.request(
            'PATCH',
            f'storage/storage-container/settings/{encode_path_param(container_name_or_id)}',
            body=data,
            cast_to=StorageContainerUpdateSettingsResponse,
            request_options=request_options,
        )

    def cancel_deletion(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerCancelDeletionResponse:
        return self._client.request(
            'PATCH',
            f'storage/storage-container/cancel-deletion/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerCancelDeletionResponse,
            request_options=request_options,
        )

    def change_class(
        self,
        container_name_or_id: str,
        data: StorageContainerChangeClassRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerChangeClassResponse:
        return self._client.request(
            'PATCH',
            f'storage/storage-container/storage-class/{encode_path_param(container_name_or_id)}',
            body=data,
            cast_to=StorageContainerChangeClassResponse,
            request_options=request_options,
        )

    def update_transition_policy(
        self,
        container_name_or_id: str,
        data: StorageContainerUpdateTransitionPolicyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerUpdateTransitionPolicyResponse:
        return self._client.request(
            'PATCH',
            (
                'storage/storage-container/transition-policy'
                f'/{encode_path_param(container_name_or_id)}'
            ),
            body=data,
            cast_to=StorageContainerUpdateTransitionPolicyResponse,
            request_options=request_options,
        )


class AsyncStorageContainersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: StorageContainerListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[StorageContainerListItem]:
        return await self._client.request(
            'GET',
            'storage/storage-container/',
            query=query,
            cast_to=AsyncPage[StorageContainerListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: StorageContainerCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerCreateResponse:
        return await self._client.request(
            'POST',
            'storage/storage-container/',
            body=data,
            cast_to=StorageContainerCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerReadResponse:
        return await self._client.request(
            'GET',
            f'storage/storage-container/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerReadResponse,
            request_options=request_options,
        )

    async def request_deletion(
        self,
        container_name_or_id: str,
        query: StorageContainerRequestDeletionQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerRequestDeletionResponse:
        return await self._client.request(
            'DELETE',
            f'storage/storage-container/{encode_path_param(container_name_or_id)}',
            query=query,
            cast_to=StorageContainerRequestDeletionResponse,
            request_options=request_options,
        )

    async def archive(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerArchiveResponse:
        return await self._client.request(
            'PATCH',
            f'storage/storage-container/archive/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerArchiveResponse,
            request_options=request_options,
        )

    async def restore(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerRestoreResponse:
        return await self._client.request(
            'PATCH',
            f'storage/storage-container/restore/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerRestoreResponse,
            request_options=request_options,
        )

    async def update_lifecycle_policy(
        self,
        container_name_or_id: str,
        data: StorageContainerUpdateLifecyclePolicyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerUpdateLifecyclePolicyResponse:
        return await self._client.request(
            'PATCH',
            f'storage/storage-container/lifecycle-policy/{encode_path_param(container_name_or_id)}',
            body=data,
            cast_to=StorageContainerUpdateLifecyclePolicyResponse,
            request_options=request_options,
        )

    async def update_settings(
        self,
        container_name_or_id: str,
        data: StorageContainerUpdateSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerUpdateSettingsResponse:
        return await self._client.request(
            'PATCH',
            f'storage/storage-container/settings/{encode_path_param(container_name_or_id)}',
            body=data,
            cast_to=StorageContainerUpdateSettingsResponse,
            request_options=request_options,
        )

    async def cancel_deletion(
        self,
        container_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerCancelDeletionResponse:
        return await self._client.request(
            'PATCH',
            f'storage/storage-container/cancel-deletion/{encode_path_param(container_name_or_id)}',
            cast_to=StorageContainerCancelDeletionResponse,
            request_options=request_options,
        )

    async def change_class(
        self,
        container_name_or_id: str,
        data: StorageContainerChangeClassRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerChangeClassResponse:
        return await self._client.request(
            'PATCH',
            f'storage/storage-container/storage-class/{encode_path_param(container_name_or_id)}',
            body=data,
            cast_to=StorageContainerChangeClassResponse,
            request_options=request_options,
        )

    async def update_transition_policy(
        self,
        container_name_or_id: str,
        data: StorageContainerUpdateTransitionPolicyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageContainerUpdateTransitionPolicyResponse:
        return await self._client.request(
            'PATCH',
            (
                'storage/storage-container/transition-policy'
                f'/{encode_path_param(container_name_or_id)}'
            ),
            body=data,
            cast_to=StorageContainerUpdateTransitionPolicyResponse,
            request_options=request_options,
        )
