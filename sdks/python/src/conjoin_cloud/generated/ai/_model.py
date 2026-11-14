from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AiModelListItem,
    AiModelListQuery,
    AiModelReadResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AiModelsResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def list(
        self,
        query: AiModelListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiModelListItem]:
        return self._client.request(
            'GET',
            'ai/model/models',
            query=query,
            cast_to=Page[AiModelListItem],
            request_options=request_options,
        )

    def read(
        self,
        model_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiModelReadResponse:
        return self._client.request(
            'GET',
            f'ai/model/models/{encode_path_param(model_id)}',
            cast_to=AiModelReadResponse,
            request_options=request_options,
        )


class AsyncAiModelsResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def list(
        self,
        query: AiModelListQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiModelListItem]:
        return await self._client.request(
            'GET',
            'ai/model/models',
            query=query,
            cast_to=AsyncPage[AiModelListItem],
            request_options=request_options,
        )

    async def read(
        self,
        model_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiModelReadResponse:
        return await self._client.request(
            'GET',
            f'ai/model/models/{encode_path_param(model_id)}',
            cast_to=AiModelReadResponse,
            request_options=request_options,
        )
