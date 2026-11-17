from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingContactAddPropertiesRequest,
    MessagingContactAddPropertiesResponse,
    MessagingContactCreateRequest,
    MessagingContactCreateResponse,
    MessagingContactDeletePropertyValueResponse,
    MessagingContactDeleteResponse,
    MessagingContactListCountQuery,
    MessagingContactListCountResponse,
    MessagingContactListItem,
    MessagingContactListQuery,
    MessagingContactSuppressMessagesRequest,
    MessagingContactSuppressMessagesResponse,
    MessagingContactUpdatePropertyRequest,
    MessagingContactUpdatePropertyResponse,
    MessagingContactUpdateRequest,
    MessagingContactUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingContactsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: MessagingContactListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingContactListItem]:
        return self._client.request(
            'GET',
            'messaging/contacts/',
            query=query,
            cast_to=Page[MessagingContactListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create(
        self,
        data: MessagingContactCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactCreateResponse:
        return self._client.request(
            'POST',
            'messaging/contacts/',
            body=data,
            cast_to=MessagingContactCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: MessagingContactListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactListCountResponse:
        return self._client.request(
            'GET',
            'messaging/contacts/count',
            query=query,
            cast_to=MessagingContactListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def suppress_messages(
        self,
        contact_id: str,
        data: MessagingContactSuppressMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactSuppressMessagesResponse:
        return self._client.request(
            'POST',
            f'messaging/contacts/{encode_path_param(contact_id)}/unsubscribe',
            body=data,
            cast_to=MessagingContactSuppressMessagesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def update(
        self,
        contact_id: str,
        data: MessagingContactUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactUpdateResponse:
        return self._client.request(
            'PATCH',
            f'messaging/contacts/{encode_path_param(contact_id)}',
            body=data,
            cast_to=MessagingContactUpdateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete(
        self,
        contact_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/contacts/{encode_path_param(contact_id)}',
            cast_to=MessagingContactDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def add_properties(
        self,
        contact_id: str,
        data: MessagingContactAddPropertiesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactAddPropertiesResponse:
        return self._client.request(
            'POST',
            f'messaging/contacts/{encode_path_param(contact_id)}/properties',
            body=data,
            cast_to=MessagingContactAddPropertiesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def update_property(
        self,
        contact_id: str,
        property_id: str,
        data: MessagingContactUpdatePropertyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactUpdatePropertyResponse:
        return self._client.request(
            'PATCH',
            (
                f'messaging/contacts/{encode_path_param(contact_id)}/properties'
                f'/{encode_path_param(property_id)}'
            ),
            body=data,
            cast_to=MessagingContactUpdatePropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_property_value(
        self,
        contact_id: str,
        property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactDeletePropertyValueResponse:
        return self._client.request(
            'DELETE',
            (
                f'messaging/contacts/{encode_path_param(contact_id)}/properties'
                f'/{encode_path_param(property_id)}'
            ),
            cast_to=MessagingContactDeletePropertyValueResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingContactsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: MessagingContactListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingContactListItem]:
        return await self._client.request(
            'GET',
            'messaging/contacts/',
            query=query,
            cast_to=AsyncPage[MessagingContactListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create(
        self,
        data: MessagingContactCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/contacts/',
            body=data,
            cast_to=MessagingContactCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: MessagingContactListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactListCountResponse:
        return await self._client.request(
            'GET',
            'messaging/contacts/count',
            query=query,
            cast_to=MessagingContactListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def suppress_messages(
        self,
        contact_id: str,
        data: MessagingContactSuppressMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactSuppressMessagesResponse:
        return await self._client.request(
            'POST',
            f'messaging/contacts/{encode_path_param(contact_id)}/unsubscribe',
            body=data,
            cast_to=MessagingContactSuppressMessagesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def update(
        self,
        contact_id: str,
        data: MessagingContactUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/contacts/{encode_path_param(contact_id)}',
            body=data,
            cast_to=MessagingContactUpdateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete(
        self,
        contact_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/contacts/{encode_path_param(contact_id)}',
            cast_to=MessagingContactDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def add_properties(
        self,
        contact_id: str,
        data: MessagingContactAddPropertiesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactAddPropertiesResponse:
        return await self._client.request(
            'POST',
            f'messaging/contacts/{encode_path_param(contact_id)}/properties',
            body=data,
            cast_to=MessagingContactAddPropertiesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def update_property(
        self,
        contact_id: str,
        property_id: str,
        data: MessagingContactUpdatePropertyRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactUpdatePropertyResponse:
        return await self._client.request(
            'PATCH',
            (
                f'messaging/contacts/{encode_path_param(contact_id)}/properties'
                f'/{encode_path_param(property_id)}'
            ),
            body=data,
            cast_to=MessagingContactUpdatePropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_property_value(
        self,
        contact_id: str,
        property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactDeletePropertyValueResponse:
        return await self._client.request(
            'DELETE',
            (
                f'messaging/contacts/{encode_path_param(contact_id)}/properties'
                f'/{encode_path_param(property_id)}'
            ),
            cast_to=MessagingContactDeletePropertyValueResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
