from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthSessionBulkRevokeAccountRequest,
    AuthSessionBulkRevokeAccountResponse,
    AuthSessionBulkRevokeClientRequest,
    AuthSessionBulkRevokeClientResponse,
    AuthSessionGetAnalyticsQuery,
    AuthSessionGetAnalyticsResponse,
    AuthSessionListCountQuery,
    AuthSessionListCountResponse,
    AuthSessionListItem,
    AuthSessionListQuery,
    AuthSessionReadResponse,
    AuthSessionReadStatsQuery,
    AuthSessionReadStatsResponse,
    AuthSessionRevokeAllForAccountResponse,
    AuthSessionRevokeResponse,
    AuthSessionUpdateRequest,
    AuthSessionUpdateResponse,
    AuthSessionValidateRequest,
    AuthSessionValidateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthSessionsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: AuthSessionListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthSessionListItem]:
        return self._client.request(
            'GET',
            'auth/sessions',
            query=query,
            cast_to=Page[AuthSessionListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def list_count(
        self,
        query: AuthSessionListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionListCountResponse:
        return self._client.request(
            'GET',
            'auth/sessions/count',
            query=query,
            cast_to=AuthSessionListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read_stats(
        self,
        query: AuthSessionReadStatsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionReadStatsResponse:
        return self._client.request(
            'GET',
            'auth/sessions/stats',
            query=query,
            cast_to=AuthSessionReadStatsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def get_analytics(
        self,
        query: AuthSessionGetAnalyticsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionGetAnalyticsResponse:
        return self._client.request(
            'GET',
            'auth/sessions/analytics',
            query=query,
            cast_to=AuthSessionGetAnalyticsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read(
        self,
        session_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionReadResponse:
        return self._client.request(
            'GET',
            f'auth/sessions/{encode_path_param(session_id)}',
            cast_to=AuthSessionReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update(
        self,
        session_id: str,
        data: AuthSessionUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionUpdateResponse:
        return self._client.request(
            'PATCH',
            f'auth/sessions/{encode_path_param(session_id)}',
            body=data,
            cast_to=AuthSessionUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def validate_(
        self,
        session_id: str,
        data: AuthSessionValidateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionValidateResponse:
        return self._client.request(
            'POST',
            f'auth/sessions/{encode_path_param(session_id)}/validate',
            body=data,
            cast_to=AuthSessionValidateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def revoke(
        self,
        session_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionRevokeResponse:
        return self._client.request(
            'POST',
            f'auth/sessions/{encode_path_param(session_id)}/revoke',
            cast_to=AuthSessionRevokeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def revoke_all_for_account(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionRevokeAllForAccountResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sessions/revoke-all',
            cast_to=AuthSessionRevokeAllForAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def bulk_revoke_account(
        self,
        account_id: str,
        data: AuthSessionBulkRevokeAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionBulkRevokeAccountResponse:
        return self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sessions/revoke',
            body=data,
            cast_to=AuthSessionBulkRevokeAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def bulk_revoke_client(
        self,
        client_id: str,
        data: AuthSessionBulkRevokeClientRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionBulkRevokeClientResponse:
        return self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sessions/revoke',
            body=data,
            cast_to=AuthSessionBulkRevokeClientResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthSessionsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: AuthSessionListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthSessionListItem]:
        return await self._client.request(
            'GET',
            'auth/sessions',
            query=query,
            cast_to=AsyncPage[AuthSessionListItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def list_count(
        self,
        query: AuthSessionListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionListCountResponse:
        return await self._client.request(
            'GET',
            'auth/sessions/count',
            query=query,
            cast_to=AuthSessionListCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read_stats(
        self,
        query: AuthSessionReadStatsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionReadStatsResponse:
        return await self._client.request(
            'GET',
            'auth/sessions/stats',
            query=query,
            cast_to=AuthSessionReadStatsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def get_analytics(
        self,
        query: AuthSessionGetAnalyticsQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionGetAnalyticsResponse:
        return await self._client.request(
            'GET',
            'auth/sessions/analytics',
            query=query,
            cast_to=AuthSessionGetAnalyticsResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read(
        self,
        session_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionReadResponse:
        return await self._client.request(
            'GET',
            f'auth/sessions/{encode_path_param(session_id)}',
            cast_to=AuthSessionReadResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update(
        self,
        session_id: str,
        data: AuthSessionUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'auth/sessions/{encode_path_param(session_id)}',
            body=data,
            cast_to=AuthSessionUpdateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def validate_(
        self,
        session_id: str,
        data: AuthSessionValidateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionValidateResponse:
        return await self._client.request(
            'POST',
            f'auth/sessions/{encode_path_param(session_id)}/validate',
            body=data,
            cast_to=AuthSessionValidateResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def revoke(
        self,
        session_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionRevokeResponse:
        return await self._client.request(
            'POST',
            f'auth/sessions/{encode_path_param(session_id)}/revoke',
            cast_to=AuthSessionRevokeResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def revoke_all_for_account(
        self,
        account_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionRevokeAllForAccountResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sessions/revoke-all',
            cast_to=AuthSessionRevokeAllForAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def bulk_revoke_account(
        self,
        account_id: str,
        data: AuthSessionBulkRevokeAccountRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionBulkRevokeAccountResponse:
        return await self._client.request(
            'POST',
            f'auth/accounts/{encode_path_param(account_id)}/sessions/revoke',
            body=data,
            cast_to=AuthSessionBulkRevokeAccountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def bulk_revoke_client(
        self,
        client_id: str,
        data: AuthSessionBulkRevokeClientRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthSessionBulkRevokeClientResponse:
        return await self._client.request(
            'POST',
            f'auth/clients/{encode_path_param(client_id)}/sessions/revoke',
            body=data,
            cast_to=AuthSessionBulkRevokeClientResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
