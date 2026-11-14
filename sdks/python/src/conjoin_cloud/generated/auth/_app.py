from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthAppCreateRequest,
    AuthAppCreateResponse,
    AuthAppListCountQuery,
    AuthAppListCountResponse,
    AuthAppListItem,
    AuthAppListQuery,
    AuthAppReadResponse,
    AuthAppRotateSigningKeysResponse,
    AuthAppUpdateRequest,
    AuthAppUpdateResponse,
    AuthAppUpdateSettingsRequest,
    AuthAppUpdateSettingsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthAppsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: AuthAppListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthAppListItem]:
        return self._client.request(
            'GET',
            'auth/apps/',
            query=query,
            cast_to=Page[AuthAppListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: AuthAppCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppCreateResponse:
        return self._client.request(
            'POST',
            'auth/apps/',
            body=data,
            cast_to=AuthAppCreateResponse,
            request_options=request_options,
        )

    def list_count(
        self,
        query: AuthAppListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppListCountResponse:
        return self._client.request(
            'GET',
            'auth/apps/count',
            query=query,
            cast_to=AuthAppListCountResponse,
            request_options=request_options,
        )

    def read(
        self,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppReadResponse:
        return self._client.request(
            'GET',
            f'auth/apps/{encode_path_param(app_id)}',
            cast_to=AuthAppReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        app_id: str,
        data: AuthAppUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppUpdateResponse:
        return self._client.request(
            'PATCH',
            f'auth/apps/{encode_path_param(app_id)}',
            body=data,
            cast_to=AuthAppUpdateResponse,
            request_options=request_options,
        )

    def update_settings(
        self,
        app_id: str,
        data: AuthAppUpdateSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppUpdateSettingsResponse:
        return self._client.request(
            'PATCH',
            f'auth/apps/{encode_path_param(app_id)}/settings',
            body=data,
            cast_to=AuthAppUpdateSettingsResponse,
            request_options=request_options,
        )

    def rotate_signing_keys(
        self,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppRotateSigningKeysResponse:
        return self._client.request(
            'POST',
            f'auth/apps/{encode_path_param(app_id)}/signing-keys/rotate',
            cast_to=AuthAppRotateSigningKeysResponse,
            request_options=request_options,
            unwrap_data=False,
        )


class AsyncAuthAppsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: AuthAppListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthAppListItem]:
        return await self._client.request(
            'GET',
            'auth/apps/',
            query=query,
            cast_to=AsyncPage[AuthAppListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: AuthAppCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppCreateResponse:
        return await self._client.request(
            'POST',
            'auth/apps/',
            body=data,
            cast_to=AuthAppCreateResponse,
            request_options=request_options,
        )

    async def list_count(
        self,
        query: AuthAppListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppListCountResponse:
        return await self._client.request(
            'GET',
            'auth/apps/count',
            query=query,
            cast_to=AuthAppListCountResponse,
            request_options=request_options,
        )

    async def read(
        self,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppReadResponse:
        return await self._client.request(
            'GET',
            f'auth/apps/{encode_path_param(app_id)}',
            cast_to=AuthAppReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        app_id: str,
        data: AuthAppUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'auth/apps/{encode_path_param(app_id)}',
            body=data,
            cast_to=AuthAppUpdateResponse,
            request_options=request_options,
        )

    async def update_settings(
        self,
        app_id: str,
        data: AuthAppUpdateSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppUpdateSettingsResponse:
        return await self._client.request(
            'PATCH',
            f'auth/apps/{encode_path_param(app_id)}/settings',
            body=data,
            cast_to=AuthAppUpdateSettingsResponse,
            request_options=request_options,
        )

    async def rotate_signing_keys(
        self,
        app_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAppRotateSigningKeysResponse:
        return await self._client.request(
            'POST',
            f'auth/apps/{encode_path_param(app_id)}/signing-keys/rotate',
            cast_to=AuthAppRotateSigningKeysResponse,
            request_options=request_options,
            unwrap_data=False,
        )
