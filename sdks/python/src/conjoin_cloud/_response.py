from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class ResponseMetadata:
    status_code: int
    headers: Mapping[str, str]
    request_id: str | None = None


@dataclass(frozen=True)
class WithResponse(Generic[T]):
    data: T
    status_code: int
    headers: Mapping[str, str]
    request_id: str | None = None

    @property
    def metadata(self) -> ResponseMetadata:
        return ResponseMetadata(
            status_code=self.status_code,
            headers=self.headers,
            request_id=self.request_id,
        )
