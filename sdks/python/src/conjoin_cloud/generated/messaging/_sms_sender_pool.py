from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingSMSSenderPoolAddSmsSendersToPoolRequest,
    MessagingSMSSenderPoolAddSmsSendersToPoolResponse,
    MessagingSMSSenderPoolCreateSmsSenderPoolRequest,
    MessagingSMSSenderPoolCreateSmsSenderPoolResponse,
    MessagingSMSSenderPoolDeleteSmsSenderPoolResponse,
    MessagingSMSSenderPoolGetSmsSenderPoolResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingSMSSenderPoolsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_sms_sender_pool(
        self,
        data: MessagingSMSSenderPoolCreateSmsSenderPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolCreateSmsSenderPoolResponse:
        return self._client.request(
            'POST',
            'messaging/sms/sender-pools/',
            body=data,
            cast_to=MessagingSMSSenderPoolCreateSmsSenderPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def add_sms_senders_to_pool(
        self,
        pool_id: str,
        data: MessagingSMSSenderPoolAddSmsSendersToPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolAddSmsSendersToPoolResponse:
        return self._client.request(
            'POST',
            f'messaging/sms/sender-pools/{encode_path_param(pool_id)}/senders',
            body=data,
            cast_to=MessagingSMSSenderPoolAddSmsSendersToPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def get_sms_sender_pool(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolGetSmsSenderPoolResponse:
        return self._client.request(
            'GET',
            f'messaging/sms/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingSMSSenderPoolGetSmsSenderPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_sms_sender_pool(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolDeleteSmsSenderPoolResponse:
        return self._client.request(
            'DELETE',
            f'messaging/sms/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingSMSSenderPoolDeleteSmsSenderPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingSMSSenderPoolsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_sms_sender_pool(
        self,
        data: MessagingSMSSenderPoolCreateSmsSenderPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolCreateSmsSenderPoolResponse:
        return await self._client.request(
            'POST',
            'messaging/sms/sender-pools/',
            body=data,
            cast_to=MessagingSMSSenderPoolCreateSmsSenderPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def add_sms_senders_to_pool(
        self,
        pool_id: str,
        data: MessagingSMSSenderPoolAddSmsSendersToPoolRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolAddSmsSendersToPoolResponse:
        return await self._client.request(
            'POST',
            f'messaging/sms/sender-pools/{encode_path_param(pool_id)}/senders',
            body=data,
            cast_to=MessagingSMSSenderPoolAddSmsSendersToPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def get_sms_sender_pool(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolGetSmsSenderPoolResponse:
        return await self._client.request(
            'GET',
            f'messaging/sms/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingSMSSenderPoolGetSmsSenderPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_sms_sender_pool(
        self,
        pool_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSSenderPoolDeleteSmsSenderPoolResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/sms/sender-pools/{encode_path_param(pool_id)}',
            cast_to=MessagingSMSSenderPoolDeleteSmsSenderPoolResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
