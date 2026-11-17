from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthSCIMManagementReadScimSettingsResponse,
    AuthSCIMManagementReconcileScimGroupMembersRequest,
    AuthSCIMManagementReconcileScimGroupMembersResponse,
    AuthSCIMManagementReconcileScimGroupsRequest,
    AuthSCIMManagementReconcileScimGroupsResponse,
    AuthSCIMManagementReconcileScimUsersRequest,
    AuthSCIMManagementReconcileScimUsersResponse,
    AuthSCIMManagementSyncScimRolesForGroupResponse,
    AuthSCIMManagementSyncScimRolesForMemberResponse,
    AuthSCIMManagementUpdateScimSettingsRequest,
    AuthSCIMManagementUpdateScimSettingsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthSCIMManagementsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_scim_settings(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReadScimSettingsResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/scim-settings',
            cast_to=AuthSCIMManagementReadScimSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_scim_settings(
        self,
        organization_id: str,
        data: AuthSCIMManagementUpdateScimSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementUpdateScimSettingsResponse:
        return self._client.request(
            'PATCH',
            f'auth/organizations/{encode_path_param(organization_id)}/scim-settings',
            body=data,
            cast_to=AuthSCIMManagementUpdateScimSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def sync_scim_roles_for_member(
        self,
        organization_id: str,
        membership_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementSyncScimRolesForMemberResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}/sync-scim-roles'
            ),
            cast_to=AuthSCIMManagementSyncScimRolesForMemberResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def sync_scim_roles_for_group(
        self,
        organization_id: str,
        group_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementSyncScimRolesForGroupResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/sync-scim-roles'
            ),
            cast_to=AuthSCIMManagementSyncScimRolesForGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def reconcile_scim_users(
        self,
        organization_id: str,
        data: AuthSCIMManagementReconcileScimUsersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReconcileScimUsersResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/reconcile-scim-users',
            body=data,
            cast_to=AuthSCIMManagementReconcileScimUsersResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def reconcile_scim_groups(
        self,
        organization_id: str,
        data: AuthSCIMManagementReconcileScimGroupsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReconcileScimGroupsResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/reconcile-scim-groups',
            body=data,
            cast_to=AuthSCIMManagementReconcileScimGroupsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def reconcile_scim_group_members(
        self,
        organization_id: str,
        data: AuthSCIMManagementReconcileScimGroupMembersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReconcileScimGroupMembersResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/reconcile-scim-group-members',
            body=data,
            cast_to=AuthSCIMManagementReconcileScimGroupMembersResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthSCIMManagementsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_scim_settings(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReadScimSettingsResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/scim-settings',
            cast_to=AuthSCIMManagementReadScimSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_scim_settings(
        self,
        organization_id: str,
        data: AuthSCIMManagementUpdateScimSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementUpdateScimSettingsResponse:
        return await self._client.request(
            'PATCH',
            f'auth/organizations/{encode_path_param(organization_id)}/scim-settings',
            body=data,
            cast_to=AuthSCIMManagementUpdateScimSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def sync_scim_roles_for_member(
        self,
        organization_id: str,
        membership_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementSyncScimRolesForMemberResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}/sync-scim-roles'
            ),
            cast_to=AuthSCIMManagementSyncScimRolesForMemberResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def sync_scim_roles_for_group(
        self,
        organization_id: str,
        group_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementSyncScimRolesForGroupResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/sync-scim-roles'
            ),
            cast_to=AuthSCIMManagementSyncScimRolesForGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def reconcile_scim_users(
        self,
        organization_id: str,
        data: AuthSCIMManagementReconcileScimUsersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReconcileScimUsersResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/reconcile-scim-users',
            body=data,
            cast_to=AuthSCIMManagementReconcileScimUsersResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def reconcile_scim_groups(
        self,
        organization_id: str,
        data: AuthSCIMManagementReconcileScimGroupsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReconcileScimGroupsResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/reconcile-scim-groups',
            body=data,
            cast_to=AuthSCIMManagementReconcileScimGroupsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def reconcile_scim_group_members(
        self,
        organization_id: str,
        data: AuthSCIMManagementReconcileScimGroupMembersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSCIMManagementReconcileScimGroupMembersResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/reconcile-scim-group-members',
            body=data,
            cast_to=AuthSCIMManagementReconcileScimGroupMembersResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
