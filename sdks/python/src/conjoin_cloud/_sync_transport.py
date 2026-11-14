from __future__ import annotations

import time
from typing import Any

import httpx

from conjoin_cloud._call import PreparedCall
from conjoin_cloud._config import ResolvedConfig
from conjoin_cloud._error_response import MAX_ERROR_BODY_BYTES, build_api_error
from conjoin_cloud._errors import ConjoinApiError, ConjoinResponseError
from conjoin_cloud._response_parsing import parse_body, response_request_id, transport_error
from conjoin_cloud._retry import (
    RETRY_AFTER_HEADER,
    compute_retry_delay,
    is_retryable_status,
    parse_retry_after,
)

MAX_SUCCESS_BODY_BYTES = 16 * 1024 * 1024
BUFFERED_BODY_EXTENSION = "conjoin_buffered_body"


def send_call(
    client: httpx.Client,
    config: ResolvedConfig,
    call: PreparedCall,
    *,
    buffer_response: bool = False,
) -> httpx.Response:
    request = client.build_request(
        call.method,
        call.url,
        headers=call.headers,
        content=call.content,
        files=call.files,
        timeout=call.timeout,
    )
    attempt = 0

    while True:
        can_retry_again = call.retry_allowed and attempt < call.max_retries
        try:
            response = client.send(request, stream=True)
            if buffer_response and response.is_success:
                response.extensions[BUFFERED_BODY_EXTENSION] = _read_success(
                    response, call.request_id
                )
        except httpx.TransportError as exc:
            if not can_retry_again:
                raise transport_error(
                    exc, timeout=call.timeout, request_id=call.request_id
                ) from exc
            _sleep_before_retry(config, attempt, None)
            attempt += 1
            continue
        except httpx.HTTPError as exc:
            raise transport_error(exc, timeout=call.timeout, request_id=call.request_id) from exc

        if can_retry_again and is_retryable_status(response.status_code):
            retry_after = parse_retry_after(response.headers.get(RETRY_AFTER_HEADER))
            response.close()
            _sleep_before_retry(config, attempt, retry_after)
            attempt += 1
            continue

        return response


def read_response(
    response: httpx.Response,
    call: PreparedCall,
    *,
    cast_to: Any,
    strict: bool,
    unwrap_data: bool,
) -> tuple[Any, str]:
    request_id = response_request_id(response, call.request_id)

    if response.status_code >= 400:
        raise read_api_error(response, request_id)

    try:
        content = response.extensions.get(BUFFERED_BODY_EXTENSION)
        if content is None:
            content = _read_success(response, call.request_id)
    except httpx.HTTPError as exc:
        raise transport_error(exc, timeout=call.timeout, request_id=call.request_id) from exc
    finally:
        response.close()

    data = parse_body(
        response,
        content,
        request_id=request_id,
        cast_to=cast_to,
        strict=strict,
        unwrap_data=unwrap_data,
    )
    return data, request_id


def _read_success(response: httpx.Response, request_id: str) -> bytes:
    collected = bytearray()
    try:
        for chunk in response.iter_bytes():
            if len(collected) + len(chunk) > MAX_SUCCESS_BODY_BYTES:
                raise ConjoinResponseError(
                    "The response body exceeded the size limit",
                    status=response.status_code,
                    request_id=request_id,
                )
            collected.extend(chunk)
    finally:
        response.close()
    return bytes(collected)


def read_api_error(response: httpx.Response, request_id: str) -> ConjoinApiError:
    return build_api_error(
        status=response.status_code,
        reason=response.reason_phrase,
        headers=response.headers,
        body=_read_bounded(response, MAX_ERROR_BODY_BYTES),
        request_id=request_id,
    )


def _read_bounded(response: httpx.Response, limit: int) -> bytes:
    collected = bytearray()
    try:
        for chunk in response.iter_bytes():
            collected.extend(chunk[: limit - len(collected)])
            if len(collected) >= limit:
                break
    except httpx.HTTPError:
        return bytes(collected)
    finally:
        response.close()
    return bytes(collected)


def _sleep_before_retry(config: ResolvedConfig, attempt: int, retry_after: float | None) -> None:
    time.sleep(
        compute_retry_delay(
            attempt,
            backoff_seconds=config.backoff_seconds,
            max_delay_seconds=config.max_retry_delay_seconds,
            retry_after=retry_after,
        )
    )
