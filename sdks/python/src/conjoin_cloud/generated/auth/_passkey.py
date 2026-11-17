from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._credential import Credential
from conjoin_cloud._declared_headers import DeclaredHeader
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthPasskeyDeleteResponse,
    AuthPasskeyListCountQuery,
    AuthPasskeyListCountResponse,
    AuthPasskeyListItem,
    AuthPasskeyListQuery,
    AuthPasskeyReadResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthPasskeysResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        account_id: str,
        query: AuthPasskeyListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthPasskeyListItem]:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/passkeys/',
            query=query,
            cast_to=Page[AuthPasskeyListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        account_id: str,
        query: AuthPasskeyListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPasskeyListCountResponse:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/passkeys/count',
            query=query,
            cast_to=AuthPasskeyListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read(
        self,
        account_id: str,
        passkey_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPasskeyReadResponse:
        return self._client.request(
            'GET',
            (
                f'auth/accounts/{encode_path_param(account_id)}/passkeys'
                f'/{encode_path_param(passkey_id)}'
            ),
            cast_to=AuthPasskeyReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete(
        self,
        account_id: str,
        passkey_id: str,
        *,
        step_up_session_id: str | None = None,
        step_up_token: Credential | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPasskeyDeleteResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/accounts/{encode_path_param(account_id)}/passkeys'
                f'/{encode_path_param(passkey_id)}'
            ),
            cast_to=AuthPasskeyDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            declared_headers=(
                DeclaredHeader(
                    name='Step-Up-Session-ID',
                    argument='step_up_session_id',
                    value=step_up_session_id,
                    min_length=1,
                    max_length=48,
                ),
                DeclaredHeader(
                    name='Step-Up-Token',
                    argument='step_up_token',
                    value=step_up_token,
                    credential=True,
                    min_length=1,
                    max_length=256,
                    pattern='^[0-9a-f]+$',
                ),
            ),
        )


class AsyncAuthPasskeysResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        account_id: str,
        query: AuthPasskeyListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthPasskeyListItem]:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/passkeys/',
            query=query,
            cast_to=AsyncPage[AuthPasskeyListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        account_id: str,
        query: AuthPasskeyListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPasskeyListCountResponse:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/passkeys/count',
            query=query,
            cast_to=AuthPasskeyListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read(
        self,
        account_id: str,
        passkey_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPasskeyReadResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/accounts/{encode_path_param(account_id)}/passkeys'
                f'/{encode_path_param(passkey_id)}'
            ),
            cast_to=AuthPasskeyReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete(
        self,
        account_id: str,
        passkey_id: str,
        *,
        step_up_session_id: str | None = None,
        step_up_token: Credential | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPasskeyDeleteResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/accounts/{encode_path_param(account_id)}/passkeys'
                f'/{encode_path_param(passkey_id)}'
            ),
            cast_to=AuthPasskeyDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            declared_headers=(
                DeclaredHeader(
                    name='Step-Up-Session-ID',
                    argument='step_up_session_id',
                    value=step_up_session_id,
                    min_length=1,
                    max_length=48,
                ),
                DeclaredHeader(
                    name='Step-Up-Token',
                    argument='step_up_token',
                    value=step_up_token,
                    credential=True,
                    min_length=1,
                    max_length=256,
                    pattern='^[0-9a-f]+$',
                ),
            ),
        )
