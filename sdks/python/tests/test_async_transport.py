from __future__ import annotations

import asyncio
import time
from collections.abc import Awaitable, Callable, Iterator
from typing import Any

import pytest

from conjoin_cloud import AsyncConjoin, AsyncPage, ConjoinNetworkError, ConjoinTimeoutError
from unreliable_server import DropAfterStore, Slow, Status, UnreliableServer, error_body

API_KEY = "cak_test_harbourledgerasync"
NEW_CUSTOMER = {"email": "ledger.owner@example.com"}
CUSTOMER_PATH = "billing/customers/cus_1"


@pytest.fixture
def server() -> Iterator[UnreliableServer]:
    running = UnreliableServer()
    try:
        yield running
    finally:
        running.stop()


def with_client(
    server: UnreliableServer,
    body: Callable[[AsyncConjoin], Awaitable[Any]],
    **settings: Any,
) -> Any:
    async def run() -> Any:
        defaults: dict[str, Any] = {
            "api_key": API_KEY,
            "base_url": server.base_url,
            "timeout": 2,
            "backoff_seconds": 0.001,
            "max_retry_delay_seconds": 0.05,
        }
        async with AsyncConjoin(**{**defaults, **settings}) as client:
            return await body(client)

    return asyncio.run(run())


async def cancel_after(delay_seconds: float, call: Awaitable[Any]) -> BaseException | None:
    task = asyncio.ensure_future(call)
    await asyncio.sleep(delay_seconds)
    task.cancel()
    try:
        await task
    except BaseException as error:
        return error
    return None


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
    assert second.headers["conjoin-request-id"] == first.headers["conjoin-request-id"]


def test_a_create_without_an_idempotency_key_goes_out_once(server: UnreliableServer) -> None:
    server.queue(DropAfterStore())

    with pytest.raises(ConjoinNetworkError):
        with_client(
            server,
            lambda client: client.request("POST", "billing/customers/", body=NEW_CUSTOMER),
        )

    assert len(server.attempts) == 1


def test_a_read_is_retried_after_a_503_and_after_a_timeout(server: UnreliableServer) -> None:
    server.queue(Status(503, error_body(503)), Slow(0.6))

    result = with_client(server, lambda client: client.request("GET", CUSTOMER_PATH), timeout=0.1)

    assert result["method"] == "GET"
    assert len(server.attempts) == 3


def test_a_timeout_raises_a_timeout_error(server: UnreliableServer) -> None:
    server.queue(Slow(0.6))

    with pytest.raises(ConjoinTimeoutError):
        with_client(
            server,
            lambda client: client.request(
                "GET", CUSTOMER_PATH, request_options={"timeout": 0.1, "max_retries": 0}
            ),
        )


def test_cancelling_the_task_stops_a_request_in_flight(server: UnreliableServer) -> None:
    server.queue(Slow(5))
    started = time.monotonic()

    error = with_client(
        server,
        lambda client: cancel_after(0.05, client.request("GET", CUSTOMER_PATH)),
    )

    assert isinstance(error, asyncio.CancelledError)
    assert time.monotonic() - started < 1
    assert len(server.attempts) == 1


def test_cancelling_the_task_stops_the_wait_before_a_retry(server: UnreliableServer) -> None:
    server.queue(Status(503, error_body(503), {"Retry-After": "30"}))
    started = time.monotonic()

    error = with_client(
        server,
        lambda client: cancel_after(0.2, client.request("GET", CUSTOMER_PATH)),
        max_retry_delay_seconds=60,
    )

    assert isinstance(error, asyncio.CancelledError)
    assert time.monotonic() - started < 1.5
    assert len(server.attempts) == 1


def test_an_async_list_pages_with_cursor_next(server: UnreliableServer) -> None:
    pages = {None: (["cus_1"], "page_two"), "page_two": (["cus_2"], None)}
    server.serve_pages(lambda cursor: pages.get(cursor, ([], None)))

    async def read_all(client: AsyncConjoin) -> list[str]:
        page = await client.request("GET", "billing/customers/", cast_to=AsyncPage[str])
        return [customer async for customer in page.iter_all()]

    assert with_client(server, read_all) == ["cus_1", "cus_2"]
    assert [attempt.query.get("cursor[next]") for attempt in server.attempts] == [
        None,
        ["page_two"],
    ]
