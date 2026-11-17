from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from conjoin_cloud._errors import (
    ConjoinApiError,
    ConjoinAuthenticationError,
    ConjoinConflictError,
    ConjoinInternalServerError,
    ConjoinNotFoundError,
    ConjoinPermissionDeniedError,
    ConjoinRateLimitError,
    ConjoinValidationError,
    ValidationFieldError,
)
from conjoin_cloud._retry import RETRY_AFTER_HEADER, parse_retry_after

MAX_ERROR_BODY_BYTES = 65_536

_FALLBACK_CODES: Mapping[int, str] = {
    400: "invalid_request",
    401: "authentication_failed",
    403: "permission_denied",
    404: "not_found",
    409: "conflict",
    422: "invalid_request",
    429: "rate_limited",
}

_API_ERROR_CLASSES: Mapping[int, type[ConjoinApiError]] = {
    401: ConjoinAuthenticationError,
    403: ConjoinPermissionDeniedError,
    404: ConjoinNotFoundError,
    409: ConjoinConflictError,
}


@dataclass(frozen=True)
class _ErrorBody:
    message: str
    code: str | None
    param: str | None
    details: Any


def build_api_error(
    *,
    status: int,
    reason: str,
    headers: Mapping[str, str],
    body: bytes,
    request_id: str | None,
) -> ConjoinApiError:
    parsed = _parse_error_body(body, reason or f"HTTP {status}")
    code = parsed.code if parsed.code is not None else _fallback_code(status)

    if status in (400, 422):
        return ConjoinValidationError(
            parsed.message,
            code=code,
            status=status,
            errors=_field_errors(parsed.details),
            param=parsed.param,
            details=parsed.details,
            request_id=request_id,
        )

    if status == 429:
        return ConjoinRateLimitError(
            parsed.message,
            code=code,
            status=status,
            retry_after=parse_retry_after(headers.get(RETRY_AFTER_HEADER)),
            param=parsed.param,
            details=parsed.details,
            request_id=request_id,
        )

    error_class = _API_ERROR_CLASSES.get(status)
    if error_class is None:
        error_class = ConjoinInternalServerError if status >= 500 else ConjoinApiError

    return error_class(
        parsed.message,
        code=code,
        status=status,
        param=parsed.param,
        details=parsed.details,
        request_id=request_id,
    )


def _parse_error_body(body: bytes, fallback_message: str) -> _ErrorBody:
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, RecursionError):
        return _ErrorBody(message=fallback_message, code=None, param=None, details=None)

    if not isinstance(payload, Mapping):
        return _ErrorBody(message=fallback_message, code=None, param=None, details=None)

    response = payload.get("response")
    error = payload.get("error")
    response_fields = response if isinstance(response, Mapping) else {}
    error_fields = error if isinstance(error, Mapping) else {}
    legacy_errors = payload.get("errors")
    details = error_fields.get("details")
    if details is None and isinstance(legacy_errors, list):
        details = legacy_errors

    return _ErrorBody(
        message=_read_string(response_fields.get("message"))
        or _read_string(payload.get("message"))
        or fallback_message,
        code=_read_string(error_fields.get("code")),
        param=_read_string(error_fields.get("param")),
        details=details,
    )


def _read_string(value: object) -> str | None:
    if isinstance(value, str) and value.strip():
        return value
    return None


def _field_errors(details: object) -> tuple[ValidationFieldError, ...]:
    if not isinstance(details, list):
        return ()

    return tuple(
        ValidationFieldError(message=item["message"], path=item["path"])
        for item in details
        if isinstance(item, Mapping)
        and isinstance(item.get("message"), str)
        and isinstance(item.get("path"), str)
    )


def _fallback_code(status: int) -> str:
    code = _FALLBACK_CODES.get(status)
    if code is not None:
        return code
    return "server_error" if status >= 500 else "api_error"
