from __future__ import annotations

import asyncio
import threading
from collections.abc import Callable, Iterator

import httpx
import pytest

from conjoin_cloud import AsyncConjoin, Conjoin, ConjoinError, Credential
from local_http import LocalHttpServer, ReceivedRequest, Reply, json_reply

API_KEY = "cak_test_harbourledgerredirect"
AUTH_APP_ID = "app_harbourledger"
ACCOUNT_ID = "acc_harbourledger_owner"
STEP_UP_SESSION_ID = "sus_harbourledger_0198f0f7"
STEP_UP_TOKEN = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
TEMPORARY_REDIRECT_STATUS = 307


class RedirectedHosts:
    def __init__(self) -> None:
        self.other_host = LocalHttpServer(self._accept)
        self.api_host = LocalHttpServer(self._redirect)

    def _accept(self, _request: ReceivedRequest, _stopping: threading.Event) -> Reply:
        return json_reply(200, {"data": {"account_id": ACCOUNT_ID, "deleted": True}})

    def _redirect(self, request: ReceivedRequest, _stopping: threading.Event) -> Reply:
        return Reply(
            status=TEMPORARY_REDIRECT_STATUS,
            headers={"Location": f"{self.other_host.base_url}{request.raw_path}"},
        )

    def stop(self) -> None:
        self.api_host.stop()
        self.other_host.stop()


@pytest.fixture
def hosts() -> Iterator[RedirectedHosts]:
    redirected = RedirectedHosts()
    try:
        yield redirected
    finally:
        redirected.stop()


def _assert_only_the_api_host_saw_the_token(hosts: RedirectedHosts) -> None:
    assert len(hosts.api_host.requests) == 1
    assert hosts.api_host.requests[0].headers.get("step-up-token") == STEP_UP_TOKEN
    assert hosts.other_host.requests == []


SYNC_HTTP_CLIENTS: dict[str, Callable[[], httpx.Client | None]] = {
    "sdk_client": lambda: None,
    "caller_client_that_follows_redirects": lambda: httpx.Client(follow_redirects=True),
}


@pytest.mark.parametrize("http_client", SYNC_HTTP_CLIENTS.values(), ids=SYNC_HTTP_CLIENTS.keys())
def test_a_redirect_never_carries_the_step_up_token_to_another_host(
    hosts: RedirectedHosts, http_client: Callable[[], httpx.Client | None]
) -> None:
    with (
        Conjoin(
            api_key=API_KEY,
            base_url=hosts.api_host.base_url,
            auth_app_id=AUTH_APP_ID,
            max_retries=0,
            http_client=http_client(),
        ) as client,
        pytest.raises(ConjoinError),
    ):
        client.auth.accounts.delete(
            ACCOUNT_ID,
            step_up_session_id=STEP_UP_SESSION_ID,
            step_up_token=Credential(STEP_UP_TOKEN),
        )

    _assert_only_the_api_host_saw_the_token(hosts)


ASYNC_HTTP_CLIENTS: dict[str, Callable[[], httpx.AsyncClient | None]] = {
    "sdk_client": lambda: None,
    "caller_client_that_follows_redirects": lambda: httpx.AsyncClient(follow_redirects=True),
}


@pytest.mark.parametrize("http_client", ASYNC_HTTP_CLIENTS.values(), ids=ASYNC_HTTP_CLIENTS.keys())
def test_the_async_client_never_follows_a_redirect_to_another_host(
    hosts: RedirectedHosts, http_client: Callable[[], httpx.AsyncClient | None]
) -> None:
    async def delete_account() -> None:
        async with AsyncConjoin(
            api_key=API_KEY,
            base_url=hosts.api_host.base_url,
            auth_app_id=AUTH_APP_ID,
            max_retries=0,
            http_client=http_client(),
        ) as client:
            await client.auth.accounts.delete(
                ACCOUNT_ID,
                step_up_session_id=STEP_UP_SESSION_ID,
                step_up_token=Credential(STEP_UP_TOKEN),
            )

    with pytest.raises(ConjoinError):
        asyncio.run(delete_account())

    _assert_only_the_api_host_saw_the_token(hosts)
