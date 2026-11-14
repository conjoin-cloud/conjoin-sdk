from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SPEC_DIR = Path(__file__).resolve().parents[3] / "spec"
GENERATED_ROOT = Path(__file__).resolve().parents[1] / "src" / "conjoin_cloud" / "generated"


@dataclass(frozen=True)
class GeneratedDocument:
    spec_file: str
    package: str
    output_dir: Path


BACKEND_DOCUMENT = GeneratedDocument(
    spec_file="openapi.json",
    package="conjoin_cloud.generated",
    output_dir=GENERATED_ROOT,
)
FRONTEND_DOCUMENT = GeneratedDocument(
    spec_file="openapi-frontend.json",
    package="conjoin_cloud.generated.frontend",
    output_dir=GENERATED_ROOT / "frontend",
)
DOCUMENTS = (BACKEND_DOCUMENT, FRONTEND_DOCUMENT)


def load_openapi(spec_file: str, spec_dir: Path = SPEC_DIR) -> dict[str, Any]:
    document = json.loads((spec_dir / spec_file).read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError(f"{spec_file} is not an OpenAPI object")
    return document


def resolve_ref(spec: dict[str, Any], value: dict[str, Any]) -> dict[str, Any]:
    ref = value.get("$ref")
    if not isinstance(ref, str):
        return value

    if not ref.startswith("#/"):
        raise ValueError(f"Unsupported OpenAPI reference: {ref}")

    current: Any = spec
    for part in ref[2:].split("/"):
        if not isinstance(current, dict) or part not in current:
            raise ValueError(f"Unresolved OpenAPI reference: {ref}")
        current = current[part]

    if not isinstance(current, dict):
        raise ValueError(f"OpenAPI reference did not resolve to an object: {ref}")
    return current


def maybe_resolve_ref(spec: dict[str, Any], value: Any) -> Any:
    if isinstance(value, dict) and "$ref" in value:
        return resolve_ref(spec, value)
    return value
