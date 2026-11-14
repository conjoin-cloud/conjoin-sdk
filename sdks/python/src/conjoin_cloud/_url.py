from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any
from urllib.parse import quote, urlencode

from conjoin_cloud._errors import ConjoinConfigurationError

_ABSOLUTE_URL_PATTERN = re.compile(r"[a-z][a-z0-9+.-]*:", re.IGNORECASE)
_LEADING_VERSION_PATTERN = re.compile(r"^v1/")
_DOT_SEGMENTS = frozenset({".", ".."})
_MAX_QUERY_DEPTH = 8


def build_url(base_url: str, path: str, query: Mapping[str, Any] | None) -> str:
    if not isinstance(path, str):
        raise ConjoinConfigurationError("path must be a string")

    stripped = path.strip()
    if _ABSOLUTE_URL_PATTERN.match(stripped) or stripped.startswith("//"):
        raise ConjoinConfigurationError("path must be relative to the Conjoin API")

    relative_path = _LEADING_VERSION_PATTERN.sub("", stripped.lstrip("/"))
    url = f"{base_url}/v1/{relative_path}"

    pairs = flatten_query(query) if query else []
    if not pairs:
        return url

    return f"{url}?{urlencode(pairs)}"


def encode_path_param(value: str) -> str:
    if not isinstance(value, str) or not value or value in _DOT_SEGMENTS:
        raise ConjoinConfigurationError("A path parameter must be a non-empty ID")
    return quote(value, safe="")


def flatten_query(query: Mapping[str, Any]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for key, value in query.items():
        _append_query_value(pairs, str(key), value, 0)
    return pairs


def _append_query_value(pairs: list[tuple[str, str]], key: str, value: Any, depth: int) -> None:
    if value is None:
        return

    if depth > _MAX_QUERY_DEPTH:
        raise ConjoinConfigurationError("query nests deeper than the SDK accepts")

    if isinstance(value, (list, tuple)):
        for item in value:
            _append_query_value(pairs, key, item, depth + 1)
        return

    if isinstance(value, Mapping):
        for nested_key, nested_value in value.items():
            _append_query_value(pairs, f"{key}[{nested_key}]", nested_value, depth + 1)
        return

    if isinstance(value, bool):
        pairs.append((key, "true" if value else "false"))
        return

    pairs.append((key, str(value)))
