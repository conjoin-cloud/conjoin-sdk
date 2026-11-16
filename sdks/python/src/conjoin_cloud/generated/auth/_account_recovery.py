from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthAccountRecoveryAdminResetAccountResponse,
    AuthAccountRecoveryCompleteRecoveryRequest,
    AuthAccountRecoveryCompleteRecoveryResponse,
    AuthAccountRecoveryStartRecoveryResponse,
    AuthAccountRecoveryVerifyRecoveryRequest,
    AuthAccountRecoveryVerifyRecoveryResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthAccountRecoveriesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def start_recovery(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryStartRecoveryResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/recoveries/start',
            cast_to=AuthAccountRecoveryStartRecoveryResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def verify_recovery(
        self,
        account_id: str,
        data: AuthAccountRecoveryVerifyRecoveryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryVerifyRecoveryResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/recoveries/verify',
            body=data,
            cast_to=AuthAccountRecoveryVerifyRecoveryResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def complete_recovery(
        self,
        account_id: str,
        data: AuthAccountRecoveryCompleteRecoveryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryCompleteRecoveryResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/recoveries/complete',
            body=data,
            cast_to=AuthAccountRecoveryCompleteRecoveryResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def admin_reset_account(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryAdminResetAccountResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/reset-mfa',
            cast_to=AuthAccountRecoveryAdminResetAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthAccountRecoveriesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def start_recovery(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryStartRecoveryResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/recoveries/start',
            cast_to=AuthAccountRecoveryStartRecoveryResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def verify_recovery(
        self,
        account_id: str,
        data: AuthAccountRecoveryVerifyRecoveryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryVerifyRecoveryResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/recoveries/verify',
            body=data,
            cast_to=AuthAccountRecoveryVerifyRecoveryResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def complete_recovery(
        self,
        account_id: str,
        data: AuthAccountRecoveryCompleteRecoveryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryCompleteRecoveryResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/recoveries/complete',
            body=data,
            cast_to=AuthAccountRecoveryCompleteRecoveryResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def admin_reset_account(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAccountRecoveryAdminResetAccountResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/reset-mfa',
            cast_to=AuthAccountRecoveryAdminResetAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
