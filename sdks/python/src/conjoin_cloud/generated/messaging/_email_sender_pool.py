from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingEmailSenderPoolAddEmailSendersToPoolRequest,
    MessagingEmailSenderPoolAddEmailSendersToPoolResponse,
    MessagingEmailSenderPoolCreateRequest,
    MessagingEmailSenderPoolCreateResponse,
    MessagingEmailSenderPoolDeleteResponse,
    MessagingEmailSenderPoolGetResponse,
    MessagingEmailSenderPoolListManyCountQuery,
    MessagingEmailSenderPoolListManyCountResponse,
    MessagingEmailSenderPoolListManyItem,
    MessagingEmailSenderPoolListManyQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingEmailSenderPoolsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_many(
        self,
        query: MessagingEmailSenderPoolListManyQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingEmailSenderPoolListManyItem]:
        return self._client.request(
            'GET',
            'messaging/email-sender-pools/',
            query=query,
            cast_to=Page[MessagingEmailSenderPoolListManyItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create(
        self,
        data: MessagingEmailSenderPoolCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolCreateResponse:
        return self._client.request(
            'POST',
            'messaging/email-sender-pools/',
            body=data,
            cast_to=MessagingEmailSenderPoolCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_many_count(
        self,
        query: MessagingEmailSenderPoolListManyCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolListManyCountResponse:
        return self._client.request(
            'GET',
            'messaging/email-sender-pools/count',
            query=query,
            cast_to=MessagingEmailSenderPoolListManyCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def add_email_senders_to_pool(
        self,
        email_sender_pool_id: str,
        data: MessagingEmailSenderPoolAddEmailSendersToPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolAddEmailSendersToPoolResponse:
        return self._client.request(
            'POST',
            f'messaging/email-sender-pools/{encode_path_param(email_sender_pool_id)}/senders',
            body=data,
            cast_to=MessagingEmailSenderPoolAddEmailSendersToPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def get(
        self,
        email_sender_pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolGetResponse:
        return self._client.request(
            'GET',
            f'messaging/email-sender-pools/{encode_path_param(email_sender_pool_id)}',
            cast_to=MessagingEmailSenderPoolGetResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete(
        self,
        email_sender_pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/email-sender-pools/{encode_path_param(email_sender_pool_id)}',
            cast_to=MessagingEmailSenderPoolDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingEmailSenderPoolsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_many(
        self,
        query: MessagingEmailSenderPoolListManyQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingEmailSenderPoolListManyItem]:
        return await self._client.request(
            'GET',
            'messaging/email-sender-pools/',
            query=query,
            cast_to=AsyncPage[MessagingEmailSenderPoolListManyItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create(
        self,
        data: MessagingEmailSenderPoolCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/email-sender-pools/',
            body=data,
            cast_to=MessagingEmailSenderPoolCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_many_count(
        self,
        query: MessagingEmailSenderPoolListManyCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolListManyCountResponse:
        return await self._client.request(
            'GET',
            'messaging/email-sender-pools/count',
            query=query,
            cast_to=MessagingEmailSenderPoolListManyCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def add_email_senders_to_pool(
        self,
        email_sender_pool_id: str,
        data: MessagingEmailSenderPoolAddEmailSendersToPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolAddEmailSendersToPoolResponse:
        return await self._client.request(
            'POST',
            f'messaging/email-sender-pools/{encode_path_param(email_sender_pool_id)}/senders',
            body=data,
            cast_to=MessagingEmailSenderPoolAddEmailSendersToPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def get(
        self,
        email_sender_pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolGetResponse:
        return await self._client.request(
            'GET',
            f'messaging/email-sender-pools/{encode_path_param(email_sender_pool_id)}',
            cast_to=MessagingEmailSenderPoolGetResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete(
        self,
        email_sender_pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderPoolDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/email-sender-pools/{encode_path_param(email_sender_pool_id)}',
            cast_to=MessagingEmailSenderPoolDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
