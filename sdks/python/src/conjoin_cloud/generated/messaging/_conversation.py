from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingConversationAddManyRecipientsItem,
    MessagingConversationAddManyRecipientsRequest,
    MessagingConversationAddOneRecipientRequest,
    MessagingConversationAddOneRecipientResponse,
    MessagingConversationArchiveResponse,
    MessagingConversationCreateRequest,
    MessagingConversationCreateResponse,
    MessagingConversationDeleteRecipientsResponse,
    MessagingConversationDeleteResponse,
    MessagingConversationDuplicateRequest,
    MessagingConversationDuplicateResponse,
    MessagingConversationListCountQuery,
    MessagingConversationListCountResponse,
    MessagingConversationListItem,
    MessagingConversationListMessagesCountQuery,
    MessagingConversationListMessagesCountResponse,
    MessagingConversationListMessagesQuery,
    MessagingConversationListQuery,
    MessagingConversationListRecipientsCountQuery,
    MessagingConversationListRecipientsCountResponse,
    MessagingConversationListRecipientsItem,
    MessagingConversationListRecipientsQuery,
    MessagingConversationReadOneRecipientResponse,
    MessagingConversationSendMessageRequest,
    MessagingConversationUpdateRequest,
    MessagingConversationUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingConversationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: MessagingConversationListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingConversationListItem]:
        return self._client.request(
            'GET',
            'messaging/conversations/',
            query=query,
            cast_to=Page[MessagingConversationListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create(
        self,
        data: MessagingConversationCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationCreateResponse:
        return self._client.request(
            'POST',
            'messaging/conversations/',
            body=data,
            cast_to=MessagingConversationCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_messages(
        self,
        conversation_id: str,
        query: MessagingConversationListMessagesQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[Any]:
        return self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/messages',
            query=query,
            cast_to=Page[Any],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_recipients(
        self,
        conversation_id: str,
        query: MessagingConversationListRecipientsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingConversationListRecipientsItem]:
        return self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients',
            query=query,
            cast_to=Page[MessagingConversationListRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def add_one_recipient(
        self,
        conversation_id: str,
        data: MessagingConversationAddOneRecipientRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationAddOneRecipientResponse:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients',
            body=data,
            cast_to=MessagingConversationAddOneRecipientResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_count(
        self,
        query: MessagingConversationListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationListCountResponse:
        return self._client.request(
            'GET',
            'messaging/conversations/count',
            query=query,
            cast_to=MessagingConversationListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_messages_count(
        self,
        conversation_id: str,
        query: MessagingConversationListMessagesCountQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationListMessagesCountResponse:
        return self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/messages/count',
            query=query,
            cast_to=MessagingConversationListMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_recipients_count(
        self,
        conversation_id: str,
        query: MessagingConversationListRecipientsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationListRecipientsCountResponse:
        return self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients/count',
            query=query,
            cast_to=MessagingConversationListRecipientsCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def duplicate(
        self,
        conversation_id: str,
        data: MessagingConversationDuplicateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationDuplicateResponse:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/duplicate',
            body=data,
            cast_to=MessagingConversationDuplicateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def send_message(
        self,
        conversation_id: str,
        data: MessagingConversationSendMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/send',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def update(
        self,
        conversation_id: str,
        data: MessagingConversationUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationUpdateResponse:
        return self._client.request(
            'PATCH',
            f'messaging/conversations/{encode_path_param(conversation_id)}',
            body=data,
            cast_to=MessagingConversationUpdateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/conversations/{encode_path_param(conversation_id)}',
            cast_to=MessagingConversationDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def archive(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationArchiveResponse:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/archive',
            cast_to=MessagingConversationArchiveResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def read_one_recipient(
        self,
        conversation_id: str,
        recipient_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationReadOneRecipientResponse:
        return self._client.request(
            'GET',
            (
                f'messaging/conversations/{encode_path_param(conversation_id)}/recipients'
                f'/{encode_path_param(recipient_id)}'
            ),
            cast_to=MessagingConversationReadOneRecipientResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_recipients(
        self,
        conversation_id: str,
        recipient_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationDeleteRecipientsResponse:
        return self._client.request(
            'DELETE',
            (
                f'messaging/conversations/{encode_path_param(conversation_id)}/recipients'
                f'/{encode_path_param(recipient_id)}'
            ),
            cast_to=MessagingConversationDeleteRecipientsResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def add_many_recipients(
        self,
        conversation_id: str,
        data: MessagingConversationAddManyRecipientsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingConversationAddManyRecipientsItem]:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/add-recipients',
            body=data,
            cast_to=Page[MessagingConversationAddManyRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingConversationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: MessagingConversationListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingConversationListItem]:
        return await self._client.request(
            'GET',
            'messaging/conversations/',
            query=query,
            cast_to=AsyncPage[MessagingConversationListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create(
        self,
        data: MessagingConversationCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/conversations/',
            body=data,
            cast_to=MessagingConversationCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_messages(
        self,
        conversation_id: str,
        query: MessagingConversationListMessagesQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[Any]:
        return await self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/messages',
            query=query,
            cast_to=AsyncPage[Any],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_recipients(
        self,
        conversation_id: str,
        query: MessagingConversationListRecipientsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingConversationListRecipientsItem]:
        return await self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients',
            query=query,
            cast_to=AsyncPage[MessagingConversationListRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def add_one_recipient(
        self,
        conversation_id: str,
        data: MessagingConversationAddOneRecipientRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationAddOneRecipientResponse:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients',
            body=data,
            cast_to=MessagingConversationAddOneRecipientResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_count(
        self,
        query: MessagingConversationListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationListCountResponse:
        return await self._client.request(
            'GET',
            'messaging/conversations/count',
            query=query,
            cast_to=MessagingConversationListCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_messages_count(
        self,
        conversation_id: str,
        query: MessagingConversationListMessagesCountQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationListMessagesCountResponse:
        return await self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/messages/count',
            query=query,
            cast_to=MessagingConversationListMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_recipients_count(
        self,
        conversation_id: str,
        query: MessagingConversationListRecipientsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationListRecipientsCountResponse:
        return await self._client.request(
            'GET',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients/count',
            query=query,
            cast_to=MessagingConversationListRecipientsCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def duplicate(
        self,
        conversation_id: str,
        data: MessagingConversationDuplicateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationDuplicateResponse:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/duplicate',
            body=data,
            cast_to=MessagingConversationDuplicateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def send_message(
        self,
        conversation_id: str,
        data: MessagingConversationSendMessageRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/send',
            body=data,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def update(
        self,
        conversation_id: str,
        data: MessagingConversationUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/conversations/{encode_path_param(conversation_id)}',
            body=data,
            cast_to=MessagingConversationUpdateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/conversations/{encode_path_param(conversation_id)}',
            cast_to=MessagingConversationDeleteResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def archive(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationArchiveResponse:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/archive',
            cast_to=MessagingConversationArchiveResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def read_one_recipient(
        self,
        conversation_id: str,
        recipient_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationReadOneRecipientResponse:
        return await self._client.request(
            'GET',
            (
                f'messaging/conversations/{encode_path_param(conversation_id)}/recipients'
                f'/{encode_path_param(recipient_id)}'
            ),
            cast_to=MessagingConversationReadOneRecipientResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_recipients(
        self,
        conversation_id: str,
        recipient_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationDeleteRecipientsResponse:
        return await self._client.request(
            'DELETE',
            (
                f'messaging/conversations/{encode_path_param(conversation_id)}/recipients'
                f'/{encode_path_param(recipient_id)}'
            ),
            cast_to=MessagingConversationDeleteRecipientsResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def add_many_recipients(
        self,
        conversation_id: str,
        data: MessagingConversationAddManyRecipientsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingConversationAddManyRecipientsItem]:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/add-recipients',
            body=data,
            cast_to=AsyncPage[MessagingConversationAddManyRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
