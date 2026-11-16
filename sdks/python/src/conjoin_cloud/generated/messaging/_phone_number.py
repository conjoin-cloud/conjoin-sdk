from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingPhoneNumberListAvailableItem,
    MessagingPhoneNumberListAvailableQuery,
    MessagingPhoneNumberListItem,
    MessagingPhoneNumberListQuery,
    MessagingPhoneNumberPurchaseRequest,
    MessagingPhoneNumberPurchaseResponse,
    MessagingPhoneNumberReleaseResponse,
    MessagingPhoneNumberUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingPhoneNumbersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def purchase(
        self,
        phone_number: str,
        data: MessagingPhoneNumberPurchaseRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberPurchaseResponse:
        return self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number)}/provision',
            body=data,
            cast_to=MessagingPhoneNumberPurchaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def update(
        self,
        phone_number: str,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberUpdateResponse:
        return self._client.request(
            'PATCH',
            (
                f'messaging/phone-numbers/transfer/{encode_path_param(phone_number)}/project'
                f'/{encode_path_param(project_id)}'
            ),
            cast_to=MessagingPhoneNumberUpdateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_available(
        self,
        query: MessagingPhoneNumberListAvailableQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingPhoneNumberListAvailableItem]:
        return self._client.request(
            'GET',
            'messaging/phone-numbers/available',
            query=query,
            cast_to=Page[MessagingPhoneNumberListAvailableItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            cursor_location='none',
        )

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

    def release(
        self,
        phone_number: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberReleaseResponse:
        return self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number)}/release',
            cast_to=MessagingPhoneNumberReleaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingPhoneNumbersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def purchase(
        self,
        phone_number: str,
        data: MessagingPhoneNumberPurchaseRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberPurchaseResponse:
        return await self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number)}/provision',
            body=data,
            cast_to=MessagingPhoneNumberPurchaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def update(
        self,
        phone_number: str,
        project_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberUpdateResponse:
        return await self._client.request(
            'PATCH',
            (
                f'messaging/phone-numbers/transfer/{encode_path_param(phone_number)}/project'
                f'/{encode_path_param(project_id)}'
            ),
            cast_to=MessagingPhoneNumberUpdateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_available(
        self,
        query: MessagingPhoneNumberListAvailableQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingPhoneNumberListAvailableItem]:
        return await self._client.request(
            'GET',
            'messaging/phone-numbers/available',
            query=query,
            cast_to=AsyncPage[MessagingPhoneNumberListAvailableItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            cursor_location='none',
        )

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

    async def release(
        self,
        phone_number: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingPhoneNumberReleaseResponse:
        return await self._client.request(
            'POST',
            f'messaging/phone-numbers/{encode_path_param(phone_number)}/release',
            cast_to=MessagingPhoneNumberReleaseResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
