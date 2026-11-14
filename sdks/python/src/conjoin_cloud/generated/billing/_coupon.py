from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    BillingCouponCreateRequest,
    BillingCouponCreateResponse,
    BillingCouponDeleteResponse,
    BillingCouponListCountQuery,
    BillingCouponListCountResponse,
    BillingCouponListItem,
    BillingCouponListQuery,
    BillingCouponUpdateRequest,
    BillingCouponUpdateResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class BillingCouponsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: BillingCouponListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[BillingCouponListItem]:
        return self._client.request(
            'GET',
            'billing/coupons/',
            query=query,
            cast_to=Page[BillingCouponListItem],
            request_options=request_options,
        )

    def create(
        self,
        data: BillingCouponCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponCreateResponse:
        return self._client.request(
            'POST',
            'billing/coupons/',
            body=data,
            cast_to=BillingCouponCreateResponse,
            request_options=request_options,
        )

    def list_count(
        self,
        query: BillingCouponListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponListCountResponse:
        return self._client.request(
            'GET',
            'billing/coupons/count',
            query=query,
            cast_to=BillingCouponListCountResponse,
            request_options=request_options,
        )

    def update(
        self,
        coupon_id: str,
        data: BillingCouponUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponUpdateResponse:
        return self._client.request(
            'PATCH',
            f'billing/coupons/{encode_path_param(coupon_id)}',
            body=data,
            cast_to=BillingCouponUpdateResponse,
            request_options=request_options,
        )

    def delete(
        self,
        coupon_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponDeleteResponse:
        return self._client.request(
            'DELETE',
            f'billing/coupons/{encode_path_param(coupon_id)}',
            cast_to=BillingCouponDeleteResponse,
            request_options=request_options,
        )


class AsyncBillingCouponsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: BillingCouponListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[BillingCouponListItem]:
        return await self._client.request(
            'GET',
            'billing/coupons/',
            query=query,
            cast_to=AsyncPage[BillingCouponListItem],
            request_options=request_options,
        )

    async def create(
        self,
        data: BillingCouponCreateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponCreateResponse:
        return await self._client.request(
            'POST',
            'billing/coupons/',
            body=data,
            cast_to=BillingCouponCreateResponse,
            request_options=request_options,
        )

    async def list_count(
        self,
        query: BillingCouponListCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponListCountResponse:
        return await self._client.request(
            'GET',
            'billing/coupons/count',
            query=query,
            cast_to=BillingCouponListCountResponse,
            request_options=request_options,
        )

    async def update(
        self,
        coupon_id: str,
        data: BillingCouponUpdateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponUpdateResponse:
        return await self._client.request(
            'PATCH',
            f'billing/coupons/{encode_path_param(coupon_id)}',
            body=data,
            cast_to=BillingCouponUpdateResponse,
            request_options=request_options,
        )

    async def delete(
        self,
        coupon_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> BillingCouponDeleteResponse:
        return await self._client.request(
            'DELETE',
            f'billing/coupons/{encode_path_param(coupon_id)}',
            cast_to=BillingCouponDeleteResponse,
            request_options=request_options,
        )
