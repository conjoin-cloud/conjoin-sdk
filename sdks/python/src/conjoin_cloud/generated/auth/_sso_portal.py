from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthSSOPortalMintSsoPortalTicketResponse,
    AuthSSOPortalReadSsoPortalSettingsResponse,
    AuthSSOPortalRevokeSsoPortalTicketResponse,
    AuthSSOPortalUpdateSsoPortalSettingsRequest,
    AuthSSOPortalUpdateSsoPortalSettingsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthSSOPortalsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_sso_portal_settings(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalReadSsoPortalSettingsResponse:
        return self._client.request(
            'GET',
            'auth/portal/settings',
            cast_to=AuthSSOPortalReadSsoPortalSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_sso_portal_settings(
        self,
        data: AuthSSOPortalUpdateSsoPortalSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalUpdateSsoPortalSettingsResponse:
        return self._client.request(
            'PATCH',
            'auth/portal/settings',
            body=data,
            cast_to=AuthSSOPortalUpdateSsoPortalSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def mint_sso_portal_ticket(
        self,
        organization_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalMintSsoPortalTicketResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/portal-tickets/',
            body=data,
            cast_to=AuthSSOPortalMintSsoPortalTicketResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def revoke_sso_portal_ticket(
        self,
        organization_id: str,
        portal_ticket_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalRevokeSsoPortalTicketResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/portal-tickets'
                f'/{encode_path_param(portal_ticket_id)}/revoke'
            ),
            cast_to=AuthSSOPortalRevokeSsoPortalTicketResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthSSOPortalsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_sso_portal_settings(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalReadSsoPortalSettingsResponse:
        return await self._client.request(
            'GET',
            'auth/portal/settings',
            cast_to=AuthSSOPortalReadSsoPortalSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_sso_portal_settings(
        self,
        data: AuthSSOPortalUpdateSsoPortalSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalUpdateSsoPortalSettingsResponse:
        return await self._client.request(
            'PATCH',
            'auth/portal/settings',
            body=data,
            cast_to=AuthSSOPortalUpdateSsoPortalSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def mint_sso_portal_ticket(
        self,
        organization_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalMintSsoPortalTicketResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/portal-tickets/',
            body=data,
            cast_to=AuthSSOPortalMintSsoPortalTicketResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def revoke_sso_portal_ticket(
        self,
        organization_id: str,
        portal_ticket_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalRevokeSsoPortalTicketResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/portal-tickets'
                f'/{encode_path_param(portal_ticket_id)}/revoke'
            ),
            cast_to=AuthSSOPortalRevokeSsoPortalTicketResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
