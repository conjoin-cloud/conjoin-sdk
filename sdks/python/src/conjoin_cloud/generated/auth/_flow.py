from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
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
        client_id: str,
        data: AuthFlowStartSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSignupResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ups/start',
            body=data,
            cast_to=AuthFlowStartSignupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def complete_signup(
        self,
        client_id: str,
        data: AuthFlowCompleteSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSignupResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ups/complete',
            body=data,
            cast_to=AuthFlowCompleteSignupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def confirm_link_signup(
        self,
        client_id: str,
        data: AuthFlowConfirmLinkSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowConfirmLinkSignupResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ups/confirm-link',
            body=data,
            cast_to=AuthFlowConfirmLinkSignupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def start_signin(
        self,
        client_id: str,
        data: AuthFlowStartSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSigninResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ins/start',
            body=data,
            cast_to=AuthFlowStartSigninResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def complete_signin(
        self,
        client_id: str,
        data: AuthFlowCompleteSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSigninResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ins/complete',
            body=data,
            cast_to=AuthFlowCompleteSigninResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def start_password_reset(
        self,
        client_id: str,
        data: AuthFlowStartPasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartPasswordResetResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/password-resets/start',
            body=data,
            cast_to=AuthFlowStartPasswordResetResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def complete_password_reset(
        self,
        client_id: str,
        data: AuthFlowCompletePasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompletePasswordResetResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/password-resets/complete',
            body=data,
            cast_to=AuthFlowCompletePasswordResetResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthFlowsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def start_signup(
        self,
        client_id: str,
        data: AuthFlowStartSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSignupResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ups/start',
            body=data,
            cast_to=AuthFlowStartSignupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def complete_signup(
        self,
        client_id: str,
        data: AuthFlowCompleteSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSignupResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ups/complete',
            body=data,
            cast_to=AuthFlowCompleteSignupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def confirm_link_signup(
        self,
        client_id: str,
        data: AuthFlowConfirmLinkSignupRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowConfirmLinkSignupResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ups/confirm-link',
            body=data,
            cast_to=AuthFlowConfirmLinkSignupResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def start_signin(
        self,
        client_id: str,
        data: AuthFlowStartSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartSigninResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ins/start',
            body=data,
            cast_to=AuthFlowStartSigninResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def complete_signin(
        self,
        client_id: str,
        data: AuthFlowCompleteSigninRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompleteSigninResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sign-ins/complete',
            body=data,
            cast_to=AuthFlowCompleteSigninResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def start_password_reset(
        self,
        client_id: str,
        data: AuthFlowStartPasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowStartPasswordResetResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/password-resets/start',
            body=data,
            cast_to=AuthFlowStartPasswordResetResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def complete_password_reset(
        self,
        client_id: str,
        data: AuthFlowCompletePasswordResetRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthFlowCompletePasswordResetResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/password-resets/complete',
            body=data,
            cast_to=AuthFlowCompletePasswordResetResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
