from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationMembershipCreateMembershipRequest,
    AuthOrganizationMembershipCreateMembershipResponse,
    AuthOrganizationMembershipDeleteMembershipResponse,
    AuthOrganizationMembershipGrantOrgAccountRoleRequest,
    AuthOrganizationMembershipGrantOrgAccountRoleResponse,
    AuthOrganizationMembershipListMembershipsCountQuery,
    AuthOrganizationMembershipListMembershipsCountResponse,
    AuthOrganizationMembershipListMembershipsItem,
    AuthOrganizationMembershipListMembershipsQuery,
    AuthOrganizationMembershipRevokeOrgAccountRoleRequest,
    AuthOrganizationMembershipRevokeOrgAccountRoleResponse,
    AuthOrganizationMembershipUpdateMembershipRequest,
    AuthOrganizationMembershipUpdateMembershipResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationMembershipsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_memberships(
        self,
        organization_id: str,
        query: AuthOrganizationMembershipListMembershipsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationMembershipListMembershipsItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/memberships/',
            query=query,
            cast_to=Page[AuthOrganizationMembershipListMembershipsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_membership(
        self,
        organization_id: str,
        data: AuthOrganizationMembershipCreateMembershipRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipCreateMembershipResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/memberships/',
            body=data,
            cast_to=AuthOrganizationMembershipCreateMembershipResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def list_memberships_count(
        self,
        organization_id: str,
        query: AuthOrganizationMembershipListMembershipsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipListMembershipsCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/memberships/count',
            query=query,
            cast_to=AuthOrganizationMembershipListMembershipsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_membership(
        self,
        organization_id: str,
        membership_id: str,
        data: AuthOrganizationMembershipUpdateMembershipRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipUpdateMembershipResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationMembershipUpdateMembershipResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete_membership(
        self,
        organization_id: str,
        membership_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipDeleteMembershipResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}'
            ),
            cast_to=AuthOrganizationMembershipDeleteMembershipResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def grant_org_account_role(
        self,
        organization_id: str,
        membership_id: str,
        data: AuthOrganizationMembershipGrantOrgAccountRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipGrantOrgAccountRoleResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}/grant-role'
            ),
            body=data,
            cast_to=AuthOrganizationMembershipGrantOrgAccountRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def revoke_org_account_role(
        self,
        organization_id: str,
        membership_id: str,
        data: AuthOrganizationMembershipRevokeOrgAccountRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipRevokeOrgAccountRoleResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}/revoke-role'
            ),
            body=data,
            cast_to=AuthOrganizationMembershipRevokeOrgAccountRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthOrganizationMembershipsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_memberships(
        self,
        organization_id: str,
        query: AuthOrganizationMembershipListMembershipsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationMembershipListMembershipsItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/memberships/',
            query=query,
            cast_to=AsyncPage[AuthOrganizationMembershipListMembershipsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_membership(
        self,
        organization_id: str,
        data: AuthOrganizationMembershipCreateMembershipRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipCreateMembershipResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/memberships/',
            body=data,
            cast_to=AuthOrganizationMembershipCreateMembershipResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def list_memberships_count(
        self,
        organization_id: str,
        query: AuthOrganizationMembershipListMembershipsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipListMembershipsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/memberships/count',
            query=query,
            cast_to=AuthOrganizationMembershipListMembershipsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_membership(
        self,
        organization_id: str,
        membership_id: str,
        data: AuthOrganizationMembershipUpdateMembershipRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipUpdateMembershipResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}'
            ),
            body=data,
            cast_to=AuthOrganizationMembershipUpdateMembershipResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete_membership(
        self,
        organization_id: str,
        membership_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipDeleteMembershipResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}'
            ),
            cast_to=AuthOrganizationMembershipDeleteMembershipResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def grant_org_account_role(
        self,
        organization_id: str,
        membership_id: str,
        data: AuthOrganizationMembershipGrantOrgAccountRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipGrantOrgAccountRoleResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}/grant-role'
            ),
            body=data,
            cast_to=AuthOrganizationMembershipGrantOrgAccountRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def revoke_org_account_role(
        self,
        organization_id: str,
        membership_id: str,
        data: AuthOrganizationMembershipRevokeOrgAccountRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationMembershipRevokeOrgAccountRoleResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/memberships'
                f'/{encode_path_param(membership_id)}/revoke-role'
            ),
            body=data,
            cast_to=AuthOrganizationMembershipRevokeOrgAccountRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
