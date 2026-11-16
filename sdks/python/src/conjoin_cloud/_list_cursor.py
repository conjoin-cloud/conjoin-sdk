from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, replace
from typing import Any, Literal

from conjoin_cloud._errors import ConjoinConfigurationError
from conjoin_cloud._idempotency import generate_idempotency_key
from conjoin_cloud._request_options import RequestOptions, coerce_request_options

CursorLocation = Literal["query", "body", "none"]


@dataclass(frozen=True)
class NextPageRequest:
    query: Mapping[str, Any] | None
    body: Any
    request_options: RequestOptions | Mapping[str, Any] | None


def next_page_request(
    cursor_location: CursorLocation,
    next_cursor: str,
    *,
    query: Mapping[str, Any] | None,
    body: Any,
    request_options: RequestOptions | Mapping[str, Any] | None,
    accepts_idempotency_key: bool,
) -> NextPageRequest:
    if cursor_location != "body":
        return NextPageRequest(
            query={**(query or {}), "cursor": {"next": next_cursor}},
            body=body,
            request_options=request_options,
        )

    if body is not None and not isinstance(body, Mapping):
        raise ConjoinConfigurationError("A list request body must be a mapping")

    options = coerce_request_options(request_options)
    if accepts_idempotency_key:
        options = replace(options, idempotency_key=generate_idempotency_key())

    return NextPageRequest(
        query=query,
        body={**(body or {}), "cursor": {"next": next_cursor}},
        request_options=options,
    )
