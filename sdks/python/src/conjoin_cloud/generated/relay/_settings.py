from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    RelaySettingsGetResponse,
    RelaySettingsRevealSigningSecretResponse,
    RelaySettingsRotateSigningSecretResponse,
    RelaySettingsUpdateRequest,
    RelaySettingsUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelaySettingsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def get(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsGetResponse:
        return self._client.request(
            'GET',
            'relay/settings/',
            cast_to=RelaySettingsGetResponse,
            request_options=request_options,
        )

    def update(
        self,
        data: RelaySettingsUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsUpdateResponse:
        return self._client.request(
            'PATCH',
            'relay/settings/',
            body=data,
            cast_to=RelaySettingsUpdateResponse,
            request_options=request_options,
        )

    def rotate_signing_secret(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsRotateSigningSecretResponse:
        return self._client.request(
            'POST',
            'relay/settings/signing-secret/rotate',
            cast_to=RelaySettingsRotateSigningSecretResponse,
            request_options=request_options,
        )

    def reveal_signing_secret(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsRevealSigningSecretResponse:
        return self._client.request(
            'GET',
            'relay/settings/signing-secret',
            cast_to=RelaySettingsRevealSigningSecretResponse,
            request_options=request_options,
        )


class AsyncRelaySettingsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def get(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsGetResponse:
        return await self._client.request(
            'GET',
            'relay/settings/',
            cast_to=RelaySettingsGetResponse,
            request_options=request_options,
        )

    async def update(
        self,
        data: RelaySettingsUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsUpdateResponse:
        return await self._client.request(
            'PATCH',
            'relay/settings/',
            body=data,
            cast_to=RelaySettingsUpdateResponse,
            request_options=request_options,
        )

    async def rotate_signing_secret(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsRotateSigningSecretResponse:
        return await self._client.request(
            'POST',
            'relay/settings/signing-secret/rotate',
            cast_to=RelaySettingsRotateSigningSecretResponse,
            request_options=request_options,
        )

    async def reveal_signing_secret(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySettingsRevealSigningSecretResponse:
        return await self._client.request(
            'GET',
            'relay/settings/signing-secret',
            cast_to=RelaySettingsRevealSigningSecretResponse,
            request_options=request_options,
        )
