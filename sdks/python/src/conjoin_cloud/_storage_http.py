from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from urllib.parse import urlsplit, urlunsplit

import httpx

from conjoin_cloud._errors import ConjoinStorageError
from conjoin_cloud._response_parsing import transport_error

RESUME_INCOMPLETE_STATUS = 308
STORAGE_MANAGED_HEADERS = frozenset(
    {
        "authorization",
        "conjoin-request-id",
        "content-type",
        "idempotency-key",
        "x-conjoin-api-version",
        "x-conjoin-sdk-version",
    }
)


def redact_storage_url(url: str) -> str:
    try:
        parts = urlsplit(url)
    except ValueError:
        return ""
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def validate_signed_url(url: str) -> str:
    stripped = url.strip() if isinstance(url, str) else ""
    if not stripped.startswith(("http://", "https://")):
        raise ConjoinStorageError(
            "Storage signed URL must be absolute",
            status=0,
            storage_url=redact_storage_url(stripped),
        )
    return stripped


def storage_error(
    message: str,
    response: httpx.Response,
    url: str,
    *,
    upload_mode: str | None,
) -> ConjoinStorageError:
    return ConjoinStorageError(
        f"{message}: {response.status_code} {response.reason_phrase}".strip(),
        status=response.status_code,
        storage_url=redact_storage_url(url),
        upload_mode=upload_mode,
    )


def build_storage_request(
    client: httpx.Client | httpx.AsyncClient,
    method: str,
    url: str,
    *,
    headers: Mapping[str, str],
    content: Any,
    timeout: float,
) -> httpx.Request:
    request = client.build_request(
        method, url, headers=dict(headers), content=content, timeout=timeout
    )
    returned = {name.lower() for name in headers}
    for managed_header in STORAGE_MANAGED_HEADERS:
        if managed_header not in returned:
            request.headers.pop(managed_header, None)
    return request


def send_storage_request(
    client: httpx.Client,
    method: str,
    url: str,
    *,
    headers: Mapping[str, str],
    content: Any = None,
    timeout: float,
    upload_mode: str | None,
    action: str,
) -> httpx.Response:
    request = build_storage_request(
        client, method, url, headers=headers, content=content, timeout=timeout
    )
    try:
        response = client.send(request, stream=True)
    except httpx.HTTPError as exc:
        raise transport_error(exc, timeout=timeout, request_id=None) from exc

    try:
        if response.status_code >= 400:
            raise storage_error(action, response, url, upload_mode=upload_mode)
        response.read()
    except httpx.HTTPError as exc:
        raise transport_error(exc, timeout=timeout, request_id=None) from exc
    finally:
        response.close()
    return response


async def send_async_storage_request(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    *,
    headers: Mapping[str, str],
    content: Any = None,
    timeout: float,
    upload_mode: str | None,
    action: str,
) -> httpx.Response:
    request = build_storage_request(
        client, method, url, headers=headers, content=content, timeout=timeout
    )
    try:
        response = await client.send(request, stream=True)
    except httpx.HTTPError as exc:
        raise transport_error(exc, timeout=timeout, request_id=None) from exc

    try:
        if response.status_code >= 400:
            raise storage_error(action, response, url, upload_mode=upload_mode)
        await response.aread()
    except httpx.HTTPError as exc:
        raise transport_error(exc, timeout=timeout, request_id=None) from exc
    finally:
        await response.aclose()
    return response


def resumable_session_url(response: httpx.Response, url: str) -> str:
    session_url = response.headers.get("Location")
    if session_url is None or not session_url.strip():
        raise ConjoinStorageError(
            "Resumable upload initiation did not return a session URL",
            status=response.status_code,
            storage_url=redact_storage_url(url),
            upload_mode="resumable",
        )
    return validate_signed_url(session_url)


def confirmed_resumable_offset(response: httpx.Response, *, expected: int, url: str) -> int:
    range_header = response.headers.get("Range")
    prefix = "bytes=0-"
    if range_header is None or not range_header.startswith(prefix):
        return expected

    try:
        confirmed = int(range_header[len(prefix) :]) + 1
    except ValueError:
        return expected

    if confirmed != expected:
        raise ConjoinStorageError(
            "Resumable upload confirmed an unexpected byte range",
            status=response.status_code,
            storage_url=redact_storage_url(url),
            upload_mode="resumable",
        )
    return confirmed
