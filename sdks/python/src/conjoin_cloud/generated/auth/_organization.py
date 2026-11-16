from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationCreateRequest,
    AuthOrganizationCreateResponse,
    AuthOrganizationDeleteQuery,
    AuthOrganizationDeleteResponse,
    AuthOrganizationListCountQuery,
    AuthOrganizationListCountResponse,
    AuthOrganizationListItem,
    AuthOrganizationListQuery,
    AuthOrganizationReadResponse,
    AuthOrganizationUpdateRequest,
    AuthOrganizationUpdateResponse,
    AuthOrganizationUpdateSettingsRequest,
    AuthOrganizationUpdateSettingsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: AuthOrganizationListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationListItem]:
        return self._client.request(
            'GET',
            'auth/organizations/',
            query=query,
            cast_to=Page[AuthOrganizationListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create(
        self,
        data: AuthOrganizationCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationCreateResponse:
        return self._client.request(
            'POST',
            'auth/organizations/',
            body=data,
            cast_to=AuthOrganizationCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: AuthOrganizationListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationListCountResponse:
        return self._client.request(
            'GET',
            'auth/organizations/count',
            query=query,
            cast_to=AuthOrganizationListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationReadResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}',
            cast_to=AuthOrganizationReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update(
        self,
        organization_id: str,
        data: AuthOrganizationUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationUpdateResponse:
        return self._client.request(
            'PATCH',
            f'auth/organizations/{encode_path_param(organization_id)}',
            body=data,
            cast_to=AuthOrganizationUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete(
        self,
        organization_id: str,
        query: AuthOrganizationDeleteQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDeleteResponse:
        return self._client.request(
            'DELETE',
            f'auth/organizations/{encode_path_param(organization_id)}',
            query=query,
            cast_to=AuthOrganizationDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_settings(
        self,
        organization_id: str,
        data: AuthOrganizationUpdateSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationUpdateSettingsResponse:
        return self._client.request(
            'PATCH',
            f'auth/organizations/{encode_path_param(organization_id)}/settings',
            body=data,
            cast_to=AuthOrganizationUpdateSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthOrganizationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: AuthOrganizationListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationListItem]:
        return await self._client.request(
            'GET',
            'auth/organizations/',
            query=query,
            cast_to=AsyncPage[AuthOrganizationListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create(
        self,
        data: AuthOrganizationCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationCreateResponse:
        return await self._client.request(
            'POST',
            'auth/organizations/',
            body=data,
            cast_to=AuthOrganizationCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: AuthOrganizationListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationListCountResponse:
        return await self._client.request(
            'GET',
            'auth/organizations/count',
            query=query,
            cast_to=AuthOrganizationListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read(
        self,
        organization_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationReadResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}',
            cast_to=AuthOrganizationReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update(
        self,
        organization_id: str,
        data: AuthOrganizationUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'auth/organizations/{encode_path_param(organization_id)}',
            body=data,
            cast_to=AuthOrganizationUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete(
        self,
        organization_id: str,
        query: AuthOrganizationDeleteQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'auth/organizations/{encode_path_param(organization_id)}',
            query=query,
            cast_to=AuthOrganizationDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_settings(
        self,
        organization_id: str,
        data: AuthOrganizationUpdateSettingsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationUpdateSettingsResponse:
        return await self._client.request(
            'PATCH',
            f'auth/organizations/{encode_path_param(organization_id)}/settings',
            body=data,
            cast_to=AuthOrganizationUpdateSettingsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
