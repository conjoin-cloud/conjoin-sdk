from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudAPIKeyCreateApiKeyRequest,
    CloudAPIKeyReadApiKeysCountQuery,
    CloudAPIKeyReadApiKeysCountResponse,
    CloudAPIKeyReadApiKeysItem,
    CloudAPIKeyReadApiKeysQuery,
    CloudAPIKeyRegenerateApiKeyRequest,
    CloudAPIKeyUpdateApiKeyRequest,
    CloudAPIKeyUpdateApiKeyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudAPIKeysResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_api_keys(
        self,
        query: CloudAPIKeyReadApiKeysQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudAPIKeyReadApiKeysItem]:
        return self._client.request(
            'GET',
            'cloud/api-keys/',
            query=query,
            cast_to=Page[CloudAPIKeyReadApiKeysItem],
            request_options=request_options,
        )

    def create_api_key(
        self,
        data: CloudAPIKeyCreateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            'cloud/api-keys/',
            body=data,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_api_keys_count(
        self,
        query: CloudAPIKeyReadApiKeysCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAPIKeyReadApiKeysCountResponse:
        return self._client.request(
            'GET',
            'cloud/api-keys/count',
            query=query,
            cast_to=CloudAPIKeyReadApiKeysCountResponse,
            request_options=request_options,
        )

    def regenerate_api_key(
        self,
        api_key_id: str,
        data: CloudAPIKeyRegenerateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            f'cloud/api-keys/{encode_path_param(api_key_id)}/regenerate',
            body=data,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def update_api_key(
        self,
        api_key_id: str,
        data: CloudAPIKeyUpdateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAPIKeyUpdateApiKeyResponse:
        return self._client.request(
            'PATCH',
            f'cloud/api-keys/{encode_path_param(api_key_id)}',
            body=data,
            cast_to=CloudAPIKeyUpdateApiKeyResponse,
            request_options=request_options,
        )

    def delete_api_key(
        self,
        api_key_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'DELETE',
            f'cloud/api-keys/{encode_path_param(api_key_id)}',
            request_options=request_options,
        )


class AsyncCloudAPIKeysResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_api_keys(
        self,
        query: CloudAPIKeyReadApiKeysQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudAPIKeyReadApiKeysItem]:
        return await self._client.request(
            'GET',
            'cloud/api-keys/',
            query=query,
            cast_to=AsyncPage[CloudAPIKeyReadApiKeysItem],
            request_options=request_options,
        )

    async def create_api_key(
        self,
        data: CloudAPIKeyCreateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            'cloud/api-keys/',
            body=data,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_api_keys_count(
        self,
        query: CloudAPIKeyReadApiKeysCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAPIKeyReadApiKeysCountResponse:
        return await self._client.request(
            'GET',
            'cloud/api-keys/count',
            query=query,
            cast_to=CloudAPIKeyReadApiKeysCountResponse,
            request_options=request_options,
        )

    async def regenerate_api_key(
        self,
        api_key_id: str,
        data: CloudAPIKeyRegenerateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            f'cloud/api-keys/{encode_path_param(api_key_id)}/regenerate',
            body=data,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def update_api_key(
        self,
        api_key_id: str,
        data: CloudAPIKeyUpdateApiKeyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudAPIKeyUpdateApiKeyResponse:
        return await self._client.request(
            'PATCH',
            f'cloud/api-keys/{encode_path_param(api_key_id)}',
            body=data,
            cast_to=CloudAPIKeyUpdateApiKeyResponse,
            request_options=request_options,
        )

    async def delete_api_key(
        self,
        api_key_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'DELETE',
            f'cloud/api-keys/{encode_path_param(api_key_id)}',
            request_options=request_options,
        )
