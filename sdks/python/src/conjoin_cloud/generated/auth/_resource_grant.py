from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthResourceGrantCheckResourcePermissionRequest,
    AuthResourceGrantCheckResourcePermissionResponse,
    AuthResourceGrantGrantResourcePermissionRequest,
    AuthResourceGrantGrantResourcePermissionResponse,
    AuthResourceGrantListCountQuery,
    AuthResourceGrantListCountResponse,
    AuthResourceGrantListItem,
    AuthResourceGrantListQuery,
    AuthResourceGrantRevokeResourcePermissionRequest,
    AuthResourceGrantRevokeResourcePermissionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthResourceGrantsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        organization_id: str,
        query: AuthResourceGrantListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthResourceGrantListItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/resource-grants/',
            query=query,
            cast_to=Page[AuthResourceGrantListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def grant_resource_permission(
        self,
        organization_id: str,
        data: AuthResourceGrantGrantResourcePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantGrantResourcePermissionResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/resource-grants/',
            body=data,
            cast_to=AuthResourceGrantGrantResourcePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def check_resource_permission(
        self,
        organization_id: str,
        data: AuthResourceGrantCheckResourcePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantCheckResourcePermissionResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/check-resource-permission',
            body=data,
            cast_to=AuthResourceGrantCheckResourcePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        organization_id: str,
        query: AuthResourceGrantListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantListCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/resource-grants/count',
            query=query,
            cast_to=AuthResourceGrantListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def revoke_resource_permission(
        self,
        organization_id: str,
        resource_grant_id: str,
        data: AuthResourceGrantRevokeResourcePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantRevokeResourcePermissionResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/resource-grants'
                f'/{encode_path_param(resource_grant_id)}/revoke'
            ),
            body=data,
            cast_to=AuthResourceGrantRevokeResourcePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthResourceGrantsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        organization_id: str,
        query: AuthResourceGrantListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthResourceGrantListItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/resource-grants/',
            query=query,
            cast_to=AsyncPage[AuthResourceGrantListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def grant_resource_permission(
        self,
        organization_id: str,
        data: AuthResourceGrantGrantResourcePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantGrantResourcePermissionResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/resource-grants/',
            body=data,
            cast_to=AuthResourceGrantGrantResourcePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def check_resource_permission(
        self,
        organization_id: str,
        data: AuthResourceGrantCheckResourcePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantCheckResourcePermissionResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/check-resource-permission',
            body=data,
            cast_to=AuthResourceGrantCheckResourcePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        organization_id: str,
        query: AuthResourceGrantListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantListCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/resource-grants/count',
            query=query,
            cast_to=AuthResourceGrantListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def revoke_resource_permission(
        self,
        organization_id: str,
        resource_grant_id: str,
        data: AuthResourceGrantRevokeResourcePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthResourceGrantRevokeResourcePermissionResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/resource-grants'
                f'/{encode_path_param(resource_grant_id)}/revoke'
            ),
            body=data,
            cast_to=AuthResourceGrantRevokeResourcePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
