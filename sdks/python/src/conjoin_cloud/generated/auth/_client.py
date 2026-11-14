from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthClientCreateRequest,
    AuthClientCreateResponse,
    AuthClientListCountQuery,
    AuthClientListCountResponse,
    AuthClientListItem,
    AuthClientListQuery,
    AuthClientReadResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthClientsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: AuthClientListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthClientListItem]:
        return self._client.request(
            'GET',
            'auth/clients/',
            query=query,
            cast_to=Page[AuthClientListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create(
        self,
        data: AuthClientCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientCreateResponse:
        return self._client.request(
            'POST',
            'auth/clients/',
            body=data,
            cast_to=AuthClientCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        query: AuthClientListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientListCountResponse:
        return self._client.request(
            'GET',
            'auth/clients/count',
            query=query,
            cast_to=AuthClientListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read(
        self,
        client_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientReadResponse:
        return self._client.request(
            'GET',
            f'auth/clients/{encode_path_param(client_id)}',
            cast_to=AuthClientReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthClientsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: AuthClientListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthClientListItem]:
        return await self._client.request(
            'GET',
            'auth/clients/',
            query=query,
            cast_to=AsyncPage[AuthClientListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create(
        self,
        data: AuthClientCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientCreateResponse:
        return await self._client.request(
            'POST',
            'auth/clients/',
            body=data,
            cast_to=AuthClientCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        query: AuthClientListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientListCountResponse:
        return await self._client.request(
            'GET',
            'auth/clients/count',
            query=query,
            cast_to=AuthClientListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read(
        self,
        client_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthClientReadResponse:
        return await self._client.request(
            'GET',
            f'auth/clients/{encode_path_param(client_id)}',
            cast_to=AuthClientReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
