from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudOrganizationCreateRequest,
    CloudOrganizationCreateResponse,
    CloudOrganizationListItem,
    CloudOrganizationListQuery,
    CloudOrganizationReadCountQuery,
    CloudOrganizationReadCountResponse,
    CloudOrganizationReadResponse,
    CloudOrganizationUpdateRequest,
    CloudOrganizationUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudOrganizationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: CloudOrganizationListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudOrganizationListItem]:
        return self._client.request(
            'GET',
            'cloud/organizations/',
            query=query,
            cast_to=Page[CloudOrganizationListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: CloudOrganizationCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationCreateResponse:
        return self._client.request(
            'POST',
            'cloud/organizations/',
            body=data,
            cast_to=CloudOrganizationCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_count(
        self,
        query: CloudOrganizationReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationReadCountResponse:
        return self._client.request(
            'GET',
            'cloud/organizations/count',
            query=query,
            cast_to=CloudOrganizationReadCountResponse,
            request_options=request_options,
        )

    def read(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationReadResponse:
        return self._client.request(
            'GET',
            f'cloud/organizations/{encode_path_param(organization_id)}',
            cast_to=CloudOrganizationReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        organization_id: str,
        data: CloudOrganizationUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationUpdateResponse:
        return self._client.request(
            'PATCH',
            f'cloud/organizations/{encode_path_param(organization_id)}',
            body=data,
            cast_to=CloudOrganizationUpdateResponse,
            request_options=request_options,
        )


class AsyncCloudOrganizationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: CloudOrganizationListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudOrganizationListItem]:
        return await self._client.request(
            'GET',
            'cloud/organizations/',
            query=query,
            cast_to=AsyncPage[CloudOrganizationListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: CloudOrganizationCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationCreateResponse:
        return await self._client.request(
            'POST',
            'cloud/organizations/',
            body=data,
            cast_to=CloudOrganizationCreateResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_count(
        self,
        query: CloudOrganizationReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationReadCountResponse:
        return await self._client.request(
            'GET',
            'cloud/organizations/count',
            query=query,
            cast_to=CloudOrganizationReadCountResponse,
            request_options=request_options,
        )

    async def read(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationReadResponse:
        return await self._client.request(
            'GET',
            f'cloud/organizations/{encode_path_param(organization_id)}',
            cast_to=CloudOrganizationReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        organization_id: str,
        data: CloudOrganizationUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudOrganizationUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'cloud/organizations/{encode_path_param(organization_id)}',
            body=data,
            cast_to=CloudOrganizationUpdateResponse,
            request_options=request_options,
        )
