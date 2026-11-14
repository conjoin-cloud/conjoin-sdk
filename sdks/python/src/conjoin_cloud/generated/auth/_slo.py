from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthSLOOidcLogoutRequest,
    AuthSLOOidcLogoutResponse,
    AuthSLOSamlIdpLogoutRequest,
    AuthSLOSamlIdpLogoutResponse,
    AuthSLOSamlSpLogoutRequest,
    AuthSLOSamlSpLogoutResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthSLOsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def oidc_logout(
        self,
        account_id: str,
        data: AuthSLOOidcLogoutRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSLOOidcLogoutResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/logout-oidc',
            body=data,
            cast_to=AuthSLOOidcLogoutResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def saml_sp_logout(
        self,
        account_id: str,
        data: AuthSLOSamlSpLogoutRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSLOSamlSpLogoutResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/logout-saml',
            body=data,
            cast_to=AuthSLOSamlSpLogoutResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def saml_idp_logout(
        self,
        data: AuthSLOSamlIdpLogoutRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSLOSamlIdpLogoutResponse:
        return self._client.request(
            'POST',
            'auth/saml-logout-requests',
            body=data,
            cast_to=AuthSLOSamlIdpLogoutResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthSLOsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def oidc_logout(
        self,
        account_id: str,
        data: AuthSLOOidcLogoutRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSLOOidcLogoutResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/logout-oidc',
            body=data,
            cast_to=AuthSLOOidcLogoutResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def saml_sp_logout(
        self,
        account_id: str,
        data: AuthSLOSamlSpLogoutRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSLOSamlSpLogoutResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/logout-saml',
            body=data,
            cast_to=AuthSLOSamlSpLogoutResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def saml_idp_logout(
        self,
        data: AuthSLOSamlIdpLogoutRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSLOSamlIdpLogoutResponse:
        return await self._client.request(
            'POST',
            'auth/saml-logout-requests',
            body=data,
            cast_to=AuthSLOSamlIdpLogoutResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
