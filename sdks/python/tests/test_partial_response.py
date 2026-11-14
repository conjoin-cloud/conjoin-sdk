from __future__ import annotations

import asyncio
import threading

import pytest

from conjoin_cloud import (
    AsyncConjoin,
    AsyncPage,
    Conjoin,
    ConjoinNetworkError,
    ConjoinResponseError,
    Page,
)
from local_http import LocalHttpServer, ReceivedRequest, Reply, json_reply


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("accepts_key", [False, True])
def test_truncated_create_response_preserves_retry_safety(
    asynchronous: bool, accepts_key: bool
) -> None:
    stored: dict[str, bytes] = {}
    attempts: list[ReceivedRequest] = []

    def handle(request: ReceivedRequest, stopping: threading.Event) -> Reply:
        attempts.append(request)
        stored[request.headers.get("idempotency-key", str(len(attempts)))] = request.body
        if len(attempts) == 1:
            return Reply(200, b'{"data":', declared_length=1000)
        return json_reply(200, {"data": {"customer_id": "cus_1"}})

    with LocalHttpServer(handle) as server:

        async def async_call() -> object:
            async with AsyncConjoin(
                api_key="cak_test_transport", base_url=server.base_url, backoff_seconds=0
            ) as client:
                return await client.request(
                    "POST",
                    "billing/customers/",
                    body={"email": "billing@example.com"},
                    accepts_idempotency_key=accepts_key,
                )

        def call() -> object:
            if asynchronous:
                return asyncio.run(async_call())
            with Conjoin(
                api_key="cak_test_transport", base_url=server.base_url, backoff_seconds=0
            ) as client:
                return client.request(
                    "POST",
                    "billing/customers/",
                    body={"email": "billing@example.com"},
                    accepts_idempotency_key=accepts_key,
                )

        if accepts_key:
            assert call() == {"customer_id": "cus_1"}
            assert len(attempts) == 2
            assert (
                attempts[0].headers["conjoin-request-id"]
                == attempts[1].headers["conjoin-request-id"]
            )
        else:
            with pytest.raises(ConjoinNetworkError):
                call()
            assert len(attempts) == 1
        assert len(stored) == 1


@pytest.mark.parametrize("asynchronous", [False, True])
def test_oversized_success_is_rejected_without_retry(asynchronous: bool) -> None:
    def handle(request: ReceivedRequest, stopping: threading.Event) -> Reply:
        return Reply(200, b" " * (16 * 1024 * 1024 + 1))

    with LocalHttpServer(handle) as server:

        async def async_call() -> None:
            async with AsyncConjoin(
                api_key="cak_test_transport", base_url=server.base_url
            ) as client:
                await client.request("GET", "billing/customers/")

        with pytest.raises(ConjoinResponseError):
            if asynchronous:
                asyncio.run(async_call())
            else:
                with Conjoin(api_key="cak_test_transport", base_url=server.base_url) as client:
                    client.request("GET", "billing/customers/")
        assert len(server.requests) == 1


@pytest.mark.parametrize("asynchronous", [False, True])
def test_manual_page_walk_stops_a_repeated_cursor(asynchronous: bool) -> None:
    def handle(request: ReceivedRequest, stopping: threading.Event) -> Reply:
        return json_reply(200, {"data": ["customer_1"], "cursor": {"prev": None, "next": "loop"}})

    with LocalHttpServer(handle) as server:

        async def async_call() -> None:
            async with AsyncConjoin(
                api_key="cak_test_transport", base_url=server.base_url
            ) as client:
                first = await client.request("GET", "billing/customers/", cast_to=AsyncPage[str])
                second = await first.next_page()
                assert second is not None
                await second.next_page()

        with pytest.raises(ConjoinResponseError):
            if asynchronous:
                asyncio.run(async_call())
            else:
                with Conjoin(api_key="cak_test_transport", base_url=server.base_url) as client:
                    first = client.request("GET", "billing/customers/", cast_to=Page[str])
                    second = first.next_page()
                    assert second is not None
                    second.next_page()
        assert len(server.requests) == 2
