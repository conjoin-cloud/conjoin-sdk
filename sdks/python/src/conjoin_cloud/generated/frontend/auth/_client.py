from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    AuthClientGetJwksResponse,
    AuthClientGetOidcDiscoveryResponse,
    AuthClientProcessHandshakeResponse,
    AuthClientProcessLogoutResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthClientsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def get_oidc_discovery(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientGetOidcDiscoveryResponse:
        return self._client.request(
            'GET',
            'auth/client/.well-known/openid-configuration',
            cast_to=AuthClientGetOidcDiscoveryResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def process_handshake(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientProcessHandshakeResponse:
        return self._client.request(
            'POST',
            'auth/client/handshakes',
            cast_to=AuthClientProcessHandshakeResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def process_logout(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientProcessLogoutResponse:
        return self._client.request(
            'POST',
            'auth/client/logout',
            cast_to=AuthClientProcessLogoutResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def get_jwks(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientGetJwksResponse:
        return self._client.request(
            'GET',
            'auth/client/.well-known/jwks.json',
            cast_to=AuthClientGetJwksResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthClientsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def get_oidc_discovery(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientGetOidcDiscoveryResponse:
        return await self._client.request(
            'GET',
            'auth/client/.well-known/openid-configuration',
            cast_to=AuthClientGetOidcDiscoveryResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def process_handshake(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientProcessHandshakeResponse:
        return await self._client.request(
            'POST',
            'auth/client/handshakes',
            cast_to=AuthClientProcessHandshakeResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def process_logout(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientProcessLogoutResponse:
        return await self._client.request(
            'POST',
            'auth/client/logout',
            cast_to=AuthClientProcessLogoutResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def get_jwks(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientGetJwksResponse:
        return await self._client.request(
            'GET',
            'auth/client/.well-known/jwks.json',
            cast_to=AuthClientGetJwksResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
