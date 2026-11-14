from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationRolePermissionAssignOrgRolePermissionItem,
    AuthOrganizationRolePermissionAssignOrgRolePermissionRequest,
    AuthOrganizationRolePermissionListOrgRolePermissionsCountQuery,
    AuthOrganizationRolePermissionListOrgRolePermissionsCountResponse,
    AuthOrganizationRolePermissionListOrgRolePermissionsItem,
    AuthOrganizationRolePermissionListOrgRolePermissionsQuery,
    AuthOrganizationRolePermissionRemoveRolePermissionRequest,
    AuthOrganizationRolePermissionRemoveRolePermissionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationRolePermissionsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_org_role_permissions(
        self,
        role_id: str,
        query: AuthOrganizationRolePermissionListOrgRolePermissionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationRolePermissionListOrgRolePermissionsItem]:
        return self._client.request(
            'GET',
            f'auth/roles/{encode_path_param(role_id)}/permissions',
            query=query,
            cast_to=Page[AuthOrganizationRolePermissionListOrgRolePermissionsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_org_role_permissions_count(
        self,
        role_id: str,
        query: AuthOrganizationRolePermissionListOrgRolePermissionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRolePermissionListOrgRolePermissionsCountResponse:
        return self._client.request(
            'GET',
            f'auth/roles/{encode_path_param(role_id)}/permissions/count',
            query=query,
            cast_to=AuthOrganizationRolePermissionListOrgRolePermissionsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def assign_org_role_permission(
        self,
        organization_id: str,
        role_id: str,
        data: AuthOrganizationRolePermissionAssignOrgRolePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> list[AuthOrganizationRolePermissionAssignOrgRolePermissionItem]:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/assign-permissions'
            ),
            body=data,
            cast_to=list[AuthOrganizationRolePermissionAssignOrgRolePermissionItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def remove_role_permission(
        self,
        organization_id: str,
        role_id: str,
        data: AuthOrganizationRolePermissionRemoveRolePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRolePermissionRemoveRolePermissionResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/remove-permissions'
            ),
            body=data,
            cast_to=AuthOrganizationRolePermissionRemoveRolePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthOrganizationRolePermissionsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_org_role_permissions(
        self,
        role_id: str,
        query: AuthOrganizationRolePermissionListOrgRolePermissionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationRolePermissionListOrgRolePermissionsItem]:
        return await self._client.request(
            'GET',
            f'auth/roles/{encode_path_param(role_id)}/permissions',
            query=query,
            cast_to=AsyncPage[AuthOrganizationRolePermissionListOrgRolePermissionsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_org_role_permissions_count(
        self,
        role_id: str,
        query: AuthOrganizationRolePermissionListOrgRolePermissionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRolePermissionListOrgRolePermissionsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/roles/{encode_path_param(role_id)}/permissions/count',
            query=query,
            cast_to=AuthOrganizationRolePermissionListOrgRolePermissionsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def assign_org_role_permission(
        self,
        organization_id: str,
        role_id: str,
        data: AuthOrganizationRolePermissionAssignOrgRolePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> list[AuthOrganizationRolePermissionAssignOrgRolePermissionItem]:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/assign-permissions'
            ),
            body=data,
            cast_to=list[AuthOrganizationRolePermissionAssignOrgRolePermissionItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def remove_role_permission(
        self,
        organization_id: str,
        role_id: str,
        data: AuthOrganizationRolePermissionRemoveRolePermissionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRolePermissionRemoveRolePermissionResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/remove-permissions'
            ),
            body=data,
            cast_to=AuthOrganizationRolePermissionRemoveRolePermissionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
