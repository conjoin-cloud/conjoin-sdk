from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthAuthorizationAuthorizeActionRequest,
    AuthAuthorizationAuthorizeActionResponse,
    AuthAuthorizationCheckRoleRequest,
    AuthAuthorizationCheckRoleResponse,
    AuthAuthorizationReadEffectivePermissionsQuery,
    AuthAuthorizationReadEffectivePermissionsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthAuthorizationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def authorize_action(
        self,
        organization_id: str,
        data: AuthAuthorizationAuthorizeActionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAuthorizationAuthorizeActionResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/authorize',
            body=data,
            cast_to=AuthAuthorizationAuthorizeActionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def check_role(
        self,
        organization_id: str,
        data: AuthAuthorizationCheckRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAuthorizationCheckRoleResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/check-role',
            body=data,
            cast_to=AuthAuthorizationCheckRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def read_effective_permissions(
        self,
        organization_id: str,
        query: AuthAuthorizationReadEffectivePermissionsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAuthorizationReadEffectivePermissionsResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/effective-permissions',
            query=query,
            cast_to=AuthAuthorizationReadEffectivePermissionsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthAuthorizationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def authorize_action(
        self,
        organization_id: str,
        data: AuthAuthorizationAuthorizeActionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAuthorizationAuthorizeActionResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/authorize',
            body=data,
            cast_to=AuthAuthorizationAuthorizeActionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def check_role(
        self,
        organization_id: str,
        data: AuthAuthorizationCheckRoleRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAuthorizationCheckRoleResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/check-role',
            body=data,
            cast_to=AuthAuthorizationCheckRoleResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def read_effective_permissions(
        self,
        organization_id: str,
        query: AuthAuthorizationReadEffectivePermissionsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthAuthorizationReadEffectivePermissionsResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/effective-permissions',
            query=query,
            cast_to=AuthAuthorizationReadEffectivePermissionsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
