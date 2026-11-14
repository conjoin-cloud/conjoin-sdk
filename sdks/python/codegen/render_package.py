from __future__ import annotations

from collections.abc import Mapping

from codegen.ir import ResourceGroup
from codegen.naming import resource_attribute_name, to_pascal, to_snake
from codegen.render_resources import MAX_LINE_LENGTH, resource_class_name

ServiceGroups = tuple[tuple[str, tuple[ResourceGroup, ...]], ...]

HANDWRITTEN_SERVICE_MODULES: Mapping[str, str] = {
    "ai": "conjoin_cloud._ai",
    "storage": "conjoin_cloud._storage",
}


def service_class_name(service: str, *, is_async: bool) -> str:
    return f"{'Async' if is_async else ''}{to_pascal(service)}Resource"


def render_service_module(package: str, service: str, groups: tuple[ResourceGroup, ...]) -> str:
    lines = ["from __future__ import annotations", "", "from typing import TYPE_CHECKING", ""]
    for group in groups:
        module = f"{package}.{to_snake(service)}._{to_snake(group.resource)}"
        lines.append(f"from {module} import (")
        lines.append(f"    {resource_class_name(group, is_async=True)},")
        lines.append(f"    {resource_class_name(group, is_async=False)},")
        lines.append(")")
    lines.extend(["", "if TYPE_CHECKING:", "    from conjoin_cloud import AsyncConjoin, Conjoin"])

    attributes = _resource_attributes(service, groups)
    for is_async in (False, True):
        client_type = "AsyncConjoin" if is_async else "Conjoin"
        lines.extend(
            [
                "",
                "",
                f"class {service_class_name(service, is_async=is_async)}:",
                f"    def __init__(self, client: {client_type}) -> None:",
                "        self._client = client",
            ]
        )
        for attribute, group in attributes:
            lines.extend(
                _assignment(f"self.{attribute}", resource_class_name(group, is_async=is_async))
            )
    return "\n".join(lines) + "\n"


def render_frontend_root(package: str, services: ServiceGroups) -> str:
    lines = ["from __future__ import annotations", "", "from typing import TYPE_CHECKING", ""]
    for service, _groups in services:
        lines.append(
            f"from {package}.{to_snake(service)} import "
            f"{service_class_name(service, is_async=True)}, "
            f"{service_class_name(service, is_async=False)}"
        )
    lines.extend(["", "if TYPE_CHECKING:", "    from conjoin_cloud import AsyncConjoin, Conjoin"])
    for is_async in (False, True):
        client_type = "AsyncConjoin" if is_async else "Conjoin"
        lines.extend(
            [
                "",
                "",
                f"class {'Async' if is_async else ''}FrontendResource:",
                f"    def __init__(self, client: {client_type}) -> None:",
                "        self._client = client",
            ]
        )
        for service, _groups in services:
            lines.append(
                f"        self.{to_snake(service)} = "
                f"{service_class_name(service, is_async=is_async)}(client)"
            )
    return "\n".join(lines) + "\n"


def render_client_mixins(package: str, frontend_package: str, services: ServiceGroups) -> str:
    lines = ["from __future__ import annotations", "", "from typing import TYPE_CHECKING, Any", ""]
    lines.append(f"from {frontend_package} import AsyncFrontendResource, FrontendResource")
    for service, _groups in services:
        if service in HANDWRITTEN_SERVICE_MODULES:
            continue
        lines.append(
            f"from {package}.{to_snake(service)} import "
            f"{service_class_name(service, is_async=True)}, "
            f"{service_class_name(service, is_async=False)}"
        )
    handwritten_imports = [
        f"    from {module} import {service_class_name(service, is_async=True)}, "
        f"{service_class_name(service, is_async=False)}"
        for service, _groups in services
        if (module := HANDWRITTEN_SERVICE_MODULES.get(service)) is not None
    ]
    if handwritten_imports:
        lines.extend(["", "if TYPE_CHECKING:", *handwritten_imports])

    for is_async in (False, True):
        lines.extend(_mixin_class(services, is_async=is_async))
    return "\n".join(lines) + "\n"


def render_generated_init(package: str, services: ServiceGroups) -> str:
    names = ["AsyncGeneratedResourcesMixin", "SyncGeneratedResourcesMixin"]
    lines = [
        f"from {package}._client_mixins import (",
        "    AsyncGeneratedResourcesMixin,",
        "    SyncGeneratedResourcesMixin,",
        ")",
    ]
    for service, _groups in services:
        async_name = service_class_name(service, is_async=True)
        sync_name = service_class_name(service, is_async=False)
        lines.append(f"from {package}.{to_snake(service)} import {async_name}, {sync_name}")
        names.extend([async_name, sync_name])
    lines.extend(["", "__all__ = ("])
    lines.extend(f"    {name!r}," for name in sorted(names))
    lines.extend([")", ""])
    return "\n".join(lines)


def _mixin_class(services: ServiceGroups, *, is_async: bool) -> list[str]:
    frontend_class = f"{'Async' if is_async else ''}FrontendResource"
    lines = ["", "", f"class {'Async' if is_async else 'Sync'}GeneratedResourcesMixin:"]
    for service, _groups in services:
        lines.append(f"    {to_snake(service)}: {service_class_name(service, is_async=is_async)}")
    lines.extend(
        [
            f"    frontend: {frontend_class}",
            "",
            "    def _init_generated_resources(self: Any) -> None:",
        ]
    )
    handwritten = [
        service for service, _groups in services if service in HANDWRITTEN_SERVICE_MODULES
    ]
    for service in handwritten:
        lines.append(
            f"        from {HANDWRITTEN_SERVICE_MODULES[service]} import "
            f"{service_class_name(service, is_async=is_async)}"
        )
    if handwritten:
        lines.append("")
    for service, _groups in services:
        class_name = service_class_name(service, is_async=is_async)
        lines.append(f"        self.{to_snake(service)} = {class_name}(self)")
    lines.append(f"        self.frontend = {frontend_class}(self)")
    return lines


def _resource_attributes(
    service: str,
    groups: tuple[ResourceGroup, ...],
) -> list[tuple[str, ResourceGroup]]:
    attributes: list[tuple[str, ResourceGroup]] = []
    seen: set[str] = set()
    for group in groups:
        attribute = resource_attribute_name(group.resource)
        if attribute in seen:
            raise ValueError(f"Two {service} resources both generate the attribute {attribute}")
        seen.add(attribute)
        attributes.append((attribute, group))
    return attributes


def _assignment(target: str, class_name: str) -> list[str]:
    line = f"        {target} = {class_name}(client)"
    if len(line) <= MAX_LINE_LENGTH:
        return [line]
    return [f"        {target} = {class_name}(", "            client,", "        )"]
