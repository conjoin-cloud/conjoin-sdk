from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthPolicyCreateRequest,
    AuthPolicyCreateResponse,
    AuthPolicyDeleteResponse,
    AuthPolicyListCountQuery,
    AuthPolicyListCountResponse,
    AuthPolicyListItem,
    AuthPolicyListQuery,
    AuthPolicyReadResponse,
    AuthPolicyUpdateRequest,
    AuthPolicyUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthPoliciesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        organization_id: str,
        query: AuthPolicyListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthPolicyListItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/policies/',
            query=query,
            cast_to=Page[AuthPolicyListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create(
        self,
        organization_id: str,
        data: AuthPolicyCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyCreateResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/policies/',
            body=data,
            cast_to=AuthPolicyCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        organization_id: str,
        query: AuthPolicyListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyListCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/policies/count',
            query=query,
            cast_to=AuthPolicyListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read(
        self,
        organization_id: str,
        policy_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyReadResponse:
        return self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/policies'
                f'/{encode_path_param(policy_id)}'
            ),
            cast_to=AuthPolicyReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update(
        self,
        organization_id: str,
        policy_id: str,
        data: AuthPolicyUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyUpdateResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/policies'
                f'/{encode_path_param(policy_id)}'
            ),
            body=data,
            cast_to=AuthPolicyUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete(
        self,
        organization_id: str,
        policy_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyDeleteResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/policies'
                f'/{encode_path_param(policy_id)}'
            ),
            cast_to=AuthPolicyDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthPoliciesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        organization_id: str,
        query: AuthPolicyListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthPolicyListItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/policies/',
            query=query,
            cast_to=AsyncPage[AuthPolicyListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create(
        self,
        organization_id: str,
        data: AuthPolicyCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyCreateResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/policies/',
            body=data,
            cast_to=AuthPolicyCreateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        organization_id: str,
        query: AuthPolicyListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyListCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/policies/count',
            query=query,
            cast_to=AuthPolicyListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read(
        self,
        organization_id: str,
        policy_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyReadResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/policies'
                f'/{encode_path_param(policy_id)}'
            ),
            cast_to=AuthPolicyReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update(
        self,
        organization_id: str,
        policy_id: str,
        data: AuthPolicyUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyUpdateResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/policies'
                f'/{encode_path_param(policy_id)}'
            ),
            body=data,
            cast_to=AuthPolicyUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete(
        self,
        organization_id: str,
        policy_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthPolicyDeleteResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/policies'
                f'/{encode_path_param(policy_id)}'
            ),
            cast_to=AuthPolicyDeleteResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
