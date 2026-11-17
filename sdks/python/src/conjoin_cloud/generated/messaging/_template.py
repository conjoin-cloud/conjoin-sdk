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
    MessagingTemplateListMessageCountQuery,
    MessagingTemplateListMessageCountResponse,
    MessagingTemplateListMessageItem,
    MessagingTemplateListMessageQuery,
    MessagingTemplateReadMessageResponse,
    MessagingTemplateUpdateMessageRequest,
    MessagingTemplateUpdateMessageResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingTemplatesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_message(
        self,
        query: MessagingTemplateListMessageQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingTemplateListMessageItem]:
        return self._client.request(
            'GET',
            'messaging/templates/',
            query=query,
            cast_to=Page[MessagingTemplateListMessageItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

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

    def list_message_count(
        self,
        query: MessagingTemplateListMessageCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateListMessageCountResponse:
        return self._client.request(
            'GET',
            'messaging/templates/count',
            query=query,
            cast_to=MessagingTemplateListMessageCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
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


class AsyncMessagingTemplatesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_message(
        self,
        query: MessagingTemplateListMessageQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingTemplateListMessageItem]:
        return await self._client.request(
            'GET',
            'messaging/templates/',
            query=query,
            cast_to=AsyncPage[MessagingTemplateListMessageItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

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

    async def list_message_count(
        self,
        query: MessagingTemplateListMessageCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingTemplateListMessageCountResponse:
        return await self._client.request(
            'GET',
            'messaging/templates/count',
            query=query,
            cast_to=MessagingTemplateListMessageCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
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
