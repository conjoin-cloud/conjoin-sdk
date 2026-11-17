from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingEmailSenderCreateResponse,
    MessagingEmailSenderDeleteResponse,
    MessagingEmailSenderDisableResponse,
    MessagingEmailSenderEnableResponse,
    MessagingEmailSenderListManyCountQuery,
    MessagingEmailSenderListManyCountResponse,
    MessagingEmailSenderListManyItem,
    MessagingEmailSenderListManyQuery,
    MessagingEmailSenderReadResponse,
    MessagingEmailSenderTransferRequest,
    MessagingEmailSenderTransferResponse,
    MessagingEmailSenderVerifyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingEmailSendersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_many(
        self,
        query: MessagingEmailSenderListManyQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingEmailSenderListManyItem]:
        return self._client.request(
            'GET',
            'messaging/email-senders/',
            query=query,
            cast_to=Page[MessagingEmailSenderListManyItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderCreateResponse:
        return self._client.request(
            'POST',
            'messaging/email-senders/',
            body=data,
            cast_to=MessagingEmailSenderCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_many_count(
        self,
        query: MessagingEmailSenderListManyCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderListManyCountResponse:
        return self._client.request(
            'GET',
            'messaging/email-senders/count',
            query=query,
            cast_to=MessagingEmailSenderListManyCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def read(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderReadResponse:
        return self._client.request(
            'GET',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}',
            cast_to=MessagingEmailSenderReadResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}',
            cast_to=MessagingEmailSenderDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def verify(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderVerifyResponse:
        return self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/verify',
            cast_to=MessagingEmailSenderVerifyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def enable(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderEnableResponse:
        return self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/enable',
            cast_to=MessagingEmailSenderEnableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def disable(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDisableResponse:
        return self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/disable',
            cast_to=MessagingEmailSenderDisableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def transfer(
        self,
        email_sender_id: str,
        data: MessagingEmailSenderTransferRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderTransferResponse:
        return self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/transfer',
            body=data,
            cast_to=MessagingEmailSenderTransferResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingEmailSendersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_many(
        self,
        query: MessagingEmailSenderListManyQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingEmailSenderListManyItem]:
        return await self._client.request(
            'GET',
            'messaging/email-senders/',
            query=query,
            cast_to=AsyncPage[MessagingEmailSenderListManyItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/email-senders/',
            body=data,
            cast_to=MessagingEmailSenderCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_many_count(
        self,
        query: MessagingEmailSenderListManyCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderListManyCountResponse:
        return await self._client.request(
            'GET',
            'messaging/email-senders/count',
            query=query,
            cast_to=MessagingEmailSenderListManyCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def read(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderReadResponse:
        return await self._client.request(
            'GET',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}',
            cast_to=MessagingEmailSenderReadResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}',
            cast_to=MessagingEmailSenderDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def verify(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderVerifyResponse:
        return await self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/verify',
            cast_to=MessagingEmailSenderVerifyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def enable(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderEnableResponse:
        return await self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/enable',
            cast_to=MessagingEmailSenderEnableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def disable(
        self,
        email_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDisableResponse:
        return await self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/disable',
            cast_to=MessagingEmailSenderDisableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def transfer(
        self,
        email_sender_id: str,
        data: MessagingEmailSenderTransferRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderTransferResponse:
        return await self._client.request(
            'POST',
            f'messaging/email-senders/{encode_path_param(email_sender_id)}/transfer',
            body=data,
            cast_to=MessagingEmailSenderTransferResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
