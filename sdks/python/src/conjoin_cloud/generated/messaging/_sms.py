from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud._wire import wire_names
from conjoin_cloud.generated._models import (
    MessagingSMSGenerateSmsSummaryRequest,
    MessagingSMSGenerateSmsSummaryResponse,
    MessagingSMSListSmsMessagesCountQuery,
    MessagingSMSListSmsMessagesCountResponse,
    MessagingSMSListSmsMessagesItem,
    MessagingSMSListSmsMessagesQuery,
    MessagingSMSReadSmsMessageResponse,
    MessagingSMSSendSmsRequest,
    MessagingSMSSendSmsResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


_SEND_SMS_BODY_ALIASES = {
    'from_': 'from',
}


class MessagingSMsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_sms_messages(
        self,
        query: MessagingSMSListSmsMessagesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingSMSListSmsMessagesItem]:
        return self._client.request(
            'GET',
            'messaging/sms-messages/',
            query=query,
            cast_to=Page[MessagingSMSListSmsMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def send_sms(
        self,
        data: MessagingSMSSendSmsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSendSmsResponse:
        return self._client.request(
            'POST',
            'messaging/sms-messages/',
            body=wire_names(data, _SEND_SMS_BODY_ALIASES),
            cast_to=MessagingSMSSendSmsResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_sms_messages_count(
        self,
        query: MessagingSMSListSmsMessagesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSListSmsMessagesCountResponse:
        return self._client.request(
            'GET',
            'messaging/sms-messages/count',
            query=query,
            cast_to=MessagingSMSListSmsMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def read_sms_message(
        self,
        sms_message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSReadSmsMessageResponse:
        return self._client.request(
            'GET',
            f'messaging/sms-messages/{encode_path_param(sms_message_id)}',
            cast_to=MessagingSMSReadSmsMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def generate_sms_summary(
        self,
        data: MessagingSMSGenerateSmsSummaryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSGenerateSmsSummaryResponse:
        return self._client.request(
            'POST',
            'messaging/sms-message-previews/',
            body=data,
            cast_to=MessagingSMSGenerateSmsSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingSMsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_sms_messages(
        self,
        query: MessagingSMSListSmsMessagesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingSMSListSmsMessagesItem]:
        return await self._client.request(
            'GET',
            'messaging/sms-messages/',
            query=query,
            cast_to=AsyncPage[MessagingSMSListSmsMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def send_sms(
        self,
        data: MessagingSMSSendSmsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSendSmsResponse:
        return await self._client.request(
            'POST',
            'messaging/sms-messages/',
            body=wire_names(data, _SEND_SMS_BODY_ALIASES),
            cast_to=MessagingSMSSendSmsResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_sms_messages_count(
        self,
        query: MessagingSMSListSmsMessagesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSListSmsMessagesCountResponse:
        return await self._client.request(
            'GET',
            'messaging/sms-messages/count',
            query=query,
            cast_to=MessagingSMSListSmsMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def read_sms_message(
        self,
        sms_message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSReadSmsMessageResponse:
        return await self._client.request(
            'GET',
            f'messaging/sms-messages/{encode_path_param(sms_message_id)}',
            cast_to=MessagingSMSReadSmsMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def generate_sms_summary(
        self,
        data: MessagingSMSGenerateSmsSummaryRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSGenerateSmsSummaryResponse:
        return await self._client.request(
            'POST',
            'messaging/sms-message-previews/',
            body=data,
            cast_to=MessagingSMSGenerateSmsSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
