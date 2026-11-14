from __future__ import annotations

import json
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, unquote, urlsplit

LOOPBACK_HOST = "127.0.0.1"
MAX_REQUEST_BODY_BYTES = 1_048_576
IDLE_CONNECTION_SECONDS = 5
SHUTDOWN_POLL_SECONDS = 0.01


@dataclass(frozen=True)
class ReceivedRequest:
    method: str
    raw_path: str
    path: str
    query: dict[str, list[str]]
    headers: dict[str, str]
    body: bytes
    received_at: float

    def json(self) -> Any:
        return json.loads(self.body.decode("utf-8"))


@dataclass(frozen=True)
class Reply:
    status: int
    body: bytes = b""
    headers: dict[str, str] = field(default_factory=dict)
    declared_length: int | None = None


def json_reply(status: int, payload: Any, headers: dict[str, str] | None = None) -> Reply:
    return Reply(
        status=status,
        body=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **(headers or {})},
    )


Handler = Callable[[ReceivedRequest, threading.Event], Reply | None]


class LocalHttpServer:
    def __init__(self, handler: Handler) -> None:
        self._handler = handler
        self._lock = threading.Lock()
        self._requests: list[ReceivedRequest] = []
        self.stopping = threading.Event()
        self._server = ThreadingHTTPServer((LOOPBACK_HOST, 0), self._request_handler_class())
        self._server.daemon_threads = True
        self._server.block_on_close = False
        self._thread = threading.Thread(
            target=self._server.serve_forever,
            kwargs={"poll_interval": SHUTDOWN_POLL_SECONDS},
            daemon=True,
        )
        self._thread.start()

    @property
    def base_url(self) -> str:
        host, port = self._server.server_address[:2]
        return f"http://{host!s}:{port}"

    @property
    def requests(self) -> list[ReceivedRequest]:
        with self._lock:
            return list(self._requests)

    def reset(self) -> None:
        with self._lock:
            self._requests.clear()

    def stop(self) -> None:
        self.stopping.set()
        self._server.shutdown()
        self._server.server_close()
        self._thread.join()

    def __enter__(self) -> LocalHttpServer:
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.stop()

    def _record(self, request: ReceivedRequest) -> None:
        with self._lock:
            self._requests.append(request)

    def _request_handler_class(self) -> type[BaseHTTPRequestHandler]:
        server = self

        class RecordingHandler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"
            timeout = IDLE_CONNECTION_SECONDS

            def do_GET(self) -> None:
                self._serve()

            def do_POST(self) -> None:
                self._serve()

            def do_PUT(self) -> None:
                self._serve()

            def do_PATCH(self) -> None:
                self._serve()

            def do_DELETE(self) -> None:
                self._serve()

            def log_message(self, format: str, *args: Any) -> None:
                return None

            def _serve(self) -> None:
                body = self._read_body()
                if body is None:
                    self._write(Reply(status=413))
                    return
                parts = urlsplit(self.path)
                received = ReceivedRequest(
                    method=self.command,
                    raw_path=parts.path,
                    path=unquote(parts.path),
                    query=parse_qs(parts.query, keep_blank_values=True),
                    headers={name.lower(): value for name, value in self.headers.items()},
                    body=body,
                    received_at=time.monotonic(),
                )
                server._record(received)
                reply = server._handler(received, server.stopping)
                if reply is None or server.stopping.is_set():
                    self.close_connection = True
                    return
                self._write(reply)

            def _read_body(self) -> bytes | None:
                length = int(self.headers.get("Content-Length") or 0)
                if length > MAX_REQUEST_BODY_BYTES:
                    self.close_connection = True
                    return None
                return self.rfile.read(length) if length else b""

            def _write(self, reply: Reply) -> None:
                try:
                    self.send_response(reply.status)
                    for name, value in reply.headers.items():
                        self.send_header(name, value)
                    length = (
                        len(reply.body) if reply.declared_length is None else reply.declared_length
                    )
                    self.send_header("Content-Length", str(length))
                    self.end_headers()
                    self.wfile.write(reply.body)
                    if length != len(reply.body):
                        self.close_connection = True
                except (BrokenPipeError, ConnectionResetError):
                    self.close_connection = True

        return RecordingHandler
