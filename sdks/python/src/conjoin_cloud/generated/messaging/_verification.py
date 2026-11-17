from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingVerificationCheckRequest,
    MessagingVerificationCheckResponse,
    MessagingVerificationCreateResponse,
    MessagingVerificationListMessagesCountQuery,
    MessagingVerificationListMessagesCountResponse,
    MessagingVerificationListMessagesItem,
    MessagingVerificationListMessagesQuery,
    MessagingVerificationResendResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingVerificationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_messages(
        self,
        query: MessagingVerificationListMessagesQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingVerificationListMessagesItem]:
        return self._client.request(
            'GET',
            'messaging/verifications/',
            query=query,
            cast_to=Page[MessagingVerificationListMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationCreateResponse:
        return self._client.request(
            'POST',
            'messaging/verifications/',
            body=data,
            cast_to=MessagingVerificationCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def list_messages_count(
        self,
        query: MessagingVerificationListMessagesCountQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationListMessagesCountResponse:
        return self._client.request(
            'GET',
            'messaging/verifications/count',
            query=query,
            cast_to=MessagingVerificationListMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def check(
        self,
        verification_id: str,
        data: MessagingVerificationCheckRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationCheckResponse:
        return self._client.request(
            'POST',
            f'messaging/verifications/{encode_path_param(verification_id)}/check',
            body=data,
            cast_to=MessagingVerificationCheckResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def resend(
        self,
        verification_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationResendResponse:
        return self._client.request(
            'POST',
            f'messaging/verifications/{encode_path_param(verification_id)}/resend',
            cast_to=MessagingVerificationResendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingVerificationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_messages(
        self,
        query: MessagingVerificationListMessagesQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingVerificationListMessagesItem]:
        return await self._client.request(
            'GET',
            'messaging/verifications/',
            query=query,
            cast_to=AsyncPage[MessagingVerificationListMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/verifications/',
            body=data,
            cast_to=MessagingVerificationCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def list_messages_count(
        self,
        query: MessagingVerificationListMessagesCountQuery,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationListMessagesCountResponse:
        return await self._client.request(
            'GET',
            'messaging/verifications/count',
            query=query,
            cast_to=MessagingVerificationListMessagesCountResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def check(
        self,
        verification_id: str,
        data: MessagingVerificationCheckRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationCheckResponse:
        return await self._client.request(
            'POST',
            f'messaging/verifications/{encode_path_param(verification_id)}/check',
            body=data,
            cast_to=MessagingVerificationCheckResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def resend(
        self,
        verification_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationResendResponse:
        return await self._client.request(
            'POST',
            f'messaging/verifications/{encode_path_param(verification_id)}/resend',
            cast_to=MessagingVerificationResendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
