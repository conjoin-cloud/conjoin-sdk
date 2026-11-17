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
    MessagingVerificationListMessagesItem,
    MessagingVerificationListMessagesRequest,
    MessagingVerificationResendResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingVerificationsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationCreateResponse:
        return self._client.request(
            'POST',
            'messaging/verifications/send',
            body=data,
            cast_to=MessagingVerificationCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
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
            'PATCH',
            f'messaging/verifications/resend/{encode_path_param(verification_id)}',
            cast_to=MessagingVerificationResendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_messages(
        self,
        data: MessagingVerificationListMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingVerificationListMessagesItem]:
        return self._client.request(
            'POST',
            'messaging/verifications/messages',
            body=data,
            cast_to=Page[MessagingVerificationListMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )


class AsyncMessagingVerificationsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingVerificationCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/verifications/send',
            body=data,
            cast_to=MessagingVerificationCreateResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
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
            'PATCH',
            f'messaging/verifications/resend/{encode_path_param(verification_id)}',
            cast_to=MessagingVerificationResendResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_messages(
        self,
        data: MessagingVerificationListMessagesRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingVerificationListMessagesItem]:
        return await self._client.request(
            'POST',
            'messaging/verifications/messages',
            body=data,
            cast_to=AsyncPage[MessagingVerificationListMessagesItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )
