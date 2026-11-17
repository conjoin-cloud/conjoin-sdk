from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._multipart import MultipartBody
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud._wire import wire_names
from conjoin_cloud.generated._models import (
    MessagingEmailGenerateSummaryRequest,
    MessagingEmailGenerateSummaryResponse,
    MessagingEmailListMessagesCountQuery,
    MessagingEmailListMessagesCountResponse,
    MessagingEmailListMessagesItem,
    MessagingEmailListMessagesQuery,
    MessagingEmailReadMessageResponse,
    MessagingEmailSendRequest,
    MessagingEmailSendResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


_SEND_BODY_ALIASES = {
    'from_': 'from',
}


class MessagingEmailsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_messages(
        self,
        query: MessagingEmailListMessagesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingEmailListMessagesItem]:
        return self._client.request(
            'GET',
            'messaging/email-messages/',
            query=query,
            cast_to=Page[MessagingEmailListMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def send(
        self,
        data: MessagingEmailSendRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSendResponse:
        return self._client.request(
            'POST',
            'messaging/email-messages/',
            body=MultipartBody(wire_names(data, _SEND_BODY_ALIASES)),
            cast_to=MessagingEmailSendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_messages_count(
        self,
        query: MessagingEmailListMessagesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailListMessagesCountResponse:
        return self._client.request(
            'GET',
            'messaging/email-messages/count',
            query=query,
            cast_to=MessagingEmailListMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def read_message(
        self,
        email_message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailReadMessageResponse:
        return self._client.request(
            'GET',
            f'messaging/email-messages/{encode_path_param(email_message_id)}',
            cast_to=MessagingEmailReadMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def generate_summary(
        self,
        data: MessagingEmailGenerateSummaryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailGenerateSummaryResponse:
        return self._client.request(
            'POST',
            'messaging/email-message-previews/',
            body=data,
            cast_to=MessagingEmailGenerateSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingEmailsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_messages(
        self,
        query: MessagingEmailListMessagesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingEmailListMessagesItem]:
        return await self._client.request(
            'GET',
            'messaging/email-messages/',
            query=query,
            cast_to=AsyncPage[MessagingEmailListMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def send(
        self,
        data: MessagingEmailSendRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSendResponse:
        return await self._client.request(
            'POST',
            'messaging/email-messages/',
            body=MultipartBody(wire_names(data, _SEND_BODY_ALIASES)),
            cast_to=MessagingEmailSendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_messages_count(
        self,
        query: MessagingEmailListMessagesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailListMessagesCountResponse:
        return await self._client.request(
            'GET',
            'messaging/email-messages/count',
            query=query,
            cast_to=MessagingEmailListMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def read_message(
        self,
        email_message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailReadMessageResponse:
        return await self._client.request(
            'GET',
            f'messaging/email-messages/{encode_path_param(email_message_id)}',
            cast_to=MessagingEmailReadMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def generate_summary(
        self,
        data: MessagingEmailGenerateSummaryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailGenerateSummaryResponse:
        return await self._client.request(
            'POST',
            'messaging/email-message-previews/',
            body=data,
            cast_to=MessagingEmailGenerateSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
