from __future__ import annotations

import math
from typing import Any

PATTERN_SAMPLES = {
    "^[A-Z]{2}$": "GH",
    "^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$": (
        "cnj_req_0198f0f7-5d0b-7b4a-8d5a-cf5693f0b2c1"
    ),
    "^[0-9a-f]+$": "a1b2c3",
    "^[a-z][a-z0-9:._-]*$": "invoice.paid",
    "^[a-z0-9][a-z0-9:._-]*$": "invoice.paid",
    "^[0-9]{6}$": "123456",
    "^[a-z]{3,8}$": "monthly",
    (
        "^[A-Za-z0-9_]+(?:\\[(?:0|[1-9][0-9]?)\\])?"
        "(?:\\.[A-Za-z0-9_]+(?:\\[(?:0|[1-9][0-9]?)\\])?){0,7}$"
    ): "items[0].name",
    "^[\\w-]{1,80}$": "harbour-ledger",
    "^[a-z.]+$": "billing.read",
    "^[a-z]{3,10}$": "weekly",
    "^authact_[a-zA-Z0-9_-]+$": "authact_harbour_ledger",
    "^[a-z][a-z0-9]*(_[a-z0-9]+)*$": "harbour_ledger",
}

FORMAT_SAMPLES = {
    "uri": "https://ledger.example.com/hooks/conjoin",
    "email": "ledger.owner@example.com",
    "date-time": "2026-11-14T10:00:00.000Z",
    "date": "2026-11-14",
    "uuid": "0198f0f7-5d0b-4b4a-8d5a-cf5693f0b2c1",
}

BINARY_SAMPLE = b"harbour ledger statement"
STRING_SEED = "harbourledger"
MAX_DEPTH = 12


class SchemaSampler:
    def __init__(self, document: dict[str, Any]) -> None:
        self._document = document

    def sample(self, schema: Any) -> Any:
        return self._sample(schema, 0)

    def resolve(self, schema: Any) -> dict[str, Any]:
        if not isinstance(schema, dict):
            return {}
        reference = schema.get("$ref")
        if not isinstance(reference, str):
            return schema
        node: Any = self._document
        for key in reference.removeprefix("#/").split("/"):
            node = node.get(key) if isinstance(node, dict) else None
        if not isinstance(node, dict):
            raise ValueError(f"Unresolved schema reference {reference}")
        return self.resolve(node)

    def _sample(self, raw: Any, depth: int) -> Any:
        if not isinstance(raw, dict) or depth > MAX_DEPTH:
            return None
        schema = self.resolve(raw)

        if "const" in schema:
            return schema["const"]
        enum = schema.get("enum")
        if isinstance(enum, list) and enum:
            return next((value for value in enum if value is not None), enum[0])

        for key in ("oneOf", "anyOf"):
            branches = schema.get(key)
            if isinstance(branches, list) and branches:
                candidates = [self._sample(branch, depth + 1) for branch in branches]
                return next((value for value in candidates if value is not None), candidates[0])

        parts = schema.get("allOf")
        if isinstance(parts, list):
            merged: dict[str, Any] = {}
            for part in parts:
                sampled = self._sample(part, depth + 1)
                if isinstance(sampled, dict):
                    merged.update(sampled)
            return merged

        declared = schema.get("type")
        if isinstance(declared, list):
            declared = next((value for value in declared if value != "null"), "null")
        return self._sample_type(schema, declared, depth)

    def _sample_type(self, schema: dict[str, Any], declared: Any, depth: int) -> Any:
        if declared == "string" and schema.get("format") == "binary":
            return BINARY_SAMPLE
        if declared == "string":
            return _sample_string(schema)
        if declared in ("integer", "number"):
            return _sample_number(schema, declared)
        if declared == "boolean":
            return True
        if declared == "null":
            return None
        if declared == "array":
            minimum = schema.get("minItems")
            count = minimum if isinstance(minimum, int) and minimum > 0 else 1
            return [self._sample(schema.get("items"), depth + 1) for _ in range(count)]

        properties = schema.get("properties")
        if declared == "object" or isinstance(properties, dict):
            fields = properties if isinstance(properties, dict) else {}
            required = schema.get("required")
            names = [str(name) for name in required] if isinstance(required, list) else list(fields)
            return {name: self._sample(fields.get(name, {}), depth + 1) for name in names}

        return "sample"


def _sample_string(schema: dict[str, Any]) -> str:
    pattern = schema.get("pattern")
    if isinstance(pattern, str):
        sample = PATTERN_SAMPLES.get(pattern)
        if sample is None:
            raise ValueError(f"Add a sample for the pattern {pattern}")
        return sample

    string_format = schema.get("format")
    if isinstance(string_format, str) and string_format in FORMAT_SAMPLES:
        return FORMAT_SAMPLES[string_format]

    min_length = schema.get("minLength")
    max_length = schema.get("maxLength")
    shortest = min_length if isinstance(min_length, int) else 1
    longest = max_length if isinstance(max_length, int) else max(shortest, 16)
    seed = STRING_SEED * math.ceil(max(shortest, 1) / len(STRING_SEED))
    return seed[: min(max(shortest, min(len(STRING_SEED), longest)), longest)]


def _sample_number(schema: dict[str, Any], declared: str) -> int | float:
    minimum = schema.get("minimum")
    exclusive_minimum = schema.get("exclusiveMinimum")
    maximum = schema.get("maximum")
    if isinstance(minimum, (int, float)):
        value: float = minimum
    elif isinstance(exclusive_minimum, (int, float)):
        value = exclusive_minimum + 1
    else:
        value = 1
    if isinstance(maximum, (int, float)) and value > maximum:
        value = maximum
    return math.ceil(value) if declared == "integer" else value
