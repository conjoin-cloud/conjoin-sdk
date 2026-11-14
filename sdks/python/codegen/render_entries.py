from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any

from codegen.ir import Operation, ResourceGroup
from codegen.naming import pluralize, to_pascal, to_snake
from codegen.schema import is_object_schema


@dataclass(frozen=True)
class MethodEntry:
    operation: Operation
    method_name: str
    base_name: str
    response_model: str | None
    response_model_schema: dict[str, Any] | None
    body_type: str | None
    query_type: str | None


def resolve_method_entries(group: ResourceGroup) -> tuple[MethodEntry, ...]:
    counts = Counter(operation.method_name for operation in group.operations)
    resolved: list[tuple[str, Operation]] = []
    for operation in group.operations:
        name = operation.method_name
        if counts[name] > 1:
            if operation.response_kind == "list":
                name = "list" if name in {"get", "read"} else f"list_{name}"
            elif pluralize(group.resource_pascal) in operation.operation_id:
                name = to_snake(pluralize(name))
        resolved.append((name, operation))

    final_counts = Counter(name for name, _operation in resolved)
    entries: list[MethodEntry] = []
    seen: set[str] = set()
    for name, operation in resolved:
        method_name = to_snake(operation.operation_id) if final_counts[name] > 1 else to_snake(name)
        if method_name in seen:
            raise ValueError(f"Two operations both generate the method {method_name}")
        seen.add(method_name)
        base_name = f"{group.service_pascal}{group.resource_pascal}{to_pascal(method_name)}"
        model_name, model_schema = _response_model(operation, base_name)
        entries.append(
            MethodEntry(
                operation=operation,
                method_name=method_name,
                base_name=base_name,
                response_model=model_name,
                response_model_schema=model_schema,
                body_type=_body_type(operation, base_name),
                query_type=f"{base_name}Query" if operation.query_parameters else None,
            )
        )
    return tuple(entries)


def response_annotation(entry: MethodEntry, *, is_async: bool) -> str:
    operation = entry.operation
    if operation.response_kind == "empty":
        return "None"
    if operation.response_kind == "list":
        page = "AsyncPage" if is_async else "Page"
        return f"{page}[{entry.response_model or 'Any'}]"
    if entry.response_model is None:
        return "Any"
    if operation.response_kind == "envelope" and operation.response_item_schema is not None:
        return f"list[{entry.response_model}]"
    return entry.response_model


def cast_expression(entry: MethodEntry, *, is_async: bool) -> str:
    annotation = response_annotation(entry, is_async=is_async)
    return "None" if annotation in ("Any", "None") else annotation


def _response_model(
    operation: Operation,
    base_name: str,
) -> tuple[str | None, dict[str, Any] | None]:
    if operation.response_kind == "empty":
        return None, None
    if operation.response_kind == "body":
        schema = operation.response_schema
        return (f"{base_name}Response", schema) if is_object_schema(schema) else (None, None)
    item_schema = operation.response_item_schema
    if operation.response_kind == "list" or item_schema is not None:
        if item_schema is not None and is_object_schema(item_schema):
            return f"{base_name}Item", item_schema
        return None, None
    schema = operation.response_data_schema
    return (f"{base_name}Response", schema) if is_object_schema(schema) else (None, None)


def _body_type(operation: Operation, base_name: str) -> str | None:
    if operation.request_schema is not None and is_object_schema(operation.request_schema):
        return f"{base_name}Request"
    return None
