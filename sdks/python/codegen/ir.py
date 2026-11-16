from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Literal

from codegen.naming import (
    operation_id_to_method_name,
    parse_tag,
    to_kebab,
    to_pascal,
    to_snake,
)
from codegen.security import (
    AuthMode,
    DeclaredHeader,
    read_declared_header,
    read_portal_ticket_header,
    resolve_auth_mode,
)
from codegen.spec import maybe_resolve_ref

HTTP_METHODS = ("get", "post", "put", "patch", "delete")
METHODS_WITHOUT_BODY = frozenset({"get", "delete"})
NO_CONTENT_STATUS = "204"
REQUEST_ID_HEADER = "conjoin-request-id"
IDEMPOTENCY_KEY_HEADER = "idempotency-key"
SCOPE_HEADER_NAMES = {
    "billing-entity-id": "billing_entity_id",
    "messaging-profile-id": "messaging_profile_id",
    "auth-app-id": "auth_app_id",
}
RESERVED_PARAMETER_NAMES = frozenset({"self", "data", "query", "request_options", "session_token"})

ResponseKind = Literal["envelope", "list", "body", "empty"]
CursorLocation = Literal["query", "body", "none"]


@dataclass(frozen=True)
class Parameter:
    name: str
    python_name: str
    required: bool
    schema: dict[str, Any]


@dataclass(frozen=True)
class Operation:
    operation_id: str
    method_name: str
    http_method: str
    path: str
    auth_mode: AuthMode
    request_content_type: str
    has_request_body: bool
    request_body_required: bool
    response_kind: ResponseKind
    cursor_location: CursorLocation
    path_parameters: tuple[Parameter, ...]
    query_parameters: tuple[Parameter, ...]
    request_schema: dict[str, Any] | None
    response_schema: dict[str, Any]
    response_data_schema: dict[str, Any]
    response_item_schema: dict[str, Any] | None
    scopes: tuple[str, ...]
    accepts_idempotency_key: bool
    declared_headers: tuple[DeclaredHeader, ...]


@dataclass(frozen=True)
class ResourceGroup:
    service: str
    resource: str
    service_pascal: str
    resource_pascal: str
    operations: tuple[Operation, ...]


def collect_resource_groups(spec: dict[str, Any]) -> tuple[ResourceGroup, ...]:
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        raise ValueError("The OpenAPI document has no paths")

    groups: dict[str, tuple[str, str, list[Operation]]] = {}
    for path, methods in paths.items():
        if not isinstance(methods, dict):
            raise ValueError(f"{path} is not a path item object")
        for method in HTTP_METHODS:
            raw_operation = methods.get(method)
            if raw_operation is None:
                continue
            if not isinstance(raw_operation, dict):
                raise ValueError(f"{method.upper()} {path} is not an operation object")
            service, resource = _read_tag(raw_operation, method, str(path))
            key = f"{service}-{to_kebab(resource)}"
            entry = groups.setdefault(key, (service, resource, []))
            entry[2].append(
                _build_operation(
                    spec,
                    path=str(path),
                    method=method,
                    raw_operation=raw_operation,
                    service_pascal=to_pascal(service),
                    resource_pascal=to_pascal(resource),
                )
            )

    return tuple(
        ResourceGroup(
            service=service,
            resource=resource,
            service_pascal=to_pascal(service),
            resource_pascal=to_pascal(resource),
            operations=tuple(operations),
        )
        for service, resource, operations in groups.values()
    )


def _read_tag(raw_operation: dict[str, Any], method: str, path: str) -> tuple[str, str]:
    tags = raw_operation.get("tags")
    tag = tags[0] if isinstance(tags, list) and tags else None
    if not isinstance(tag, str) or not isinstance(raw_operation.get("operationId"), str):
        raise ValueError(f"{method.upper()} {path} has no tag or operationId")
    service, resource = parse_tag(tag)
    if not resource:
        raise ValueError(f"{method.upper()} {path} has the tag {tag} without a resource")
    return service, resource


def _build_operation(
    spec: dict[str, Any],
    *,
    path: str,
    method: str,
    raw_operation: dict[str, Any],
    service_pascal: str,
    resource_pascal: str,
) -> Operation:
    operation_id = str(raw_operation["operationId"])
    parameters = _resolved_parameters(spec, raw_operation, operation_id)
    scopes, declares_idempotency_key, declared_headers = _header_semantics(
        spec, parameters, operation_id
    )
    auth_mode = resolve_auth_mode(raw_operation, operation_id)
    if auth_mode == "portal_ticket":
        declared_headers.append(read_portal_ticket_header(spec, operation_id))
    path_parameters = _path_parameters(path, operation_id)
    _check_argument_names(path_parameters, declared_headers, operation_id)
    request_content_type, request_schema, has_request_body = _request_schema(spec, raw_operation)
    if has_request_body and method in METHODS_WITHOUT_BODY:
        raise ValueError(f"{operation_id} is a {method.upper()} that declares a request body")
    response_kind, response_schema = _response(spec, raw_operation)
    response_data_schema = _data_schema(spec, response_schema)
    request_body = maybe_resolve_ref(spec, raw_operation.get("requestBody"))
    query_parameters = _query_parameters(spec, parameters)

    return Operation(
        operation_id=operation_id,
        method_name=to_snake(
            operation_id_to_method_name(operation_id, service_pascal, resource_pascal)
        ),
        http_method=method.upper(),
        path=path,
        auth_mode=auth_mode,
        request_content_type=request_content_type,
        has_request_body=has_request_body,
        request_body_required=(
            isinstance(request_body, dict) and request_body.get("required") is True
        ),
        response_kind=response_kind,
        cursor_location=_cursor_location(
            response_kind, request_content_type, request_schema, query_parameters, operation_id
        ),
        path_parameters=path_parameters,
        query_parameters=query_parameters,
        request_schema=request_schema,
        response_schema=response_schema,
        response_data_schema=response_data_schema,
        response_item_schema=_item_schema(spec, response_data_schema),
        scopes=scopes,
        accepts_idempotency_key=method == "post" and declares_idempotency_key,
        declared_headers=tuple(declared_headers),
    )


def _check_argument_names(
    path_parameters: tuple[Parameter, ...],
    declared_headers: list[DeclaredHeader],
    operation_id: str,
) -> None:
    names = [parameter.python_name for parameter in path_parameters]
    for header in declared_headers:
        if header.python_name in RESERVED_PARAMETER_NAMES or header.python_name in names:
            raise ValueError(f"{operation_id} declares the header argument {header.python_name}")
        names.append(header.python_name)


def _resolved_parameters(
    spec: dict[str, Any],
    operation: dict[str, Any],
    operation_id: str,
) -> list[dict[str, Any]]:
    declared = operation.get("parameters", [])
    if not isinstance(declared, list):
        raise ValueError(f"{operation_id} has parameters that are not a list")
    resolved: list[dict[str, Any]] = []
    for raw_parameter in declared:
        parameter = maybe_resolve_ref(spec, raw_parameter)
        if not isinstance(parameter, dict) or not isinstance(parameter.get("name"), str):
            raise ValueError(f"{operation_id} has a parameter without a name")
        resolved.append(parameter)
    return resolved


def _header_semantics(
    spec: dict[str, Any],
    parameters: list[dict[str, Any]],
    operation_id: str,
) -> tuple[tuple[str, ...], bool, list[DeclaredHeader]]:
    scopes: list[str] = []
    declared_headers: list[DeclaredHeader] = []
    declares_idempotency_key = False
    for parameter in parameters:
        if parameter.get("in") != "header":
            continue
        header_name = str(parameter["name"]).lower()
        scope = SCOPE_HEADER_NAMES.get(header_name)
        if scope is not None:
            scopes.append(scope)
        elif header_name == IDEMPOTENCY_KEY_HEADER:
            declares_idempotency_key = True
        elif header_name != REQUEST_ID_HEADER:
            declared_headers.append(read_declared_header(spec, parameter, operation_id))
    return tuple(scopes), declares_idempotency_key, declared_headers


def _path_parameters(path: str, operation_id: str) -> tuple[Parameter, ...]:
    parameters: list[Parameter] = []
    for match in re.finditer(r"\{(\w+)\}", path):
        python_name = to_snake(match.group(1))
        if python_name in RESERVED_PARAMETER_NAMES:
            raise ValueError(f"{operation_id} has the path parameter {python_name}")
        if any(parameter.python_name == python_name for parameter in parameters):
            raise ValueError(f"{operation_id} repeats the path parameter {python_name}")
        parameters.append(
            Parameter(
                name=match.group(1),
                python_name=python_name,
                required=True,
                schema={"type": "string"},
            )
        )
    return tuple(parameters)


def _query_parameters(
    spec: dict[str, Any],
    parameters: list[dict[str, Any]],
) -> tuple[Parameter, ...]:
    query: list[Parameter] = []
    for parameter in parameters:
        if parameter.get("in") != "query":
            continue
        schema = maybe_resolve_ref(spec, parameter.get("schema"))
        query.append(
            Parameter(
                name=str(parameter["name"]),
                python_name=to_snake(str(parameter["name"])),
                required=parameter.get("required") is True,
                schema=schema if isinstance(schema, dict) else {},
            )
        )
    return tuple(query)


def _cursor_location(
    response_kind: ResponseKind,
    request_content_type: str,
    request_schema: dict[str, Any] | None,
    query_parameters: tuple[Parameter, ...],
    operation_id: str,
) -> CursorLocation:
    if response_kind != "list":
        return "none"
    properties = request_schema.get("properties") if request_schema is not None else None
    in_body = (
        request_content_type == "application/json"
        and isinstance(properties, dict)
        and "cursor" in properties
    )
    in_query = any(parameter.name == "cursor" for parameter in query_parameters)
    if in_body and in_query:
        raise ValueError(f"{operation_id} declares a cursor in both its query and its body")
    if in_body:
        return "body"
    return "query" if in_query else "none"


def _request_schema(
    spec: dict[str, Any],
    operation: dict[str, Any],
) -> tuple[str, dict[str, Any] | None, bool]:
    request_body = maybe_resolve_ref(spec, operation.get("requestBody"))
    if not isinstance(request_body, dict):
        return "application/json", None, False
    content = request_body.get("content")
    if not isinstance(content, dict) or not content:
        return "application/json", None, True
    content_type = str(next(iter(content)))
    media = content.get(content_type)
    schema = maybe_resolve_ref(spec, media.get("schema")) if isinstance(media, dict) else None
    return content_type, schema if isinstance(schema, dict) else None, True


def _response(
    spec: dict[str, Any],
    operation: dict[str, Any],
) -> tuple[ResponseKind, dict[str, Any]]:
    responses = operation.get("responses")
    responses = responses if isinstance(responses, dict) else {}
    success_code = next((str(code) for code in responses if str(code).startswith("2")), "200")
    response = maybe_resolve_ref(spec, responses.get(success_code))
    content = response.get("content") if isinstance(response, dict) else None
    media = None
    if isinstance(content, dict) and content:
        media = content.get(next(iter(content)))
    if not isinstance(media, dict) or success_code == NO_CONTENT_STATUS:
        return "empty", {}

    schema = maybe_resolve_ref(spec, media.get("schema"))
    schema = schema if isinstance(schema, dict) else {}
    properties = schema.get("properties")
    if not isinstance(properties, dict) or "data" not in properties:
        return "body", schema

    data = properties["data"]
    if isinstance(data, dict) and data.get("type") == "array" and "cursor" in properties:
        return "list", schema
    return "envelope", schema


def _data_schema(spec: dict[str, Any], response_schema: dict[str, Any]) -> dict[str, Any]:
    properties = response_schema.get("properties")
    if not isinstance(properties, dict) or "data" not in properties:
        return response_schema
    data_schema = maybe_resolve_ref(spec, properties["data"])
    return data_schema if isinstance(data_schema, dict) else {}


def _item_schema(spec: dict[str, Any], data_schema: dict[str, Any]) -> dict[str, Any] | None:
    if data_schema.get("type") != "array":
        return None
    items = maybe_resolve_ref(spec, data_schema.get("items"))
    return items if isinstance(items, dict) else {}
