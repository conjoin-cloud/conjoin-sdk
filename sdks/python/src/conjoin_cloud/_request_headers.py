from __future__ import annotations

import re
from collections.abc import Mapping, Sequence

from conjoin_cloud._config import HEADER_VALUE_PATTERN, ResolvedConfig, ScopeName
from conjoin_cloud._errors import ConjoinConfigurationError
from conjoin_cloud._idempotency import IDEMPOTENCY_KEY_HEADER
from conjoin_cloud._request_options import AuthOverride
from conjoin_cloud._request_tracing import CONJOIN_REQUEST_ID_HEADER
from conjoin_cloud._version import __version__

SDK_VERSION_HEADER = "X-Conjoin-SDK-Version"
API_VERSION_HEADER = "X-Conjoin-API-Version"

SCOPE_HEADERS: Mapping[ScopeName, str] = {
    "billing_entity_id": "Billing-Entity-ID",
    "messaging_profile_id": "Messaging-Profile-ID",
    "auth_app_id": "Auth-App-ID",
}

_HEADER_NAME_PATTERN = re.compile(r"[!#$%&'*+\-.^_`|~0-9A-Za-z]+")
_CALLER_HEADER_VALUE_PATTERN = re.compile(r"[\t\x20-\x7e]*")

_MANAGED_HEADER_NAMES = frozenset(
    name.lower()
    for name in (
        "Authorization",
        "Content-Type",
        SDK_VERSION_HEADER,
        API_VERSION_HEADER,
        CONJOIN_REQUEST_ID_HEADER,
        IDEMPOTENCY_KEY_HEADER,
        *SCOPE_HEADERS.values(),
    )
)


def read_header_value(headers: Mapping[str, str] | None, name: str) -> str | None:
    if headers is None:
        return None

    lower_name = name.lower()
    for header_name, value in headers.items():
        if isinstance(header_name, str) and header_name.lower() == lower_name:
            return value
    return None


def build_request_headers(
    config: ResolvedConfig,
    *,
    caller_headers: Mapping[str, str] | None,
    auth: AuthOverride,
    scopes: Sequence[ScopeName],
    request_id: str,
    idempotency_key: str | None,
    json_body: bool,
) -> dict[str, str]:
    headers = _caller_headers(caller_headers)

    authorization = _resolve_authorization(config, auth)
    if authorization is not None:
        headers["Authorization"] = authorization

    if json_body:
        headers["Content-Type"] = "application/json"

    headers[SDK_VERSION_HEADER] = __version__
    headers[API_VERSION_HEADER] = config.api_version
    headers.update(_scope_headers(config, scopes))
    headers[CONJOIN_REQUEST_ID_HEADER] = request_id
    if idempotency_key is not None:
        headers[IDEMPOTENCY_KEY_HEADER] = idempotency_key

    return headers


def _caller_headers(headers: Mapping[str, str] | None) -> dict[str, str]:
    if headers is None:
        return {}

    if not isinstance(headers, Mapping):
        raise ConjoinConfigurationError("request_options.headers must be a mapping")

    sendable: dict[str, str] = {}
    for name, value in headers.items():
        if not isinstance(name, str) or _HEADER_NAME_PATTERN.fullmatch(name) is None:
            raise ConjoinConfigurationError("A request header has a name that HTTP does not allow")
        if not isinstance(value, str) or _CALLER_HEADER_VALUE_PATTERN.fullmatch(value) is None:
            raise ConjoinConfigurationError(
                f"The request header {name} has a value that HTTP does not allow"
            )
        if name.lower() in _MANAGED_HEADER_NAMES:
            continue
        sendable[name] = value
    return sendable


def _resolve_authorization(config: ResolvedConfig, auth: AuthOverride) -> str | None:
    if auth.type == "none":
        return None

    if auth.type == "bearer":
        token = auth.token
        if not isinstance(token, str) or HEADER_VALUE_PATTERN.fullmatch(token) is None:
            raise ConjoinConfigurationError(
                "A bearer token must be a non-empty value without spaces or control characters"
            )
        return f"Bearer {token}"

    if auth.type != "default":
        raise ConjoinConfigurationError(
            "request_options.auth.type must be default, none, or bearer"
        )

    return f"Bearer {config.auth_token}"


def _scope_headers(config: ResolvedConfig, scopes: Sequence[ScopeName]) -> dict[str, str]:
    headers: dict[str, str] = {}
    for scope in scopes:
        value = config.scope.value_of(scope)
        if value is None:
            raise ConjoinConfigurationError(f"This call needs {scope} in the client settings")
        headers[SCOPE_HEADERS[scope]] = value
    return headers
