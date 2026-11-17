from __future__ import annotations

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
        if request.path == "/upload/resumable" and request.method == "POST":
            return Reply(status=201, headers={"Location": f"{self.base_url}/session/1"})
        if request.path == "/session/1" and request.method == "PUT":
            return self._accept_chunk(request)
        if request.path == "/files/monthly.csv":
            with self.lock:
                return Reply(status=self.download_status, body=bytes(self.stored))
        return Reply(status=404)

    def _upload_url(self) -> dict[str, Any]:
        return {
            "upload_url": f"{self.base_url}/upload/resumable?{SIGNATURE}",
            "upload_mode": "resumable",
            "required_fields": {"method": "POST", "headers": {"Content-Type": "text/csv"}},
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


def test_an_upload_sends_no_conjoin_credentials_to_storage(
    storage: tuple[StorageBackend, LocalHttpServer, Conjoin],
) -> None:
    backend, server, client = storage
    payload = bytes(range(256)) * (CHUNK_SIZE // 256 * 2 + 3)

    client.storage.upload(
        container=CONTAINER,
        path=OBJECT_PATH,
        content_type="text/csv",
        body=payload,
        chunk_size=CHUNK_SIZE,
    )

    assert bytes(backend.stored) == payload
    assert server.requests[0].headers["authorization"] == f"Bearer {API_KEY}"
    storage_requests = [
        request for request in server.requests if not request.path.startswith("/v1/")
    ]
    assert len(storage_requests) > 1
    for request in storage_requests:
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
