from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud._wire import wire_names
from conjoin_cloud.generated._models import (
    MessagingSMSGetSmsSummaryResponse,
    MessagingSMSReadSmsMessagesItem,
    MessagingSMSReadSmsMessagesRequest,
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

    def send_sms(
        self,
        data: MessagingSMSSendSmsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSendSmsResponse:
        return self._client.request(
            'POST',
            'messaging/sms/send',
            body=wire_names(data, _SEND_SMS_BODY_ALIASES),
            cast_to=MessagingSMSSendSmsResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def read_sms_messages(
        self,
        message_id: str,
        data: MessagingSMSReadSmsMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingSMSReadSmsMessagesItem]:
        return self._client.request(
            'POST',
            f'messaging/sms/messages/{encode_path_param(message_id)}',
            body=data,
            cast_to=Page[MessagingSMSReadSmsMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def get_sms_summary(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSGetSmsSummaryResponse:
        return self._client.request(
            'GET',
            'messaging/sms/summary',
            cast_to=MessagingSMSGetSmsSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingSMsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def send_sms(
        self,
        data: MessagingSMSSendSmsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSendSmsResponse:
        return await self._client.request(
            'POST',
            'messaging/sms/send',
            body=wire_names(data, _SEND_SMS_BODY_ALIASES),
            cast_to=MessagingSMSSendSmsResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def read_sms_messages(
        self,
        message_id: str,
        data: MessagingSMSReadSmsMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingSMSReadSmsMessagesItem]:
        return await self._client.request(
            'POST',
            f'messaging/sms/messages/{encode_path_param(message_id)}',
            body=data,
            cast_to=AsyncPage[MessagingSMSReadSmsMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def get_sms_summary(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSGetSmsSummaryResponse:
        return await self._client.request(
            'GET',
            'messaging/sms/summary',
            cast_to=MessagingSMSGetSmsSummaryResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
