from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingConversationAddManyRecipientsItem,
    MessagingConversationAddOneRecipientResponse,
    MessagingConversationArchiveRequest,
    MessagingConversationArchiveResponse,
    MessagingConversationCloneRequest,
    MessagingConversationCloneResponse,
    MessagingConversationCreateRequest,
    MessagingConversationCreateResponse,
    MessagingConversationDeleteRecipientsResponse,
    MessagingConversationDeleteResponse,
    MessagingConversationListItem,
    MessagingConversationListRequest,
    MessagingConversationReadManyRecipientsItem,
    MessagingConversationReadMessagesItem,
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
        )

    def clone(
        self,
        conversation_id: str,
        data: MessagingConversationCloneRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationCloneResponse:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/clone',
            body=data,
            cast_to=MessagingConversationCloneResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
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
        data: MessagingConversationArchiveRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationArchiveResponse:
        return self._client.request(
            'PATCH',
            f'messaging/conversations/{encode_path_param(conversation_id)}/archive',
            body=data,
            cast_to=MessagingConversationArchiveResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list(
        self,
        data: MessagingConversationListRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingConversationListItem]:
        return self._client.request(
            'POST',
            'messaging/conversations/retrieve',
            body=data,
            cast_to=Page[MessagingConversationListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def read_messages(
        self,
        conversation_id: str,
        parent_message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingConversationReadMessagesItem]:
        return self._client.request(
            'POST',
            (
                f'messaging/conversations/{encode_path_param(conversation_id)}/messages'
                f'/{encode_path_param(parent_message_id)}'
            ),
            cast_to=Page[MessagingConversationReadMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
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

    def read_many_recipients(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingConversationReadManyRecipientsItem]:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients/retrieve',
            cast_to=Page[MessagingConversationReadManyRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def add_one_recipient(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationAddOneRecipientResponse:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients',
            cast_to=MessagingConversationAddOneRecipientResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def add_many_recipients(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingConversationAddManyRecipientsItem]:
        return self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients/batch',
            cast_to=Page[MessagingConversationAddManyRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )


class AsyncMessagingConversationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

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
        )

    async def clone(
        self,
        conversation_id: str,
        data: MessagingConversationCloneRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationCloneResponse:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/clone',
            body=data,
            cast_to=MessagingConversationCloneResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
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
        data: MessagingConversationArchiveRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationArchiveResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/conversations/{encode_path_param(conversation_id)}/archive',
            body=data,
            cast_to=MessagingConversationArchiveResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list(
        self,
        data: MessagingConversationListRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingConversationListItem]:
        return await self._client.request(
            'POST',
            'messaging/conversations/retrieve',
            body=data,
            cast_to=AsyncPage[MessagingConversationListItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def read_messages(
        self,
        conversation_id: str,
        parent_message_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingConversationReadMessagesItem]:
        return await self._client.request(
            'POST',
            (
                f'messaging/conversations/{encode_path_param(conversation_id)}/messages'
                f'/{encode_path_param(parent_message_id)}'
            ),
            cast_to=AsyncPage[MessagingConversationReadMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
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

    async def read_many_recipients(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingConversationReadManyRecipientsItem]:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients/retrieve',
            cast_to=AsyncPage[MessagingConversationReadManyRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def add_one_recipient(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingConversationAddOneRecipientResponse:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients',
            cast_to=MessagingConversationAddOneRecipientResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def add_many_recipients(
        self,
        conversation_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingConversationAddManyRecipientsItem]:
        return await self._client.request(
            'POST',
            f'messaging/conversations/{encode_path_param(conversation_id)}/recipients/batch',
            cast_to=AsyncPage[MessagingConversationAddManyRecipientsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )
