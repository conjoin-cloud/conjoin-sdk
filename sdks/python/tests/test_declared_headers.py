from __future__ import annotations

import io
import json
import logging
import pickle
import re
import threading
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any

import pytest
from codegen.spec import DOCUMENTS, load_openapi

from conjoin_cloud import Conjoin, ConjoinConfigurationError, Credential
from local_http import LocalHttpServer, ReceivedRequest, Reply, json_reply
from schema_sample import SchemaSampler

SECRET_API_KEY = "cak_live_harbourledgerserverside"
PUBLISHABLE_KEY = "cpk_live_harbourledgerbrowser"
SESSION_TOKEN = "sess_harbourledger_signedin_owner"
PORTAL_TICKET = "ptk_harbourledger_portal_ticket"
AUTH_APP_ID = "app_harbourledger"
ACCOUNT_ID = "acc_harbourledger_owner"
STEP_UP_SESSION_ID = "sus_harbourledger_0198f0f7"
STEP_UP_TOKEN = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
HTTP_METHODS = ("get", "post", "put", "patch", "delete")
PATH_PARAMETER_PATTERN = re.compile(r"\\\{[^}]+\\\}")
NOT_DOCUMENTED_STATUS = 404


@dataclass(frozen=True)
class DocumentedRoute:
    method: str
    path: re.Pattern[str]
    reply: Reply


def _documented_routes() -> list[DocumentedRoute]:
    routes: list[DocumentedRoute] = []
    for document in (load_openapi(spec.spec_file) for spec in DOCUMENTS):
        sampler = SchemaSampler(document)
        for template, item in document["paths"].items():
            for method in HTTP_METHODS:
                operation = item.get(method)
                if not isinstance(operation, dict):
                    continue
                status = next(code for code in operation["responses"] if str(code).startswith("2"))
                response = sampler.resolve(operation["responses"][status])
                schema = response.get("content", {}).get("application/json", {}).get("schema")
                body = None if schema is None else sampler.sample(schema)
                routes.append(
                    DocumentedRoute(
                        method=method.upper(),
                        path=re.compile(PATH_PARAMETER_PATTERN.sub("[^/]+", re.escape(template))),
                        reply=json_reply(int(status), body),
                    )
                )
    return routes


DOCUMENTED_ROUTES = _documented_routes()


@pytest.fixture
def receiver() -> Iterator[LocalHttpServer]:
    def reply(request: ReceivedRequest, _stopping: threading.Event) -> Reply:
        for route in DOCUMENTED_ROUTES:
            if route.method == request.method and route.path.fullmatch(request.raw_path):
                return route.reply
        return Reply(status=NOT_DOCUMENTED_STATUS)

    server = LocalHttpServer(reply)
    try:
        yield server
    finally:
        server.stop()


def _server_client(receiver: LocalHttpServer) -> Conjoin:
    return Conjoin(
        api_key=SECRET_API_KEY,
        base_url=receiver.base_url,
        auth_app_id=AUTH_APP_ID,
        max_retries=0,
    )


def _browser_client(receiver: LocalHttpServer) -> Conjoin:
    return Conjoin(publishable_key=PUBLISHABLE_KEY, base_url=receiver.base_url, max_retries=0)


def _every_received_value(receiver: LocalHttpServer) -> str:
    return json.dumps(
        [
            {"path": request.raw_path, "query": request.query, "headers": request.headers}
            for request in receiver.requests
        ]
    )


def test_delete_auth_account_sends_both_step_up_headers(receiver: LocalHttpServer) -> None:
    with _server_client(receiver) as client:
        client.auth.accounts.delete(
            ACCOUNT_ID,
            step_up_session_id=STEP_UP_SESSION_ID,
            step_up_token=Credential(STEP_UP_TOKEN),
        )

    [request] = receiver.requests
    assert request.method == "DELETE"
    assert request.raw_path == f"/v1/auth/accounts/{ACCOUNT_ID}"
    assert request.headers["step-up-session-id"] == STEP_UP_SESSION_ID
    assert request.headers["step-up-token"] == STEP_UP_TOKEN
    assert request.headers["auth-app-id"] == AUTH_APP_ID


def test_typed_step_up_values_replace_free_form_headers(receiver: LocalHttpServer) -> None:
    with _server_client(receiver) as client:
        client.auth.accounts.delete(
            ACCOUNT_ID,
            step_up_session_id=STEP_UP_SESSION_ID,
            step_up_token=Credential(STEP_UP_TOKEN),
            request_options={"headers": {"step-up-token": "ffff", "STEP-UP-SESSION-ID": "sus_x"}},
        )
        client.auth.accounts.delete(
            ACCOUNT_ID, request_options={"headers": {"Step-Up-Token": "ffff"}}
        )

    first, second = receiver.requests
    assert first.headers["step-up-token"] == STEP_UP_TOKEN
    assert first.headers["step-up-session-id"] == STEP_UP_SESSION_ID
    assert "step-up-token" not in second.headers
    assert "step-up-session-id" not in second.headers


@pytest.mark.parametrize(
    "token",
    [
        STEP_UP_TOKEN.upper(),
        "a" * 257,
        "",
        f"{STEP_UP_TOKEN}\r\nX-Injected: yes",
    ],
    ids=["uppercase", "257 characters", "empty", "line break"],
)
def test_a_malformed_step_up_token_is_refused_without_repeating_it(
    receiver: LocalHttpServer, token: str
) -> None:
    with _server_client(receiver) as client, pytest.raises(ConjoinConfigurationError) as raised:
        client.auth.accounts.delete(
            ACCOUNT_ID,
            step_up_session_id=STEP_UP_SESSION_ID,
            step_up_token=Credential(token),
        )

    message = f"{raised.value} {raised.value!r}"
    assert "step_up_token" in message
    if token:
        assert token not in message
    assert receiver.requests == []


def test_a_plain_string_step_up_token_is_refused_before_sending(receiver: LocalHttpServer) -> None:
    plain_token: Any = STEP_UP_TOKEN
    with _server_client(receiver) as client, pytest.raises(ConjoinConfigurationError) as raised:
        client.auth.accounts.delete(ACCOUNT_ID, step_up_token=plain_token)

    assert STEP_UP_TOKEN not in str(raised.value)
    assert receiver.requests == []


def test_a_session_id_longer_than_documented_is_refused(receiver: LocalHttpServer) -> None:
    with _server_client(receiver) as client, pytest.raises(ConjoinConfigurationError):
        client.auth.accounts.delete(ACCOUNT_ID, step_up_session_id="s" * 49)

    assert receiver.requests == []


def test_a_credential_stays_out_of_every_printed_form() -> None:
    credential = Credential(STEP_UP_TOKEN)
    stream = io.StringIO()
    logger = logging.getLogger("conjoin_cloud.tests.redaction")
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    try:
        logger.warning("step-up %s %r", credential, {"token": credential})
    finally:
        logger.removeHandler(handler)

    printed = " ".join(
        [str(credential), repr(credential), f"{credential}", f"{credential:>80}", stream.getvalue()]
    )
    assert STEP_UP_TOKEN not in printed
    with pytest.raises(TypeError):
        pickle.dumps(credential)
    with pytest.raises(TypeError):
        vars(credential)


def test_frontend_calls_from_a_secret_key_client_never_send_the_secret_key(
    receiver: LocalHttpServer,
) -> None:
    with _server_client(receiver) as client:
        client.frontend.auth.clients.get_jwks()
        client.frontend.auth.selves.read_profile(session_token=Credential(SESSION_TOKEN))
        with pytest.raises(ConjoinConfigurationError, match="publishable_key"):
            client.frontend.cloud.sd_ks.read_sdk_settings()

    public, session = receiver.requests
    assert "authorization" not in public.headers
    assert session.headers["authorization"] == f"Bearer {SESSION_TOKEN}"
    assert SECRET_API_KEY not in _every_received_value(receiver)


def test_the_publishable_key_goes_only_where_the_document_asks(receiver: LocalHttpServer) -> None:
    with _browser_client(receiver) as client:
        client.frontend.cloud.sd_ks.read_sdk_settings()
        client.frontend.auth.clients.get_jwks()

    settings, public = receiver.requests
    assert settings.headers["authorization"] == f"Bearer {PUBLISHABLE_KEY}"
    assert "authorization" not in public.headers


def test_a_session_call_refuses_an_auth_override(receiver: LocalHttpServer) -> None:
    with _browser_client(receiver) as client, pytest.raises(ConjoinConfigurationError):
        client.frontend.auth.selves.read_profile(
            session_token=Credential(SESSION_TOKEN),
            request_options={"auth": {"type": "bearer", "token": SECRET_API_KEY}},
        )

    assert receiver.requests == []


def test_a_portal_ticket_travels_only_in_its_header(receiver: LocalHttpServer) -> None:
    with _browser_client(receiver) as client:
        client.frontend.auth.sso_portals.read_sso_portal_context(
            portal_ticket=Credential(PORTAL_TICKET)
        )

    [request] = receiver.requests
    assert request.headers["x-portal-ticket"] == PORTAL_TICKET
    assert "authorization" not in request.headers
    assert PORTAL_TICKET not in json.dumps(request.query)


def test_a_malformed_portal_ticket_is_refused_without_repeating_it(
    receiver: LocalHttpServer,
) -> None:
    malformed = "ptk_harbourledger portal_ticket"
    with _browser_client(receiver) as client, pytest.raises(ConjoinConfigurationError) as raised:
        client.frontend.auth.sso_portals.read_sso_portal_context(
            portal_ticket=Credential(malformed)
        )

    assert malformed not in f"{raised.value} {raised.value!r}"
    assert receiver.requests == []
