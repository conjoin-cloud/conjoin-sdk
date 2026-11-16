from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Literal, TypedDict, cast

from conjoin_cloud._credential import Credential
from conjoin_cloud._errors import ConjoinConfigurationError

AuthType = Literal["default", "none", "bearer"]
DeclaredAuthType = Literal["publishable_key", "session"]


@dataclass(frozen=True)
class AuthOverride:
    type: AuthType = "default"
    token: str | None = field(default=None, repr=False)


@dataclass(frozen=True)
class DeclaredAuth:
    type: DeclaredAuthType
    session_token: Credential | None = None


class AuthOverrideDict(TypedDict, total=False):
    type: AuthType
    token: str


@dataclass(frozen=True)
class RequestOptions:
    timeout: float | None = None
    max_retries: int | None = None
    conjoin_request_id: str | None = None
    idempotency_key: str | None = None
    headers: Mapping[str, str] | None = None
    auth: AuthOverride | AuthOverrideDict | None = None


AUTH_NONE = AuthOverride(type="none")
AUTH_PUBLISHABLE_KEY = DeclaredAuth(type="publishable_key")


def session_auth(session_token: Credential) -> DeclaredAuth:
    if not isinstance(session_token, Credential):
        raise ConjoinConfigurationError("session_token must be a Credential")
    return DeclaredAuth(type="session", session_token=session_token)


def coerce_request_options(options: RequestOptions | Mapping[str, Any] | None) -> RequestOptions:
    if options is None:
        return RequestOptions()

    if isinstance(options, RequestOptions):
        return options

    if not isinstance(options, Mapping):
        raise ConjoinConfigurationError("request_options must be RequestOptions or a mapping")

    return RequestOptions(
        timeout=cast(float | None, options.get("timeout")),
        max_retries=cast(int | None, options.get("max_retries")),
        conjoin_request_id=cast(str | None, options.get("conjoin_request_id")),
        idempotency_key=cast(str | None, options.get("idempotency_key")),
        headers=cast(Mapping[str, str] | None, options.get("headers")),
        auth=cast(AuthOverride | AuthOverrideDict | None, options.get("auth")),
    )


def resolve_auth_override(auth: AuthOverride | AuthOverrideDict | None) -> AuthOverride | None:
    if auth is None:
        return None

    if isinstance(auth, AuthOverride):
        return auth

    if not isinstance(auth, Mapping):
        raise ConjoinConfigurationError("request_options.auth must be AuthOverride or a mapping")

    return AuthOverride(type=auth.get("type", "default"), token=auth.get("token"))


def scim_bearer_auth(scim_token: str | None) -> AuthOverride:
    if scim_token is None or not scim_token.strip():
        raise ConjoinConfigurationError("SCIM token is required for tenant SCIM operations")
    return AuthOverride(type="bearer", token=scim_token.strip())
