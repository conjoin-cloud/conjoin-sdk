from __future__ import annotations

import json
from functools import lru_cache
from typing import Any, get_origin

import httpx
from pydantic import TypeAdapter, ValidationError

from conjoin_cloud._errors import (
    ConjoinError,
    ConjoinNetworkError,
    ConjoinResponseError,
    ConjoinTimeoutError,
)
from conjoin_cloud._models import ConjoinModel, ListPage
from conjoin_cloud._request_tracing import CONJOIN_REQUEST_ID_HEADER, is_valid_conjoin_request_id
from conjoin_cloud._response import WithResponse

_TYPE_ADAPTER_CACHE_SIZE = 2048


def response_request_id(response: httpx.Response, sent_request_id: str) -> str:
    returned = response.headers.get(CONJOIN_REQUEST_ID_HEADER)
    return returned if is_valid_conjoin_request_id(returned) else sent_request_id


def transport_error(
    error: httpx.HTTPError,
    *,
    timeout: float,
    request_id: str | None,
) -> ConjoinError:
    if isinstance(error, httpx.TimeoutException):
        return ConjoinTimeoutError(f"Request timed out after {timeout:g}s", request_id=request_id)
    return ConjoinNetworkError(str(error) or "Network request failed", request_id=request_id)


def parse_body(
    response: httpx.Response,
    content: bytes,
    *,
    request_id: str,
    cast_to: Any,
    strict: bool,
    unwrap_data: bool,
) -> Any:
    if not content:
        payload: Any = None
    else:
        try:
            payload = json.loads(content.decode("utf-8"))
        except (UnicodeDecodeError, ValueError, RecursionError) as exc:
            raise ConjoinResponseError(
                "The response body was not valid JSON",
                status=response.status_code,
                request_id=request_id,
            ) from exc

    expects_list_page = _expects_list_page(cast_to)
    if not expects_list_page and unwrap_data and isinstance(payload, dict) and "data" in payload:
        payload = payload["data"]

    if cast_to is None:
        return payload

    try:
        parsed = _type_adapter(cast_to).validate_python(payload, strict=strict)
    except ValidationError as exc:
        raise ConjoinResponseError(
            "The response body did not match the expected schema",
            status=response.status_code,
            request_id=request_id,
        ) from exc

    _attach_request_id(parsed, request_id)
    if isinstance(parsed, ListPage):
        parsed._status = response.status_code
    return parsed


def with_response(response: httpx.Response, data: Any, request_id: str) -> WithResponse[Any]:
    return WithResponse(
        data=data,
        status_code=response.status_code,
        headers=dict(response.headers),
        request_id=request_id,
    )


def _attach_request_id(value: Any, request_id: str) -> None:
    if isinstance(value, ConjoinModel):
        value._set_request_id(request_id)

    if isinstance(value, ListPage):
        for item in value.data:
            if isinstance(item, ConjoinModel):
                item._set_request_id(request_id)


def _expects_list_page(cast_to: Any) -> bool:
    origin = get_origin(cast_to) or cast_to
    return isinstance(origin, type) and issubclass(origin, ListPage)


def _type_adapter(cast_to: Any) -> TypeAdapter[Any]:
    try:
        return _cached_type_adapter(cast_to)
    except TypeError:
        return TypeAdapter(cast_to)


@lru_cache(maxsize=_TYPE_ADAPTER_CACHE_SIZE)
def _cached_type_adapter(cast_to: Any) -> TypeAdapter[Any]:
    return TypeAdapter(cast_to)
