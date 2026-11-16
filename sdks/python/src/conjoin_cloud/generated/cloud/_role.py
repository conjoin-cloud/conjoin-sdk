from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudRoleCreateRequest,
    CloudRoleCreateResponse,
    CloudRoleReadCountQuery,
    CloudRoleReadCountResponse,
    CloudRoleReadItem,
    CloudRoleReadQuery,
    CloudRoleUpdateRequest,
    CloudRoleUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudRolesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read(
        self,
        query: CloudRoleReadQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudRoleReadItem]:
        return self._client.request(
            'GET',
            'cloud/roles/',
            query=query,
            cast_to=Page[CloudRoleReadItem],
            request_options=request_options,
        )

    def create(
        self,
        data: CloudRoleCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudRoleCreateResponse:
        return self._client.request(
            'POST',
            'cloud/roles/',
            body=data,
            cast_to=CloudRoleCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_count(
        self,
        query: CloudRoleReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudRoleReadCountResponse:
        return self._client.request(
            'GET',
            'cloud/roles/count',
            query=query,
            cast_to=CloudRoleReadCountResponse,
            request_options=request_options,
        )

    def update(
        self,
        role_id: str,
        data: CloudRoleUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudRoleUpdateResponse:
        return self._client.request(
            'PATCH',
            f'cloud/roles/{encode_path_param(role_id)}',
            body=data,
            cast_to=CloudRoleUpdateResponse,
            request_options=request_options,
        )


class AsyncCloudRolesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read(
        self,
        query: CloudRoleReadQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudRoleReadItem]:
        return await self._client.request(
            'GET',
            'cloud/roles/',
            query=query,
            cast_to=AsyncPage[CloudRoleReadItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: CloudRoleCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudRoleCreateResponse:
        return await self._client.request(
            'POST',
            'cloud/roles/',
            body=data,
            cast_to=CloudRoleCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_count(
        self,
        query: CloudRoleReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudRoleReadCountResponse:
        return await self._client.request(
            'GET',
            'cloud/roles/count',
            query=query,
            cast_to=CloudRoleReadCountResponse,
            request_options=request_options,
        )

    async def update(
        self,
        role_id: str,
        data: CloudRoleUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudRoleUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'cloud/roles/{encode_path_param(role_id)}',
            body=data,
            cast_to=CloudRoleUpdateResponse,
            request_options=request_options,
        )
