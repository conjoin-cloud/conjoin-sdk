from __future__ import annotations

from collections.abc import Mapping
from typing import Any, overload


@overload
def wire_names(value: Mapping[str, Any], aliases: Mapping[str, str]) -> dict[str, Any]: ...


@overload
def wire_names(value: None, aliases: Mapping[str, str]) -> None: ...


def wire_names(
    value: Mapping[str, Any] | None,
    aliases: Mapping[str, str],
) -> dict[str, Any] | None:
    if value is None:
        return None
    mapped = dict(value)
    for python_name, wire_name in aliases.items():
        if python_name in mapped and wire_name not in mapped:
            mapped[wire_name] = mapped.pop(python_name)
    return mapped
