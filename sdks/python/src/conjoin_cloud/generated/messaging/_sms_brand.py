from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    MessagingSMSBrandCreateSmsBrandResponse,
    MessagingSMSBrandDeleteSmsBrandResponse,
    MessagingSMSBrandListSmsBrandsItem,
    MessagingSMSBrandListSmsBrandsRequest,
    MessagingSMSBrandReadSmsBrandResponse,
    MessagingSMSBrandUpdateSmsBrandRequest,
    MessagingSMSBrandUpdateSmsBrandResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class MessagingSMSBrandsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_sms_brand(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandCreateSmsBrandResponse:
        return self._client.request(
            'POST',
            'messaging/sms/brands/',
            body=data,
            cast_to=MessagingSMSBrandCreateSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    def read_sms_brand(
        self,
        brand_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandReadSmsBrandResponse:
        return self._client.request(
            'GET',
            f'messaging/sms/brands/{encode_path_param(brand_id)}',
            cast_to=MessagingSMSBrandReadSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def update_sms_brand(
        self,
        brand_id: str,
        data: MessagingSMSBrandUpdateSmsBrandRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandUpdateSmsBrandResponse:
        return self._client.request(
            'PATCH',
            f'messaging/sms/brands/{encode_path_param(brand_id)}',
            body=data,
            cast_to=MessagingSMSBrandUpdateSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def delete_sms_brand(
        self,
        brand_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandDeleteSmsBrandResponse:
        return self._client.request(
            'DELETE',
            f'messaging/sms/brands/{encode_path_param(brand_id)}',
            cast_to=MessagingSMSBrandDeleteSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    def list_sms_brands(
        self,
        data: MessagingSMSBrandListSmsBrandsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[MessagingSMSBrandListSmsBrandsItem]:
        return self._client.request(
            'POST',
            'messaging/sms/brands/retrieve',
            body=data,
            cast_to=Page[MessagingSMSBrandListSmsBrandsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
            cursor_location='body',
        )


class AsyncMessagingSMSBrandsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_sms_brand(
        self,
        data: Mapping[str, Any],
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandCreateSmsBrandResponse:
        return await self._client.request(
            'POST',
            'messaging/sms/brands/',
            body=data,
            cast_to=MessagingSMSBrandCreateSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
        )

    async def read_sms_brand(
        self,
        brand_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandReadSmsBrandResponse:
        return await self._client.request(
            'GET',
            f'messaging/sms/brands/{encode_path_param(brand_id)}',
            cast_to=MessagingSMSBrandReadSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def update_sms_brand(
        self,
        brand_id: str,
        data: MessagingSMSBrandUpdateSmsBrandRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandUpdateSmsBrandResponse:
        return await self._client.request(
            'PATCH',
            f'messaging/sms/brands/{encode_path_param(brand_id)}',
            body=data,
            cast_to=MessagingSMSBrandUpdateSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def delete_sms_brand(
        self,
        brand_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> MessagingSMSBrandDeleteSmsBrandResponse:
        return await self._client.request(
            'DELETE',
            f'messaging/sms/brands/{encode_path_param(brand_id)}',
            cast_to=MessagingSMSBrandDeleteSmsBrandResponse,
            request_options=request_options,
            scopes=('messaging_profile_id',),
        )

    async def list_sms_brands(
        self,
        data: MessagingSMSBrandListSmsBrandsRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[MessagingSMSBrandListSmsBrandsItem]:
        return await self._client.request(
            'POST',
            'messaging/sms/brands/retrieve',
            body=data,
            cast_to=AsyncPage[MessagingSMSBrandListSmsBrandsItem],
            request_options=request_options,
            scopes=('messaging_profile_id',),
            accepts_idempotency_key=True,
            cursor_location='body',
        )
