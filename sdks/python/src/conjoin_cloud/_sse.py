from __future__ import annotations

import codecs
import re
from collections.abc import AsyncIterable, AsyncIterator, Iterable, Iterator
from dataclasses import dataclass

from conjoin_cloud._errors import ConjoinResponseError

MAX_PENDING_EVENT_CHARACTERS = 4_194_304

_EVENT_SEPARATOR = re.compile(r"\r\n\r\n|\n\n|\r\r")
_LONGEST_SEPARATOR_CHARACTERS = 4


@dataclass(frozen=True)
class ServerSentEvent:
    event: str | None
    data: str


class SseDecoder:
    def __init__(self, *, status: int, request_id: str) -> None:
        self._decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
        self._buffer = ""
        self._status = status
        self._request_id = request_id

    def feed(self, chunk: bytes) -> list[ServerSentEvent]:
        search_from = max(0, len(self._buffer) - _LONGEST_SEPARATOR_CHARACTERS + 1)
        self._buffer += self._decoder.decode(chunk, final=False)
        events: list[ServerSentEvent] = []
        while True:
            match = _EVENT_SEPARATOR.search(self._buffer, search_from)
            if match is None:
                break
            event = _parse_event(self._buffer[: match.start()])
            self._buffer = self._buffer[match.end() :]
            search_from = 0
            if event is not None:
                events.append(event)

        if len(self._buffer) > MAX_PENDING_EVENT_CHARACTERS:
            raise ConjoinResponseError(
                "The stream sent an event larger than the SDK accepts",
                status=self._status,
                request_id=self._request_id,
            )
        return events

    def finish(self) -> ServerSentEvent | None:
        self._buffer += self._decoder.decode(b"", final=True)
        event = _parse_event(self._buffer)
        self._buffer = ""
        return event


def iter_sse_events(
    chunks: Iterable[bytes],
    *,
    status: int,
    request_id: str,
) -> Iterator[ServerSentEvent]:
    decoder = SseDecoder(status=status, request_id=request_id)
    for chunk in chunks:
        yield from decoder.feed(chunk)
    last = decoder.finish()
    if last is not None:
        yield last


async def aiter_sse_events(
    chunks: AsyncIterable[bytes],
    *,
    status: int,
    request_id: str,
) -> AsyncIterator[ServerSentEvent]:
    decoder = SseDecoder(status=status, request_id=request_id)
    async for chunk in chunks:
        for event in decoder.feed(chunk):
            yield event
    last = decoder.finish()
    if last is not None:
        yield last


def _parse_event(raw_event: str) -> ServerSentEvent | None:
    event_type: str | None = None
    data_lines: list[str] = []

    for line in raw_event.splitlines():
        if not line or line.startswith(":"):
            continue

        field, separator, value = line.partition(":")
        if not separator:
            continue

        if value.startswith(" "):
            value = value[1:]

        if field == "event":
            event_type = value
        elif field == "data":
            data_lines.append(value)

    if not data_lines:
        return None

    return ServerSentEvent(event=event_type, data="\n".join(data_lines))
