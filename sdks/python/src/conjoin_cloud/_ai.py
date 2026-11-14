from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Any, cast

import httpx
from pydantic import ValidationError

from conjoin_cloud import _async_transport, _sync_transport
from conjoin_cloud._ai_models import ChatCompletionChunk
from conjoin_cloud._call import PreparedCall, prepare_call
from conjoin_cloud._errors import ConjoinApiError, ConjoinConfigurationError, ConjoinResponseError
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._response_parsing import response_request_id, transport_error
from conjoin_cloud._sse import aiter_sse_events, iter_sse_events
from conjoin_cloud.generated._models import (
    AiInferenceCreateChatCompletionRequest,
    AiInferenceCreateChatCompletionResponse,
)
from conjoin_cloud.generated.ai import AiResource as GeneratedAiResource
from conjoin_cloud.generated.ai import AsyncAiResource as GeneratedAsyncAiResource

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin
    from conjoin_cloud.generated.ai import AiInferencesResource, AsyncAiInferencesResource

CHAT_COMPLETIONS_PATH = "ai/inference/chat/completions"
CHAT_COMPLETION_ACCEPTS_IDEMPOTENCY_KEY = False
STREAM_DONE_MARKER = "[DONE]"
MAX_REPORTED_CHUNK_CHARACTERS = 200


class AiResource(GeneratedAiResource):
    def __init__(self, client: Conjoin) -> None:
        super().__init__(client)
        self.chat = AiChatResource(client, self.inferences)


class AsyncAiResource(GeneratedAsyncAiResource):
    def __init__(self, client: AsyncConjoin) -> None:
        super().__init__(client)
        self.chat = AsyncAiChatResource(client, self.inferences)


class AiChatResource:
    def __init__(self, client: Conjoin, inferences: AiInferencesResource) -> None:
        self._client = client
        self._inferences = inferences

    def complete(
        self,
        *,
        model: str,
        messages: Sequence[Mapping[str, Any]],
        temperature: float | None = None,
        top_p: float | None = None,
        max_tokens: int | None = None,
        stop: Sequence[str] | None = None,
        tools: Sequence[Mapping[str, Any]] | None = None,
        response_format: Mapping[str, Any] | None = None,
        context: Mapping[str, Any] | None = None,
        metadata: Mapping[str, Any] | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateChatCompletionResponse:
        body = chat_body(
            model=model,
            messages=messages,
            stream=False,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            stop=stop,
            tools=tools,
            response_format=response_format,
            context=context,
            metadata=metadata,
        )
        return self._inferences.create_chat_completion(body, request_options=request_options)

    def stream(
        self,
        *,
        model: str,
        messages: Sequence[Mapping[str, Any]],
        temperature: float | None = None,
        top_p: float | None = None,
        max_tokens: int | None = None,
        stop: Sequence[str] | None = None,
        tools: Sequence[Mapping[str, Any]] | None = None,
        response_format: Mapping[str, Any] | None = None,
        context: Mapping[str, Any] | None = None,
        metadata: Mapping[str, Any] | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Iterator[ChatCompletionChunk]:
        body = chat_body(
            model=model,
            messages=messages,
            stream=True,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            stop=stop,
            tools=tools,
            response_format=response_format,
            context=context,
            metadata=metadata,
        )
        call = _prepare_stream_call(self._client, body, request_options)
        return _iter_chat_stream(self._client, call)


class AsyncAiChatResource:
    def __init__(self, client: AsyncConjoin, inferences: AsyncAiInferencesResource) -> None:
        self._client = client
        self._inferences = inferences

    async def complete(
        self,
        *,
        model: str,
        messages: Sequence[Mapping[str, Any]],
        temperature: float | None = None,
        top_p: float | None = None,
        max_tokens: int | None = None,
        stop: Sequence[str] | None = None,
        tools: Sequence[Mapping[str, Any]] | None = None,
        response_format: Mapping[str, Any] | None = None,
        context: Mapping[str, Any] | None = None,
        metadata: Mapping[str, Any] | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AiInferenceCreateChatCompletionResponse:
        body = chat_body(
            model=model,
            messages=messages,
            stream=False,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            stop=stop,
            tools=tools,
            response_format=response_format,
            context=context,
            metadata=metadata,
        )
        return await self._inferences.create_chat_completion(body, request_options=request_options)

    def stream(
        self,
        *,
        model: str,
        messages: Sequence[Mapping[str, Any]],
        temperature: float | None = None,
        top_p: float | None = None,
        max_tokens: int | None = None,
        stop: Sequence[str] | None = None,
        tools: Sequence[Mapping[str, Any]] | None = None,
        response_format: Mapping[str, Any] | None = None,
        context: Mapping[str, Any] | None = None,
        metadata: Mapping[str, Any] | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncIterator[ChatCompletionChunk]:
        body = chat_body(
            model=model,
            messages=messages,
            stream=True,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            stop=stop,
            tools=tools,
            response_format=response_format,
            context=context,
            metadata=metadata,
        )
        call = _prepare_stream_call(self._client, body, request_options)
        return _aiter_chat_stream(self._client, call)


def chat_body(
    *,
    model: str,
    messages: Sequence[Mapping[str, Any]],
    stream: bool,
    temperature: float | None,
    top_p: float | None,
    max_tokens: int | None,
    stop: Sequence[str] | None,
    tools: Sequence[Mapping[str, Any]] | None,
    response_format: Mapping[str, Any] | None,
    context: Mapping[str, Any] | None,
    metadata: Mapping[str, Any] | None,
) -> AiInferenceCreateChatCompletionRequest:
    if not isinstance(model, str) or not model.strip():
        raise ConjoinConfigurationError("model must not be empty")
    if not messages:
        raise ConjoinConfigurationError("messages must not be empty")

    body: dict[str, Any] = {
        "model": model,
        "messages": [dict(message) for message in messages],
        "stream": stream,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "stop": list(stop) if stop is not None else None,
        "tools": [dict(tool) for tool in tools] if tools is not None else None,
        "response_format": dict(response_format) if response_format is not None else None,
        "context": dict(context) if context is not None else None,
        "metadata": dict(metadata) if metadata is not None else None,
    }
    return cast(
        AiInferenceCreateChatCompletionRequest,
        {key: value for key, value in body.items() if value is not None},
    )


def _prepare_stream_call(
    client: Conjoin | AsyncConjoin,
    body: AiInferenceCreateChatCompletionRequest,
    request_options: RequestOptions | Mapping[str, Any] | None,
) -> PreparedCall:
    return prepare_call(
        client.config,
        "POST",
        CHAT_COMPLETIONS_PATH,
        query=None,
        body=body,
        request_options=request_options,
        scopes=(),
        accepts_idempotency_key=CHAT_COMPLETION_ACCEPTS_IDEMPOTENCY_KEY,
        default_auth=None,
    )


def _iter_chat_stream(client: Conjoin, call: PreparedCall) -> Iterator[ChatCompletionChunk]:
    response = _sync_transport.send_call(client._client, client.config, call)
    try:
        request_id = response_request_id(response, call.request_id)
        if response.status_code >= 400:
            raise _sync_transport.read_api_error(response, request_id)
        status = response.status_code
        events = iter_sse_events(response.iter_bytes(), status=status, request_id=request_id)
        try:
            for event in events:
                if event.data == STREAM_DONE_MARKER:
                    return
                yield parse_chat_chunk(event.data, status=status, request_id=request_id)
        except httpx.HTTPError as exc:
            raise transport_error(exc, timeout=call.timeout, request_id=request_id) from exc
    finally:
        response.close()


async def _aiter_chat_stream(
    client: AsyncConjoin,
    call: PreparedCall,
) -> AsyncIterator[ChatCompletionChunk]:
    response = await _async_transport.send_call(client._client, client.config, call)
    try:
        request_id = response_request_id(response, call.request_id)
        if response.status_code >= 400:
            raise await _async_transport.read_api_error(response, request_id)
        status = response.status_code
        events = aiter_sse_events(response.aiter_bytes(), status=status, request_id=request_id)
        try:
            async for event in events:
                if event.data == STREAM_DONE_MARKER:
                    return
                yield parse_chat_chunk(event.data, status=status, request_id=request_id)
        except httpx.HTTPError as exc:
            raise transport_error(exc, timeout=call.timeout, request_id=request_id) from exc
    finally:
        await response.aclose()


def parse_chat_chunk(event_data: str, *, status: int, request_id: str) -> ChatCompletionChunk:
    try:
        payload = json.loads(event_data)
    except (ValueError, RecursionError) as exc:
        raise ConjoinResponseError(
            "The stream sent a chunk that is not JSON: "
            f"{event_data[:MAX_REPORTED_CHUNK_CHARACTERS]}",
            status=status,
            request_id=request_id,
        ) from exc

    if isinstance(payload, Mapping):
        error = payload.get("error")
        if isinstance(error, Mapping):
            message = error.get("message")
            code = error.get("code")
            if not isinstance(message, str) or not message.strip():
                message = "The stream reported an error"
            raise ConjoinApiError(
                message,
                code=code if isinstance(code, str) and code.strip() else "stream_error",
                status=status,
                request_id=request_id,
            )

    try:
        chunk = ChatCompletionChunk.model_validate(payload)
    except ValidationError as exc:
        raise ConjoinResponseError(
            "The stream sent a chunk that did not match the expected schema",
            status=status,
            request_id=request_id,
        ) from exc

    chunk._set_request_id(request_id)
    return chunk
