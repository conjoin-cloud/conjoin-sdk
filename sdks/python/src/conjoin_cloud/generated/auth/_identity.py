from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthIdentityDiscoverAccountRequest,
    AuthIdentityDiscoverAccountResponse,
    AuthIdentityLinkRequest,
    AuthIdentityLinkResponse,
    AuthIdentityUnlinkRequest,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthIdentitiesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def discover_account(
        self,
        data: AuthIdentityDiscoverAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthIdentityDiscoverAccountResponse:
        return self._client.request(
            'POST',
            'auth/accounts/discover',
            body=data,
            cast_to=AuthIdentityDiscoverAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def link(
        self,
        account_id: str,
        data: AuthIdentityLinkRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthIdentityLinkResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/identities/link',
            body=data,
            cast_to=AuthIdentityLinkResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def unlink(
        self,
        account_id: str,
        data: AuthIdentityUnlinkRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/identities/unlink',
            body=data,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthIdentitiesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def discover_account(
        self,
        data: AuthIdentityDiscoverAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthIdentityDiscoverAccountResponse:
        return await self._client.request(
            'POST',
            'auth/accounts/discover',
            body=data,
            cast_to=AuthIdentityDiscoverAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def link(
        self,
        account_id: str,
        data: AuthIdentityLinkRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthIdentityLinkResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/identities/link',
            body=data,
            cast_to=AuthIdentityLinkResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def unlink(
        self,
        account_id: str,
        data: AuthIdentityUnlinkRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/identities/unlink',
            body=data,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
