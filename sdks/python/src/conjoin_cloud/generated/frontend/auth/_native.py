from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    AuthNativeCompleteSigninRequest,
    AuthNativeCompleteSigninResponse,
    AuthNativeCompleteSignupRequest,
    AuthNativeCompleteSignupResponse,
    AuthNativeConfirmLinkSignupRequest,
    AuthNativeConfirmLinkSignupResponse,
    AuthNativeProcessLogoutResponse,
    AuthNativeProcessTokenMintResponse,
    AuthNativeRefreshSessionRequest,
    AuthNativeRefreshSessionResponse,
    AuthNativeStartSigninRequest,
    AuthNativeStartSigninResponse,
    AuthNativeStartSignupRequest,
    AuthNativeStartSignupResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthNativesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def start_signup(
        self,
        data: AuthNativeStartSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeStartSignupResponse:
        return self._client.request(
            'POST',
            'auth/client/native/sign-ups/start',
            body=data,
            cast_to=AuthNativeStartSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def complete_signup(
        self,
        data: AuthNativeCompleteSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeCompleteSignupResponse:
        return self._client.request(
            'POST',
            'auth/client/native/sign-ups/complete',
            body=data,
            cast_to=AuthNativeCompleteSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def confirm_link_signup(
        self,
        data: AuthNativeConfirmLinkSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeConfirmLinkSignupResponse:
        return self._client.request(
            'POST',
            'auth/client/native/sign-ups/confirm-link',
            body=data,
            cast_to=AuthNativeConfirmLinkSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def start_signin(
        self,
        data: AuthNativeStartSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeStartSigninResponse:
        return self._client.request(
            'POST',
            'auth/client/native/sign-ins/start',
            body=data,
            cast_to=AuthNativeStartSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def complete_signin(
        self,
        data: AuthNativeCompleteSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeCompleteSigninResponse:
        return self._client.request(
            'POST',
            'auth/client/native/sign-ins/complete',
            body=data,
            cast_to=AuthNativeCompleteSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def process_token_mint(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeProcessTokenMintResponse:
        return self._client.request(
            'POST',
            'auth/client/native/tokens',
            cast_to=AuthNativeProcessTokenMintResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def refresh_session(
        self,
        data: AuthNativeRefreshSessionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeRefreshSessionResponse:
        return self._client.request(
            'POST',
            'auth/client/native/tokens/refresh',
            body=data,
            cast_to=AuthNativeRefreshSessionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def process_logout(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeProcessLogoutResponse:
        return self._client.request(
            'POST',
            'auth/client/native/logout',
            cast_to=AuthNativeProcessLogoutResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthNativesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def start_signup(
        self,
        data: AuthNativeStartSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeStartSignupResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/sign-ups/start',
            body=data,
            cast_to=AuthNativeStartSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def complete_signup(
        self,
        data: AuthNativeCompleteSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeCompleteSignupResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/sign-ups/complete',
            body=data,
            cast_to=AuthNativeCompleteSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def confirm_link_signup(
        self,
        data: AuthNativeConfirmLinkSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeConfirmLinkSignupResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/sign-ups/confirm-link',
            body=data,
            cast_to=AuthNativeConfirmLinkSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def start_signin(
        self,
        data: AuthNativeStartSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeStartSigninResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/sign-ins/start',
            body=data,
            cast_to=AuthNativeStartSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def complete_signin(
        self,
        data: AuthNativeCompleteSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeCompleteSigninResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/sign-ins/complete',
            body=data,
            cast_to=AuthNativeCompleteSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def process_token_mint(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeProcessTokenMintResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/tokens',
            cast_to=AuthNativeProcessTokenMintResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def refresh_session(
        self,
        data: AuthNativeRefreshSessionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeRefreshSessionResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/tokens/refresh',
            body=data,
            cast_to=AuthNativeRefreshSessionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def process_logout(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthNativeProcessLogoutResponse:
        return await self._client.request(
            'POST',
            'auth/client/native/logout',
            cast_to=AuthNativeProcessLogoutResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
