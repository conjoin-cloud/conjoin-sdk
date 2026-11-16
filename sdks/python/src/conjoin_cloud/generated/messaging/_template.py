from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingTemplateCreateMessageRequest,
    MessagingTemplateCreateMessageResponse,
    MessagingTemplateDeleteMessageResponse,
    MessagingTemplateDeleteMessagesRequest,
    MessagingTemplateDeleteMessagesResponse,
    MessagingTemplateListMessageItem,
    MessagingTemplateListMessageRequest,
    MessagingTemplateReadMessageResponse,
    MessagingTemplateUpdateMessageRequest,
    MessagingTemplateUpdateMessageResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingTemplatesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_message(
        self,
        data: MessagingTemplateCreateMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateCreateMessageResponse:
        return self._client.request(
            'POST',
            'messaging/templates/',
            body=data,
            cast_to=MessagingTemplateCreateMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_message(
        self,
        data: MessagingTemplateListMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingTemplateListMessageItem]:
        return self._client.request(
            'POST',
            'messaging/templates/retrieve',
            body=data,
            cast_to=Page[MessagingTemplateListMessageItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
            cursor_location='body',
        )

    def read_message(
        self,
        template_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateReadMessageResponse:
        return self._client.request(
            'GET',
            f'messaging/templates/{encode_path_param(template_id)}',
            cast_to=MessagingTemplateReadMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def update_message(
        self,
        template_id: str,
        data: MessagingTemplateUpdateMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateUpdateMessageResponse:
        return self._client.request(
            'PATCH',
            f'messaging/templates/{encode_path_param(template_id)}',
            body=data,
            cast_to=MessagingTemplateUpdateMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_message(
        self,
        template_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateDeleteMessageResponse:
        return self._client.request(
            'DELETE',
            f'messaging/templates/{encode_path_param(template_id)}',
            cast_to=MessagingTemplateDeleteMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_messages(
        self,
        data: MessagingTemplateDeleteMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateDeleteMessagesResponse:
        return self._client.request(
            'PATCH',
            'messaging/templates/wipe',
            body=data,
            cast_to=MessagingTemplateDeleteMessagesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            unwrap_data=False,
        )


class AsyncMessagingTemplatesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_message(
        self,
        data: MessagingTemplateCreateMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateCreateMessageResponse:
        return await self._client.request(
            'POST',
            'messaging/templates/',
            body=data,
            cast_to=MessagingTemplateCreateMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_message(
        self,
        data: MessagingTemplateListMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingTemplateListMessageItem]:
        return await self._client.request(
            'POST',
            'messaging/templates/retrieve',
            body=data,
            cast_to=AsyncPage[MessagingTemplateListMessageItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
            cursor_location='body',
        )

    async def read_message(
        self,
        template_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateReadMessageResponse:
        return await self._client.request(
            'GET',
            f'messaging/templates/{encode_path_param(template_id)}',
            cast_to=MessagingTemplateReadMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def update_message(
        self,
        template_id: str,
        data: MessagingTemplateUpdateMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateUpdateMessageResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/templates/{encode_path_param(template_id)}',
            body=data,
            cast_to=MessagingTemplateUpdateMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_message(
        self,
        template_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateDeleteMessageResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/templates/{encode_path_param(template_id)}',
            cast_to=MessagingTemplateDeleteMessageResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_messages(
        self,
        data: MessagingTemplateDeleteMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateDeleteMessagesResponse:
        return await self._client.request(
            'PATCH',
            'messaging/templates/wipe',
            body=data,
            cast_to=MessagingTemplateDeleteMessagesResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            unwrap_data=False,
        )
