from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthStepUpRequestRequest,
    AuthStepUpRequestResponse,
    AuthStepUpValidateRequest,
    AuthStepUpValidateResponse,
    AuthStepUpVerifyRequest,
    AuthStepUpVerifyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthStepUpsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def request(
        self,
        account_id: str,
        data: AuthStepUpRequestRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthStepUpRequestResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/step-ups/start',
            body=data,
            cast_to=AuthStepUpRequestResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def verify(
        self,
        account_id: str,
        data: AuthStepUpVerifyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthStepUpVerifyResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/step-ups/verify',
            body=data,
            cast_to=AuthStepUpVerifyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def validate_(
        self,
        account_id: str,
        data: AuthStepUpValidateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthStepUpValidateResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/step-ups/validate',
            body=data,
            cast_to=AuthStepUpValidateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthStepUpsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def request(
        self,
        account_id: str,
        data: AuthStepUpRequestRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthStepUpRequestResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/step-ups/start',
            body=data,
            cast_to=AuthStepUpRequestResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def verify(
        self,
        account_id: str,
        data: AuthStepUpVerifyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthStepUpVerifyResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/step-ups/verify',
            body=data,
            cast_to=AuthStepUpVerifyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def validate_(
        self,
        account_id: str,
        data: AuthStepUpValidateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthStepUpValidateResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/step-ups/validate',
            body=data,
            cast_to=AuthStepUpValidateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
