from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingPhoneNumberListAvailableItem,
    MessagingPhoneNumberListAvailableQuery,
    MessagingPhoneNumberListCountQuery,
    MessagingPhoneNumberListCountResponse,
    MessagingPhoneNumberListItem,
    MessagingPhoneNumberListQuery,
    MessagingPhoneNumberPurchaseRequest,
    MessagingPhoneNumberPurchaseResponse,
    MessagingPhoneNumberReleaseResponse,
    MessagingPhoneNumberTransferRequest,
    MessagingPhoneNumberTransferResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingPhoneNumbersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: MessagingPhoneNumberListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingPhoneNumberListItem]:
        return self._client.request(
            'GET',
            'messaging/phone-numbers/',
            query=query,
            cast_to=Page[MessagingPhoneNumberListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def purchase(
        self,
        data: MessagingPhoneNumberPurchaseRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberPurchaseResponse:
        return self._client.request(
            'POST',
            'messaging/phone-numbers/',
            body=data,
            cast_to=MessagingPhoneNumberPurchaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: MessagingPhoneNumberListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberListCountResponse:
        return self._client.request(
            'GET',
            'messaging/phone-numbers/count',
            query=query,
            cast_to=MessagingPhoneNumberListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def transfer(
        self,
        phone_number_id: str,
        data: MessagingPhoneNumberTransferRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberTransferResponse:
        return self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number_id)}/transfer',
            body=data,
            cast_to=MessagingPhoneNumberTransferResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def release(
        self,
        phone_number_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberReleaseResponse:
        return self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number_id)}/release',
            cast_to=MessagingPhoneNumberReleaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_available(
        self,
        query: MessagingPhoneNumberListAvailableQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingPhoneNumberListAvailableItem]:
        return self._client.request(
            'GET',
            'messaging/available-phone-numbers/',
            query=query,
            cast_to=Page[MessagingPhoneNumberListAvailableItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingPhoneNumbersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: MessagingPhoneNumberListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingPhoneNumberListItem]:
        return await self._client.request(
            'GET',
            'messaging/phone-numbers/',
            query=query,
            cast_to=AsyncPage[MessagingPhoneNumberListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def purchase(
        self,
        data: MessagingPhoneNumberPurchaseRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberPurchaseResponse:
        return await self._client.request(
            'POST',
            'messaging/phone-numbers/',
            body=data,
            cast_to=MessagingPhoneNumberPurchaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: MessagingPhoneNumberListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberListCountResponse:
        return await self._client.request(
            'GET',
            'messaging/phone-numbers/count',
            query=query,
            cast_to=MessagingPhoneNumberListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def transfer(
        self,
        phone_number_id: str,
        data: MessagingPhoneNumberTransferRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberTransferResponse:
        return await self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number_id)}/transfer',
            body=data,
            cast_to=MessagingPhoneNumberTransferResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def release(
        self,
        phone_number_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberReleaseResponse:
        return await self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number_id)}/release',
            cast_to=MessagingPhoneNumberReleaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_available(
        self,
        query: MessagingPhoneNumberListAvailableQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingPhoneNumberListAvailableItem]:
        return await self._client.request(
            'GET',
            'messaging/available-phone-numbers/',
            query=query,
            cast_to=AsyncPage[MessagingPhoneNumberListAvailableItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
