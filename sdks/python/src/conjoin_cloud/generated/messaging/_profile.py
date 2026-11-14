from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingProfileCloseResponse,
    MessagingProfileCreateRequest,
    MessagingProfileCreateResponse,
    MessagingProfileDeleteResponse,
    MessagingProfileDisableResponse,
    MessagingProfileEnableResponse,
    MessagingProfileListItem,
    MessagingProfileListRequest,
    MessagingProfileReadResponse,
    MessagingProfileUpdateEmailConfigRequest,
    MessagingProfileUpdateEmailConfigResponse,
    MessagingProfileUpdateMultisendConfigRequest,
    MessagingProfileUpdateMultisendConfigResponse,
    MessagingProfileUpdateRequest,
    MessagingProfileUpdateResponse,
    MessagingProfileUpdateVerificationsConfigRequest,
    MessagingProfileUpdateVerificationsConfigResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingProfilesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create(
        self,
        data: MessagingProfileCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCreateResponse:
        return self._client.request(
            'POST',
            'messaging/profiles/',
            body=data,
            cast_to=MessagingProfileCreateResponse,
            request_options=request_options,
        )

    def enable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileEnableResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/enable',
            cast_to=MessagingProfileEnableResponse,
            request_options=request_options,
        )

    def disable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDisableResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/disable',
            cast_to=MessagingProfileDisableResponse,
            request_options=request_options,
        )

    def close(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCloseResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/close',
            cast_to=MessagingProfileCloseResponse,
            request_options=request_options,
        )

    def read(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileReadResponse:
        return self._client.request(
            'GET',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileReadResponse,
            request_options=request_options,
        )

    def update(
        self,
        profile_id: str,
        data: MessagingProfileUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            body=data,
            cast_to=MessagingProfileUpdateResponse,
            request_options=request_options,
        )

    def delete(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDeleteResponse:
        return self._client.request(
            'DELETE',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileDeleteResponse,
            request_options=request_options,
        )

    def update_email_config(
        self,
        profile_id: str,
        data: MessagingProfileUpdateEmailConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateEmailConfigResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/emails-config',
            body=data,
            cast_to=MessagingProfileUpdateEmailConfigResponse,
            request_options=request_options,
        )

    def update_multisend_config(
        self,
        profile_id: str,
        data: MessagingProfileUpdateMultisendConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateMultisendConfigResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/multisend-config',
            body=data,
            cast_to=MessagingProfileUpdateMultisendConfigResponse,
            request_options=request_options,
        )

    def update_verifications_config(
        self,
        profile_id: str,
        data: MessagingProfileUpdateVerificationsConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateVerificationsConfigResponse:
        return self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/verifications-config',
            body=data,
            cast_to=MessagingProfileUpdateVerificationsConfigResponse,
            request_options=request_options,
        )

    def list(
        self,
        data: MessagingProfileListRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingProfileListItem]:
        return self._client.request(
            'POST',
            'messaging/profiles/retrieve',
            body=data,
            cast_to=Page[MessagingProfileListItem],
            request_options=request_options,
        )


class AsyncMessagingProfilesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create(
        self,
        data: MessagingProfileCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCreateResponse:
        return await self._client.request(
            'POST',
            'messaging/profiles/',
            body=data,
            cast_to=MessagingProfileCreateResponse,
            request_options=request_options,
        )

    async def enable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileEnableResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/enable',
            cast_to=MessagingProfileEnableResponse,
            request_options=request_options,
        )

    async def disable(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDisableResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/disable',
            cast_to=MessagingProfileDisableResponse,
            request_options=request_options,
        )

    async def close(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileCloseResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/close',
            cast_to=MessagingProfileCloseResponse,
            request_options=request_options,
        )

    async def read(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileReadResponse:
        return await self._client.request(
            'GET',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileReadResponse,
            request_options=request_options,
        )

    async def update(
        self,
        profile_id: str,
        data: MessagingProfileUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            body=data,
            cast_to=MessagingProfileUpdateResponse,
            request_options=request_options,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/profiles/{encode_path_param(profile_id)}',
            cast_to=MessagingProfileDeleteResponse,
            request_options=request_options,
        )

    async def update_email_config(
        self,
        profile_id: str,
        data: MessagingProfileUpdateEmailConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateEmailConfigResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/emails-config',
            body=data,
            cast_to=MessagingProfileUpdateEmailConfigResponse,
            request_options=request_options,
        )

    async def update_multisend_config(
        self,
        profile_id: str,
        data: MessagingProfileUpdateMultisendConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateMultisendConfigResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/multisend-config',
            body=data,
            cast_to=MessagingProfileUpdateMultisendConfigResponse,
            request_options=request_options,
        )

    async def update_verifications_config(
        self,
        profile_id: str,
        data: MessagingProfileUpdateVerificationsConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingProfileUpdateVerificationsConfigResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/profiles/{encode_path_param(profile_id)}/verifications-config',
            body=data,
            cast_to=MessagingProfileUpdateVerificationsConfigResponse,
            request_options=request_options,
        )

    async def list(
        self,
        data: MessagingProfileListRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingProfileListItem]:
        return await self._client.request(
            'POST',
            'messaging/profiles/retrieve',
            body=data,
            cast_to=AsyncPage[MessagingProfileListItem],
            request_options=request_options,
        )
