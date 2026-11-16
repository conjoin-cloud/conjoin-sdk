from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingMultisendCreateResponse,
    MessagingMultisendReadResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingMultisendsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingMultisendCreateResponse:
        return self._client.request(
            'POST',
            'messaging/multisend/send',
            body=data,
            cast_to=MessagingMultisendCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def read(
        self,
        message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingMultisendReadResponse:
        return self._client.request(
            'GET',
            f'messaging/multisend/{encode_path_param(message_id)}',
            cast_to=MessagingMultisendReadResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingMultisendsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingMultisendCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/multisend/send',
            body=data,
            cast_to=MessagingMultisendCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def read(
        self,
        message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingMultisendReadResponse:
        return await self._client.request(
            'GET',
            f'messaging/multisend/{encode_path_param(message_id)}',
            cast_to=MessagingMultisendReadResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
