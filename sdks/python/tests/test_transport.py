from __future__ import annotations

import re
from collections.abc import Iterator
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from typing import Any

import pytest

from conjoin_cloud import (
    Conjoin,
    ConjoinApiError,
    ConjoinAuthenticationError,
    ConjoinConfigurationError,
    ConjoinConflictError,
    ConjoinInternalServerError,
    ConjoinNetworkError,
    ConjoinNotFoundError,
    ConjoinPermissionDeniedError,
    ConjoinRateLimitError,
    ConjoinResponseError,
    ConjoinTimeoutError,
    ConjoinValidationError,
    Page,
)
from unreliable_server import (
    DropAfterStore,
    DropBeforeStore,
    Slow,
    Status,
    UnreliableServer,
    error_body,
)

API_KEY = "cak_test_harbourledgertransport"
REQUEST_ID_PATTERN = re.compile(
    r"^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
SERVER_IDEMPOTENCY_KEY_PATTERN = re.compile(r"^[A-Za-z0-9\-_:.]{1,64}$")
CALLER_REQUEST_ID = "cnj_req_0198f0f7-5d0b-7b4a-8d5a-cf5693f0b2c1"
NEW_CUSTOMER = {"email": "ledger.owner@example.com"}
CUSTOMER_PATH = "billing/customers/cus_1"


@pytest.fixture
def server() -> Iterator[UnreliableServer]:
    running = UnreliableServer()
    try:
        yield running
    finally:
        running.stop()


def make_client(server: UnreliableServer, **settings: Any) -> Conjoin:
    defaults: dict[str, Any] = {
        "api_key": API_KEY,
        "base_url": server.base_url,
        "timeout": 2,
        "backoff_seconds": 0.001,
        "max_retry_delay_seconds": 0.05,
    }
    return Conjoin(**{**defaults, **settings})


@pytest.fixture
def client(server: UnreliableServer) -> Iterator[Conjoin]:
    with make_client(server) as created:
        yield created


def create_customer(client: Conjoin, *, accepts_idempotency_key: bool, **options: Any) -> Any:
    return client.request(
        "POST",
        "billing/customers/",
        body=NEW_CUSTOMER,
        accepts_idempotency_key=accepts_idempotency_key,
        request_options=options,
    )


def header_values(server: UnreliableServer, name: str) -> list[str | None]:
    return [attempt.headers.get(name) for attempt in server.attempts]


def test_one_customer_is_stored_when_the_connection_drops_after_the_store(
    server: UnreliableServer, client: Conjoin
) -> None:
    server.queue(DropAfterStore())

    customer = create_customer(client, accepts_idempotency_key=True)

    assert server.stored_customers() == [{"customer_id": "cus_1", "email": NEW_CUSTOMER["email"]}]
    assert customer == {"customer_id": "cus_1", "email": NEW_CUSTOMER["email"]}
    first, second = header_values(server, "idempotency-key")
    assert first is not None and SERVER_IDEMPOTENCY_KEY_PATTERN.fullmatch(first)
    assert second == first
    request_ids = header_values(server, "conjoin-request-id")
    assert request_ids[0] == request_ids[1]


def test_separate_creates_send_different_idempotency_keys(
    server: UnreliableServer, client: Conjoin
) -> None:
    create_customer(client, accepts_idempotency_key=True)
    create_customer(client, accepts_idempotency_key=True)

    assert len(server.stored_customers()) == 2
    first, second = header_values(server, "idempotency-key")
    assert first != second


def test_the_caller_key_is_kept_on_every_retry(server: UnreliableServer, client: Conjoin) -> None:
    server.queue(Status(503), DropBeforeStore())

    create_customer(client, accepts_idempotency_key=True, idempotency_key="ledger-order-7731")

    assert header_values(server, "idempotency-key") == ["ledger-order-7731"] * 3
    assert len(server.stored_customers()) == 1


def test_a_create_without_an_idempotency_key_goes_out_once(
    server: UnreliableServer, client: Conjoin
) -> None:
    server.queue(DropAfterStore())

    with pytest.raises(ConjoinNetworkError):
        create_customer(client, accepts_idempotency_key=False)

    assert len(server.attempts) == 1
    assert len(server.stored_customers()) == 1


def test_a_caller_key_does_not_make_an_undeclared_create_retry(
    server: UnreliableServer, client: Conjoin
) -> None:
    server.queue(Status(503, error_body(503)))

    with pytest.raises(ConjoinInternalServerError):
        create_customer(client, accepts_idempotency_key=False, idempotency_key="ledger-order-7732")

    assert len(server.attempts) == 1


@pytest.mark.parametrize("status", [429, 500, 502, 503, 504])
def test_a_read_is_retried_after_a_retryable_status(
    server: UnreliableServer, client: Conjoin, status: int
) -> None:
    server.queue(Status(status, error_body(status)))

    assert client.request("GET", CUSTOMER_PATH)["method"] == "GET"
    assert len(server.attempts) == 2
    request_ids = header_values(server, "conjoin-request-id")
    assert request_ids[0] == request_ids[1]


@pytest.mark.parametrize("method", ["PUT", "PATCH", "DELETE"])
def test_an_idempotent_write_is_retried_after_a_dropped_connection(
    server: UnreliableServer, client: Conjoin, method: str
) -> None:
    server.queue(DropBeforeStore())

    client.request(method, CUSTOMER_PATH, body=None if method == "DELETE" else {})

    assert [attempt.method for attempt in server.attempts] == [method, method]


@pytest.mark.parametrize(
    ("status", "error_class"),
    [
        (400, ConjoinValidationError),
        (401, ConjoinAuthenticationError),
        (403, ConjoinPermissionDeniedError),
        (404, ConjoinNotFoundError),
        (409, ConjoinConflictError),
        (422, ConjoinValidationError),
        (501, ConjoinInternalServerError),
    ],
)
def test_a_final_status_is_not_retried_and_reports_the_error_body(
    server: UnreliableServer, client: Conjoin, status: int, error_class: type[ConjoinApiError]
) -> None:
    server.queue(Status(status, error_body(status)))

    with pytest.raises(ConjoinApiError) as caught:
        client.request("GET", CUSTOMER_PATH)

    error = caught.value
    assert type(error) is error_class
    assert error.status == status
    assert error.code == "ledger_locked"
    assert error.param == "email"
    assert error.details == [{"message": "is locked", "path": "body.email"}]
    assert error.request_id == server.attempts[0].headers["conjoin-request-id"]
    assert len(server.attempts) == 1


def test_a_call_stops_after_its_own_retry_limit(server: UnreliableServer, client: Conjoin) -> None:
    server.queue(*(Status(503, error_body(503)) for _ in range(5)))

    with pytest.raises(ConjoinInternalServerError):
        client.request("GET", CUSTOMER_PATH, request_options={"max_retries": 2})

    assert len(server.attempts) == 3


def test_the_retry_waits_the_retry_after_seconds(server: UnreliableServer) -> None:
    server.queue(Status(429, error_body(429), {"Retry-After": "1"}))

    with make_client(server, backoff_seconds=0, max_retry_delay_seconds=60) as patient:
        patient.request("GET", CUSTOMER_PATH)

    first, second = server.attempts
    assert second.received_at - first.received_at >= 0.95


def test_a_retry_after_date_is_capped_at_the_client_maximum_delay(
    server: UnreliableServer,
) -> None:
    retry_at = format_datetime(datetime.now(timezone.utc) + timedelta(seconds=30), usegmt=True)
    server.queue(Status(503, error_body(503), {"Retry-After": retry_at}))

    with make_client(server, backoff_seconds=0, max_retry_delay_seconds=0.2) as capped:
        capped.request("GET", CUSTOMER_PATH)

    first, second = server.attempts
    assert 0.15 <= second.received_at - first.received_at < 2


def test_a_429_reports_its_retry_after_once_the_retries_run_out(server: UnreliableServer) -> None:
    server.queue(Status(429, error_body(429), {"Retry-After": "7"}))

    with (
        make_client(server, max_retries=0) as single,
        pytest.raises(ConjoinRateLimitError) as caught,
    ):
        single.request("GET", CUSTOMER_PATH)

    assert caught.value.retry_after == 7


def test_a_read_that_timed_out_is_retried(server: UnreliableServer) -> None:
    server.queue(Slow(0.6))

    with make_client(server, timeout=0.1) as quick:
        assert quick.request("GET", CUSTOMER_PATH)["method"] == "GET"

    assert len(server.attempts) == 2


def test_a_per_call_timeout_raises_a_timeout_error(
    server: UnreliableServer, client: Conjoin
) -> None:
    server.queue(Slow(0.6))

    with pytest.raises(ConjoinTimeoutError) as caught:
        client.request("GET", CUSTOMER_PATH, request_options={"timeout": 0.1, "max_retries": 0})

    assert caught.value.request_id == server.attempts[0].headers["conjoin-request-id"]


def test_request_ids_differ_per_call_and_the_caller_id_is_kept_on_retries(
    server: UnreliableServer, client: Conjoin
) -> None:
    client.request("GET", "billing/customers/cus_1")
    client.request("GET", "billing/customers/cus_2")
    server.queue(Status(502, error_body(502)))
    client.request(
        "GET",
        "billing/customers/cus_3",
        request_options={"conjoin_request_id": CALLER_REQUEST_ID},
    )

    ids = header_values(server, "conjoin-request-id")
    assert ids[0] is not None and REQUEST_ID_PATTERN.fullmatch(ids[0])
    assert ids[1] is not None and REQUEST_ID_PATTERN.fullmatch(ids[1])
    assert ids[0] != ids[1]
    assert ids[2:] == [CALLER_REQUEST_ID, CALLER_REQUEST_ID]


@pytest.mark.parametrize(
    ("method", "request_options", "scopes"),
    [
        ("GET", {"idempotency_key": "ledger-order-7733"}, ()),
        ("POST", {"idempotency_key": "ledger order 7733"}, ()),
        ("GET", {}, ("billing_entity_id",)),
    ],
    ids=["key-on-a-read", "malformed-key", "missing-scope"],
)
def test_a_rejected_call_sends_nothing(
    server: UnreliableServer,
    client: Conjoin,
    method: str,
    request_options: dict[str, Any],
    scopes: Any,
) -> None:
    with pytest.raises(ConjoinConfigurationError):
        client.request(
            method,
            CUSTOMER_PATH,
            request_options=request_options,
            scopes=scopes,
            accepts_idempotency_key=method == "POST",
        )

    assert server.attempts == []


def test_a_scoped_copy_sends_its_scope_and_leaves_the_client_unscoped(
    server: UnreliableServer, client: Conjoin
) -> None:
    scoped = client.with_scope(billing_entity_id="ent_harbourledger")

    scoped.request("GET", CUSTOMER_PATH, scopes=("billing_entity_id",))
    with pytest.raises(ConjoinConfigurationError):
        client.request("GET", CUSTOMER_PATH, scopes=("billing_entity_id",))

    assert header_values(server, "billing-entity-id") == ["ent_harbourledger"]


def test_a_list_pages_with_cursor_next_and_keeps_the_other_query_parameters(
    server: UnreliableServer, client: Conjoin
) -> None:
    pages = {
        None: (["cus_1", "cus_2"], "page_two"),
        "page_two": (["cus_3", "cus_4"], "page_three"),
        "page_three": (["cus_5"], None),
    }
    server.serve_pages(lambda cursor: pages.get(cursor, ([], None)))

    page = client.request("GET", "billing/customers/", query={"limit": 2}, cast_to=Page[str])

    assert list(page.iter_all()) == ["cus_1", "cus_2", "cus_3", "cus_4", "cus_5"]
    assert [
        (attempt.query.get("cursor[next]"), attempt.query.get("limit"))
        for attempt in server.attempts
    ] == [(None, ["2"]), (["page_two"], ["2"]), (["page_three"], ["2"])]


def test_paging_stops_when_the_server_repeats_a_cursor(
    server: UnreliableServer, client: Conjoin
) -> None:
    server.serve_pages(lambda _cursor: (["cus_1"], "page_loop"))

    page = client.request("GET", "billing/customers/", cast_to=Page[str])

    with pytest.raises(ConjoinResponseError):
        for _customer in page.iter_all():
            if len(server.attempts) > 10:
                break

    assert len(server.attempts) <= 3
