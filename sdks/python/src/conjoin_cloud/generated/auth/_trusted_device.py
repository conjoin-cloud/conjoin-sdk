from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthTrustedDeviceListCountQuery,
    AuthTrustedDeviceListCountResponse,
    AuthTrustedDeviceListItem,
    AuthTrustedDeviceListQuery,
    AuthTrustedDeviceRevokeAllResponse,
    AuthTrustedDeviceRevokeResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthTrustedDevicesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        account_id: str,
        query: AuthTrustedDeviceListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthTrustedDeviceListItem]:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/trusted-devices/',
            query=query,
            cast_to=Page[AuthTrustedDeviceListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        account_id: str,
        query: AuthTrustedDeviceListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthTrustedDeviceListCountResponse:
        return self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/trusted-devices/count',
            query=query,
            cast_to=AuthTrustedDeviceListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def revoke_all(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthTrustedDeviceRevokeAllResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/trusted-devices/revoke-all',
            cast_to=AuthTrustedDeviceRevokeAllResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def revoke(
        self,
        account_id: str,
        trusted_device_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthTrustedDeviceRevokeResponse:
        return self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/trusted-devices'
                f'/{encode_path_param(trusted_device_id)}/revoke'
            ),
            cast_to=AuthTrustedDeviceRevokeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthTrustedDevicesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        account_id: str,
        query: AuthTrustedDeviceListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthTrustedDeviceListItem]:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/trusted-devices/',
            query=query,
            cast_to=AsyncPage[AuthTrustedDeviceListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        account_id: str,
        query: AuthTrustedDeviceListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthTrustedDeviceListCountResponse:
        return await self._client.request(
            'GET',
            f'auth/accounts/{encode_path_param(account_id)}/trusted-devices/count',
            query=query,
            cast_to=AuthTrustedDeviceListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def revoke_all(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthTrustedDeviceRevokeAllResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/trusted-devices/revoke-all',
            cast_to=AuthTrustedDeviceRevokeAllResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def revoke(
        self,
        account_id: str,
        trusted_device_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthTrustedDeviceRevokeResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/accounts/{encode_path_param(account_id)}/trusted-devices'
                f'/{encode_path_param(trusted_device_id)}/revoke'
            ),
            cast_to=AuthTrustedDeviceRevokeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
