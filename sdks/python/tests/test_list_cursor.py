from __future__ import annotations

import asyncio
import threading
from typing import Any

from codegen.spec import load_openapi

from conjoin_cloud import AsyncConjoin
from conjoin_cloud.generated._models import MessagingContactListRequest
from local_http import LocalHttpServer, ReceivedRequest, Reply, json_reply
from schema_sample import SchemaSampler

API_KEY = "cak_test_harbourledgerlists"
MESSAGING_PROFILE_ID = "mpr_harbourledger"
SECOND_PAGE_CURSOR = "cur_harbourledger_page_two"
CONTACT_FILTER: MessagingContactListRequest = {
    "filter": {"email": "owner@harbourledger.example"},
    "limit": 1,
}


def _contact_page(next_cursor: str | None) -> dict[str, Any]:
    document = load_openapi("openapi.json")
    sampler = SchemaSampler(document)
    operation = document["paths"]["/v1/messaging/contacts/retrieve"]["post"]
    response = sampler.resolve(operation["responses"]["200"])
    sample = sampler.sample(response["content"]["application/json"]["schema"])
    return {**sample, "cursor": {"next": next_cursor} if next_cursor else {}}


def test_the_async_client_sends_the_next_cursor_of_a_post_list_in_its_body() -> None:
    pages = [_contact_page(SECOND_PAGE_CURSOR), _contact_page(None)]

    def reply(request: ReceivedRequest, _stopping: threading.Event) -> Reply:
        return json_reply(200, pages[min(len(server.requests) - 1, 1)])

    server = LocalHttpServer(reply)

    async def read_every_contact() -> list[Any]:
        async with AsyncConjoin(
            api_key=API_KEY,
            base_url=server.base_url,
            messaging_profile_id=MESSAGING_PROFILE_ID,
            max_retries=0,
        ) as client:
            page = await client.messaging.contacts.list(CONTACT_FILTER)
            return [contact async for contact in page.iter_all()]

    try:
        contacts = asyncio.run(read_every_contact())
        first, second = server.requests
    finally:
        server.stop()

    assert len(contacts) == 2
    assert first.json() == CONTACT_FILTER
    assert second.json() == {**CONTACT_FILTER, "cursor": {"next": SECOND_PAGE_CURSOR}}
    assert second.query == first.query == {}
    assert second.headers["idempotency-key"] != first.headers["idempotency-key"]
