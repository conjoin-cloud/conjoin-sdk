from __future__ import annotations

import json
import threading
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Any

import pytest

from conjoin_cloud import Conjoin, ConjoinStorageError
from local_http import LocalHttpServer, ReceivedRequest, Reply, json_reply

API_KEY = "cak_test_harbourledgerstorage"
CONTAINER = "ledger-exports"
OBJECT_PATH = "reports/monthly.csv"
SIGNATURE = "X-Goog-Signature=ledgersecretsignature"
CHUNK_SIZE = 256 * 1024
SIGNED_URL_PREFIX = f"/v1/storage/storage-object/{CONTAINER}/signed-url"
CONJOIN_HEADERS = ("authorization", "conjoin-request-id", "x-conjoin-sdk-version")


@dataclass
class StorageBackend:
    upload_mode: str = "single"
    download_status: int = 200
    stored: bytearray = field(default_factory=bytearray)
    base_url: str = ""
    lock: threading.Lock = field(default_factory=threading.Lock)

    def handle(self, request: ReceivedRequest, _stopping: threading.Event) -> Reply:
        if request.path == f"{SIGNED_URL_PREFIX}/upload":
            return json_reply(200, {"data": self._upload_url()})
        if request.path == f"{SIGNED_URL_PREFIX}/download":
            url = f"{self.base_url}/files/monthly.csv?{SIGNATURE}"
            return json_reply(200, {"data": {"url": url, "headers": {}}})
        if request.path == "/upload/single" and request.method == "PUT":
            with self.lock:
                self.stored[:] = request.body
            return Reply(status=200)
        if request.path == "/upload/resumable" and request.method == "POST":
            return Reply(status=201, headers={"Location": f"{self.base_url}/session/1"})
        if request.path == "/session/1" and request.method == "PUT":
            return self._accept_chunk(request)
        if request.path == "/files/monthly.csv":
            with self.lock:
                return Reply(status=self.download_status, body=bytes(self.stored))
        return Reply(status=404)

    def _upload_url(self) -> dict[str, Any]:
        method = "PUT" if self.upload_mode == "single" else "POST"
        return {
            "upload_url": f"{self.base_url}/upload/{self.upload_mode}?{SIGNATURE}",
            "upload_mode": self.upload_mode,
            "required_fields": {"method": method, "headers": {"Content-Type": "text/csv"}},
        }

    def _accept_chunk(self, request: ReceivedRequest) -> Reply:
        content_range = request.headers.get("content-range", "")
        span, total = content_range.removeprefix("bytes ").split("/")
        start, end = (int(value) for value in span.split("-"))
        with self.lock:
            if start != len(self.stored) or end - start + 1 != len(request.body):
                return Reply(status=400)
            self.stored.extend(request.body)
            stored_size = len(self.stored)
        if stored_size == int(total):
            return Reply(status=200)
        return Reply(status=308, headers={"Range": f"bytes=0-{stored_size - 1}"})


@pytest.fixture
def storage() -> Iterator[tuple[StorageBackend, LocalHttpServer, Conjoin]]:
    backend = StorageBackend()
    server = LocalHttpServer(backend.handle)
    backend.base_url = server.base_url
    try:
        with Conjoin(api_key=API_KEY, base_url=server.base_url) as client:
            yield backend, server, client
    finally:
        server.stop()


def storage_requests(server: LocalHttpServer) -> list[ReceivedRequest]:
    return [request for request in server.requests if not request.path.startswith("/v1/")]


@pytest.mark.parametrize("upload_mode", ["single", "resumable"])
def test_an_upload_stores_every_byte_and_sends_no_conjoin_credentials_to_storage(
    storage: tuple[StorageBackend, LocalHttpServer, Conjoin], upload_mode: str
) -> None:
    backend, server, client = storage
    backend.upload_mode = upload_mode
    payload = bytes(range(256)) * (CHUNK_SIZE // 256 * 2 + 3)
    progress: list[int] = []

    client.storage.upload(
        container=CONTAINER,
        path=OBJECT_PATH,
        content_type="text/csv",
        body=payload,
        chunk_size=CHUNK_SIZE,
        on_progress=lambda update: progress.append(update.loaded),
    )

    assert bytes(backend.stored) == payload
    assert progress[0] == 0
    assert progress[-1] == len(payload)
    signed_url_request = server.requests[0]
    assert signed_url_request.headers["authorization"] == f"Bearer {API_KEY}"
    assert signed_url_request.json() == {
        "path": OBJECT_PATH,
        "content_type": "text/csv",
        "file_size": len(payload),
    }
    for request in storage_requests(server):
        assert all(header not in request.headers for header in CONJOIN_HEADERS)


def test_a_download_returns_the_stored_bytes(
    storage: tuple[StorageBackend, LocalHttpServer, Conjoin],
) -> None:
    backend, server, client = storage
    backend.stored[:] = b"month,total\n2026-10,1200\n"

    with client.storage.download(container=CONTAINER, path=OBJECT_PATH) as download:
        assert download.read() == b"month,total\n2026-10,1200\n"

    for request in storage_requests(server):
        assert all(header not in request.headers for header in CONJOIN_HEADERS)


def test_a_failed_download_keeps_the_signature_out_of_the_error(
    storage: tuple[StorageBackend, LocalHttpServer, Conjoin],
) -> None:
    backend, _server, client = storage
    backend.download_status = 403

    with pytest.raises(ConjoinStorageError) as caught:
        client.storage.download(container=CONTAINER, path=OBJECT_PATH)

    error = caught.value
    assert error.status == 403
    assert "ledgersecretsignature" not in f"{error} {error.storage_url}"


def sse_event(payload: Any) -> bytes:
    return f"data: {json.dumps(payload)}\n\n".encode()


def chunk(content: str) -> dict[str, Any]:
    return {
        "id": "chatcmpl_ledger",
        "object": "chat.completion.chunk",
        "created": 1_794_000_000,
        "model": "ledger-model",
        "choices": [{"index": 0, "delta": {"content": content}, "finish_reason": None}],
    }


def test_a_chat_stream_yields_every_chunk_until_done() -> None:
    stream = sse_event(chunk("Invoice ")) + sse_event(chunk("paid.")) + b"data: [DONE]\n\n"

    def handle(request: ReceivedRequest, _stopping: threading.Event) -> Reply:
        if request.path != "/v1/ai/inference/chat/completions":
            return Reply(status=404)
        return Reply(status=200, body=stream, headers={"Content-Type": "text/event-stream"})

    with (
        LocalHttpServer(handle) as server,
        Conjoin(api_key=API_KEY, base_url=server.base_url) as client,
    ):
        chunks = list(
            client.ai.chat.stream(
                model="ledger-model",
                messages=[{"role": "user", "content": "Is the invoice paid?"}],
            )
        )
        sent = server.requests[0].json()

    assert "".join(choice.delta.content or "" for item in chunks for choice in item.choices) == (
        "Invoice paid."
    )
    assert sent["stream"] is True
    assert sent["model"] == "ledger-model"
