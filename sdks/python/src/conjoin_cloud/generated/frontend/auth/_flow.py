from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    AuthFlowCompletePasswordResetRequest,
    AuthFlowCompletePasswordResetResponse,
    AuthFlowCompleteSigninRequest,
    AuthFlowCompleteSigninResponse,
    AuthFlowCompleteSignupRequest,
    AuthFlowCompleteSignupResponse,
    AuthFlowConfirmLinkSignupRequest,
    AuthFlowConfirmLinkSignupResponse,
    AuthFlowStartPasswordResetRequest,
    AuthFlowStartPasswordResetResponse,
    AuthFlowStartSigninRequest,
    AuthFlowStartSigninResponse,
    AuthFlowStartSignupRequest,
    AuthFlowStartSignupResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthFlowsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def start_signup(
        self,
        data: AuthFlowStartSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSignupResponse:
        return self._client.request(
            'POST',
            'auth/client/sign-ups/start',
            body=data,
            cast_to=AuthFlowStartSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def complete_signup(
        self,
        data: AuthFlowCompleteSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSignupResponse:
        return self._client.request(
            'POST',
            'auth/client/sign-ups/complete',
            body=data,
            cast_to=AuthFlowCompleteSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def confirm_link_signup(
        self,
        data: AuthFlowConfirmLinkSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowConfirmLinkSignupResponse:
        return self._client.request(
            'POST',
            'auth/client/sign-ups/confirm-link',
            body=data,
            cast_to=AuthFlowConfirmLinkSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def start_signin(
        self,
        data: AuthFlowStartSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSigninResponse:
        return self._client.request(
            'POST',
            'auth/client/sign-ins/start',
            body=data,
            cast_to=AuthFlowStartSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def complete_signin(
        self,
        data: AuthFlowCompleteSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSigninResponse:
        return self._client.request(
            'POST',
            'auth/client/sign-ins/complete',
            body=data,
            cast_to=AuthFlowCompleteSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def start_password_reset(
        self,
        data: AuthFlowStartPasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartPasswordResetResponse:
        return self._client.request(
            'POST',
            'auth/client/password-resets/start',
            body=data,
            cast_to=AuthFlowStartPasswordResetResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def complete_password_reset(
        self,
        data: AuthFlowCompletePasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompletePasswordResetResponse:
        return self._client.request(
            'POST',
            'auth/client/password-resets/complete',
            body=data,
            cast_to=AuthFlowCompletePasswordResetResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthFlowsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def start_signup(
        self,
        data: AuthFlowStartSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSignupResponse:
        return await self._client.request(
            'POST',
            'auth/client/sign-ups/start',
            body=data,
            cast_to=AuthFlowStartSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def complete_signup(
        self,
        data: AuthFlowCompleteSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSignupResponse:
        return await self._client.request(
            'POST',
            'auth/client/sign-ups/complete',
            body=data,
            cast_to=AuthFlowCompleteSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def confirm_link_signup(
        self,
        data: AuthFlowConfirmLinkSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowConfirmLinkSignupResponse:
        return await self._client.request(
            'POST',
            'auth/client/sign-ups/confirm-link',
            body=data,
            cast_to=AuthFlowConfirmLinkSignupResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def start_signin(
        self,
        data: AuthFlowStartSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSigninResponse:
        return await self._client.request(
            'POST',
            'auth/client/sign-ins/start',
            body=data,
            cast_to=AuthFlowStartSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def complete_signin(
        self,
        data: AuthFlowCompleteSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSigninResponse:
        return await self._client.request(
            'POST',
            'auth/client/sign-ins/complete',
            body=data,
            cast_to=AuthFlowCompleteSigninResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def start_password_reset(
        self,
        data: AuthFlowStartPasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartPasswordResetResponse:
        return await self._client.request(
            'POST',
            'auth/client/password-resets/start',
            body=data,
            cast_to=AuthFlowStartPasswordResetResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def complete_password_reset(
        self,
        data: AuthFlowCompletePasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompletePasswordResetResponse:
        return await self._client.request(
            'POST',
            'auth/client/password-resets/complete',
            body=data,
            cast_to=AuthFlowCompletePasswordResetResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
