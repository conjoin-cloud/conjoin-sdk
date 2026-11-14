from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    CloudPlanListItem,
    CloudPlanListQuery,
    CloudPlanReadCountQuery,
    CloudPlanReadCountResponse,
    CloudPlanReadResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class CloudPlansResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_account(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return self._client.request(
            'GET',
            'cloud/account/plan',
            request_options=request_options,
        )

    def list(
        self,
        query: CloudPlanListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[CloudPlanListItem]:
        return self._client.request(
            'GET',
            'cloud/plans/',
            query=query,
            cast_to=Page[CloudPlanListItem],
            request_options=request_options,
        )

    def read_count(
        self,
        query: CloudPlanReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPlanReadCountResponse:
        return self._client.request(
            'GET',
            'cloud/plans/count',
            query=query,
            cast_to=CloudPlanReadCountResponse,
            request_options=request_options,
        )

    def read(
        self,
        plan_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPlanReadResponse:
        return self._client.request(
            'GET',
            f'cloud/plans/{encode_path_param(plan_id)}',
            cast_to=CloudPlanReadResponse,
            request_options=request_options,
        )


class AsyncCloudPlansResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_account(
        self,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Any:
        return await self._client.request(
            'GET',
            'cloud/account/plan',
            request_options=request_options,
        )

    async def list(
        self,
        query: CloudPlanListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[CloudPlanListItem]:
        return await self._client.request(
            'GET',
            'cloud/plans/',
            query=query,
            cast_to=AsyncPage[CloudPlanListItem],
            request_options=request_options,
        )

    async def read_count(
        self,
        query: CloudPlanReadCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPlanReadCountResponse:
        return await self._client.request(
            'GET',
            'cloud/plans/count',
            query=query,
            cast_to=CloudPlanReadCountResponse,
            request_options=request_options,
        )

    async def read(
        self,
        plan_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> CloudPlanReadResponse:
        return await self._client.request(
            'GET',
            f'cloud/plans/{encode_path_param(plan_id)}',
            cast_to=CloudPlanReadResponse,
            request_options=request_options,
        )
