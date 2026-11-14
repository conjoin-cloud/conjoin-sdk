from __future__ import annotations

from codegen.ir import Operation, ResourceGroup
from codegen.naming import pluralize, strip_v1, to_snake
from codegen.render_entries import MethodEntry, cast_expression, response_annotation

MAX_LINE_LENGTH = 100
MULTIPART = "multipart/form-data"


def resource_class_name(group: ResourceGroup, *, is_async: bool) -> str:
    prefix = "Async" if is_async else ""
    return f"{prefix}{group.service_pascal}{pluralize(group.resource_pascal)}Resource"


def render_resource_module(
    group: ResourceGroup,
    entries: tuple[MethodEntry, ...],
    models_module: str,
) -> str:
    lines = [
        "from __future__ import annotations",
        "",
        "from collections.abc import Mapping",
        "from typing import TYPE_CHECKING, Any",
        "",
        *_runtime_imports(entries),
    ]
    model_names = _model_imports(entries)
    if model_names:
        lines.append(f"from {models_module} import (")
        lines.extend(f"    {name}," for name in model_names)
        lines.append(")")
    lines.extend(["", "if TYPE_CHECKING:", "    from conjoin_cloud import AsyncConjoin, Conjoin"])

    alias_lines = _alias_constants(entries)
    if alias_lines:
        lines.extend(["", "", *alias_lines])

    for is_async in (False, True):
        lines.extend(["", ""])
        lines.extend(_resource_class(group, entries, is_async=is_async))
    return "\n".join(lines).rstrip() + "\n"


def _runtime_imports(entries: tuple[MethodEntry, ...]) -> list[str]:
    operations = [entry.operation for entry in entries]
    lines: list[str] = []
    if any(operation.response_kind == "list" for operation in operations):
        lines.append("from conjoin_cloud._models import AsyncPage, Page")
    if any(_is_multipart(operation) for operation in operations):
        lines.append("from conjoin_cloud._multipart import MultipartBody")
    option_names = ["RequestOptions"]
    if any(operation.auth_mode == "none" for operation in operations):
        option_names.insert(0, "AUTH_NONE")
    if any(operation.auth_mode == "scim_bearer" for operation in operations):
        option_names.append("scim_bearer_auth")
    lines.append(f"from conjoin_cloud._request_options import {', '.join(option_names)}")
    if any(operation.path_parameters for operation in operations):
        lines.append("from conjoin_cloud._url import encode_path_param")
    if any(_body_aliases(entry) or _query_aliases(entry) for entry in entries):
        lines.append("from conjoin_cloud._wire import wire_names")
    return lines


def _resource_class(
    group: ResourceGroup,
    entries: tuple[MethodEntry, ...],
    *,
    is_async: bool,
) -> list[str]:
    class_name = resource_class_name(group, is_async=is_async)
    client_type = "AsyncConjoin" if is_async else "Conjoin"
    uses_scim = any(entry.operation.auth_mode == "scim_bearer" for entry in entries)
    lines = [f"class {class_name}:"]
    if uses_scim:
        lines.extend(
            [
                "    def __init__(self, client: "
                f"{client_type}, *, scim_token: str | None = None) -> None:",
                "        self._client = client",
                "        self._scim_token = scim_token",
                "",
                f"    def with_token(self, scim_token: str) -> {class_name}:",
                f"        return {class_name}(self._client, scim_token=scim_token)",
            ]
        )
    else:
        lines.extend(
            [
                f"    def __init__(self, client: {client_type}) -> None:",
                "        self._client = client",
            ]
        )
    for entry in entries:
        lines.append("")
        lines.extend(_method(entry, is_async=is_async))
    return lines


def _method(entry: MethodEntry, *, is_async: bool) -> list[str]:
    operation = entry.operation
    annotation = response_annotation(entry, is_async=is_async)
    lines = [f"    {'async ' if is_async else ''}def {entry.method_name}(", "        self,"]
    lines.extend(f"        {parameter}," for parameter in _method_parameters(entry))
    lines.extend(
        [
            "        *,",
            "        request_options: RequestOptions | Mapping[str, Any] | None = None,",
            f"    ) -> {annotation}:",
        ]
    )
    call_prefix = "await " if is_async else ""
    statement = "" if annotation == "None" else "return "
    lines.append(f"        {statement}{call_prefix}self._client.request(")
    lines.append(f"            {operation.http_method!r},")
    lines.extend(_path_lines(operation))
    for argument in _call_arguments(entry, is_async=is_async):
        lines.append(f"            {argument},")
    lines.append("        )")
    return lines


def _call_arguments(entry: MethodEntry, *, is_async: bool) -> list[str]:
    operation = entry.operation
    arguments: list[str] = []
    if operation.query_parameters:
        aliases = _query_aliases(entry)
        arguments.append(
            f"query=wire_names(query, {_alias_name(entry, 'query')})" if aliases else "query=query"
        )
    if operation.has_request_body:
        arguments.append(f"body={_body_expression(entry)}")
    cast = cast_expression(entry, is_async=is_async)
    if cast != "None":
        arguments.append(f"cast_to={cast}")
    arguments.append("request_options=request_options")
    if operation.scopes:
        scopes = "".join(f"{scope!r}, " for scope in operation.scopes).rstrip()
        arguments.append(f"scopes=({scopes})")
    if operation.accepts_idempotency_key:
        arguments.append("accepts_idempotency_key=True")
    if operation.auth_mode == "none":
        arguments.append("default_auth=AUTH_NONE")
    elif operation.auth_mode == "scim_bearer":
        arguments.append("default_auth=scim_bearer_auth(self._scim_token)")
    if operation.response_kind == "body":
        arguments.append("unwrap_data=False")
    return arguments


def _method_parameters(entry: MethodEntry) -> list[str]:
    operation = entry.operation
    parameters = [f"{parameter.python_name}: str" for parameter in operation.path_parameters]
    query_required = any(parameter.required for parameter in operation.query_parameters)
    if operation.has_request_body:
        body_type = entry.body_type or "Mapping[str, Any]"
        if operation.request_body_required:
            parameters.append(f"data: {body_type}")
        elif operation.query_parameters and query_required:
            raise ValueError(f"{operation.operation_id} has an optional body and a required query")
        else:
            parameters.append(f"data: {body_type} | None = None")
    if operation.query_parameters:
        query_type = entry.query_type or "Mapping[str, Any]"
        parameters.append(
            f"query: {query_type}" if query_required else f"query: {query_type} | None = None"
        )
    return parameters


def _body_expression(entry: MethodEntry) -> str:
    operation = entry.operation
    expression = "data"
    if _body_aliases(entry):
        expression = f"wire_names(data, {_alias_name(entry, 'body')})"
    if not _is_multipart(operation):
        return expression
    if operation.request_body_required:
        return f"MultipartBody({expression})"
    return f"None if data is None else MultipartBody({expression})"


def _path_lines(operation: Operation) -> list[str]:
    path = strip_v1(operation.path)
    if not operation.path_parameters:
        return [f"            {path!r},"]

    segments: list[str] = []
    for index, part in enumerate(path.split("/")):
        rendered = part
        for parameter in operation.path_parameters:
            rendered = rendered.replace(
                f"{{{parameter.name}}}",
                f"{{encode_path_param({parameter.python_name})}}",
            )
        segments.append(rendered if index == 0 else f"/{rendered}")

    single = f"            {_string_literal(''.join(segments))},"
    if len(single) <= MAX_LINE_LENGTH:
        return [single]

    lines = ["            ("]
    current = ""
    for segment in segments:
        candidate = f"                {_string_literal(current + segment)}"
        if current and len(candidate) > MAX_LINE_LENGTH:
            lines.append(f"                {_string_literal(current)}")
            current = ""
        current += segment
    lines.append(f"                {_string_literal(current)}")
    lines.append("            ),")
    return lines


def _string_literal(value: str) -> str:
    return f"f{value!r}" if "{" in value else repr(value)


def _alias_constants(entries: tuple[MethodEntry, ...]) -> list[str]:
    lines: list[str] = []
    for entry in entries:
        for kind, aliases in (("body", _body_aliases(entry)), ("query", _query_aliases(entry))):
            if not aliases:
                continue
            lines.append(f"{_alias_name(entry, kind)} = {{")
            lines.extend(
                f"    {python_name!r}: {wire_name!r}," for python_name, wire_name in aliases.items()
            )
            lines.append("}")
    return lines


def _alias_name(entry: MethodEntry, kind: str) -> str:
    return f"_{entry.method_name.upper()}_{kind.upper()}_ALIASES"


def _body_aliases(entry: MethodEntry) -> dict[str, str]:
    schema = entry.operation.request_schema
    properties = schema.get("properties") if schema is not None else None
    return _aliases(properties) if isinstance(properties, dict) else {}


def _query_aliases(entry: MethodEntry) -> dict[str, str]:
    parameters = entry.operation.query_parameters
    return _aliases({parameter.name: parameter.schema for parameter in parameters})


def _aliases(fields: dict[str, object]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for wire_name in sorted(fields):
        python_name = to_snake(wire_name)
        if python_name != wire_name:
            aliases[python_name] = wire_name
    return aliases


def _model_imports(entries: tuple[MethodEntry, ...]) -> tuple[str, ...]:
    names: set[str] = set()
    for entry in entries:
        for name in (entry.response_model, entry.body_type, entry.query_type):
            if name is not None:
                names.add(name)
    return tuple(sorted(names))


def _is_multipart(operation: Operation) -> bool:
    return operation.has_request_body and operation.request_content_type.lower() == MULTIPART
