from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthOrganizationDomainCreateRequest,
    AuthOrganizationDomainCreateResponse,
    AuthOrganizationDomainDeleteResponse,
    AuthOrganizationDomainListCountQuery,
    AuthOrganizationDomainListCountResponse,
    AuthOrganizationDomainListItem,
    AuthOrganizationDomainListQuery,
    AuthOrganizationDomainVerifyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationDomainsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        organization_id: str,
        query: AuthOrganizationDomainListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthOrganizationDomainListItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/domains/',
            query=query,
            cast_to=Page[AuthOrganizationDomainListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create(
        self,
        organization_id: str,
        data: AuthOrganizationDomainCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainCreateResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/domains/',
            body=data,
            cast_to=AuthOrganizationDomainCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        organization_id: str,
        query: AuthOrganizationDomainListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainListCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/domains/count',
            query=query,
            cast_to=AuthOrganizationDomainListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def verify(
        self,
        organization_id: str,
        domain_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainVerifyResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/domains'
                f'/{encode_path_param(domain_id)}/verify'
            ),
            cast_to=AuthOrganizationDomainVerifyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete(
        self,
        organization_id: str,
        domain_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainDeleteResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/domains'
                f'/{encode_path_param(domain_id)}'
            ),
            cast_to=AuthOrganizationDomainDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthOrganizationDomainsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        organization_id: str,
        query: AuthOrganizationDomainListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthOrganizationDomainListItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/domains/',
            query=query,
            cast_to=AsyncPage[AuthOrganizationDomainListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create(
        self,
        organization_id: str,
        data: AuthOrganizationDomainCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainCreateResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/domains/',
            body=data,
            cast_to=AuthOrganizationDomainCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        organization_id: str,
        query: AuthOrganizationDomainListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainListCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/domains/count',
            query=query,
            cast_to=AuthOrganizationDomainListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def verify(
        self,
        organization_id: str,
        domain_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainVerifyResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/domains'
                f'/{encode_path_param(domain_id)}/verify'
            ),
            cast_to=AuthOrganizationDomainVerifyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete(
        self,
        organization_id: str,
        domain_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainDeleteResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/domains'
                f'/{encode_path_param(domain_id)}'
            ),
            cast_to=AuthOrganizationDomainDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
