from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudPublishableKeyListCountQuery,
    CloudPublishableKeyListCountResponse,
    CloudPublishableKeyListItem,
    CloudPublishableKeyListQuery,
    CloudPublishableKeyUpdateRequest,
    CloudPublishableKeyUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudPublishableKeysResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: CloudPublishableKeyListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudPublishableKeyListItem]:
        return self._client.request(
            'GET',
            'cloud/publishable-keys/',
            query=query,
            cast_to=Page[CloudPublishableKeyListItem],
            request_options=request_options,
        )

    def create(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            'cloud/publishable-keys/',
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: CloudPublishableKeyListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPublishableKeyListCountResponse:
        return self._client.request(
            'GET',
            'cloud/publishable-keys/count',
            query=query,
            cast_to=CloudPublishableKeyListCountResponse,
            request_options=request_options,
        )

    def rotate(
        self,
        publishable_key_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            f'cloud/publishable-keys/{encode_path_param(publishable_key_id)}/rotate',
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def update(
        self,
        publishable_key_id: str,
        data: CloudPublishableKeyUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPublishableKeyUpdateResponse:
        return self._client.request(
            'PATCH',
            f'cloud/publishable-keys/{encode_path_param(publishable_key_id)}',
            body=data,
            cast_to=CloudPublishableKeyUpdateResponse,
            request_options=request_options,
        )

    def revoke(
        self,
        publishable_key_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'DELETE',
            f'cloud/publishable-keys/{encode_path_param(publishable_key_id)}',
            request_options=request_options,
        )


class AsyncCloudPublishableKeysResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: CloudPublishableKeyListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudPublishableKeyListItem]:
        return await self._client.request(
            'GET',
            'cloud/publishable-keys/',
            query=query,
            cast_to=AsyncPage[CloudPublishableKeyListItem],
            request_options=request_options,
        )

    async def create(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            'cloud/publishable-keys/',
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: CloudPublishableKeyListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPublishableKeyListCountResponse:
        return await self._client.request(
            'GET',
            'cloud/publishable-keys/count',
            query=query,
            cast_to=CloudPublishableKeyListCountResponse,
            request_options=request_options,
        )

    async def rotate(
        self,
        publishable_key_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            f'cloud/publishable-keys/{encode_path_param(publishable_key_id)}/rotate',
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def update(
        self,
        publishable_key_id: str,
        data: CloudPublishableKeyUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPublishableKeyUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'cloud/publishable-keys/{encode_path_param(publishable_key_id)}',
            body=data,
            cast_to=CloudPublishableKeyUpdateResponse,
            request_options=request_options,
        )

    async def revoke(
        self,
        publishable_key_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'DELETE',
            f'cloud/publishable-keys/{encode_path_param(publishable_key_id)}',
            request_options=request_options,
        )
