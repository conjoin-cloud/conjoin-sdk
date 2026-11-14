from __future__ import annotations

import json
import threading
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from local_http import LocalHttpServer, ReceivedRequest, Reply, json_reply

CUSTOMERS_PATH = "/v1/billing/customers/"


@dataclass(frozen=True)
class Answer:
    pass


@dataclass(frozen=True)
class DropBeforeStore:
    pass


@dataclass(frozen=True)
class DropAfterStore:
    pass


@dataclass(frozen=True)
class Slow:
    delay_seconds: float


@dataclass(frozen=True)
class Status:
    status: int
    body: Any = None
    headers: dict[str, str] = field(default_factory=dict)


Behaviour = Answer | DropBeforeStore | DropAfterStore | Slow | Status
PageSource = Callable[[str | None], tuple[list[Any], str | None]]


def success(status: int, data: Any) -> dict[str, Any]:
    return {"response": {"type": "SUCCESS", "code": status, "message": "Success"}, "data": data}


def error_body(status: int) -> dict[str, Any]:
    return {
        "response": {
            "type": "SERVER_ERROR" if status >= 500 else "CLIENT_ERROR",
            "code": status,
            "message": "The ledger refused it",
        },
        "data": None,
        "error": {
            "code": "ledger_locked",
            "param": "email",
            "details": [{"message": "is locked", "path": "body.email"}],
        },
    }


class UnreliableServer:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._behaviours: deque[Behaviour] = deque()
        self._customers: list[dict[str, str]] = []
        self._customers_by_key: dict[str, tuple[bytes, dict[str, str]]] = {}
        self._page_source: PageSource | None = None
        self._http = LocalHttpServer(self._handle)

    @property
    def base_url(self) -> str:
        return self._http.base_url

    @property
    def attempts(self) -> list[ReceivedRequest]:
        return self._http.requests

    def stored_customers(self) -> list[dict[str, str]]:
        with self._lock:
            return [dict(customer) for customer in self._customers]

    def queue(self, *behaviours: Behaviour) -> None:
        with self._lock:
            self._behaviours.extend(behaviours)

    def serve_pages(self, source: PageSource) -> None:
        with self._lock:
            self._page_source = source

    def stop(self) -> None:
        self._http.stop()

    def _next_behaviour(self) -> Behaviour:
        with self._lock:
            return self._behaviours.popleft() if self._behaviours else Answer()

    def _handle(self, request: ReceivedRequest, stopping: threading.Event) -> Reply | None:
        behaviour = self._next_behaviour()
        if isinstance(behaviour, DropBeforeStore):
            return None
        if isinstance(behaviour, DropAfterStore):
            if _is_customer_create(request):
                self._store_customer(request)
            return None
        if isinstance(behaviour, Slow):
            if stopping.wait(behaviour.delay_seconds):
                return None
            return self._answer(request)
        if isinstance(behaviour, Status):
            body = behaviour.body if behaviour.body is not None else {"data": None}
            return json_reply(behaviour.status, body, behaviour.headers)
        return self._answer(request)

    def _answer(self, request: ReceivedRequest) -> Reply:
        if _is_customer_create(request):
            status, customer = self._store_customer(request)
            return json_reply(status, success(status, customer) if customer else {"data": None})

        with self._lock:
            page_source = self._page_source
        if page_source is not None and request.method == "GET":
            cursor_values = request.query.get("cursor[next]")
            data, next_cursor = page_source(cursor_values[0] if cursor_values else None)
            cursor = {"prev": None, "next": next_cursor}
            return json_reply(200, {**success(200, data), "cursor": cursor})

        return json_reply(200, success(200, {"path": request.path, "method": request.method}))

    def _store_customer(self, request: ReceivedRequest) -> tuple[int, dict[str, str] | None]:
        key = request.headers.get("idempotency-key")
        with self._lock:
            previous = None if key is None else self._customers_by_key.get(key)
            if previous is not None:
                previous_body, previous_customer = previous
                return (200, previous_customer) if previous_body == request.body else (422, None)

            parsed = json.loads(request.body.decode("utf-8"))
            email = str(parsed.get("email", "")) if isinstance(parsed, dict) else ""
            customer = {"customer_id": f"cus_{len(self._customers) + 1}", "email": email}
            self._customers.append(customer)
            if key is not None:
                self._customers_by_key[key] = (request.body, customer)
            return 201, customer


def _is_customer_create(request: ReceivedRequest) -> bool:
    return request.method == "POST" and request.path == CUSTOMERS_PATH
