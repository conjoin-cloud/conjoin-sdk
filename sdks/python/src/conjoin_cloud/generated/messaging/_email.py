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
    MessagingEmailReadMessagesItem,
    MessagingEmailReadMessagesRequest,
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

    def send(
        self,
        data: MessagingEmailSendRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSendResponse:
        return self._client.request(
            'POST',
            'messaging/email/send',
            body=MultipartBody(wire_names(data, _SEND_BODY_ALIASES)),
            cast_to=MessagingEmailSendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def read_messages(
        self,
        message_id: str,
        data: MessagingEmailReadMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingEmailReadMessagesItem]:
        return self._client.request(
            'POST',
            f'messaging/email/messages/{encode_path_param(message_id)}',
            body=data,
            cast_to=Page[MessagingEmailReadMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def generate_summary(
        self,
        data: MessagingEmailGenerateSummaryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailGenerateSummaryResponse:
        return self._client.request(
            'POST',
            'messaging/email/summary',
            body=data,
            cast_to=MessagingEmailGenerateSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingEmailsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def send(
        self,
        data: MessagingEmailSendRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSendResponse:
        return await self._client.request(
            'POST',
            'messaging/email/send',
            body=MultipartBody(wire_names(data, _SEND_BODY_ALIASES)),
            cast_to=MessagingEmailSendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def read_messages(
        self,
        message_id: str,
        data: MessagingEmailReadMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingEmailReadMessagesItem]:
        return await self._client.request(
            'POST',
            f'messaging/email/messages/{encode_path_param(message_id)}',
            body=data,
            cast_to=AsyncPage[MessagingEmailReadMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def generate_summary(
        self,
        data: MessagingEmailGenerateSummaryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailGenerateSummaryResponse:
        return await self._client.request(
            'POST',
            'messaging/email/summary',
            body=data,
            cast_to=MessagingEmailGenerateSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
