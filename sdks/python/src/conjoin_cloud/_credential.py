from __future__ import annotations

import hmac
from typing import NoReturn

REDACTED_CREDENTIAL = "[redacted]"


class Credential:
    __slots__ = ("_value",)

    _value: str

    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("A Credential holds a string")
        object.__setattr__(self, "_value", value)

    def reveal(self) -> str:
        return self._value

    def __setattr__(self, name: str, value: object) -> NoReturn:
        raise AttributeError("A Credential cannot be changed")

    def __repr__(self) -> str:
        return f"Credential({REDACTED_CREDENTIAL!r})"

    def __str__(self) -> str:
        return REDACTED_CREDENTIAL

    def __format__(self, format_spec: str) -> str:
        return format(REDACTED_CREDENTIAL, format_spec)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Credential) and hmac.compare_digest(
            other._value.encode("utf-8"), self._value.encode("utf-8")
        )

    def __hash__(self) -> int:
        return hash((Credential, self._value))

    def __reduce__(self) -> NoReturn:
        raise TypeError("A Credential cannot be pickled")
