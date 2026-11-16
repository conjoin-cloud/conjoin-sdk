from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudWebhookListItem,
    CloudWebhookListQuery,
    CloudWebhookReadCountQuery,
    CloudWebhookReadCountResponse,
    CloudWebhookReadEventsCountQuery,
    CloudWebhookReadEventsCountResponse,
    CloudWebhookReadEventsItem,
    CloudWebhookReadEventsQuery,
    CloudWebhookReadResponse,
    CloudWebhookRegisterRequest,
    CloudWebhookRegisterResponse,
    CloudWebhookUpdateRequest,
    CloudWebhookUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudWebhooksResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: CloudWebhookListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudWebhookListItem]:
        return self._client.request(
            'GET',
            'cloud/webhooks/',
            query=query,
            cast_to=Page[CloudWebhookListItem],
            request_options=request_options,
        )

    def register(
        self,
        data: CloudWebhookRegisterRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookRegisterResponse:
        return self._client.request(
            'POST',
            'cloud/webhooks/',
            body=data,
            cast_to=CloudWebhookRegisterResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_count(
        self,
        query: CloudWebhookReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookReadCountResponse:
        return self._client.request(
            'GET',
            'cloud/webhooks/count',
            query=query,
            cast_to=CloudWebhookReadCountResponse,
            request_options=request_options,
        )

    def read(
        self,
        webhook_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookReadResponse:
        return self._client.request(
            'GET',
            f'cloud/webhooks/{encode_path_param(webhook_id)}',
            cast_to=CloudWebhookReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        webhook_id: str,
        data: CloudWebhookUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookUpdateResponse:
        return self._client.request(
            'PATCH',
            f'cloud/webhooks/{encode_path_param(webhook_id)}',
            body=data,
            cast_to=CloudWebhookUpdateResponse,
            request_options=request_options,
        )

    def delete(
        self,
        webhook_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'DELETE',
            f'cloud/webhooks/{encode_path_param(webhook_id)}',
            request_options=request_options,
        )

    def read_events(
        self,
        query: CloudWebhookReadEventsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudWebhookReadEventsItem]:
        return self._client.request(
            'GET',
            'cloud/webhook-events/',
            query=query,
            cast_to=Page[CloudWebhookReadEventsItem],
            request_options=request_options,
        )

    def read_events_count(
        self,
        query: CloudWebhookReadEventsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookReadEventsCountResponse:
        return self._client.request(
            'GET',
            'cloud/webhook-events/count',
            query=query,
            cast_to=CloudWebhookReadEventsCountResponse,
            request_options=request_options,
        )


class AsyncCloudWebhooksResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: CloudWebhookListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudWebhookListItem]:
        return await self._client.request(
            'GET',
            'cloud/webhooks/',
            query=query,
            cast_to=AsyncPage[CloudWebhookListItem],
            request_options=request_options,
        )

    async def register(
        self,
        data: CloudWebhookRegisterRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookRegisterResponse:
        return await self._client.request(
            'POST',
            'cloud/webhooks/',
            body=data,
            cast_to=CloudWebhookRegisterResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_count(
        self,
        query: CloudWebhookReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookReadCountResponse:
        return await self._client.request(
            'GET',
            'cloud/webhooks/count',
            query=query,
            cast_to=CloudWebhookReadCountResponse,
            request_options=request_options,
        )

    async def read(
        self,
        webhook_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookReadResponse:
        return await self._client.request(
            'GET',
            f'cloud/webhooks/{encode_path_param(webhook_id)}',
            cast_to=CloudWebhookReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        webhook_id: str,
        data: CloudWebhookUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'cloud/webhooks/{encode_path_param(webhook_id)}',
            body=data,
            cast_to=CloudWebhookUpdateResponse,
            request_options=request_options,
        )

    async def delete(
        self,
        webhook_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'DELETE',
            f'cloud/webhooks/{encode_path_param(webhook_id)}',
            request_options=request_options,
        )

    async def read_events(
        self,
        query: CloudWebhookReadEventsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudWebhookReadEventsItem]:
        return await self._client.request(
            'GET',
            'cloud/webhook-events/',
            query=query,
            cast_to=AsyncPage[CloudWebhookReadEventsItem],
            request_options=request_options,
        )

    async def read_events_count(
        self,
        query: CloudWebhookReadEventsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudWebhookReadEventsCountResponse:
        return await self._client.request(
            'GET',
            'cloud/webhook-events/count',
            query=query,
            cast_to=CloudWebhookReadEventsCountResponse,
            request_options=request_options,
        )
