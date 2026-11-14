from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationInvitationCreateInvitationRequest,
    AuthOrganizationInvitationCreateInvitationResponse,
    AuthOrganizationInvitationListInvitationsCountQuery,
    AuthOrganizationInvitationListInvitationsCountResponse,
    AuthOrganizationInvitationListInvitationsItem,
    AuthOrganizationInvitationListInvitationsQuery,
    AuthOrganizationInvitationResendInvitationRequest,
    AuthOrganizationInvitationResendInvitationResponse,
    AuthOrganizationInvitationRevokeInvitationResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationInvitationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_invitations(
        self,
        organization_id: str,
        query: AuthOrganizationInvitationListInvitationsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationInvitationListInvitationsItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/invitations/',
            query=query,
            cast_to=Page[AuthOrganizationInvitationListInvitationsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_invitation(
        self,
        organization_id: str,
        data: AuthOrganizationInvitationCreateInvitationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationCreateInvitationResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/invitations/',
            body=data,
            cast_to=AuthOrganizationInvitationCreateInvitationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_invitations_count(
        self,
        organization_id: str,
        query: AuthOrganizationInvitationListInvitationsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationListInvitationsCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/invitations/count',
            query=query,
            cast_to=AuthOrganizationInvitationListInvitationsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def revoke_invitation(
        self,
        organization_id: str,
        invitation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationRevokeInvitationResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/invitations'
                f'/{encode_path_param(invitation_id)}/revoke'
            ),
            cast_to=AuthOrganizationInvitationRevokeInvitationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def resend_invitation(
        self,
        organization_id: str,
        invitation_id: str,
        data: AuthOrganizationInvitationResendInvitationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationResendInvitationResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/invitations'
                f'/{encode_path_param(invitation_id)}/resend'
            ),
            body=data,
            cast_to=AuthOrganizationInvitationResendInvitationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthOrganizationInvitationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_invitations(
        self,
        organization_id: str,
        query: AuthOrganizationInvitationListInvitationsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationInvitationListInvitationsItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/invitations/',
            query=query,
            cast_to=AsyncPage[AuthOrganizationInvitationListInvitationsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_invitation(
        self,
        organization_id: str,
        data: AuthOrganizationInvitationCreateInvitationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationCreateInvitationResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/invitations/',
            body=data,
            cast_to=AuthOrganizationInvitationCreateInvitationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_invitations_count(
        self,
        organization_id: str,
        query: AuthOrganizationInvitationListInvitationsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationListInvitationsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/invitations/count',
            query=query,
            cast_to=AuthOrganizationInvitationListInvitationsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def revoke_invitation(
        self,
        organization_id: str,
        invitation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationRevokeInvitationResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/invitations'
                f'/{encode_path_param(invitation_id)}/revoke'
            ),
            cast_to=AuthOrganizationInvitationRevokeInvitationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def resend_invitation(
        self,
        organization_id: str,
        invitation_id: str,
        data: AuthOrganizationInvitationResendInvitationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationInvitationResendInvitationResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/invitations'
                f'/{encode_path_param(invitation_id)}/resend'
            ),
            body=data,
            cast_to=AuthOrganizationInvitationResendInvitationResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
