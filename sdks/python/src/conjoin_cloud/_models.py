from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr, field_validator

from conjoin_cloud._errors import ConjoinResponseError

T = TypeVar("T")

_REPEATED_CURSOR_MESSAGE = "The list returned a cursor that it had returned before"


class ConjoinModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _request_id: str | None = PrivateAttr(default=None)

    def _set_request_id(self, request_id: str | None) -> None:
        self._request_id = request_id


class ResponseMeta(ConjoinModel):
    type: str | None = None
    code: int | None = None
    message: str | None = None


class Cursor(ConjoinModel):
    prev: str | None = None
    next: str | None = None

    @field_validator("prev", "next", mode="before")
    @classmethod
    def _token_or_none(cls, value: object) -> str | None:
        return value if isinstance(value, str) and value else None


class ListPage(ConjoinModel, Generic[T]):
    response: ResponseMeta = Field(default_factory=ResponseMeta)
    data: list[T]
    cursor: Cursor = Field(default_factory=Cursor)

    _status: int = PrivateAttr(default=0)

    @field_validator("response", "cursor", mode="before")
    @classmethod
    def _object_or_empty(cls, value: object) -> object:
        return value if isinstance(value, (dict, BaseModel)) else {}

    def _next_cursor(self) -> str | None:
        token = self.cursor.next
        return token if isinstance(token, str) and token else None

    def _repeated_cursor_error(self) -> ConjoinResponseError:
        return ConjoinResponseError(
            _REPEATED_CURSOR_MESSAGE,
            status=self._status,
            request_id=self._request_id,
        )


class Page(ListPage[T], Generic[T]):
    _fetch_next: Callable[[str], Page[T]] | None = PrivateAttr(default=None)

    def has_next_page(self) -> bool:
        return self._next_cursor() is not None and self._fetch_next is not None

    def next_page(self) -> Page[T] | None:
        token = self._next_cursor()
        if token is None or self._fetch_next is None:
            return None
        return self._fetch_next(token)

    def iter_all(self) -> Iterator[T]:
        page: Page[T] = self
        seen: set[str] = set()
        while True:
            yield from page.data
            token = page._next_cursor()
            if token is None or page._fetch_next is None:
                return
            if token in seen:
                raise page._repeated_cursor_error()
            seen.add(token)
            page = page._fetch_next(token)


class AsyncPage(ListPage[T], Generic[T]):
    _fetch_next: Callable[[str], Awaitable[AsyncPage[T]]] | None = PrivateAttr(default=None)

    def has_next_page(self) -> bool:
        return self._next_cursor() is not None and self._fetch_next is not None

    async def next_page(self) -> AsyncPage[T] | None:
        token = self._next_cursor()
        if token is None or self._fetch_next is None:
            return None
        return await self._fetch_next(token)

    async def iter_all(self) -> AsyncIterator[T]:
        page: AsyncPage[T] = self
        seen: set[str] = set()
        while True:
            for item in page.data:
                yield item
            token = page._next_cursor()
            if token is None or page._fetch_next is None:
                return
            if token in seen:
                raise page._repeated_cursor_error()
            seen.add(token)
            page = await page._fetch_next(token)
