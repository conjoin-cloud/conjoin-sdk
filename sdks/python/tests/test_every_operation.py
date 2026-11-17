from __future__ import annotations

import json
import re
import threading
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any
from urllib.parse import unquote

import pytest
from codegen.ir import collect_resource_groups
from codegen.naming import resource_attribute_name, to_snake
from codegen.render_entries import resolve_method_entries
from codegen.spec import DOCUMENTS, load_openapi
from pydantic import BaseModel

from conjoin_cloud import Conjoin, Credential
from local_http import LocalHttpServer, ReceivedRequest, Reply
from schema_sample import SchemaSampler

API_KEY = "cak_test_harbourledgerintegration"
PUBLISHABLE_KEY = "cpk_test_harbourledgerbrowser"
SCIM_TOKEN = "scim_harbourledger_directory"
SESSION_TOKEN = "sess_harbourledger_signedin_owner"
PORTAL_TICKET = "ptk_harbourledger_portal_ticket"
PORTAL_TICKET_HEADER = "x-portal-ticket"
PORTAL_TICKET_ARGUMENT = "portal_ticket"
PORTAL_TICKET_QUERY_KEY = "ticket"
EXPECTED_AUTHORIZATION_BY_SCHEME = {
    "conjoinApiKey": f"Bearer {API_KEY}",
    "scimBearer": f"Bearer {SCIM_TOKEN}",
    "conjoinPublishableKey": f"Bearer {PUBLISHABLE_KEY}",
    "conjoinSessionBearer": f"Bearer {SESSION_TOKEN}",
}
SDK_MANAGED_HEADER_NAMES = frozenset(
    {
        "billing-entity-id",
        "messaging-profile-id",
        "auth-app-id",
        "idempotency-key",
        "conjoin-request-id",
    }
)
CREDENTIAL_HEADER_NAMES = frozenset({"step-up-token"})
SCOPE_HEADER_VALUES = {
    "billing-entity-id": "ent_harbourledger",
    "messaging-profile-id": "mpr_harbourledger",
    "auth-app-id": "app_harbourledger",
}
SERVER_IDEMPOTENCY_KEY_PATTERN = re.compile(r"^[A-Za-z0-9\-_:.]{1,64}$")
PATH_PARAMETER_PATTERN = re.compile(r"\{([^}]+)\}")
HTTP_METHODS = ("get", "post", "put", "patch", "delete")
FRONTEND_SPEC_FILE = "openapi-frontend.json"


@dataclass(frozen=True)
class OperationCase:
    spec_file: str
    attribute_path: tuple[str, ...]
    method_name: str
    http_method: str
    path_template: str


def _document_cases(spec_file: str) -> list[OperationCase]:
    prefix = ("frontend",) if spec_file == FRONTEND_SPEC_FILE else ()
    cases: list[OperationCase] = []
    for group in collect_resource_groups(load_openapi(spec_file)):
        attribute_path = (*prefix, to_snake(group.service), resource_attribute_name(group.resource))
        for entry in resolve_method_entries(group):
            cases.append(
                OperationCase(
                    spec_file=spec_file,
                    attribute_path=attribute_path,
                    method_name=entry.method_name,
                    http_method=entry.operation.http_method.upper(),
                    path_template=entry.operation.path,
                )
            )
    return cases


DOCUMENT_FILES = tuple(document.spec_file for document in DOCUMENTS)
LOADED_DOCUMENTS = {spec_file: load_openapi(spec_file) for spec_file in DOCUMENT_FILES}
CASES_BY_DOCUMENT = {spec_file: _document_cases(spec_file) for spec_file in DOCUMENT_FILES}
ALL_CASES = [case for cases in CASES_BY_DOCUMENT.values() for case in cases]


class ReplySlot:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._reply = Reply(status=500)

    def set(self, reply: Reply) -> None:
        with self._lock:
            self._reply = reply

    def handle(self, _request: ReceivedRequest, _stopping: threading.Event) -> Reply:
        with self._lock:
            return self._reply


@dataclass(frozen=True)
class ContractHarness:
    server: LocalHttpServer
    replies: ReplySlot
    clients: dict[str, Conjoin]


def _contract_client(base_url: str, spec_file: str) -> Conjoin:
    is_frontend = spec_file == FRONTEND_SPEC_FILE
    return Conjoin(
        api_key=None if is_frontend else API_KEY,
        publishable_key=PUBLISHABLE_KEY if is_frontend else None,
        base_url=base_url,
        billing_entity_id=SCOPE_HEADER_VALUES["billing-entity-id"],
        messaging_profile_id=SCOPE_HEADER_VALUES["messaging-profile-id"],
        auth_app_id=SCOPE_HEADER_VALUES["auth-app-id"],
        max_retries=0,
    )


@pytest.fixture(scope="module")
def harness() -> Iterator[ContractHarness]:
    replies = ReplySlot()
    server = LocalHttpServer(replies.handle)
    clients = {
        spec_file: _contract_client(server.base_url, spec_file) for spec_file in DOCUMENT_FILES
    }
    try:
        yield ContractHarness(server=server, replies=replies, clients=clients)
    finally:
        for client in clients.values():
            client.close()
        server.stop()


def _resolve(document: dict[str, Any], value: Any) -> dict[str, Any]:
    return SchemaSampler(document).resolve(value)


def _operation(case: OperationCase) -> dict[str, Any]:
    return LOADED_DOCUMENTS[case.spec_file]["paths"][case.path_template][case.http_method.lower()]


def _parameters(document: dict[str, Any], operation: dict[str, Any]) -> list[dict[str, Any]]:
    return [_resolve(document, parameter) for parameter in operation.get("parameters", [])]


def _header(document: dict[str, Any], operation: dict[str, Any], name: str) -> dict[str, Any]:
    for parameter in _parameters(document, operation):
        if parameter.get("in") == "header" and str(parameter.get("name")).lower() == name:
            return parameter
    return {}


def _success_response(document: dict[str, Any], operation: dict[str, Any]) -> tuple[int, Any]:
    status = next(code for code in operation["responses"] if str(code).startswith("2"))
    response = _resolve(document, operation["responses"][status])
    media = response.get("content", {}).get("application/json", {})
    return int(status), None if str(status) == "204" else media.get("schema")


def _request_body(document: dict[str, Any], operation: dict[str, Any]) -> tuple[str, Any] | None:
    if "requestBody" not in operation:
        return None
    content = _resolve(document, operation["requestBody"])["content"]
    content_type = next(iter(content))
    return content_type, _resolve(document, content[content_type]).get("schema")


def _plain(value: Any) -> Any:
    if isinstance(value, BaseModel):
        return _plain(value.model_dump(mode="json", by_alias=True, exclude_unset=True))
    if isinstance(value, dict):
        return {key: _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _path_value(name: str) -> str:
    return f"ledger/{name} 7?#%ä"


def _list_document_operations(document: dict[str, Any]) -> list[str]:
    return [
        f"{method.upper()} {path}"
        for path, item in document["paths"].items()
        for method in HTTP_METHODS
        if isinstance(item.get(method), dict)
    ]


def _resource(client: Conjoin, case: OperationCase) -> Any:
    target: Any = client
    for attribute in case.attribute_path:
        target = getattr(target, attribute)
    return target


@pytest.mark.parametrize("spec_file", DOCUMENT_FILES)
def test_every_document_operation_has_exactly_one_method(spec_file: str) -> None:
    generated = [
        f"{case.http_method} {case.path_template}" for case in CASES_BY_DOCUMENT[spec_file]
    ]

    assert len(set(generated)) == len(generated)
    assert sorted(generated) == sorted(_list_document_operations(LOADED_DOCUMENTS[spec_file]))


@pytest.mark.parametrize("spec_file", DOCUMENT_FILES)
def test_every_resource_exposes_only_its_generated_methods(
    harness: ContractHarness, spec_file: str
) -> None:
    expected: dict[tuple[str, ...], set[str]] = {}
    for case in CASES_BY_DOCUMENT[spec_file]:
        expected.setdefault(case.attribute_path, set()).add(case.method_name)

    for attribute_path, method_names in expected.items():
        resource: Any = harness.clients[spec_file]
        for attribute in attribute_path:
            resource = getattr(resource, attribute)
        public = {
            name
            for name in dir(resource)
            if not name.startswith("_") and callable(getattr(resource, name))
        }
        assert public - {"with_token"} == method_names, attribute_path


@pytest.mark.parametrize(
    "case",
    ALL_CASES,
    ids=[f"{'.'.join(case.attribute_path)}.{case.method_name}" for case in ALL_CASES],
)
def test_the_operation_sends_the_documented_request_and_returns_the_documented_data(
    harness: ContractHarness, case: OperationCase
) -> None:
    document = LOADED_DOCUMENTS[case.spec_file]
    operation = _operation(case)
    sampler = SchemaSampler(document)
    parameter_names = PATH_PARAMETER_PATTERN.findall(case.path_template)
    arguments = [_path_value(name) for name in parameter_names]
    keywords: dict[str, Any] = {}

    request_body = _request_body(document, operation)
    data = None if request_body is None else sampler.sample(request_body[1])
    if request_body is not None:
        keywords["data"] = data

    query_parameters = [
        parameter
        for parameter in _parameters(document, operation)
        if parameter.get("in") == "query"
    ]
    required_query = {
        str(parameter["name"]): sampler.sample(parameter.get("schema"))
        for parameter in query_parameters
        if parameter.get("required") is True
    }
    if required_query:
        keywords["query"] = required_query

    scheme = _security_scheme(operation)
    header_values = _declared_header_values(document, operation, sampler)
    for name, value in header_values.items():
        if name == PORTAL_TICKET_HEADER:
            keywords[PORTAL_TICKET_ARGUMENT] = Credential(value)
        elif name in CREDENTIAL_HEADER_NAMES:
            keywords[to_snake(name)] = Credential(value)
        else:
            keywords[to_snake(name)] = value
    if scheme == "conjoinSessionBearer":
        keywords["session_token"] = Credential(SESSION_TOKEN)

    status, response_schema = _success_response(document, operation)
    body = None if response_schema is None else sampler.sample(response_schema)
    harness.replies.set(
        Reply(
            status=status,
            body=b"" if body is None else json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
    )
    harness.server.reset()

    resource = _resource(harness.clients[case.spec_file], case)
    if hasattr(resource, "with_token"):
        resource = resource.with_token(SCIM_TOKEN)
    result = getattr(resource, case.method_name)(*arguments, **keywords)

    requests = harness.server.requests
    assert len(requests) == 1
    request = requests[0]
    _assert_documented_request(request, case, document, operation, parameter_names)
    for name, value in header_values.items():
        assert request.headers.get(name) == value, name
    assert PORTAL_TICKET_QUERY_KEY not in request.query
    assert all(PORTAL_TICKET not in values for values in request.query.values())
    if request_body is not None and request_body[0] == "application/json":
        assert request.json() == data
    _assert_returned_data(result, body, response_schema, document)


def _assert_documented_request(
    request: ReceivedRequest,
    case: OperationCase,
    document: dict[str, Any],
    operation: dict[str, Any],
    parameter_names: list[str],
) -> None:
    assert request.method == case.http_method
    template = re.escape(case.path_template).replace(r"\{", "{").replace(r"\}", "}")
    path_pattern = PATH_PARAMETER_PATTERN.sub("([^/]+)", template)
    matched = re.fullmatch(path_pattern, request.raw_path)
    assert matched is not None, request.raw_path
    assert [unquote(value) for value in matched.groups()] == [
        _path_value(name) for name in parameter_names
    ]

    request_id_schema = _resolve(document, _header(document, operation, "conjoin-request-id"))
    pattern = _resolve(document, request_id_schema.get("schema")).get("pattern")
    assert isinstance(pattern, str)
    assert re.search(pattern, request.headers.get("conjoin-request-id", ""))

    for header, value in SCOPE_HEADER_VALUES.items():
        declared = bool(_header(document, operation, header))
        assert request.headers.get(header) == (value if declared else None), header

    idempotency_key = request.headers.get("idempotency-key")
    if case.http_method == "POST" and _header(document, operation, "idempotency-key"):
        assert idempotency_key is not None
        assert SERVER_IDEMPOTENCY_KEY_PATTERN.fullmatch(idempotency_key)
    else:
        assert idempotency_key is None

    expected_authorization = EXPECTED_AUTHORIZATION_BY_SCHEME.get(str(_security_scheme(operation)))
    assert request.headers.get("authorization") == expected_authorization


def _security_scheme(operation: dict[str, Any]) -> str | None:
    security = operation.get("security")
    if not isinstance(security, list) or not security or not isinstance(security[0], dict):
        return None
    return next(iter(security[0]), None)


def _declared_header_values(
    document: dict[str, Any], operation: dict[str, Any], sampler: SchemaSampler
) -> dict[str, str]:
    values = {
        str(parameter["name"]).lower(): str(sampler.sample(parameter.get("schema")))
        for parameter in _parameters(document, operation)
        if parameter.get("in") == "header"
        and str(parameter.get("name")).lower() not in SDK_MANAGED_HEADER_NAMES
    }
    if _security_scheme(operation) == "conjoinPortalTicketHeader":
        values[PORTAL_TICKET_HEADER] = PORTAL_TICKET
    return values


def _assert_returned_data(result: Any, body: Any, schema: Any, document: dict[str, Any]) -> None:
    if body is None:
        assert result is None
        return

    properties = _resolve(document, schema).get("properties")
    if not isinstance(properties, dict) or "data" not in properties or not isinstance(body, dict):
        assert _plain(result) == body
        return

    if "cursor" in properties:
        assert _plain(result.data) == body["data"]
        assert _plain(result.cursor) == body["cursor"]
        return

    assert _plain(result) == body["data"]
