from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingEmailSenderCreateResponse,
    MessagingEmailSenderDeleteResponse,
    MessagingEmailSenderDisableRequest,
    MessagingEmailSenderDisableResponse,
    MessagingEmailSenderEnableRequest,
    MessagingEmailSenderEnableResponse,
    MessagingEmailSenderListManyItem,
    MessagingEmailSenderListManyRequest,
    MessagingEmailSenderListOneResponse,
    MessagingEmailSenderTransferResponse,
    MessagingEmailSenderVerifyResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingEmailSendersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def verify(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderVerifyResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/senders/{encode_path_param(sender_id)}/verify',
            cast_to=MessagingEmailSenderVerifyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_many(
        self,
        data: MessagingEmailSenderListManyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingEmailSenderListManyItem]:
        return self._client.request(
            'POST',
            'messaging/email/senders/retrieve',
            body=data,
            cast_to=Page[MessagingEmailSenderListManyItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_one(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderListOneResponse:
        return self._client.request(
            'GET',
            f'messaging/email/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingEmailSenderListOneResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/email/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingEmailSenderDeleteResponse,
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
            'messaging/email/senders/',
            body=data,
            cast_to=MessagingEmailSenderCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def enable(
        self,
        sender_id: str,
        data: MessagingEmailSenderEnableRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderEnableResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/senders/{encode_path_param(sender_id)}/enable',
            body=data,
            cast_to=MessagingEmailSenderEnableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def disable(
        self,
        sender_id: str,
        data: MessagingEmailSenderDisableRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDisableResponse:
        return self._client.request(
            'PATCH',
            f'messaging/email/senders/{encode_path_param(sender_id)}/disable',
            body=data,
            cast_to=MessagingEmailSenderDisableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def transfer(
        self,
        sender_id: str,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderTransferResponse:
        return self._client.request(
            'PATCH',
            (
                f'messaging/email/senders/transfers/{encode_path_param(sender_id)}'
                f'/{encode_path_param(project_id)}'
            ),
            cast_to=MessagingEmailSenderTransferResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingEmailSendersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def verify(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderVerifyResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/senders/{encode_path_param(sender_id)}/verify',
            cast_to=MessagingEmailSenderVerifyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_many(
        self,
        data: MessagingEmailSenderListManyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingEmailSenderListManyItem]:
        return await self._client.request(
            'POST',
            'messaging/email/senders/retrieve',
            body=data,
            cast_to=AsyncPage[MessagingEmailSenderListManyItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_one(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderListOneResponse:
        return await self._client.request(
            'GET',
            f'messaging/email/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingEmailSenderListOneResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete(
        self,
        sender_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/email/senders/{encode_path_param(sender_id)}',
            cast_to=MessagingEmailSenderDeleteResponse,
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
            'messaging/email/senders/',
            body=data,
            cast_to=MessagingEmailSenderCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def enable(
        self,
        sender_id: str,
        data: MessagingEmailSenderEnableRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderEnableResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/senders/{encode_path_param(sender_id)}/enable',
            body=data,
            cast_to=MessagingEmailSenderEnableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def disable(
        self,
        sender_id: str,
        data: MessagingEmailSenderDisableRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderDisableResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/email/senders/{encode_path_param(sender_id)}/disable',
            body=data,
            cast_to=MessagingEmailSenderDisableResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def transfer(
        self,
        sender_id: str,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingEmailSenderTransferResponse:
        return await self._client.request(
            'PATCH',
            (
                f'messaging/email/senders/transfers/{encode_path_param(sender_id)}'
                f'/{encode_path_param(project_id)}'
            ),
            cast_to=MessagingEmailSenderTransferResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
