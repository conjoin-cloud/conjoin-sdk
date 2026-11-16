from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingSMSSenderCreateSmsSenderResponse,
    MessagingSMSSenderDeleteSmsSenderResponse,
    MessagingSMSSenderDisableSmsSenderResponse,
    MessagingSMSSenderEnableSmsSenderResponse,
    MessagingSMSSenderListSmsSenderResponse,
    MessagingSMSSenderTransferSmsSenderResponse,
    MessagingSMSSenderUpdateOneSmsSenderRequest,
    MessagingSMSSenderUpdateOneSmsSenderResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingSMSSendersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_sms_sender(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderCreateSmsSenderResponse:
        return self._client.request(
            'POST',
            'messaging/sms/senders/',
            body=data,
            cast_to=MessagingSMSSenderCreateSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def enable_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderEnableSmsSenderResponse:
        return self._client.request(
            'PATCH',
            f'messaging/sms/senders/{encode_path_param(sender_id)}/enable',
            cast_to=MessagingSMSSenderEnableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def disable_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDisableSmsSenderResponse:
        return self._client.request(
            'PATCH',
            f'messaging/sms/senders/{encode_path_param(sender_id)}/disable',
            cast_to=MessagingSMSSenderDisableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderListSmsSenderResponse:
        return self._client.request(
            'GET',
            f'messaging/sms/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingSMSSenderListSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def update_one_sms_sender(
        self,
        sender_id: str,
        data: MessagingSMSSenderUpdateOneSmsSenderRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderUpdateOneSmsSenderResponse:
        return self._client.request(
            'PATCH',
            f'messaging/sms/senders/{encode_path_param(sender_id)}',
            body=data,
            cast_to=MessagingSMSSenderUpdateOneSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDeleteSmsSenderResponse:
        return self._client.request(
            'DELETE',
            f'messaging/sms/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingSMSSenderDeleteSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def transfer_sms_sender(
        self,
        sender_id: str,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderTransferSmsSenderResponse:
        return self._client.request(
            'PATCH',
            (
                f'messaging/sms/senders/transfers/{encode_path_param(sender_id)}'
                f'/{encode_path_param(project_id)}'
            ),
            cast_to=MessagingSMSSenderTransferSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingSMSSendersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_sms_sender(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderCreateSmsSenderResponse:
        return await self._client.request(
            'POST',
            'messaging/sms/senders/',
            body=data,
            cast_to=MessagingSMSSenderCreateSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def enable_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderEnableSmsSenderResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/sms/senders/{encode_path_param(sender_id)}/enable',
            cast_to=MessagingSMSSenderEnableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def disable_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDisableSmsSenderResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/sms/senders/{encode_path_param(sender_id)}/disable',
            cast_to=MessagingSMSSenderDisableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderListSmsSenderResponse:
        return await self._client.request(
            'GET',
            f'messaging/sms/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingSMSSenderListSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def update_one_sms_sender(
        self,
        sender_id: str,
        data: MessagingSMSSenderUpdateOneSmsSenderRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderUpdateOneSmsSenderResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/sms/senders/{encode_path_param(sender_id)}',
            body=data,
            cast_to=MessagingSMSSenderUpdateOneSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_sms_sender(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDeleteSmsSenderResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/sms/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingSMSSenderDeleteSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def transfer_sms_sender(
        self,
        sender_id: str,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderTransferSmsSenderResponse:
        return await self._client.request(
            'PATCH',
            (
                f'messaging/sms/senders/transfers/{encode_path_param(sender_id)}'
                f'/{encode_path_param(project_id)}'
            ),
            cast_to=MessagingSMSSenderTransferSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
