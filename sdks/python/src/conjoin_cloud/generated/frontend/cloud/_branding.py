from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_PUBLISHABLE_KEY, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    CloudBrandingReadPublicProjectQuery,
    CloudBrandingReadPublicProjectResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudBrandingsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_public_project(
        self,
        query: CloudBrandingReadPublicProjectQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingReadPublicProjectResponse:
        return self._client.request(
            'GET',
            'cloud/client/branding/',
            query=query,
            cast_to=CloudBrandingReadPublicProjectResponse,
            request_options=request_options,
            default_auth=AUTH_PUBLISHABLE_KEY,
        )


class AsyncCloudBrandingsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_public_project(
        self,
        query: CloudBrandingReadPublicProjectQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudBrandingReadPublicProjectResponse:
        return await self._client.request(
            'GET',
            'cloud/client/branding/',
            query=query,
            cast_to=CloudBrandingReadPublicProjectResponse,
            request_options=request_options,
            default_auth=AUTH_PUBLISHABLE_KEY,
        )
