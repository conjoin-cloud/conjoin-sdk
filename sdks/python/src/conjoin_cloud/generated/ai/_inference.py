from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    AiInferenceCreateAiBestOfNRequest,
    AiInferenceCreateAiBestOfNResponse,
    AiInferenceCreateAiMultiModelRequest,
    AiInferenceCreateAiMultiModelResponse,
    AiInferenceCreateChatCompletionRequest,
    AiInferenceCreateChatCompletionResponse,
    AiInferenceListRequestsCountQuery,
    AiInferenceListRequestsCountResponse,
    AiInferenceListRequestsItem,
    AiInferenceListRequestsQuery,
    AiInferenceReadRequestResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class AiInferencesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def create_chat_completion(
        self,
        data: AiInferenceCreateChatCompletionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateChatCompletionResponse:
        return self._client.request(
            'POST',
            'ai/inference/chat/completions',
            body=data,
            cast_to=AiInferenceCreateChatCompletionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    def create_ai_multi_model(
        self,
        data: AiInferenceCreateAiMultiModelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateAiMultiModelResponse:
        return self._client.request(
            'POST',
            'ai/multi-model-inferences/',
            body=data,
            cast_to=AiInferenceCreateAiMultiModelResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def create_ai_best_of_n(
        self,
        data: AiInferenceCreateAiBestOfNRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateAiBestOfNResponse:
        return self._client.request(
            'POST',
            'ai/best-of-n-inferences/',
            body=data,
            cast_to=AiInferenceCreateAiBestOfNResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def list_requests(
        self,
        query: AiInferenceListRequestsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[AiInferenceListRequestsItem]:
        return self._client.request(
            'GET',
            'ai/inference-requests/',
            query=query,
            cast_to=Page[AiInferenceListRequestsItem],
            request_options=request_options,
        )

    def list_requests_count(
        self,
        query: AiInferenceListRequestsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceListRequestsCountResponse:
        return self._client.request(
            'GET',
            'ai/inference-requests/count',
            query=query,
            cast_to=AiInferenceListRequestsCountResponse,
            request_options=request_options,
        )

    def read_request(
        self,
        inference_request_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceReadRequestResponse:
        return self._client.request(
            'GET',
            f'ai/inference-requests/{encode_path_param(inference_request_id)}',
            cast_to=AiInferenceReadRequestResponse,
            request_options=request_options,
        )


class AsyncAiInferencesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def create_chat_completion(
        self,
        data: AiInferenceCreateChatCompletionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateChatCompletionResponse:
        return await self._client.request(
            'POST',
            'ai/inference/chat/completions',
            body=data,
            cast_to=AiInferenceCreateChatCompletionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
            unwrap_data=False,
        )

    async def create_ai_multi_model(
        self,
        data: AiInferenceCreateAiMultiModelRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateAiMultiModelResponse:
        return await self._client.request(
            'POST',
            'ai/multi-model-inferences/',
            body=data,
            cast_to=AiInferenceCreateAiMultiModelResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def create_ai_best_of_n(
        self,
        data: AiInferenceCreateAiBestOfNRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateAiBestOfNResponse:
        return await self._client.request(
            'POST',
            'ai/best-of-n-inferences/',
            body=data,
            cast_to=AiInferenceCreateAiBestOfNResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def list_requests(
        self,
        query: AiInferenceListRequestsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[AiInferenceListRequestsItem]:
        return await self._client.request(
            'GET',
            'ai/inference-requests/',
            query=query,
            cast_to=AsyncPage[AiInferenceListRequestsItem],
            request_options=request_options,
        )

    async def list_requests_count(
        self,
        query: AiInferenceListRequestsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceListRequestsCountResponse:
        return await self._client.request(
            'GET',
            'ai/inference-requests/count',
            query=query,
            cast_to=AiInferenceListRequestsCountResponse,
            request_options=request_options,
        )

    async def read_request(
        self,
        inference_request_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceReadRequestResponse:
        return await self._client.request(
            'GET',
            f'ai/inference-requests/{encode_path_param(inference_request_id)}',
            cast_to=AiInferenceReadRequestResponse,
            request_options=request_options,
        )
