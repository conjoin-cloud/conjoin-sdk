from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingEmailSenderPoolAddEmailSendersToPoolRequest,
    MessagingEmailSenderPoolAddEmailSendersToPoolResponse,
    MessagingEmailSenderPoolCreateRequest,
    MessagingEmailSenderPoolCreateResponse,
    MessagingEmailSenderPoolDeleteResponse,
    MessagingEmailSenderPoolGetResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingEmailSenderPoolsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create(
        self,
        data: MessagingEmailSenderPoolCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolCreateResponse:
        return self._client.request(
            'POST',
            'messaging/email/sender-pools/',
            body=data,
            cast_to=MessagingEmailSenderPoolCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def add_email_senders_to_pool(
        self,
        pool_id: str,
        data: MessagingEmailSenderPoolAddEmailSendersToPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolAddEmailSendersToPoolResponse:
        return self._client.request(
            'POST',
            f'messaging/email/sender-pools/{encode_path_param(pool_id)}/senders',
            body=data,
            cast_to=MessagingEmailSenderPoolAddEmailSendersToPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def get(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolGetResponse:
        return self._client.request(
            'GET',
            f'messaging/email/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingEmailSenderPoolGetResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/email/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingEmailSenderPoolDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingEmailSenderPoolsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create(
        self,
        data: MessagingEmailSenderPoolCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/email/sender-pools/',
            body=data,
            cast_to=MessagingEmailSenderPoolCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def add_email_senders_to_pool(
        self,
        pool_id: str,
        data: MessagingEmailSenderPoolAddEmailSendersToPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolAddEmailSendersToPoolResponse:
        return await self._client.request(
            'POST',
            f'messaging/email/sender-pools/{encode_path_param(pool_id)}/senders',
            body=data,
            cast_to=MessagingEmailSenderPoolAddEmailSendersToPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def get(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolGetResponse:
        return await self._client.request(
            'GET',
            f'messaging/email/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingEmailSenderPoolGetResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/email/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingEmailSenderPoolDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
