from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    AuthSSOPortalReadSsoPortalCatalogResponse,
    AuthSSOPortalReadSsoPortalContextResponse,
    AuthSSOPortalStartSsoPortalTestRequest,
    AuthSSOPortalStartSsoPortalTestResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthSSOPortalsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_sso_portal_context(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalReadSsoPortalContextResponse:
        return self._client.request(
            'GET',
            'auth/portal/',
            cast_to=AuthSSOPortalReadSsoPortalContextResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def read_sso_portal_catalog(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalReadSsoPortalCatalogResponse:
        return self._client.request(
            'GET',
            'auth/portal/providers',
            cast_to=AuthSSOPortalReadSsoPortalCatalogResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def start_sso_portal_test(
        self,
        data: AuthSSOPortalStartSsoPortalTestRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalStartSsoPortalTestResponse:
        return self._client.request(
            'POST',
            'auth/portal/test/start',
            body=data,
            cast_to=AuthSSOPortalStartSsoPortalTestResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthSSOPortalsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_sso_portal_context(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalReadSsoPortalContextResponse:
        return await self._client.request(
            'GET',
            'auth/portal/',
            cast_to=AuthSSOPortalReadSsoPortalContextResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def read_sso_portal_catalog(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalReadSsoPortalCatalogResponse:
        return await self._client.request(
            'GET',
            'auth/portal/providers',
            cast_to=AuthSSOPortalReadSsoPortalCatalogResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def start_sso_portal_test(
        self,
        data: AuthSSOPortalStartSsoPortalTestRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSSOPortalStartSsoPortalTestResponse:
        return await self._client.request(
            'POST',
            'auth/portal/test/start',
            body=data,
            cast_to=AuthSSOPortalStartSsoPortalTestResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
