from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._multipart import MultipartBody
from conjoin_cloud._request_options import AUTH_NONE, RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated.frontend._models import (
    AuthConnectionEnterpriseConfigureSsoPortalConnectionResponse,
    AuthConnectionEnterpriseImportSsoPortalMetadataResponse,
    AuthConnectionEnterpriseUpdateSsoPortalConnectionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AuthConnectionEnterprisesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def configure_sso_portal_connection(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseConfigureSsoPortalConnectionResponse:
        return self._client.request(
            'POST',
            'auth/portal/connections',
            body=data,
            cast_to=AuthConnectionEnterpriseConfigureSsoPortalConnectionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def update_sso_portal_connection(
        self,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseUpdateSsoPortalConnectionResponse:
        return self._client.request(
            'PATCH',
            f'auth/portal/connections/{encode_path_param(connection_id)}',
            body=data,
            cast_to=AuthConnectionEnterpriseUpdateSsoPortalConnectionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def import_sso_portal_metadata(
        self,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseImportSsoPortalMetadataResponse:
        return self._client.request(
            'POST',
            f'auth/portal/connections/{encode_path_param(connection_id)}/import-metadata',
            body=MultipartBody(data),
            cast_to=AuthConnectionEnterpriseImportSsoPortalMetadataResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    def read_sso_portal_provider_config(
        self,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'GET',
            f'auth/portal/connections/{encode_path_param(connection_id)}/service-provider-settings',
            request_options=request_options,
            default_auth=AUTH_NONE,
        )


class AsyncAuthConnectionEnterprisesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def configure_sso_portal_connection(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseConfigureSsoPortalConnectionResponse:
        return await self._client.request(
            'POST',
            'auth/portal/connections',
            body=data,
            cast_to=AuthConnectionEnterpriseConfigureSsoPortalConnectionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def update_sso_portal_connection(
        self,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseUpdateSsoPortalConnectionResponse:
        return await self._client.request(
            'PATCH',
            f'auth/portal/connections/{encode_path_param(connection_id)}',
            body=data,
            cast_to=AuthConnectionEnterpriseUpdateSsoPortalConnectionResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def import_sso_portal_metadata(
        self,
        connection_id: str,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AuthConnectionEnterpriseImportSsoPortalMetadataResponse:
        return await self._client.request(
            'POST',
            f'auth/portal/connections/{encode_path_param(connection_id)}/import-metadata',
            body=MultipartBody(data),
            cast_to=AuthConnectionEnterpriseImportSsoPortalMetadataResponse,
            request_options=request_options,
            default_auth=AUTH_NONE,
        )

    async def read_sso_portal_provider_config(
        self,
        connection_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'GET',
            f'auth/portal/connections/{encode_path_param(connection_id)}/service-provider-settings',
            request_options=request_options,
            default_auth=AUTH_NONE,
        )
