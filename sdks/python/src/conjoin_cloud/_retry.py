from __future__ import annotations

import math
import random
import re
import time
from datetime import timezone
from email.utils import parsedate_to_datetime

RETRYABLE_STATUSES = frozenset({429, 500, 502, 503, 504})
METHODS_SAFE_TO_RETRY = frozenset({"GET", "PUT", "PATCH", "DELETE"})
RETRY_AFTER_HEADER = "Retry-After"

_RETRY_AFTER_SECONDS_PATTERN = re.compile(r"\d+(\.\d+)?")
_MAX_RETRY_AFTER_CHARACTERS = 64
_LARGEST_BACKOFF_EXPONENT = 64
_jitter = random.Random()


def can_retry_method(method: str, *, has_idempotency_key: bool) -> bool:
    return method in METHODS_SAFE_TO_RETRY or (method == "POST" and has_idempotency_key)


def is_retryable_status(status: int) -> bool:
    return status in RETRYABLE_STATUSES


def parse_retry_after(value: str | None, now: float | None = None) -> float | None:
    if value is None:
        return None

    stripped = value.strip()
    if not stripped or len(stripped) > _MAX_RETRY_AFTER_CHARACTERS:
        return None

    if _RETRY_AFTER_SECONDS_PATTERN.fullmatch(stripped) is not None:
        seconds = float(stripped)
        return seconds if math.isfinite(seconds) else None

    try:
        retry_at = parsedate_to_datetime(stripped)
    except (TypeError, ValueError, IndexError, OverflowError):
        return None

    if retry_at.tzinfo is None:
        retry_at = retry_at.replace(tzinfo=timezone.utc)

    current = time.time() if now is None else now
    try:
        return max(0.0, retry_at.timestamp() - current)
    except (OverflowError, OSError):
        return None


def compute_retry_delay(
    attempt: int,
    *,
    backoff_seconds: float,
    max_delay_seconds: float,
    retry_after: float | None,
) -> float:
    if retry_after is not None:
        return min(retry_after, max_delay_seconds)

    if attempt >= _LARGEST_BACKOFF_EXPONENT:
        ceiling = max_delay_seconds
    else:
        ceiling = min(backoff_seconds * (2**attempt), max_delay_seconds)

    return _jitter.uniform(0.0, ceiling)
