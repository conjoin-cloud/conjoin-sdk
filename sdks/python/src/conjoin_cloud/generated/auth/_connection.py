from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud.generated._models import (
    AuthConnectionListFirstPartyQuery,
    AuthConnectionListFirstPartyResponse,
    AuthConnectionUpsertFirstPartyRequest,
    AuthConnectionUpsertFirstPartyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthConnectionsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_first_party(
        self,
        query: AuthConnectionListFirstPartyQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionListFirstPartyResponse:
        return self._client.request(
            'GET',
            'auth/connection-configs/',
            query=query,
            cast_to=AuthConnectionListFirstPartyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def upsert_first_party(
        self,
        data: AuthConnectionUpsertFirstPartyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionUpsertFirstPartyResponse:
        return self._client.request(
            'POST',
            'auth/connection-configs/',
            body=data,
            cast_to=AuthConnectionUpsertFirstPartyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthConnectionsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_first_party(
        self,
        query: AuthConnectionListFirstPartyQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionListFirstPartyResponse:
        return await self._client.request(
            'GET',
            'auth/connection-configs/',
            query=query,
            cast_to=AuthConnectionListFirstPartyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def upsert_first_party(
        self,
        data: AuthConnectionUpsertFirstPartyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionUpsertFirstPartyResponse:
        return await self._client.request(
            'POST',
            'auth/connection-configs/',
            body=data,
            cast_to=AuthConnectionUpsertFirstPartyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
