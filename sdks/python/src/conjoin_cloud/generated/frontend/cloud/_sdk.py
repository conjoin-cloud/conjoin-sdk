from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import AUTH_PUBLISHABLE_KEY, RequestOptions
from conjoin_cloud.generated.frontend._models import (
    CloudSDKReadSdkSettingsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudSDKsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_sdk_settings(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSDKReadSdkSettingsResponse:
        return self._client.request(
            'GET',
            'cloud/client/settings/',
            cast_to=CloudSDKReadSdkSettingsResponse,
            request_options=request_options,
            default_auth=AUTH_PUBLISHABLE_KEY,
        )


class AsyncCloudSDKsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_sdk_settings(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudSDKReadSdkSettingsResponse:
        return await self._client.request(
            'GET',
            'cloud/client/settings/',
            cast_to=CloudSDKReadSdkSettingsResponse,
            request_options=request_options,
            default_auth=AUTH_PUBLISHABLE_KEY,
        )
