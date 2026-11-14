from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingContactPropertiesCreateContactPropertyResponse,
    MessagingContactPropertiesDeleteContactPropertyResponse,
    MessagingContactPropertiesDeleteManyResponse,
    MessagingContactPropertiesFetchOneContactPropertyResponse,
    MessagingContactPropertiesListItem,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingContactPropertiesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_contact_property(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesCreateContactPropertyResponse:
        return self._client.request(
            'POST',
            'messaging/contacts/properties',
            body=data,
            cast_to=MessagingContactPropertiesCreateContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_many(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesDeleteManyResponse:
        return self._client.request(
            'DELETE',
            'messaging/contacts/properties',
            cast_to=MessagingContactPropertiesDeleteManyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def fetch_one_contact_property(
        self,
        property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesFetchOneContactPropertyResponse:
        return self._client.request(
            'GET',
            f'messaging/contacts/properties/{encode_path_param(property_id)}',
            cast_to=MessagingContactPropertiesFetchOneContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_contact_property(
        self,
        property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesDeleteContactPropertyResponse:
        return self._client.request(
            'DELETE',
            f'messaging/contacts/properties/{encode_path_param(property_id)}',
            cast_to=MessagingContactPropertiesDeleteContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingContactPropertiesListItem]:
        return self._client.request(
            'POST',
            'messaging/contacts/properties/retrieve',
            cast_to=Page[MessagingContactPropertiesListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingContactPropertiesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_contact_property(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesCreateContactPropertyResponse:
        return await self._client.request(
            'POST',
            'messaging/contacts/properties',
            body=data,
            cast_to=MessagingContactPropertiesCreateContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_many(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesDeleteManyResponse:
        return await self._client.request(
            'DELETE',
            'messaging/contacts/properties',
            cast_to=MessagingContactPropertiesDeleteManyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def fetch_one_contact_property(
        self,
        property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesFetchOneContactPropertyResponse:
        return await self._client.request(
            'GET',
            f'messaging/contacts/properties/{encode_path_param(property_id)}',
            cast_to=MessagingContactPropertiesFetchOneContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_contact_property(
        self,
        property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesDeleteContactPropertyResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/contacts/properties/{encode_path_param(property_id)}',
            cast_to=MessagingContactPropertiesDeleteContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingContactPropertiesListItem]:
        return await self._client.request(
            'POST',
            'messaging/contacts/properties/retrieve',
            cast_to=AsyncPage[MessagingContactPropertiesListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
