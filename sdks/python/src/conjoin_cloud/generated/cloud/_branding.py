from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudBrandingGetOrgOverrideResponse,
    CloudBrandingGetProjectResponse,
    CloudBrandingPatchOrgOverrideRequest,
    CloudBrandingPatchOrgOverrideResponse,
    CloudBrandingPatchProjectRequest,
    CloudBrandingPatchProjectResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudBrandingsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def get_project(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingGetProjectResponse:
        return self._client.request(
            'GET',
            'cloud/branding/',
            cast_to=CloudBrandingGetProjectResponse,
            request_options=request_options,
        )

    def patch_project(
        self,
        data: CloudBrandingPatchProjectRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingPatchProjectResponse:
        return self._client.request(
            'PATCH',
            'cloud/branding/',
            body=data,
            cast_to=CloudBrandingPatchProjectResponse,
            request_options=request_options,
        )

    def get_org_override(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingGetOrgOverrideResponse:
        return self._client.request(
            'GET',
            f'cloud/branding/organizations/{encode_path_param(organization_id)}',
            cast_to=CloudBrandingGetOrgOverrideResponse,
            request_options=request_options,
        )

    def patch_org_override(
        self,
        organization_id: str,
        data: CloudBrandingPatchOrgOverrideRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingPatchOrgOverrideResponse:
        return self._client.request(
            'PATCH',
            f'cloud/branding/organizations/{encode_path_param(organization_id)}',
            body=data,
            cast_to=CloudBrandingPatchOrgOverrideResponse,
            request_options=request_options,
        )


class AsyncCloudBrandingsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def get_project(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingGetProjectResponse:
        return await self._client.request(
            'GET',
            'cloud/branding/',
            cast_to=CloudBrandingGetProjectResponse,
            request_options=request_options,
        )

    async def patch_project(
        self,
        data: CloudBrandingPatchProjectRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingPatchProjectResponse:
        return await self._client.request(
            'PATCH',
            'cloud/branding/',
            body=data,
            cast_to=CloudBrandingPatchProjectResponse,
            request_options=request_options,
        )

    async def get_org_override(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingGetOrgOverrideResponse:
        return await self._client.request(
            'GET',
            f'cloud/branding/organizations/{encode_path_param(organization_id)}',
            cast_to=CloudBrandingGetOrgOverrideResponse,
            request_options=request_options,
        )

    async def patch_org_override(
        self,
        organization_id: str,
        data: CloudBrandingPatchOrgOverrideRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingPatchOrgOverrideResponse:
        return await self._client.request(
            'PATCH',
            f'cloud/branding/organizations/{encode_path_param(organization_id)}',
            body=data,
            cast_to=CloudBrandingPatchOrgOverrideResponse,
            request_options=request_options,
        )
