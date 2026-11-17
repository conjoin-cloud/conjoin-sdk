from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import httpx

from conjoin_cloud._config import require_positive_seconds
from conjoin_cloud._errors import ConjoinConfigurationError, ConjoinStorageError
from conjoin_cloud._request_options import RequestOptions, coerce_request_options
from conjoin_cloud._response_parsing import transport_error
from conjoin_cloud._storage_body import (
    AsyncUploadBody,
    SyncUploadBody,
    async_content,
    iter_async_chunks,
    iter_sync_chunks,
    resolve_body_size,
    sync_content,
)
from conjoin_cloud._storage_download import AsyncStorageDownload, StorageDownload
from conjoin_cloud._storage_http import (
    RESUME_INCOMPLETE_STATUS,
    build_storage_request,
    confirmed_resumable_offset,
    redact_storage_url,
    resumable_session_url,
    send_async_storage_request,
    send_storage_request,
    storage_error,
    validate_signed_url,
)
from conjoin_cloud.generated._models import StorageObjectCreateUploadSignedUrlRequest
from conjoin_cloud.generated.storage import AsyncStorageResource as GeneratedAsyncStorageResource
from conjoin_cloud.generated.storage import StorageResource as GeneratedStorageResource

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin

CHUNK_ALIGNMENT = 256 * 1024
DEFAULT_CHUNK_SIZE = 8 * 1024 * 1024


@dataclass(frozen=True)
class UploadProgress:
    loaded: int
    total: int
    percentage: int


UploadProgressCallback = Callable[[UploadProgress], None]


@dataclass(frozen=True)
class _UploadPlan:
    method: str
    url: str
    headers: dict[str, str]
    mode: str
    total_size: int
    chunk_size: int
    timeout: float


class StorageResource(GeneratedStorageResource):
    def upload(
        self,
        *,
        container: str,
        path: str,
        content_type: str,
        body: SyncUploadBody,
        file_size: int | None = None,
        expires_in_minutes: int | None = None,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        on_progress: UploadProgressCallback | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> None:
        _validate_storage_request(container=container, path=path, content_type=content_type)
        validated_chunk_size = _validate_chunk_size(chunk_size)
        total_size = resolve_body_size(body, file_size)
        signed_url = self.objects.create_upload_signed_url(
            container,
            _upload_request(path, content_type, total_size, expires_in_minutes),
            request_options=request_options,
        )
        plan = _upload_plan(
            signed_url.upload_url,
            signed_url.required_fields,
            signed_url.upload_mode,
            total_size=total_size,
            chunk_size=validated_chunk_size,
            timeout=_storage_timeout(self._client, request_options),
        )
        client = self._client._client
        _emit_progress(on_progress, loaded=0, total=total_size)

        if plan.mode == "single":
            with sync_content(body) as content:
                send_storage_request(
                    client, plan.method, plan.url, headers=plan.headers, content=content,
                    timeout=plan.timeout, upload_mode="single", action="Upload failed",
                )
            _emit_progress(on_progress, loaded=total_size, total=total_size)
            return

        session = send_storage_request(
            client, "POST", plan.url, headers=plan.headers, timeout=plan.timeout,
            upload_mode="resumable", action="Resumable upload initiation failed",
        )
        session_url = resumable_session_url(session, plan.url)
        loaded = 0
        for chunk in iter_sync_chunks(body, plan.chunk_size):
            if not chunk:
                continue
            response = send_storage_request(
                client, "PUT", session_url, headers=_chunk_headers(loaded, chunk, total_size),
                content=chunk, timeout=plan.timeout, upload_mode="resumable",
                action="Chunk upload failed",
            )
            loaded = _next_offset(response, loaded, chunk, total_size, session_url)
            _emit_progress(on_progress, loaded=loaded, total=total_size)

    def download(
        self,
        *,
        container: str,
        path: str,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> StorageDownload:
        _validate_storage_request(container=container, path=path, content_type=None)
        signed_url = self.objects.create_download_signed_url(
            container,
            {"path": path},
            request_options=request_options,
        )
        url = validate_signed_url(signed_url.url)
        timeout = _storage_timeout(self._client, request_options)
        client = self._client._client
        headers = dict(signed_url.headers or {})
        request = build_storage_request(
            client, "GET", url, headers=headers, content=None, timeout=timeout
        )
        try:
            response = client.send(request, stream=True)
        except httpx.HTTPError as exc:
            raise transport_error(exc, timeout=timeout, request_id=None) from exc

        if response.status_code >= 400:
            response.close()
            raise storage_error("Download failed", response, url, upload_mode=None)
        return StorageDownload(url=url, response=response)


class AsyncStorageResource(GeneratedAsyncStorageResource):
    async def upload(
        self,
        *,
        container: str,
        path: str,
        content_type: str,
        body: AsyncUploadBody,
        file_size: int | None = None,
        expires_in_minutes: int | None = None,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        on_progress: UploadProgressCallback | None = None,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> None:
        _validate_storage_request(container=container, path=path, content_type=content_type)
        validated_chunk_size = _validate_chunk_size(chunk_size)
        total_size = resolve_body_size(body, file_size)
        signed_url = await self.objects.create_upload_signed_url(
            container,
            _upload_request(path, content_type, total_size, expires_in_minutes),
            request_options=request_options,
        )
        plan = _upload_plan(
            signed_url.upload_url,
            signed_url.required_fields,
            signed_url.upload_mode,
            total_size=total_size,
            chunk_size=validated_chunk_size,
            timeout=_storage_timeout(self._client, request_options),
        )
        client = self._client._client
        _emit_progress(on_progress, loaded=0, total=total_size)

        if plan.mode == "single":
            async with async_content(body) as content:
                await send_async_storage_request(
                    client, plan.method, plan.url, headers=plan.headers, content=content,
                    timeout=plan.timeout, upload_mode="single", action="Upload failed",
                )
            _emit_progress(on_progress, loaded=total_size, total=total_size)
            return

        session = await send_async_storage_request(
            client, "POST", plan.url, headers=plan.headers, timeout=plan.timeout,
            upload_mode="resumable", action="Resumable upload initiation failed",
        )
        session_url = resumable_session_url(session, plan.url)
        loaded = 0
        async for chunk in iter_async_chunks(body, plan.chunk_size):
            if not chunk:
                continue
            response = await send_async_storage_request(
                client, "PUT", session_url, headers=_chunk_headers(loaded, chunk, total_size),
                content=chunk, timeout=plan.timeout, upload_mode="resumable",
                action="Chunk upload failed",
            )
            loaded = _next_offset(response, loaded, chunk, total_size, session_url)
            _emit_progress(on_progress, loaded=loaded, total=total_size)

    async def download(
        self,
        *,
        container: str,
        path: str,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncStorageDownload:
        _validate_storage_request(container=container, path=path, content_type=None)
        signed_url = await self.objects.create_download_signed_url(
            container,
            {"path": path},
            request_options=request_options,
        )
        url = validate_signed_url(signed_url.url)
        timeout = _storage_timeout(self._client, request_options)
        client = self._client._client
        headers = dict(signed_url.headers or {})
        request = build_storage_request(
            client, "GET", url, headers=headers, content=None, timeout=timeout
        )
        try:
            response = await client.send(request, stream=True)
        except httpx.HTTPError as exc:
            raise transport_error(exc, timeout=timeout, request_id=None) from exc

        if response.status_code >= 400:
            await response.aclose()
            raise storage_error("Download failed", response, url, upload_mode=None)
        return AsyncStorageDownload(url=url, response=response)


def _validate_storage_request(*, container: str, path: str, content_type: str | None) -> None:
    if not isinstance(container, str) or not container.strip():
        raise ConjoinConfigurationError("container must not be empty")
    if not isinstance(path, str) or not path.strip():
        raise ConjoinConfigurationError("path must not be empty")
    if content_type is not None and (not isinstance(content_type, str) or not content_type.strip()):
        raise ConjoinConfigurationError("content_type must not be empty")


def _validate_chunk_size(chunk_size: int) -> int:
    if isinstance(chunk_size, bool) or not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ConjoinConfigurationError("chunk_size must be a whole number greater than 0")
    if chunk_size % CHUNK_ALIGNMENT != 0:
        raise ConjoinConfigurationError(
            f"chunk_size must be a multiple of {CHUNK_ALIGNMENT} bytes (256 KiB)"
        )
    return chunk_size


def _upload_request(
    path: str,
    content_type: str,
    file_size: int,
    expires_in_minutes: int | None,
) -> StorageObjectCreateUploadSignedUrlRequest:
    request: StorageObjectCreateUploadSignedUrlRequest = {
        "path": path,
        "content_type": content_type,
        "file_size": file_size,
    }
    if expires_in_minutes is not None:
        request["expires_in_minutes"] = expires_in_minutes
    return request


def _upload_plan(
    upload_url: str,
    required_fields: Mapping[str, Any],
    upload_mode: str,
    *,
    total_size: int,
    chunk_size: int,
    timeout: float,
) -> _UploadPlan:
    url = validate_signed_url(upload_url)
    if upload_mode not in ("single", "resumable"):
        raise ConjoinStorageError(
            f"Unsupported upload mode: {upload_mode}",
            status=0,
            storage_url=redact_storage_url(url),
            upload_mode=upload_mode,
        )

    method = required_fields.get("method")
    normalized_method = method.strip().upper() if isinstance(method, str) else ""
    if normalized_method not in ("POST", "PUT"):
        raise ConjoinStorageError(
            "Upload signed URL did not include a POST or PUT storage method",
            status=0,
            storage_url=redact_storage_url(url),
        )

    headers = required_fields.get("headers")
    if not isinstance(headers, Mapping):
        raise ConjoinStorageError(
            "Upload signed URL did not include storage headers",
            status=0,
            storage_url=redact_storage_url(url),
        )

    return _UploadPlan(
        method=normalized_method,
        url=url,
        headers={str(name): str(value) for name, value in headers.items()},
        mode=upload_mode,
        total_size=total_size,
        chunk_size=chunk_size,
        timeout=timeout,
    )


def _chunk_headers(start: int, chunk: bytes, total_size: int) -> dict[str, str]:
    end = start + len(chunk) - 1
    return {
        "Content-Range": f"bytes {start}-{end}/{total_size}",
        "Content-Length": str(len(chunk)),
    }


def _next_offset(
    response: httpx.Response,
    start: int,
    chunk: bytes,
    total_size: int,
    session_url: str,
) -> int:
    if response.status_code == RESUME_INCOMPLETE_STATUS:
        return confirmed_resumable_offset(response, expected=start + len(chunk), url=session_url)
    return total_size


def _storage_timeout(
    client: Conjoin | AsyncConjoin,
    request_options: RequestOptions | Mapping[str, Any] | None,
) -> float:
    options = coerce_request_options(request_options)
    return require_positive_seconds(
        "request_options.timeout", options.timeout, client.config.timeout
    )


def _emit_progress(on_progress: UploadProgressCallback | None, *, loaded: int, total: int) -> None:
    if on_progress is None:
        return
    percentage = 100 if total == 0 else round((loaded / total) * 100)
    on_progress(UploadProgress(loaded=loaded, total=total, percentage=percentage))
