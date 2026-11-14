from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AiBYOKCreateByokConfigRequest,
    AiBYOKCreateByokConfigResponse,
    AiBYOKDeleteByokConfigResponse,
    AiBYOKListByokConfigsItem,
    AiBYOKListByokConfigsQuery,
    AiBYOKReadByokConfigResponse,
    AiBYOKTestByokConnectionResponse,
    AiBYOKUpdateByokConfigRequest,
    AiBYOKUpdateByokConfigResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AiBYOKsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list_byok_configs(
        self,
        query: AiBYOKListByokConfigsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiBYOKListByokConfigsItem]:
        return self._client.request(
            'GET',
            'ai/byok/',
            query=query,
            cast_to=Page[AiBYOKListByokConfigsItem],
            request_options=request_options,
        )

    def create_byok_config(
        self,
        data: AiBYOKCreateByokConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKCreateByokConfigResponse:
        return self._client.request(
            'POST',
            'ai/byok/',
            body=data,
            cast_to=AiBYOKCreateByokConfigResponse,
            request_options=request_options,
        )

    def read_byok_config(
        self,
        byok_config_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKReadByokConfigResponse:
        return self._client.request(
            'GET',
            f'ai/byok/{encode_path_param(byok_config_id)}',
            cast_to=AiBYOKReadByokConfigResponse,
            request_options=request_options,
        )

    def update_byok_config(
        self,
        byok_config_id: str,
        data: AiBYOKUpdateByokConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKUpdateByokConfigResponse:
        return self._client.request(
            'PATCH',
            f'ai/byok/{encode_path_param(byok_config_id)}',
            body=data,
            cast_to=AiBYOKUpdateByokConfigResponse,
            request_options=request_options,
        )

    def delete_byok_config(
        self,
        byok_config_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKDeleteByokConfigResponse:
        return self._client.request(
            'DELETE',
            f'ai/byok/{encode_path_param(byok_config_id)}',
            cast_to=AiBYOKDeleteByokConfigResponse,
            request_options=request_options,
        )

    def test_byok_connection(
        self,
        byok_config_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKTestByokConnectionResponse:
        return self._client.request(
            'POST',
            f'ai/byok/{encode_path_param(byok_config_id)}/test',
            cast_to=AiBYOKTestByokConnectionResponse,
            request_options=request_options,
        )


class AsyncAiBYOKsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list_byok_configs(
        self,
        query: AiBYOKListByokConfigsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiBYOKListByokConfigsItem]:
        return await self._client.request(
            'GET',
            'ai/byok/',
            query=query,
            cast_to=AsyncPage[AiBYOKListByokConfigsItem],
            request_options=request_options,
        )

    async def create_byok_config(
        self,
        data: AiBYOKCreateByokConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKCreateByokConfigResponse:
        return await self._client.request(
            'POST',
            'ai/byok/',
            body=data,
            cast_to=AiBYOKCreateByokConfigResponse,
            request_options=request_options,
        )

    async def read_byok_config(
        self,
        byok_config_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKReadByokConfigResponse:
        return await self._client.request(
            'GET',
            f'ai/byok/{encode_path_param(byok_config_id)}',
            cast_to=AiBYOKReadByokConfigResponse,
            request_options=request_options,
        )

    async def update_byok_config(
        self,
        byok_config_id: str,
        data: AiBYOKUpdateByokConfigRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKUpdateByokConfigResponse:
        return await self._client.request(
            'PATCH',
            f'ai/byok/{encode_path_param(byok_config_id)}',
            body=data,
            cast_to=AiBYOKUpdateByokConfigResponse,
            request_options=request_options,
        )

    async def delete_byok_config(
        self,
        byok_config_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKDeleteByokConfigResponse:
        return await self._client.request(
            'DELETE',
            f'ai/byok/{encode_path_param(byok_config_id)}',
            cast_to=AiBYOKDeleteByokConfigResponse,
            request_options=request_options,
        )

    async def test_byok_connection(
        self,
        byok_config_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiBYOKTestByokConnectionResponse:
        return await self._client.request(
            'POST',
            f'ai/byok/{encode_path_param(byok_config_id)}/test',
            cast_to=AiBYOKTestByokConnectionResponse,
            request_options=request_options,
        )
