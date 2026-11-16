from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationGroupAddGroupMemberRequest,
    AuthOrganizationGroupAddGroupMemberResponse,
    AuthOrganizationGroupBulkSyncGroupMembersRequest,
    AuthOrganizationGroupBulkSyncGroupMembersResponse,
    AuthOrganizationGroupCreateGroupRequest,
    AuthOrganizationGroupCreateGroupResponse,
    AuthOrganizationGroupDeleteGroupResponse,
    AuthOrganizationGroupListGroupMembersCountQuery,
    AuthOrganizationGroupListGroupMembersCountResponse,
    AuthOrganizationGroupListGroupMembersItem,
    AuthOrganizationGroupListGroupMembersQuery,
    AuthOrganizationGroupListGroupsCountQuery,
    AuthOrganizationGroupListGroupsCountResponse,
    AuthOrganizationGroupListGroupsItem,
    AuthOrganizationGroupListGroupsQuery,
    AuthOrganizationGroupRemoveGroupMemberRequest,
    AuthOrganizationGroupRemoveGroupMemberResponse,
    AuthOrganizationGroupUpdateGroupRequest,
    AuthOrganizationGroupUpdateGroupResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationGroupsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_groups(
        self,
        organization_id: str,
        query: AuthOrganizationGroupListGroupsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationGroupListGroupsItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/groups/',
            query=query,
            cast_to=Page[AuthOrganizationGroupListGroupsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_group(
        self,
        organization_id: str,
        data: AuthOrganizationGroupCreateGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupCreateGroupResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/groups/',
            body=data,
            cast_to=AuthOrganizationGroupCreateGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def list_group_members(
        self,
        group_id: str,
        query: AuthOrganizationGroupListGroupMembersQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationGroupListGroupMembersItem]:
        return self._client.request(
            'GET',
            f'auth/groups/{encode_path_param(group_id)}/members',
            query=query,
            cast_to=Page[AuthOrganizationGroupListGroupMembersItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_group_members_count(
        self,
        group_id: str,
        query: AuthOrganizationGroupListGroupMembersCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupListGroupMembersCountResponse:
        return self._client.request(
            'GET',
            f'auth/groups/{encode_path_param(group_id)}/members/count',
            query=query,
            cast_to=AuthOrganizationGroupListGroupMembersCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_groups_count(
        self,
        organization_id: str,
        query: AuthOrganizationGroupListGroupsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupListGroupsCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/groups/count',
            query=query,
            cast_to=AuthOrganizationGroupListGroupsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_group(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupUpdateGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupUpdateGroupResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationGroupUpdateGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete_group(
        self,
        organization_id: str,
        group_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupDeleteGroupResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}'
            ),
            cast_to=AuthOrganizationGroupDeleteGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def add_group_member(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupAddGroupMemberRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupAddGroupMemberResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/add-members'
            ),
            body=data,
            cast_to=AuthOrganizationGroupAddGroupMemberResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def remove_group_member(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupRemoveGroupMemberRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupRemoveGroupMemberResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/remove-members'
            ),
            body=data,
            cast_to=AuthOrganizationGroupRemoveGroupMemberResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def bulk_sync_group_members(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupBulkSyncGroupMembersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupBulkSyncGroupMembersResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/sync-members'
            ),
            body=data,
            cast_to=AuthOrganizationGroupBulkSyncGroupMembersResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthOrganizationGroupsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_groups(
        self,
        organization_id: str,
        query: AuthOrganizationGroupListGroupsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationGroupListGroupsItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/groups/',
            query=query,
            cast_to=AsyncPage[AuthOrganizationGroupListGroupsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_group(
        self,
        organization_id: str,
        data: AuthOrganizationGroupCreateGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupCreateGroupResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/groups/',
            body=data,
            cast_to=AuthOrganizationGroupCreateGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def list_group_members(
        self,
        group_id: str,
        query: AuthOrganizationGroupListGroupMembersQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationGroupListGroupMembersItem]:
        return await self._client.request(
            'GET',
            f'auth/groups/{encode_path_param(group_id)}/members',
            query=query,
            cast_to=AsyncPage[AuthOrganizationGroupListGroupMembersItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_group_members_count(
        self,
        group_id: str,
        query: AuthOrganizationGroupListGroupMembersCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupListGroupMembersCountResponse:
        return await self._client.request(
            'GET',
            f'auth/groups/{encode_path_param(group_id)}/members/count',
            query=query,
            cast_to=AuthOrganizationGroupListGroupMembersCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_groups_count(
        self,
        organization_id: str,
        query: AuthOrganizationGroupListGroupsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupListGroupsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/groups/count',
            query=query,
            cast_to=AuthOrganizationGroupListGroupsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_group(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupUpdateGroupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupUpdateGroupResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationGroupUpdateGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete_group(
        self,
        organization_id: str,
        group_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupDeleteGroupResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}'
            ),
            cast_to=AuthOrganizationGroupDeleteGroupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def add_group_member(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupAddGroupMemberRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupAddGroupMemberResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/add-members'
            ),
            body=data,
            cast_to=AuthOrganizationGroupAddGroupMemberResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def remove_group_member(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupRemoveGroupMemberRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupRemoveGroupMemberResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/remove-members'
            ),
            body=data,
            cast_to=AuthOrganizationGroupRemoveGroupMemberResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def bulk_sync_group_members(
        self,
        organization_id: str,
        group_id: str,
        data: AuthOrganizationGroupBulkSyncGroupMembersRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationGroupBulkSyncGroupMembersResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/groups'
                f'/{encode_path_param(group_id)}/sync-members'
            ),
            body=data,
            cast_to=AuthOrganizationGroupBulkSyncGroupMembersResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
