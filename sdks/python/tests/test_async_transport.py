from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable, Iterator
from typing import Any

import pytest

from conjoin_cloud import AsyncConjoin, ConjoinNetworkError
from unreliable_server import DropAfterStore, UnreliableServer

API_KEY = "cak_test_harbourledgerasync"
NEW_CUSTOMER = {"email": "ledger.owner@example.com"}


@pytest.fixture
def server() -> Iterator[UnreliableServer]:
    running = UnreliableServer()
    try:
        yield running
    finally:
        running.stop()


def with_client(server: UnreliableServer, body: Callable[[AsyncConjoin], Awaitable[Any]]) -> Any:
    async def run() -> Any:
        async with AsyncConjoin(
            api_key=API_KEY,
            base_url=server.base_url,
            timeout=2,
            backoff_seconds=0.001,
            max_retry_delay_seconds=0.05,
        ) as client:
            return await body(client)

    return asyncio.run(run())


def test_one_customer_is_stored_when_the_connection_drops_after_the_store(
    server: UnreliableServer,
) -> None:
    server.queue(DropAfterStore())

    customer = with_client(
        server,
        lambda client: client.request(
            "POST", "billing/customers/", body=NEW_CUSTOMER, accepts_idempotency_key=True
        ),
    )

    assert server.stored_customers() == [customer]
    first, second = server.attempts
    assert second.headers["idempotency-key"] == first.headers["idempotency-key"]


def test_a_create_without_an_idempotency_key_goes_out_once(server: UnreliableServer) -> None:
    server.queue(DropAfterStore())

    with pytest.raises(ConjoinNetworkError):
        with_client(
            server,
            lambda client: client.request("POST", "billing/customers/", body=NEW_CUSTOMER),
        )

    assert len(server.attempts) == 1
