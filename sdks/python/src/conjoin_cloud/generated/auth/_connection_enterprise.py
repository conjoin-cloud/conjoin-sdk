from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._multipart import MultipartBody
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AuthConnectionEnterpriseActivateEnterpriseConnectionSigningKeyResponse,
    AuthConnectionEnterpriseCancelEnterpriseConnectionSigningKeyResponse,
    AuthConnectionEnterpriseCreateEnterpriseConnectionResponse,
    AuthConnectionEnterpriseDeleteEnterpriseConnectionResponse,
    AuthConnectionEnterpriseDisableEnterpriseConnectionResponse,
    AuthConnectionEnterpriseEnableEnterpriseConnectionResponse,
    AuthConnectionEnterpriseImportEnterpriseSamlMetadataResponse,
    AuthConnectionEnterpriseListEnterpriseConnectionsCountQuery,
    AuthConnectionEnterpriseListEnterpriseConnectionsCountResponse,
    AuthConnectionEnterpriseListEnterpriseConnectionsItem,
    AuthConnectionEnterpriseListEnterpriseConnectionsQuery,
    AuthConnectionEnterpriseReadEnterpriseConnectionResponse,
    AuthConnectionEnterpriseRevokeEnterpriseConnectionSigningKeyResponse,
    AuthConnectionEnterpriseRotateEnterpriseConnectionSigningKeyResponse,
    AuthConnectionEnterpriseSyncEnterpriseSamlMetadataRequest,
    AuthConnectionEnterpriseSyncEnterpriseSamlMetadataResponse,
    AuthConnectionEnterpriseUpdateEnterpriseConnectionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthConnectionEnterprisesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_enterprise_connections(
        self,
        organization_id: str,
        query: AuthConnectionEnterpriseListEnterpriseConnectionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AuthConnectionEnterpriseListEnterpriseConnectionsItem]:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/connections/',
            query=query,
            cast_to=Page[AuthConnectionEnterpriseListEnterpriseConnectionsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def create_enterprise_connection(
        self,
        organization_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseCreateEnterpriseConnectionResponse:
        return self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/connections/',
            body=data,
            cast_to=AuthConnectionEnterpriseCreateEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def list_enterprise_connections_count(
        self,
        organization_id: str,
        query: AuthConnectionEnterpriseListEnterpriseConnectionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseListEnterpriseConnectionsCountResponse:
        return self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/connections/count',
            query=query,
            cast_to=AuthConnectionEnterpriseListEnterpriseConnectionsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def read_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseReadEnterpriseConnectionResponse:
        return self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}'
            ),
            cast_to=AuthConnectionEnterpriseReadEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def update_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseUpdateEnterpriseConnectionResponse:
        return self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}'
            ),
            body=data,
            cast_to=AuthConnectionEnterpriseUpdateEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def delete_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseDeleteEnterpriseConnectionResponse:
        return self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}'
            ),
            cast_to=AuthConnectionEnterpriseDeleteEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def enable_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseEnableEnterpriseConnectionResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/enable'
            ),
            cast_to=AuthConnectionEnterpriseEnableEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def disable_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseDisableEnterpriseConnectionResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/disable'
            ),
            cast_to=AuthConnectionEnterpriseDisableEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def rotate_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseRotateEnterpriseConnectionSigningKeyResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/rotate'
            ),
            cast_to=AuthConnectionEnterpriseRotateEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def activate_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseActivateEnterpriseConnectionSigningKeyResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/activate'
            ),
            cast_to=AuthConnectionEnterpriseActivateEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def cancel_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseCancelEnterpriseConnectionSigningKeyResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/cancel'
            ),
            cast_to=AuthConnectionEnterpriseCancelEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def revoke_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseRevokeEnterpriseConnectionSigningKeyResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/revoke'
            ),
            cast_to=AuthConnectionEnterpriseRevokeEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def read_enterprise_provider_settings(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/provider-settings'
            ),
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    def import_enterprise_saml_metadata(
        self,
        organization_id: str,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseImportEnterpriseSamlMetadataResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/import-metadata'
            ),
            body=MultipartBody(data),
            cast_to=AuthConnectionEnterpriseImportEnterpriseSamlMetadataResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    def sync_enterprise_saml_metadata(
        self,
        organization_id: str,
        connection_id: str,
        data: AuthConnectionEnterpriseSyncEnterpriseSamlMetadataRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseSyncEnterpriseSamlMetadataResponse:
        return self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/sync-metadata'
            ),
            body=data,
            cast_to=AuthConnectionEnterpriseSyncEnterpriseSamlMetadataResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )


class AsyncAuthConnectionEnterprisesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_enterprise_connections(
        self,
        organization_id: str,
        query: AuthConnectionEnterpriseListEnterpriseConnectionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AuthConnectionEnterpriseListEnterpriseConnectionsItem]:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/connections/',
            query=query,
            cast_to=AsyncPage[AuthConnectionEnterpriseListEnterpriseConnectionsItem],
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def create_enterprise_connection(
        self,
        organization_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseCreateEnterpriseConnectionResponse:
        return await self._client.request(
            'POST',
            f'auth/organizations/{encode_path_param(organization_id)}/connections/',
            body=data,
            cast_to=AuthConnectionEnterpriseCreateEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def list_enterprise_connections_count(
        self,
        organization_id: str,
        query: AuthConnectionEnterpriseListEnterpriseConnectionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseListEnterpriseConnectionsCountResponse:
        return await self._client.request(
            'GET',
            f'auth/organizations/{encode_path_param(organization_id)}/connections/count',
            query=query,
            cast_to=AuthConnectionEnterpriseListEnterpriseConnectionsCountResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def read_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseReadEnterpriseConnectionResponse:
        return await self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}'
            ),
            cast_to=AuthConnectionEnterpriseReadEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def update_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseUpdateEnterpriseConnectionResponse:
        return await self._client.request(
            'PATCH',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}'
            ),
            body=data,
            cast_to=AuthConnectionEnterpriseUpdateEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def delete_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseDeleteEnterpriseConnectionResponse:
        return await self._client.request(
            'DELETE',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}'
            ),
            cast_to=AuthConnectionEnterpriseDeleteEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def enable_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseEnableEnterpriseConnectionResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/enable'
            ),
            cast_to=AuthConnectionEnterpriseEnableEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def disable_enterprise_connection(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseDisableEnterpriseConnectionResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/disable'
            ),
            cast_to=AuthConnectionEnterpriseDisableEnterpriseConnectionResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def rotate_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseRotateEnterpriseConnectionSigningKeyResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/rotate'
            ),
            cast_to=AuthConnectionEnterpriseRotateEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def activate_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseActivateEnterpriseConnectionSigningKeyResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/activate'
            ),
            cast_to=AuthConnectionEnterpriseActivateEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def cancel_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseCancelEnterpriseConnectionSigningKeyResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/cancel'
            ),
            cast_to=AuthConnectionEnterpriseCancelEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def revoke_enterprise_connection_signing_key(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseRevokeEnterpriseConnectionSigningKeyResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/signing-keys/revoke'
            ),
            cast_to=AuthConnectionEnterpriseRevokeEnterpriseConnectionSigningKeyResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def read_enterprise_provider_settings(
        self,
        organization_id: str,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'GET',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/provider-settings'
            ),
            request_options=request_options,
            scopes=('auth_app_id',),
        )

    async def import_enterprise_saml_metadata(
        self,
        organization_id: str,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseImportEnterpriseSamlMetadataResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/import-metadata'
            ),
            body=MultipartBody(data),
            cast_to=AuthConnectionEnterpriseImportEnterpriseSamlMetadataResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )

    async def sync_enterprise_saml_metadata(
        self,
        organization_id: str,
        connection_id: str,
        data: AuthConnectionEnterpriseSyncEnterpriseSamlMetadataRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseSyncEnterpriseSamlMetadataResponse:
        return await self._client.request(
            'POST',
            (
                f'auth/organizations/{encode_path_param(organization_id)}/connections'
                f'/{encode_path_param(connection_id)}/sync-metadata'
            ),
            body=data,
            cast_to=AuthConnectionEnterpriseSyncEnterpriseSamlMetadataResponse,
            request_options=request_options,
            scopes=('auth_app_id',),
            accepts_idempotency_key=True,
        )
