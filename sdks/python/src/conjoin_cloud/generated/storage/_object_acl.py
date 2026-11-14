from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    StorageObjectACLGrantObjectAclRequest,
    StorageObjectACLGrantObjectAclResponse,
    StorageObjectACLRevokeObjectAclRequest,
    StorageObjectACLRevokeObjectAclResponse,
    StorageObjectACLSetObjectPublicRequest,
    StorageObjectACLSetObjectPublicResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class StorageObjectACLsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def grant_object_acl(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectACLGrantObjectAclRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectACLGrantObjectAclResponse:
        return self._client.request(
            'POST',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}/acl/grant'
            ),
            body=data,
            cast_to=StorageObjectACLGrantObjectAclResponse,
            request_options=request_options,
        )

    def revoke_object_acl(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectACLRevokeObjectAclRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectACLRevokeObjectAclResponse:
        return self._client.request(
            'POST',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}/acl/revoke'
            ),
            body=data,
            cast_to=StorageObjectACLRevokeObjectAclResponse,
            request_options=request_options,
        )

    def set_object_public(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectACLSetObjectPublicRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectACLSetObjectPublicResponse:
        return self._client.request(
            'PATCH',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}/acl/public'
            ),
            body=data,
            cast_to=StorageObjectACLSetObjectPublicResponse,
            request_options=request_options,
        )


class AsyncStorageObjectACLsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def grant_object_acl(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectACLGrantObjectAclRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectACLGrantObjectAclResponse:
        return await self._client.request(
            'POST',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}/acl/grant'
            ),
            body=data,
            cast_to=StorageObjectACLGrantObjectAclResponse,
            request_options=request_options,
        )

    async def revoke_object_acl(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectACLRevokeObjectAclRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectACLRevokeObjectAclResponse:
        return await self._client.request(
            'POST',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}/acl/revoke'
            ),
            body=data,
            cast_to=StorageObjectACLRevokeObjectAclResponse,
            request_options=request_options,
        )

    async def set_object_public(
        self,
        container_name_or_id: str,
        object_name_or_id: str,
        data: StorageObjectACLSetObjectPublicRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageObjectACLSetObjectPublicResponse:
        return await self._client.request(
            'PATCH',
            (
                f'storage/storage-object/{encode_path_param(container_name_or_id)}'
                f'/{encode_path_param(object_name_or_id)}/acl/public'
            ),
            body=data,
            cast_to=StorageObjectACLSetObjectPublicResponse,
            request_options=request_options,
        )
