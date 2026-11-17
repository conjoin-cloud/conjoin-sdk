from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationPermissionArchiveOrgPermissionResponse,
    AuthOrganizationPermissionCreateOrgPermissionRequest,
    AuthOrganizationPermissionCreateOrgPermissionResponse,
    AuthOrganizationPermissionDeleteOrgPermissionResponse,
    AuthOrganizationPermissionListOrgPermissionsCountQuery,
    AuthOrganizationPermissionListOrgPermissionsCountResponse,
    AuthOrganizationPermissionListOrgPermissionsItem,
    AuthOrganizationPermissionListOrgPermissionsQuery,
    AuthOrganizationPermissionReadOrgPermissionResponse,
    AuthOrganizationPermissionRestoreOrgPermissionResponse,
    AuthOrganizationPermissionUpdateOrgPermissionRequest,
    AuthOrganizationPermissionUpdateOrgPermissionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationPermissionsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_org_permissions(
        self,
        organization_id: str,
        query: AuthOrganizationPermissionListOrgPermissionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationPermissionListOrgPermissionsItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/permissions/',
            query=query,
            cast_to=Page[AuthOrganizationPermissionListOrgPermissionsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_org_permission(
        self,
        organization_id: str,
        data: AuthOrganizationPermissionCreateOrgPermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionCreateOrgPermissionResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/permissions/',
            body=data,
            cast_to=AuthOrganizationPermissionCreateOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def list_org_permissions_count(
        self,
        organization_id: str,
        query: AuthOrganizationPermissionListOrgPermissionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionListOrgPermissionsCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/permissions/count',
            query=query,
            cast_to=AuthOrganizationPermissionListOrgPermissionsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionReadOrgPermissionResponse:
        return self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}'
            ),
            cast_to=AuthOrganizationPermissionReadOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        data: AuthOrganizationPermissionUpdateOrgPermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionUpdateOrgPermissionResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationPermissionUpdateOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionDeleteOrgPermissionResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}'
            ),
            cast_to=AuthOrganizationPermissionDeleteOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def archive_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionArchiveOrgPermissionResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}/archive'
            ),
            cast_to=AuthOrganizationPermissionArchiveOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def restore_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionRestoreOrgPermissionResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}/restore'
            ),
            cast_to=AuthOrganizationPermissionRestoreOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthOrganizationPermissionsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_org_permissions(
        self,
        organization_id: str,
        query: AuthOrganizationPermissionListOrgPermissionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationPermissionListOrgPermissionsItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/permissions/',
            query=query,
            cast_to=AsyncPage[AuthOrganizationPermissionListOrgPermissionsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_org_permission(
        self,
        organization_id: str,
        data: AuthOrganizationPermissionCreateOrgPermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionCreateOrgPermissionResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/permissions/',
            body=data,
            cast_to=AuthOrganizationPermissionCreateOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def list_org_permissions_count(
        self,
        organization_id: str,
        query: AuthOrganizationPermissionListOrgPermissionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionListOrgPermissionsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/permissions/count',
            query=query,
            cast_to=AuthOrganizationPermissionListOrgPermissionsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionReadOrgPermissionResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}'
            ),
            cast_to=AuthOrganizationPermissionReadOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        data: AuthOrganizationPermissionUpdateOrgPermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionUpdateOrgPermissionResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationPermissionUpdateOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionDeleteOrgPermissionResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}'
            ),
            cast_to=AuthOrganizationPermissionDeleteOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def archive_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionArchiveOrgPermissionResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}/archive'
            ),
            cast_to=AuthOrganizationPermissionArchiveOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def restore_org_permission(
        self,
        organization_id: str,
        permission_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationPermissionRestoreOrgPermissionResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/permissions'
                f'/{encode_path_param(permission_id)}/restore'
            ),
            cast_to=AuthOrganizationPermissionRestoreOrgPermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
