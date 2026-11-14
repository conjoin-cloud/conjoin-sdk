from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudProjectCreateRequest,
    CloudProjectCreateResponse,
    CloudProjectListItem,
    CloudProjectListQuery,
    CloudProjectReadCountQuery,
    CloudProjectReadCountResponse,
    CloudProjectReadResponse,
    CloudProjectUpdateRequest,
    CloudProjectUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudProjectsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        organization_id: str,
        query: CloudProjectListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudProjectListItem]:
        return self._client.request(
            'GET',
            f'cloud/organizations/{encode_path_param(organization_id)}/projects/',
            query=query,
            cast_to=Page[CloudProjectListItem],
            request_options=request_options,
        )

    def create(
        self,
        organization_id: str,
        data: CloudProjectCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectCreateResponse:
        return self._client.request(
            'POST',
            f'cloud/organizations/{encode_path_param(organization_id)}/projects/',
            body=data,
            cast_to=CloudProjectCreateResponse,
            request_options=request_options,
        )

    def read_count(
        self,
        organization_id: str,
        query: CloudProjectReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectReadCountResponse:
        return self._client.request(
            'GET',
            f'cloud/organizations/{encode_path_param(organization_id)}/projects/count',
            query=query,
            cast_to=CloudProjectReadCountResponse,
            request_options=request_options,
        )

    def read(
        self,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectReadResponse:
        return self._client.request(
            'GET',
            f'cloud/projects/{encode_path_param(project_id)}',
            cast_to=CloudProjectReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        project_id: str,
        data: CloudProjectUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectUpdateResponse:
        return self._client.request(
            'PATCH',
            f'cloud/projects/{encode_path_param(project_id)}',
            body=data,
            cast_to=CloudProjectUpdateResponse,
            request_options=request_options,
        )


class AsyncCloudProjectsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        organization_id: str,
        query: CloudProjectListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudProjectListItem]:
        return await self._client.request(
            'GET',
            f'cloud/organizations/{encode_path_param(organization_id)}/projects/',
            query=query,
            cast_to=AsyncPage[CloudProjectListItem],
            request_options=request_options,
        )

    async def create(
        self,
        organization_id: str,
        data: CloudProjectCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectCreateResponse:
        return await self._client.request(
            'POST',
            f'cloud/organizations/{encode_path_param(organization_id)}/projects/',
            body=data,
            cast_to=CloudProjectCreateResponse,
            request_options=request_options,
        )

    async def read_count(
        self,
        organization_id: str,
        query: CloudProjectReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectReadCountResponse:
        return await self._client.request(
            'GET',
            f'cloud/organizations/{encode_path_param(organization_id)}/projects/count',
            query=query,
            cast_to=CloudProjectReadCountResponse,
            request_options=request_options,
        )

    async def read(
        self,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectReadResponse:
        return await self._client.request(
            'GET',
            f'cloud/projects/{encode_path_param(project_id)}',
            cast_to=CloudProjectReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        project_id: str,
        data: CloudProjectUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudProjectUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'cloud/projects/{encode_path_param(project_id)}',
            body=data,
            cast_to=CloudProjectUpdateResponse,
            request_options=request_options,
        )
