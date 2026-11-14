from __future__ import annotations

import math
import re
from dataclasses import dataclass
from os import environ
from typing import Literal
from urllib.parse import urlsplit

from conjoin_cloud._constants import DEFAULT_API_VERSION
from conjoin_cloud._errors import ConjoinConfigurationError
from conjoin_cloud._region import build_conjoin_region_base_url, read_conjoin_key_region

DEFAULT_TIMEOUT_SECONDS = 30.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_BACKOFF_SECONDS = 0.5
DEFAULT_MAX_RETRY_DELAY_SECONDS = 60.0

CONJOIN_API_KEY_ENV = "CONJOIN_API_KEY"
CONJOIN_PUBLISHABLE_KEY_ENV = "CONJOIN_PUBLISHABLE_KEY"

ScopeName = Literal["billing_entity_id", "messaging_profile_id", "auth_app_id"]

HEADER_VALUE_PATTERN = re.compile(r"[\x21-\x7e]+")


@dataclass(frozen=True)
class ConjoinScope:
    billing_entity_id: str | None = None
    messaging_profile_id: str | None = None
    auth_app_id: str | None = None

    def value_of(self, name: ScopeName) -> str | None:
        if name == "billing_entity_id":
            return self.billing_entity_id
        if name == "messaging_profile_id":
            return self.messaging_profile_id
        return self.auth_app_id


@dataclass(frozen=True)
class ResolvedConfig:
    api_key: str | None
    publishable_key: str | None
    base_url: str
    api_version: str
    timeout: float
    conjoin_request_id: str | None
    max_retries: int
    backoff_seconds: float
    max_retry_delay_seconds: float
    strict_response_validation: bool
    scope: ConjoinScope

    @property
    def auth_token(self) -> str:
        token = self.api_key if self.api_key is not None else self.publishable_key
        if token is None:
            raise ConjoinConfigurationError("Either api_key or publishable_key must be provided")
        return token


def resolve_config(
    *,
    api_key: str | None,
    publishable_key: str | None,
    base_url: str | None,
    api_version: str | None,
    timeout: float | None,
    conjoin_request_id: str | None,
    max_retries: int | None,
    backoff_seconds: float | None,
    max_retry_delay_seconds: float | None,
    strict_response_validation: bool,
    scope: ConjoinScope,
) -> ResolvedConfig:
    resolved_api_key, resolved_publishable_key = _resolve_credentials(
        api_key=api_key,
        publishable_key=publishable_key,
    )
    key = resolved_api_key if resolved_api_key is not None else resolved_publishable_key
    if key is None:
        raise ConjoinConfigurationError("Either api_key or publishable_key must be provided")

    return ResolvedConfig(
        api_key=resolved_api_key,
        publishable_key=resolved_publishable_key,
        base_url=_resolve_base_url(base_url, key),
        api_version=_resolve_api_version(api_version),
        timeout=require_positive_seconds("timeout", timeout, DEFAULT_TIMEOUT_SECONDS),
        conjoin_request_id=conjoin_request_id,
        max_retries=require_retry_count("max_retries", max_retries, DEFAULT_MAX_RETRIES),
        backoff_seconds=require_non_negative_seconds(
            "backoff_seconds", backoff_seconds, DEFAULT_BACKOFF_SECONDS
        ),
        max_retry_delay_seconds=require_non_negative_seconds(
            "max_retry_delay_seconds", max_retry_delay_seconds, DEFAULT_MAX_RETRY_DELAY_SECONDS
        ),
        strict_response_validation=strict_response_validation,
        scope=resolve_scope(scope),
    )


def resolve_scope(scope: ConjoinScope) -> ConjoinScope:
    return ConjoinScope(
        billing_entity_id=_validate_scope_value("billing_entity_id", scope.billing_entity_id),
        messaging_profile_id=_validate_scope_value(
            "messaging_profile_id", scope.messaging_profile_id
        ),
        auth_app_id=_validate_scope_value("auth_app_id", scope.auth_app_id),
    )


def require_positive_seconds(name: str, value: float | None, fallback: float) -> float:
    resolved = _require_finite_number(name, value, fallback)
    if resolved <= 0:
        raise ConjoinConfigurationError(f"{name} must be a finite number greater than 0")
    return resolved


def require_non_negative_seconds(name: str, value: float | None, fallback: float) -> float:
    resolved = _require_finite_number(name, value, fallback)
    if resolved < 0:
        raise ConjoinConfigurationError(f"{name} must be a finite number of 0 or more")
    return resolved


def require_retry_count(name: str, value: int | None, fallback: int) -> int:
    if value is None:
        return fallback
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ConjoinConfigurationError(f"{name} must be a whole number of 0 or more")
    return value


def _require_finite_number(name: str, value: float | None, fallback: float) -> float:
    if value is None:
        return fallback
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ConjoinConfigurationError(f"{name} must be a finite number")
    resolved = float(value)
    if not math.isfinite(resolved):
        raise ConjoinConfigurationError(f"{name} must be a finite number")
    return resolved


def _validate_scope_value(name: str, value: str | None) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or HEADER_VALUE_PATTERN.fullmatch(value) is None:
        raise ConjoinConfigurationError(
            f"{name} must be a non-empty value without spaces or control characters"
        )
    return value


def _resolve_credentials(
    *,
    api_key: str | None,
    publishable_key: str | None,
) -> tuple[str | None, str | None]:
    explicit_api_key = _resolve_optional_credential("api_key", api_key)
    explicit_publishable_key = _resolve_optional_credential("publishable_key", publishable_key)

    if explicit_api_key is not None or explicit_publishable_key is not None:
        if explicit_api_key is not None and explicit_publishable_key is not None:
            raise ConjoinConfigurationError("Provide exactly one of api_key or publishable_key")
        return explicit_api_key, explicit_publishable_key

    env_api_key = _resolve_optional_credential(
        CONJOIN_API_KEY_ENV,
        environ.get(CONJOIN_API_KEY_ENV),
    )
    env_publishable_key = _resolve_optional_credential(
        CONJOIN_PUBLISHABLE_KEY_ENV,
        environ.get(CONJOIN_PUBLISHABLE_KEY_ENV),
    )

    if env_api_key is not None and env_publishable_key is not None:
        raise ConjoinConfigurationError(
            f"Only one of {CONJOIN_API_KEY_ENV} or {CONJOIN_PUBLISHABLE_KEY_ENV} may be set"
        )

    if env_api_key is None and env_publishable_key is None:
        raise ConjoinConfigurationError("Either api_key or publishable_key must be provided")

    return env_api_key, env_publishable_key


def _resolve_optional_credential(name: str, value: str | None) -> str | None:
    if value is None:
        return None

    if not isinstance(value, str):
        raise ConjoinConfigurationError(f"{name} must be a string")

    stripped = value.strip()
    if HEADER_VALUE_PATTERN.fullmatch(stripped) is None:
        raise ConjoinConfigurationError(
            f"{name} must be a non-empty value without spaces or control characters"
        )

    return stripped


def _resolve_api_version(value: str | None) -> str:
    if value is None:
        return DEFAULT_API_VERSION

    stripped = value.strip() if isinstance(value, str) else ""
    if HEADER_VALUE_PATTERN.fullmatch(stripped) is None:
        raise ConjoinConfigurationError(
            "api_version must be a non-empty value without spaces or control characters"
        )

    return stripped


def _resolve_base_url(value: str | None, key: str) -> str:
    if value is None:
        return build_conjoin_region_base_url(read_conjoin_key_region(key))

    stripped = value.strip()
    try:
        parts = urlsplit(stripped)
    except ValueError as exc:
        raise ConjoinConfigurationError("base_url must be an absolute http or https URL") from exc

    if parts.scheme not in ("http", "https") or not parts.netloc:
        raise ConjoinConfigurationError("base_url must be an absolute http or https URL")

    return stripped.rstrip("/")
