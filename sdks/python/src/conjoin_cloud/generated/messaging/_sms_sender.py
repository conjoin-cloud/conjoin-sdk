from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingSMSSenderCreateSmsSenderResponse,
    MessagingSMSSenderDeleteSmsSenderResponse,
    MessagingSMSSenderDisableSmsSenderResponse,
    MessagingSMSSenderEnableSmsSenderResponse,
    MessagingSMSSenderListManySmsSendersCountQuery,
    MessagingSMSSenderListManySmsSendersCountResponse,
    MessagingSMSSenderListManySmsSendersItem,
    MessagingSMSSenderListManySmsSendersQuery,
    MessagingSMSSenderReadSmsSenderResponse,
    MessagingSMSSenderTransferSmsSenderRequest,
    MessagingSMSSenderTransferSmsSenderResponse,
    MessagingSMSSenderUpdateOneSmsSenderRequest,
    MessagingSMSSenderUpdateOneSmsSenderResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingSMSSendersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_many_sms_senders(
        self,
        query: MessagingSMSSenderListManySmsSendersQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingSMSSenderListManySmsSendersItem]:
        return self._client.request(
            'GET',
            'messaging/sms-senders/',
            query=query,
            cast_to=Page[MessagingSMSSenderListManySmsSendersItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create_sms_sender(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderCreateSmsSenderResponse:
        return self._client.request(
            'POST',
            'messaging/sms-senders/',
            body=data,
            cast_to=MessagingSMSSenderCreateSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_many_sms_senders_count(
        self,
        query: MessagingSMSSenderListManySmsSendersCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderListManySmsSendersCountResponse:
        return self._client.request(
            'GET',
            'messaging/sms-senders/count',
            query=query,
            cast_to=MessagingSMSSenderListManySmsSendersCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def read_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderReadSmsSenderResponse:
        return self._client.request(
            'GET',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}',
            cast_to=MessagingSMSSenderReadSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def update_one_sms_sender(
        self,
        sms_sender_id: str,
        data: MessagingSMSSenderUpdateOneSmsSenderRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderUpdateOneSmsSenderResponse:
        return self._client.request(
            'PATCH',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}',
            body=data,
            cast_to=MessagingSMSSenderUpdateOneSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDeleteSmsSenderResponse:
        return self._client.request(
            'DELETE',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}',
            cast_to=MessagingSMSSenderDeleteSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def enable_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderEnableSmsSenderResponse:
        return self._client.request(
            'POST',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}/enable',
            cast_to=MessagingSMSSenderEnableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def disable_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDisableSmsSenderResponse:
        return self._client.request(
            'POST',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}/disable',
            cast_to=MessagingSMSSenderDisableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def transfer_sms_sender(
        self,
        sms_sender_id: str,
        data: MessagingSMSSenderTransferSmsSenderRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderTransferSmsSenderResponse:
        return self._client.request(
            'POST',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}/transfer',
            body=data,
            cast_to=MessagingSMSSenderTransferSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingSMSSendersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_many_sms_senders(
        self,
        query: MessagingSMSSenderListManySmsSendersQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingSMSSenderListManySmsSendersItem]:
        return await self._client.request(
            'GET',
            'messaging/sms-senders/',
            query=query,
            cast_to=AsyncPage[MessagingSMSSenderListManySmsSendersItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create_sms_sender(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderCreateSmsSenderResponse:
        return await self._client.request(
            'POST',
            'messaging/sms-senders/',
            body=data,
            cast_to=MessagingSMSSenderCreateSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_many_sms_senders_count(
        self,
        query: MessagingSMSSenderListManySmsSendersCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderListManySmsSendersCountResponse:
        return await self._client.request(
            'GET',
            'messaging/sms-senders/count',
            query=query,
            cast_to=MessagingSMSSenderListManySmsSendersCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def read_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderReadSmsSenderResponse:
        return await self._client.request(
            'GET',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}',
            cast_to=MessagingSMSSenderReadSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def update_one_sms_sender(
        self,
        sms_sender_id: str,
        data: MessagingSMSSenderUpdateOneSmsSenderRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderUpdateOneSmsSenderResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}',
            body=data,
            cast_to=MessagingSMSSenderUpdateOneSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDeleteSmsSenderResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}',
            cast_to=MessagingSMSSenderDeleteSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def enable_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderEnableSmsSenderResponse:
        return await self._client.request(
            'POST',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}/enable',
            cast_to=MessagingSMSSenderEnableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def disable_sms_sender(
        self,
        sms_sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderDisableSmsSenderResponse:
        return await self._client.request(
            'POST',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}/disable',
            cast_to=MessagingSMSSenderDisableSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def transfer_sms_sender(
        self,
        sms_sender_id: str,
        data: MessagingSMSSenderTransferSmsSenderRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderTransferSmsSenderResponse:
        return await self._client.request(
            'POST',
            f'messaging/sms-senders/{encode_path_param(sms_sender_id)}/transfer',
            body=data,
            cast_to=MessagingSMSSenderTransferSmsSenderResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
