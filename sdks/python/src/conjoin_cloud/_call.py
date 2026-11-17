from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

from conjoin_cloud._config import (
    ResolvedConfig,
    ScopeName,
    require_positive_seconds,
    require_retry_count,
)
from conjoin_cloud._declared_headers import DeclaredHeader
from conjoin_cloud._errors import ConjoinConfigurationError
from conjoin_cloud._idempotency import (
    IDEMPOTENCY_KEY_HEADER,
    generate_idempotency_key,
    validate_idempotency_key,
)
from conjoin_cloud._multipart import MultipartBody, MultipartPart
from conjoin_cloud._request_headers import build_request_headers, read_header_value
from conjoin_cloud._request_options import (
    AuthOverride,
    DeclaredAuth,
    RequestOptions,
    coerce_request_options,
    resolve_auth_override,
)
from conjoin_cloud._request_tracing import (
    CONJOIN_REQUEST_ID_HEADER,
    generate_conjoin_request_id,
    is_valid_conjoin_request_id,
)
from conjoin_cloud._retry import can_retry_method
from conjoin_cloud._url import build_url

HTTP_METHODS = frozenset({"GET", "POST", "PUT", "PATCH", "DELETE"})


@dataclass(frozen=True)
class PreparedCall:
    method: str
    url: str
    headers: dict[str, str] = field(repr=False)
    content: bytes | None
    files: list[MultipartPart] | None
    timeout: float
    max_retries: int
    retry_allowed: bool
    request_id: str


def prepare_call(
    config: ResolvedConfig,
    method: str,
    path: str,
    *,
    query: Mapping[str, Any] | None,
    body: Any,
    request_options: RequestOptions | Mapping[str, Any] | None,
    scopes: Sequence[ScopeName],
    accepts_idempotency_key: bool,
    default_auth: AuthOverride | DeclaredAuth | None,
    declared_headers: Sequence[DeclaredHeader] = (),
) -> PreparedCall:
    options = coerce_request_options(request_options)
    override = resolve_auth_override(options.auth)
    if override is not None and _declares_its_credential(default_auth):
        raise ConjoinConfigurationError(
            "This call sends only the credential that its operation declares, "
            "so it does not take request_options.auth"
        )
    normalized_method = _normalize_method(method)
    url = build_url(config.base_url, path, query)
    request_id = _resolve_request_id(config, options)
    idempotency_key = _resolve_idempotency_key(
        normalized_method,
        options,
        accepts_idempotency_key=accepts_idempotency_key,
    )
    auth = override or default_auth or AuthOverride()
    content, files = _encode_body(body)
    headers = build_request_headers(
        config,
        caller_headers=options.headers,
        auth=auth,
        scopes=scopes,
        request_id=request_id,
        idempotency_key=idempotency_key,
        json_body=content is not None,
        declared_headers=declared_headers,
    )

    return PreparedCall(
        method=normalized_method,
        url=url,
        headers=headers,
        content=content,
        files=files,
        timeout=require_positive_seconds(
            "request_options.timeout", options.timeout, config.timeout
        ),
        max_retries=require_retry_count(
            "request_options.max_retries", options.max_retries, config.max_retries
        ),
        retry_allowed=can_retry_method(
            normalized_method,
            has_idempotency_key=idempotency_key is not None and accepts_idempotency_key,
        ),
        request_id=request_id,
    )


def _declares_its_credential(default_auth: AuthOverride | DeclaredAuth | None) -> bool:
    return isinstance(default_auth, DeclaredAuth) or (
        isinstance(default_auth, AuthOverride) and default_auth.type == "none"
    )


def _normalize_method(method: str) -> str:
    normalized = method.upper() if isinstance(method, str) else ""
    if normalized not in HTTP_METHODS:
        raise ConjoinConfigurationError("method must be GET, POST, PUT, PATCH, or DELETE")
    return normalized


def _resolve_request_id(config: ResolvedConfig, options: RequestOptions) -> str:
    for candidate in (
        options.conjoin_request_id,
        read_header_value(options.headers, CONJOIN_REQUEST_ID_HEADER),
        config.conjoin_request_id,
    ):
        if is_valid_conjoin_request_id(candidate):
            return candidate
    return generate_conjoin_request_id()


def _resolve_idempotency_key(
    method: str,
    options: RequestOptions,
    *,
    accepts_idempotency_key: bool,
) -> str | None:
    supplied = options.idempotency_key
    if supplied is None:
        supplied = read_header_value(options.headers, IDEMPOTENCY_KEY_HEADER)

    if supplied is not None:
        if method != "POST":
            raise ConjoinConfigurationError("Only a POST takes an idempotency key")
        return validate_idempotency_key(supplied)

    if method == "POST" and accepts_idempotency_key:
        return generate_idempotency_key()
    return None


def _encode_body(body: Any) -> tuple[bytes | None, list[MultipartPart] | None]:
    if body is None:
        return None, None

    if isinstance(body, MultipartBody):
        return None, body.to_httpx_files()

    try:
        text = json.dumps(body, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    except (TypeError, ValueError, RecursionError) as exc:
        raise ConjoinConfigurationError("The request body cannot be sent as JSON") from exc

    return text.encode("utf-8"), None
