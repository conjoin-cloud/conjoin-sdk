from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    StorageObjectArchiveResponse,
    StorageObjectCheckDuplicateQuery,
    StorageObjectCheckDuplicateResponse,
    StorageObjectCreateDownloadSignedUrlRequest,
    StorageObjectCreateDownloadSignedUrlResponse,
    StorageObjectCreateUploadSignedUrlRequest,
    StorageObjectCreateUploadSignedUrlResponse,
    StorageObjectDeleteResponse,
    StorageObjectListItem,
    StorageObjectListQuery,
    StorageObjectListVersionsItem,
    StorageObjectListVersionsQuery,
    StorageObjectReadResponse,
    StorageObjectRenameResponse,
    StorageObjectRestoreResponse,
    StorageObjectRestoreVersionRequest,
    StorageObjectRestoreVersionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class StorageObjectsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_upload_signed_url(
        self,
        container_name_or_id: str,
        data: StorageObjectCreateUploadSignedUrlRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectCreateUploadSignedUrlResponse:
        return self._client.request(
            'POST',
            f'storage/storage-object/{encode_path_param(container_name_or_id)}/signed-url/upload',
            body=data,
            cast_to=StorageObjectCreateUploadSignedUrlResponse,
            request_options=request_options,
        )

    def create_download_signed_url(
        self,
        container_name_or_id: str,
        data: StorageObjectCreateDownloadSignedUrlRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectCreateDownloadSignedUrlResponse:
        return self._client.request(
            'POST',
            f'storage/storage-object/{encode_path_param(container_name_or_id)}/signed-url/download',
            body=data,
            cast_to=StorageObjectCreateDownloadSignedUrlResponse,
            request_options=request_options,
        )

    def rename(
        self,
        container_name_or_id: str,
        old_name: str,
        new_name: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectRenameResponse:
        return self._client.request(
            'PATCH',
            (
                f'storage/storage-object/rename/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(old_name)}/{encode_path_param(new_name)}'
            ),
            cast_to=StorageObjectRenameResponse,
            request_options=request_options,
        )

    def archive(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectArchiveResponse:
        return self._client.request(
            'PATCH',
            (
                f'storage/storage-object/archive/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            cast_to=StorageObjectArchiveResponse,
            request_options=request_options,
        )

    def restore(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectRestoreResponse:
        return self._client.request(
            'PATCH',
            (
                f'storage/storage-object/restore/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            cast_to=StorageObjectRestoreResponse,
            request_options=request_options,
        )

    def delete(
        self,
        container_name_or_id: str,
        prefix: str,
        name: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectDeleteResponse:
        return self._client.request(
            'DELETE',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(prefix)}/{encode_path_param(name)}'
            ),
            cast_to=StorageObjectDeleteResponse,
            request_options=request_options,
        )

    def list_versions(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        query: StorageObjectListVersionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[StorageObjectListVersionsItem]:
        return self._client.request(
            'GET',
            (
                f'storage/storage-object/versions/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            query=query,
            cast_to=Page[StorageObjectListVersionsItem],
            request_options=request_options,
        )

    def restore_version(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectRestoreVersionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectRestoreVersionResponse:
        return self._client.request(
            'POST',
            (
                f'storage/storage-object/versions/restore/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            body=data,
            cast_to=StorageObjectRestoreVersionResponse,
            request_options=request_options,
        )

    def check_duplicate(
        self,
        container_name_or_id: str,
        query: StorageObjectCheckDuplicateQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectCheckDuplicateResponse:
        return self._client.request(
            'GET',
            f'storage/storage-object/check-duplicate/{encode_path_param(container_name_or_id)}',
            query=query,
            cast_to=StorageObjectCheckDuplicateResponse,
            request_options=request_options,
        )

    def read(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectReadResponse:
        return self._client.request(
            'GET',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            cast_to=StorageObjectReadResponse,
            request_options=request_options,
        )

    def list(
        self,
        container_name_or_id: str,
        query: StorageObjectListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[StorageObjectListItem]:
        return self._client.request(
            'GET',
            f'storage/storage-object/{encode_path_param(container_name_or_id)}',
            query=query,
            cast_to=Page[StorageObjectListItem],
            request_options=request_options,
        )


class AsyncStorageObjectsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_upload_signed_url(
        self,
        container_name_or_id: str,
        data: StorageObjectCreateUploadSignedUrlRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectCreateUploadSignedUrlResponse:
        return await self._client.request(
            'POST',
            f'storage/storage-object/{encode_path_param(container_name_or_id)}/signed-url/upload',
            body=data,
            cast_to=StorageObjectCreateUploadSignedUrlResponse,
            request_options=request_options,
        )

    async def create_download_signed_url(
        self,
        container_name_or_id: str,
        data: StorageObjectCreateDownloadSignedUrlRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectCreateDownloadSignedUrlResponse:
        return await self._client.request(
            'POST',
            f'storage/storage-object/{encode_path_param(container_name_or_id)}/signed-url/download',
            body=data,
            cast_to=StorageObjectCreateDownloadSignedUrlResponse,
            request_options=request_options,
        )

    async def rename(
        self,
        container_name_or_id: str,
        old_name: str,
        new_name: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectRenameResponse:
        return await self._client.request(
            'PATCH',
            (
                f'storage/storage-object/rename/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(old_name)}/{encode_path_param(new_name)}'
            ),
            cast_to=StorageObjectRenameResponse,
            request_options=request_options,
        )

    async def archive(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectArchiveResponse:
        return await self._client.request(
            'PATCH',
            (
                f'storage/storage-object/archive/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            cast_to=StorageObjectArchiveResponse,
            request_options=request_options,
        )

    async def restore(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectRestoreResponse:
        return await self._client.request(
            'PATCH',
            (
                f'storage/storage-object/restore/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            cast_to=StorageObjectRestoreResponse,
            request_options=request_options,
        )

    async def delete(
        self,
        container_name_or_id: str,
        prefix: str,
        name: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectDeleteResponse:
        return await self._client.request(
            'DELETE',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(prefix)}/{encode_path_param(name)}'
            ),
            cast_to=StorageObjectDeleteResponse,
            request_options=request_options,
        )

    async def list_versions(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        query: StorageObjectListVersionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[StorageObjectListVersionsItem]:
        return await self._client.request(
            'GET',
            (
                f'storage/storage-object/versions/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            query=query,
            cast_to=AsyncPage[StorageObjectListVersionsItem],
            request_options=request_options,
        )

    async def restore_version(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectRestoreVersionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectRestoreVersionResponse:
        return await self._client.request(
            'POST',
            (
                f'storage/storage-object/versions/restore/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            body=data,
            cast_to=StorageObjectRestoreVersionResponse,
            request_options=request_options,
        )

    async def check_duplicate(
        self,
        container_name_or_id: str,
        query: StorageObjectCheckDuplicateQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectCheckDuplicateResponse:
        return await self._client.request(
            'GET',
            f'storage/storage-object/check-duplicate/{encode_path_param(container_name_or_id)}',
            query=query,
            cast_to=StorageObjectCheckDuplicateResponse,
            request_options=request_options,
        )

    async def read(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectReadResponse:
        return await self._client.request(
            'GET',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}'
            ),
            cast_to=StorageObjectReadResponse,
            request_options=request_options,
        )

    async def list(
        self,
        container_name_or_id: str,
        query: StorageObjectListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[StorageObjectListItem]:
        return await self._client.request(
            'GET',
            f'storage/storage-object/{encode_path_param(container_name_or_id)}',
            query=query,
            cast_to=AsyncPage[StorageObjectListItem],
            request_options=request_options,
        )
