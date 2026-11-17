from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingContactPropertiesCreateContactPropertyResponse,
    MessagingContactPropertiesDeleteContactPropertyResponse,
    MessagingContactPropertiesFetchOneContactPropertyResponse,
    MessagingContactPropertiesListCountQuery,
    MessagingContactPropertiesListCountResponse,
    MessagingContactPropertiesListItem,
    MessagingContactPropertiesListQuery,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingContactPropertiesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: MessagingContactPropertiesListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingContactPropertiesListItem]:
        return self._client.request(
            'GET',
            'messaging/contact-properties/',
            query=query,
            cast_to=Page[MessagingContactPropertiesListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create_contact_property(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesCreateContactPropertyResponse:
        return self._client.request(
            'POST',
            'messaging/contact-properties/',
            body=data,
            cast_to=MessagingContactPropertiesCreateContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: MessagingContactPropertiesListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesListCountResponse:
        return self._client.request(
            'GET',
            'messaging/contact-properties/count',
            query=query,
            cast_to=MessagingContactPropertiesListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def fetch_one_contact_property(
        self,
        contact_property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesFetchOneContactPropertyResponse:
        return self._client.request(
            'GET',
            f'messaging/contact-properties/{encode_path_param(contact_property_id)}',
            cast_to=MessagingContactPropertiesFetchOneContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_contact_property(
        self,
        contact_property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesDeleteContactPropertyResponse:
        return self._client.request(
            'DELETE',
            f'messaging/contact-properties/{encode_path_param(contact_property_id)}',
            cast_to=MessagingContactPropertiesDeleteContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingContactPropertiesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: MessagingContactPropertiesListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingContactPropertiesListItem]:
        return await self._client.request(
            'GET',
            'messaging/contact-properties/',
            query=query,
            cast_to=AsyncPage[MessagingContactPropertiesListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create_contact_property(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesCreateContactPropertyResponse:
        return await self._client.request(
            'POST',
            'messaging/contact-properties/',
            body=data,
            cast_to=MessagingContactPropertiesCreateContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: MessagingContactPropertiesListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesListCountResponse:
        return await self._client.request(
            'GET',
            'messaging/contact-properties/count',
            query=query,
            cast_to=MessagingContactPropertiesListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def fetch_one_contact_property(
        self,
        contact_property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesFetchOneContactPropertyResponse:
        return await self._client.request(
            'GET',
            f'messaging/contact-properties/{encode_path_param(contact_property_id)}',
            cast_to=MessagingContactPropertiesFetchOneContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_contact_property(
        self,
        contact_property_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingContactPropertiesDeleteContactPropertyResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/contact-properties/{encode_path_param(contact_property_id)}',
            cast_to=MessagingContactPropertiesDeleteContactPropertyResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
