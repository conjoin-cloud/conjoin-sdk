from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from functools import lru_cache

from conjoin_cloud._config import HEADER_VALUE_PATTERN
from conjoin_cloud._credential import Credential
from conjoin_cloud._errors import ConjoinConfigurationError

MAX_CACHED_HEADER_PATTERNS = 64


@dataclass(frozen=True)
class DeclaredHeader:
    name: str
    argument: str
    value: str | Credential | None = field(repr=False)
    required: bool = False
    credential: bool = False
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | None = None


@lru_cache(maxsize=MAX_CACHED_HEADER_PATTERNS)
def _compile_pattern(pattern: str) -> re.Pattern[str]:
    return re.compile(pattern)


def declared_header_names(declared: Sequence[DeclaredHeader]) -> frozenset[str]:
    return frozenset(header.name.lower() for header in declared)


def resolve_declared_headers(declared: Sequence[DeclaredHeader]) -> dict[str, str]:
    headers: dict[str, str] = {}
    for header in declared:
        value = _read_value(header)
        if value is None:
            if header.required:
                raise ConjoinConfigurationError(f"This call needs {header.argument}")
            continue
        _check_value(header, value)
        headers[header.name] = value
    return headers


def _read_value(header: DeclaredHeader) -> str | None:
    if header.value is None:
        return None
    if header.credential:
        if not isinstance(header.value, Credential):
            raise ConjoinConfigurationError(f"{header.argument} must be a Credential")
        return header.value.reveal()
    if not isinstance(header.value, str):
        raise ConjoinConfigurationError(f"{header.argument} must be a string")
    return header.value


def _check_value(header: DeclaredHeader, value: str) -> None:
    is_too_short = header.min_length is not None and len(value) < header.min_length
    is_too_long = header.max_length is not None and len(value) > header.max_length
    breaks_pattern = (
        header.pattern is not None and _compile_pattern(header.pattern).search(value) is None
    )
    if (
        HEADER_VALUE_PATTERN.fullmatch(value) is None
        or is_too_short
        or is_too_long
        or breaks_pattern
    ):
        raise ConjoinConfigurationError(
            f"{header.argument} does not meet the documented length or format"
        )
