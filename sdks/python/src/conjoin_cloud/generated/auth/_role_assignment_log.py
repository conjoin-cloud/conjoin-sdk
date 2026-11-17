from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthRoleAssignmentLogListCountQuery,
    AuthRoleAssignmentLogListCountResponse,
    AuthRoleAssignmentLogListItem,
    AuthRoleAssignmentLogListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthRoleAssignmentLogsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        organization_id: str,
        query: AuthRoleAssignmentLogListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthRoleAssignmentLogListItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/role-assignment-logs/',
            query=query,
            cast_to=Page[AuthRoleAssignmentLogListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        organization_id: str,
        query: AuthRoleAssignmentLogListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthRoleAssignmentLogListCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/role-assignment-logs/count',
            query=query,
            cast_to=AuthRoleAssignmentLogListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )


class AsyncAuthRoleAssignmentLogsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        organization_id: str,
        query: AuthRoleAssignmentLogListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthRoleAssignmentLogListItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/role-assignment-logs/',
            query=query,
            cast_to=AsyncPage[AuthRoleAssignmentLogListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        organization_id: str,
        query: AuthRoleAssignmentLogListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthRoleAssignmentLogListCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/role-assignment-logs/count',
            query=query,
            cast_to=AuthRoleAssignmentLogListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )
