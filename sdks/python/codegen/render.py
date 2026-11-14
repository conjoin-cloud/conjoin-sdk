from __future__ import annotations

import shutil
from pathlib import Path

from codegen.ir import ResourceGroup, collect_resource_groups
from codegen.naming import to_snake
from codegen.render_entries import MethodEntry, resolve_method_entries
from codegen.render_models import render_models_module
from codegen.render_package import (
    ServiceGroups,
    render_client_mixins,
    render_frontend_root,
    render_generated_init,
    render_service_module,
)
from codegen.render_resources import render_resource_module
from codegen.spec import BACKEND_DOCUMENT, FRONTEND_DOCUMENT, GeneratedDocument, load_openapi


def render_all(output_root: Path | None = None) -> dict[str, int]:
    backend_root = BACKEND_DOCUMENT.output_dir if output_root is None else output_root
    frontend_root = backend_root / FRONTEND_DOCUMENT.output_dir.relative_to(
        BACKEND_DOCUMENT.output_dir
    )
    if backend_root.exists():
        shutil.rmtree(backend_root)

    counts: dict[str, int] = {}
    backend_services = _render_document(BACKEND_DOCUMENT, backend_root, counts)
    frontend_services = _render_document(FRONTEND_DOCUMENT, frontend_root, counts)

    _write(
        frontend_root / "__init__.py",
        render_frontend_root(FRONTEND_DOCUMENT.package, frontend_services),
    )
    _write(
        backend_root / "_client_mixins.py",
        render_client_mixins(BACKEND_DOCUMENT.package, FRONTEND_DOCUMENT.package, backend_services),
    )
    _write(
        backend_root / "__init__.py",
        render_generated_init(BACKEND_DOCUMENT.package, backend_services),
    )
    return counts


def document_groups(document: GeneratedDocument) -> tuple[ResourceGroup, ...]:
    return collect_resource_groups(load_openapi(document.spec_file))


def _render_document(
    document: GeneratedDocument,
    output_root: Path,
    counts: dict[str, int],
) -> ServiceGroups:
    groups = sorted(document_groups(document), key=lambda group: (group.service, group.resource))
    rendered: list[tuple[ResourceGroup, tuple[MethodEntry, ...]]] = [
        (group, resolve_method_entries(group)) for group in groups
    ]
    models_module = f"{document.package}._models"

    _write(
        output_root / "_models.py",
        render_models_module(entry for _group, entries in rendered for entry in entries),
    )
    written: set[Path] = set()
    for group, entries in rendered:
        module_path = output_root / to_snake(group.service) / f"_{to_snake(group.resource)}.py"
        if module_path in written:
            raise ValueError(f"Two {group.service} resources both generate {module_path.name}")
        written.add(module_path)
        _write(module_path, render_resource_module(group, entries, models_module))

    services = _services(groups)
    for service, service_groups in services:
        _write(
            output_root / to_snake(service) / "__init__.py",
            render_service_module(document.package, service, service_groups),
        )

    counts[document.spec_file] = sum(len(group.operations) for group in groups)
    return services


def _services(groups: list[ResourceGroup]) -> ServiceGroups:
    by_service: dict[str, list[ResourceGroup]] = {}
    for group in groups:
        by_service.setdefault(group.service, []).append(group)
    return tuple(
        (service, tuple(sorted(service_groups, key=lambda group: group.resource)))
        for service, service_groups in sorted(by_service.items())
    )


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
