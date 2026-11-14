from __future__ import annotations

import re
import uuid

from conjoin_cloud._errors import ConjoinConfigurationError

IDEMPOTENCY_KEY_HEADER = "Idempotency-Key"

_IDEMPOTENCY_KEY_PATTERN = re.compile(r"[A-Za-z0-9\-_:.]{1,64}")


def generate_idempotency_key() -> str:
    return str(uuid.uuid4())


def validate_idempotency_key(key: object) -> str:
    if not isinstance(key, str) or _IDEMPOTENCY_KEY_PATTERN.fullmatch(key) is None:
        raise ConjoinConfigurationError(
            "idempotency_key must be 1 to 64 characters of letters, digits, hyphens, "
            "underscores, colons, and dots"
        )
    return key
