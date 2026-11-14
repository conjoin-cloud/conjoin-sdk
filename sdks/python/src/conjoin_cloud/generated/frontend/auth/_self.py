from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated.frontend._models import (
    AuthSelfListOrganizationsCountQuery,
    AuthSelfListOrganizationsCountResponse,
    AuthSelfListOrganizationsItem,
    AuthSelfListOrganizationsQuery,
    AuthSelfListSessionsCountQuery,
    AuthSelfListSessionsCountResponse,
    AuthSelfListSessionsItem,
    AuthSelfListSessionsQuery,
    AuthSelfReadActiveOrganizationResponse,
    AuthSelfReadProfileResponse,
    AuthSelfRevokeSessionResponse,
    AuthSelfUpdateActiveOrganizationRequest,
    AuthSelfUpdateActiveOrganizationResponse,
    AuthSelfUpdateProfileRequest,
    AuthSelfUpdateProfileResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthSelvesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_organizations(
        self,
        query: AuthSelfListOrganizationsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthSelfListOrganizationsItem]:
        return self._client.request(
            'GET',
            'auth/self/organizations',
            query=query,
            cast_to=Page[AuthSelfListOrganizationsItem],
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def list_sessions(
        self,
        query: AuthSelfListSessionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthSelfListSessionsItem]:
        return self._client.request(
            'GET',
            'auth/self/sessions',
            query=query,
            cast_to=Page[AuthSelfListSessionsItem],
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def read_profile(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfReadProfileResponse:
        return self._client.request(
            'GET',
            'auth/self/',
            cast_to=AuthSelfReadProfileResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def update_profile(
        self,
        data: AuthSelfUpdateProfileRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfUpdateProfileResponse:
        return self._client.request(
            'PATCH',
            'auth/self/',
            body=data,
            cast_to=AuthSelfUpdateProfileResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def list_sessions_count(
        self,
        query: AuthSelfListSessionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfListSessionsCountResponse:
        return self._client.request(
            'GET',
            'auth/self/sessions/count',
            query=query,
            cast_to=AuthSelfListSessionsCountResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def revoke_session(
        self,
        session_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfRevokeSessionResponse:
        return self._client.request(
            'DELETE',
            f'auth/self/sessions/{encode_path_param(session_id)}',
            cast_to=AuthSelfRevokeSessionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def list_organizations_count(
        self,
        query: AuthSelfListOrganizationsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfListOrganizationsCountResponse:
        return self._client.request(
            'GET',
            'auth/self/organizations/count',
            query=query,
            cast_to=AuthSelfListOrganizationsCountResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def read_active_organization(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfReadActiveOrganizationResponse:
        return self._client.request(
            'GET',
            'auth/self/active-organization',
            cast_to=AuthSelfReadActiveOrganizationResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def update_active_organization(
        self,
        data: AuthSelfUpdateActiveOrganizationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfUpdateActiveOrganizationResponse:
        return self._client.request(
            'PATCH',
            'auth/self/active-organization',
            body=data,
            cast_to=AuthSelfUpdateActiveOrganizationResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthSelvesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_organizations(
        self,
        query: AuthSelfListOrganizationsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthSelfListOrganizationsItem]:
        return await self._client.request(
            'GET',
            'auth/self/organizations',
            query=query,
            cast_to=AsyncPage[AuthSelfListOrganizationsItem],
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def list_sessions(
        self,
        query: AuthSelfListSessionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthSelfListSessionsItem]:
        return await self._client.request(
            'GET',
            'auth/self/sessions',
            query=query,
            cast_to=AsyncPage[AuthSelfListSessionsItem],
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def read_profile(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfReadProfileResponse:
        return await self._client.request(
            'GET',
            'auth/self/',
            cast_to=AuthSelfReadProfileResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def update_profile(
        self,
        data: AuthSelfUpdateProfileRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfUpdateProfileResponse:
        return await self._client.request(
            'PATCH',
            'auth/self/',
            body=data,
            cast_to=AuthSelfUpdateProfileResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def list_sessions_count(
        self,
        query: AuthSelfListSessionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfListSessionsCountResponse:
        return await self._client.request(
            'GET',
            'auth/self/sessions/count',
            query=query,
            cast_to=AuthSelfListSessionsCountResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def revoke_session(
        self,
        session_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfRevokeSessionResponse:
        return await self._client.request(
            'DELETE',
            f'auth/self/sessions/{encode_path_param(session_id)}',
            cast_to=AuthSelfRevokeSessionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def list_organizations_count(
        self,
        query: AuthSelfListOrganizationsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfListOrganizationsCountResponse:
        return await self._client.request(
            'GET',
            'auth/self/organizations/count',
            query=query,
            cast_to=AuthSelfListOrganizationsCountResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def read_active_organization(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfReadActiveOrganizationResponse:
        return await self._client.request(
            'GET',
            'auth/self/active-organization',
            cast_to=AuthSelfReadActiveOrganizationResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def update_active_organization(
        self,
        data: AuthSelfUpdateActiveOrganizationRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSelfUpdateActiveOrganizationResponse:
        return await self._client.request(
            'PATCH',
            'auth/self/active-organization',
            body=data,
            cast_to=AuthSelfUpdateActiveOrganizationResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
