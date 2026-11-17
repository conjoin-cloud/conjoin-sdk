from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Literal

from codegen.naming import to_snake
from codegen.spec import maybe_resolve_ref

AuthMode = Literal["default", "none", "scim_bearer", "publishable_key", "session", "portal_ticket"]

SECURITY_SCHEME_GROUPS: tuple[tuple[AuthMode, frozenset[str]], ...] = (
    ("default", frozenset({"conjoinApiKey"})),
    ("scim_bearer", frozenset({"scimBearer"})),
    ("publishable_key", frozenset({"conjoinPublishableKey"})),
    ("session", frozenset({"conjoinSessionBearer", "conjoinSessionCookie"})),
    ("portal_ticket", frozenset({"conjoinPortalTicketHeader", "conjoinPortalTicketQuery"})),
)
PORTAL_TICKET_HEADER_SCHEME = "conjoinPortalTicketHeader"
PORTAL_TICKET_ARGUMENT = "portal_ticket"
RESERVED_HEADER_NAMES = frozenset(
    {
        "accept",
        "authorization",
        "content-length",
        "content-type",
        "cookie",
        "host",
        "user-agent",
        "x-conjoin-api-version",
        "x-conjoin-sdk-version",
    }
)
CREDENTIAL_HEADER_NAMES = frozenset({"step-up-token"})


@dataclass(frozen=True)
class DeclaredHeader:
    name: str
    python_name: str
    required: bool
    credential: bool
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | None = None


def resolve_auth_mode(operation: dict[str, Any], operation_id: str) -> AuthMode:
    security = operation.get("security")
    if not isinstance(security, list):
        return "default"
    schemes = [
        scheme
        for requirement in security
        if isinstance(requirement, dict)
        for scheme in requirement
    ]
    if not schemes:
        return "none"
    for mode, group in SECURITY_SCHEME_GROUPS:
        if all(scheme in group for scheme in schemes):
            return mode
    raise ValueError(
        f"{operation_id} declares the security schemes {', '.join(schemes)}, "
        "which no SDK call supports"
    )


def read_portal_ticket_header(spec: dict[str, Any], operation_id: str) -> DeclaredHeader:
    components = spec.get("components")
    schemes = components.get("securitySchemes") if isinstance(components, dict) else None
    scheme = schemes.get(PORTAL_TICKET_HEADER_SCHEME) if isinstance(schemes, dict) else None
    if (
        not isinstance(scheme, dict)
        or scheme.get("in") != "header"
        or not isinstance(scheme.get("name"), str)
    ):
        raise ValueError(f"{operation_id} needs {PORTAL_TICKET_HEADER_SCHEME} as a header")
    return DeclaredHeader(
        name=scheme["name"],
        python_name=PORTAL_TICKET_ARGUMENT,
        required=True,
        credential=True,
    )


def read_declared_header(
    spec: dict[str, Any], parameter: dict[str, Any], operation_id: str
) -> DeclaredHeader:
    name = str(parameter["name"])
    if name.lower() in RESERVED_HEADER_NAMES:
        raise ValueError(f"{operation_id} declares the reserved header {name} as a parameter")
    schema = maybe_resolve_ref(spec, parameter.get("schema"))
    if not isinstance(schema, dict) or schema.get("type") != "string":
        raise ValueError(f"{operation_id} declares the header {name} without a string schema")
    pattern = schema.get("pattern")
    if pattern is not None:
        if not isinstance(pattern, str):
            raise ValueError(f"{operation_id} declares the header {name} with a pattern")
        try:
            re.compile(pattern)
        except re.error as error:
            raise ValueError(
                f"{operation_id} declares the header {name} with a pattern Python cannot check"
            ) from error
    return DeclaredHeader(
        name=name,
        python_name=to_snake(name),
        required=parameter.get("required") is True,
        credential=name.lower() in CREDENTIAL_HEADER_NAMES,
        min_length=_read_bound(schema, "minLength", operation_id, name),
        max_length=_read_bound(schema, "maxLength", operation_id, name),
        pattern=pattern,
    )


def _read_bound(schema: dict[str, Any], key: str, operation_id: str, name: str) -> int | None:
    value = schema.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(
            f"{operation_id} declares the header {name} with a {key} that is not whole"
        )
    return value
