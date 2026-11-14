from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    AuthOrganizationDomainVerifySsoPortalDomainRequest,
    AuthOrganizationDomainVerifySsoPortalDomainResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthOrganizationDomainsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def verify_sso_portal_domain(
        self,
        data: AuthOrganizationDomainVerifySsoPortalDomainRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainVerifySsoPortalDomainResponse:
        return self._client.request(
            'POST',
            'auth/portal/domains',
            body=data,
            cast_to=AuthOrganizationDomainVerifySsoPortalDomainResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthOrganizationDomainsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def verify_sso_portal_domain(
        self,
        data: AuthOrganizationDomainVerifySsoPortalDomainRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthOrganizationDomainVerifySsoPortalDomainResponse:
        return await self._client.request(
            'POST',
            'auth/portal/domains',
            body=data,
            cast_to=AuthOrganizationDomainVerifySsoPortalDomainResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
