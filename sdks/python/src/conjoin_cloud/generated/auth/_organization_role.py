from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationRoleArchiveOrgRoleResponse,
    AuthOrganizationRoleCreateOrgRoleRequest,
    AuthOrganizationRoleCreateOrgRoleResponse,
    AuthOrganizationRoleDeleteOrgRoleResponse,
    AuthOrganizationRoleListOrgRolesCountQuery,
    AuthOrganizationRoleListOrgRolesCountResponse,
    AuthOrganizationRoleListOrgRolesItem,
    AuthOrganizationRoleListOrgRolesQuery,
    AuthOrganizationRoleReadOrgRoleResponse,
    AuthOrganizationRoleRestoreOrgRoleResponse,
    AuthOrganizationRoleUpdateOrgRoleRequest,
    AuthOrganizationRoleUpdateOrgRoleResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationRolesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_org_roles(
        self,
        organization_id: str,
        query: AuthOrganizationRoleListOrgRolesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationRoleListOrgRolesItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/roles/',
            query=query,
            cast_to=Page[AuthOrganizationRoleListOrgRolesItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_org_role(
        self,
        organization_id: str,
        data: AuthOrganizationRoleCreateOrgRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleCreateOrgRoleResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/roles/',
            body=data,
            cast_to=AuthOrganizationRoleCreateOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def list_org_roles_count(
        self,
        organization_id: str,
        query: AuthOrganizationRoleListOrgRolesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleListOrgRolesCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/roles/count',
            query=query,
            cast_to=AuthOrganizationRoleListOrgRolesCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleReadOrgRoleResponse:
        return self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}'
            ),
            cast_to=AuthOrganizationRoleReadOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_org_role(
        self,
        organization_id: str,
        role_id: str,
        data: AuthOrganizationRoleUpdateOrgRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleUpdateOrgRoleResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationRoleUpdateOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleDeleteOrgRoleResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}'
            ),
            cast_to=AuthOrganizationRoleDeleteOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def archive_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleArchiveOrgRoleResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/archive'
            ),
            cast_to=AuthOrganizationRoleArchiveOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def restore_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleRestoreOrgRoleResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/restore'
            ),
            cast_to=AuthOrganizationRoleRestoreOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthOrganizationRolesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_org_roles(
        self,
        organization_id: str,
        query: AuthOrganizationRoleListOrgRolesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationRoleListOrgRolesItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/roles/',
            query=query,
            cast_to=AsyncPage[AuthOrganizationRoleListOrgRolesItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_org_role(
        self,
        organization_id: str,
        data: AuthOrganizationRoleCreateOrgRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleCreateOrgRoleResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/roles/',
            body=data,
            cast_to=AuthOrganizationRoleCreateOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def list_org_roles_count(
        self,
        organization_id: str,
        query: AuthOrganizationRoleListOrgRolesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleListOrgRolesCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/roles/count',
            query=query,
            cast_to=AuthOrganizationRoleListOrgRolesCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleReadOrgRoleResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}'
            ),
            cast_to=AuthOrganizationRoleReadOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_org_role(
        self,
        organization_id: str,
        role_id: str,
        data: AuthOrganizationRoleUpdateOrgRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleUpdateOrgRoleResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationRoleUpdateOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleDeleteOrgRoleResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}'
            ),
            cast_to=AuthOrganizationRoleDeleteOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def archive_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleArchiveOrgRoleResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/archive'
            ),
            cast_to=AuthOrganizationRoleArchiveOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def restore_org_role(
        self,
        organization_id: str,
        role_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationRoleRestoreOrgRoleResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/roles'
                f'/{encode_path_param(role_id)}/restore'
            ),
            cast_to=AuthOrganizationRoleRestoreOrgRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
