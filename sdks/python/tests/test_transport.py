from __future__ import annotations

import re
from collections.abc import Iterator
from typing import Any

import pytest

from conjoin_cloud import Conjoin, ConjoinNetworkError
from unreliable_server import DropAfterStore, UnreliableServer

API_KEY = "cak_test_harbourledgertransport"
SERVER_IDEMPOTENCY_KEY_PATTERN = re.compile(r"^[A-Za-z0-9\-_:.]{1,64}$")
NEW_CUSTOMER = {"email": "ledger.owner@example.com"}


@pytest.fixture
def server() -> Iterator[UnreliableServer]:
    running = UnreliableServer()
    try:
        yield running
    finally:
        running.stop()


@pytest.fixture
def client(server: UnreliableServer) -> Iterator[Conjoin]:
    with Conjoin(
        api_key=API_KEY,
        base_url=server.base_url,
        timeout=2,
        backoff_seconds=0.001,
        max_retry_delay_seconds=0.05,
    ) as created:
        yield created


def create_customer(client: Conjoin, *, accepts_idempotency_key: bool) -> Any:
    return client.request(
        "POST",
        "billing/customers/",
        body=NEW_CUSTOMER,
        accepts_idempotency_key=accepts_idempotency_key,
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


def test_separate_creates_send_different_idempotency_keys(
    server: UnreliableServer, client: Conjoin
) -> None:
    create_customer(client, accepts_idempotency_key=True)
    create_customer(client, accepts_idempotency_key=True)

    assert len(server.stored_customers()) == 2
    first, second = header_values(server, "idempotency-key")
    assert first != second


def test_a_create_without_an_idempotency_key_goes_out_once(
    server: UnreliableServer, client: Conjoin
) -> None:
    server.queue(DropAfterStore())

    with pytest.raises(ConjoinNetworkError):
        create_customer(client, accepts_idempotency_key=False)

    assert len(server.attempts) == 1
    assert len(server.stored_customers()) == 1
