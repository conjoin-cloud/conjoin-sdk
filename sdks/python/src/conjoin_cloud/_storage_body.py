from __future__ import annotations

import os
from collections.abc import AsyncIterable, AsyncIterator, Iterable, Iterator
from contextlib import asynccontextmanager, contextmanager
from pathlib import Path
from typing import Any, BinaryIO, TypeGuard, cast

from conjoin_cloud._errors import ConjoinConfigurationError

STREAM_READ_SIZE = 64 * 1024

BytesLike = bytes | bytearray | memoryview
PathInput = str | os.PathLike[str]
SyncUploadBody = BytesLike | str | os.PathLike[str] | BinaryIO | Iterable[BytesLike]
AsyncUploadBody = SyncUploadBody | AsyncIterable[BytesLike]


def resolve_body_size(body: AsyncUploadBody, file_size: int | None) -> int:
    if file_size is not None:
        if isinstance(file_size, bool) or not isinstance(file_size, int) or file_size < 0:
            raise ConjoinConfigurationError("file_size must be a whole number of 0 or more")
        return file_size

    if isinstance(body, (bytes, bytearray, memoryview)):
        return len(body)

    if _is_path(body):
        return Path(body).stat().st_size

    size = _file_remaining_size(body)
    if size is not None:
        return size

    raise ConjoinConfigurationError("file_size is required for stream-like upload bodies")


@contextmanager
def sync_content(body: SyncUploadBody) -> Iterator[Any]:
    if isinstance(body, (bytes, bytearray, memoryview)):
        yield bytes(body)
        return

    if _is_path(body):
        with Path(body).open("rb") as file:
            yield file
        return

    if _is_readable(body):
        yield body
        return

    yield _coerce_sync_iterable(body)


@asynccontextmanager
async def async_content(body: AsyncUploadBody) -> AsyncIterator[Any]:
    if isinstance(body, (bytes, bytearray, memoryview)):
        yield bytes(body)
        return

    if _is_path(body):
        with Path(body).open("rb") as file:
            yield _iter_sync_file_as_async(file)
        return

    if _is_readable(body):
        yield _iter_sync_file_as_async(body)
        return

    if isinstance(body, AsyncIterable):
        yield _coerce_async_iterable(body)
        return

    yield _iter_sync_iterable_as_async(body)


def iter_sync_chunks(body: SyncUploadBody, chunk_size: int) -> Iterator[bytes]:
    if isinstance(body, (bytes, bytearray, memoryview)):
        data = bytes(body)
        for offset in range(0, len(data), chunk_size):
            yield data[offset : offset + chunk_size]
        return

    if _is_path(body):
        with Path(body).open("rb") as file:
            yield from _iter_file_chunks(file, chunk_size)
        return

    if _is_readable(body):
        yield from _iter_file_chunks(body, chunk_size)
        return

    yield from _coalesce_chunks(_coerce_sync_iterable(body), chunk_size)


async def iter_async_chunks(body: AsyncUploadBody, chunk_size: int) -> AsyncIterator[bytes]:
    if isinstance(body, (bytes, bytearray, memoryview)):
        data = bytes(body)
        for offset in range(0, len(data), chunk_size):
            yield data[offset : offset + chunk_size]
        return

    if _is_path(body):
        with Path(body).open("rb") as file:
            async for chunk in _iter_sync_file_as_async(file, chunk_size=chunk_size):
                yield chunk
        return

    if _is_readable(body):
        async for chunk in _iter_sync_file_as_async(body, chunk_size=chunk_size):
            yield chunk
        return

    if isinstance(body, AsyncIterable):
        async for chunk in _coalesce_async_chunks(_coerce_async_iterable(body), chunk_size):
            yield chunk
        return

    async for chunk in _coalesce_async_chunks(_iter_sync_iterable_as_async(body), chunk_size):
        yield chunk


def _file_remaining_size(body: object) -> int | None:
    tell = getattr(body, "tell", None)
    seek = getattr(body, "seek", None)
    if not callable(tell) or not callable(seek):
        return None

    try:
        current = int(cast(Any, tell)())
        cast(Any, seek)(0, os.SEEK_END)
        end = int(cast(Any, tell)())
        cast(Any, seek)(current, os.SEEK_SET)
    except (OSError, ValueError, TypeError):
        return None

    return max(0, end - current)


def _iter_file_chunks(file: Any, chunk_size: int) -> Iterator[bytes]:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            return
        yield _coerce_bytes(chunk)


async def _iter_sync_file_as_async(
    file: Any,
    *,
    chunk_size: int = STREAM_READ_SIZE,
) -> AsyncIterator[bytes]:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            return
        yield _coerce_bytes(chunk)


def _coerce_sync_iterable(body: Any) -> Iterator[bytes]:
    for chunk in body:
        coerced = _coerce_bytes(chunk)
        if coerced:
            yield coerced


async def _coerce_async_iterable(body: AsyncIterable[BytesLike]) -> AsyncIterator[bytes]:
    async for chunk in body:
        coerced = _coerce_bytes(chunk)
        if coerced:
            yield coerced


async def _iter_sync_iterable_as_async(body: Any) -> AsyncIterator[bytes]:
    for chunk in body:
        coerced = _coerce_bytes(chunk)
        if coerced:
            yield coerced


def _coalesce_chunks(chunks: Iterable[bytes], chunk_size: int) -> Iterator[bytes]:
    buffer = bytearray()
    for chunk in chunks:
        buffer.extend(chunk)
        while len(buffer) >= chunk_size:
            yield bytes(buffer[:chunk_size])
            del buffer[:chunk_size]
    if buffer:
        yield bytes(buffer)


async def _coalesce_async_chunks(
    chunks: AsyncIterable[bytes],
    chunk_size: int,
) -> AsyncIterator[bytes]:
    buffer = bytearray()
    async for chunk in chunks:
        buffer.extend(chunk)
        while len(buffer) >= chunk_size:
            yield bytes(buffer[:chunk_size])
            del buffer[:chunk_size]
    if buffer:
        yield bytes(buffer)


def _coerce_bytes(value: object) -> bytes:
    if isinstance(value, (bytes, bytearray, memoryview)):
        return bytes(value)
    raise ConjoinConfigurationError("upload body chunks must be bytes-like")


def _is_path(value: object) -> TypeGuard[PathInput]:
    return isinstance(value, (str, os.PathLike))


def _is_readable(value: object) -> bool:
    read = getattr(value, "read", None)
    return callable(read)
