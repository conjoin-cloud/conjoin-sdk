from __future__ import annotations

from collections.abc import AsyncIterator, Iterator

import httpx


class StorageDownload:
    def __init__(self, *, url: str, response: httpx.Response) -> None:
        self.url = url
        self.response = response
        self._closed = False

    def read(self) -> bytes:
        try:
            return self.response.read()
        finally:
            self.close()

    def text(self) -> str:
        try:
            self.response.read()
            return self.response.text
        finally:
            self.close()

    def iter_bytes(self, chunk_size: int | None = None) -> Iterator[bytes]:
        try:
            yield from self.response.iter_bytes(chunk_size=chunk_size)
        finally:
            self.close()

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self.response.close()

    def __enter__(self) -> StorageDownload:
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.close()


class AsyncStorageDownload:
    def __init__(self, *, url: str, response: httpx.Response) -> None:
        self.url = url
        self.response = response
        self._closed = False

    async def read(self) -> bytes:
        try:
            return await self.response.aread()
        finally:
            await self.aclose()

    async def text(self) -> str:
        try:
            await self.response.aread()
            return self.response.text
        finally:
            await self.aclose()

    async def aiter_bytes(self, chunk_size: int | None = None) -> AsyncIterator[bytes]:
        try:
            async for chunk in self.response.aiter_bytes(chunk_size=chunk_size):
                yield chunk
        finally:
            await self.aclose()

    async def aclose(self) -> None:
        if self._closed:
            return
        self._closed = True
        await self.response.aclose()

    async def __aenter__(self) -> AsyncStorageDownload:
        return self

    async def __aexit__(self, exc_type: object, exc: object, traceback: object) -> None:
        await self.aclose()
