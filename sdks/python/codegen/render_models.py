from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar

from codegen.naming import to_snake
from codegen.render_entries import MethodEntry
from codegen.schema import (
    FieldDef,
    ModelDef,
    TypedDictDef,
    model_from_schema,
    schema_annotation,
    typed_dict_from_schema,
    union_with_none,
)

MAX_LINE_LENGTH = 100

GeneratedType = TypeVar("GeneratedType", ModelDef, TypedDictDef)


def render_models_module(entries: Iterable[MethodEntry]) -> str:
    models: dict[str, ModelDef] = {}
    typed_dicts: dict[str, TypedDictDef] = {}

    for entry in entries:
        if entry.response_model is not None and entry.response_model_schema is not None:
            _add_unique(
                models,
                model_from_schema(entry.response_model, entry.response_model_schema),
            )
        if entry.body_type is not None and entry.operation.request_schema is not None:
            _add_unique(
                typed_dicts,
                typed_dict_from_schema(entry.body_type, entry.operation.request_schema),
            )
        if entry.query_type is not None:
            _add_unique(
                typed_dicts,
                TypedDictDef(
                    name=entry.query_type,
                    fields=tuple(
                        FieldDef(
                            wire_name=parameter.name,
                            python_name=to_snake(parameter.name),
                            annotation=schema_annotation(parameter.schema),
                            required=parameter.required,
                        )
                        for parameter in entry.operation.query_parameters
                    ),
                ),
            )

    body: list[str] = []
    for model in sorted(models.values(), key=lambda item: item.name):
        body.extend(_render_model(model))
        body.extend(["", ""])
    for typed_dict in sorted(typed_dicts.values(), key=lambda item: item.name):
        body.extend(_render_typed_dict(typed_dict))
        body.extend(["", ""])
    return "\n".join([*_module_imports(body), *body]).rstrip() + "\n"


def _module_imports(body: list[str]) -> list[str]:
    text = "\n".join(body)
    lines = ["from __future__ import annotations", ""]
    if "Sequence[" in text:
        lines.append("from collections.abc import Sequence")
    lines.extend(["from typing import Any, TypedDict", ""])
    if "Field(" in text:
        lines.extend(["from pydantic import Field", ""])
    lines.extend(["from conjoin_cloud._models import ConjoinModel", "", ""])
    return lines


def _add_unique(registry: dict[str, GeneratedType], item: GeneratedType) -> None:
    existing = registry.get(item.name)
    if existing is not None and existing != item:
        raise ValueError(f"Two operations both generate the type {item.name}")
    registry[item.name] = item


def _render_model(model: ModelDef) -> list[str]:
    lines = [f"class {model.name}(ConjoinModel):"]
    if not model.fields:
        return [*lines, "    pass"]
    for field in model.fields:
        annotation = field.annotation if field.required else union_with_none(field.annotation)
        if field.wire_name == field.python_name:
            default = "" if field.required else " = None"
            lines.append(f"    {field.python_name}: {annotation}{default}")
            continue
        default_expr = "..." if field.required else "None"
        lines.extend(_field_assignment_lines(field, annotation, default_expr))
    return lines


def _render_typed_dict(typed_dict: TypedDictDef) -> list[str]:
    required_fields = tuple(field for field in typed_dict.fields if field.required)
    optional_fields = tuple(field for field in typed_dict.fields if not field.required)
    if not typed_dict.fields:
        return [*_class_header(typed_dict.name, ("TypedDict", "total=False")), "    pass"]

    if required_fields and optional_fields:
        required_name = f"_{typed_dict.name}Required"
        lines = _class_header(required_name, ("TypedDict",))
        lines.extend(f"    {field.python_name}: {field.annotation}" for field in required_fields)
        lines.extend(["", "", *_class_header(typed_dict.name, (required_name, "total=False"))])
        lines.extend(f"    {field.python_name}: {field.annotation}" for field in optional_fields)
        return lines

    bases = ("TypedDict",) if required_fields else ("TypedDict", "total=False")
    lines = _class_header(typed_dict.name, bases)
    lines.extend(f"    {field.python_name}: {field.annotation}" for field in typed_dict.fields)
    return lines


def _class_header(name: str, bases: tuple[str, ...]) -> list[str]:
    line = f"class {name}({', '.join(bases)}):"
    if len(line) <= MAX_LINE_LENGTH:
        return [line]
    return [f"class {name}(", *(f"    {base}," for base in bases), "):"]


def _field_assignment_lines(field: FieldDef, annotation: str, default_expr: str) -> list[str]:
    alias = f"alias={field.wire_name!r}"
    line = f"    {field.python_name}: {annotation} = Field({default_expr}, {alias})"
    if len(line) <= MAX_LINE_LENGTH:
        return [line]
    return [
        f"    {field.python_name}: {annotation} = Field(",
        f"        {default_expr},",
        f"        alias={field.wire_name!r},",
        "    )",
    ]
