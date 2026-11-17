from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from conjoin_cloud._models import ConjoinModel


class ChatCompletionUsage(ConjoinModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionChunkDelta(ConjoinModel):
    role: str | None = None
    content: str | None = None
    tool_calls: Sequence[dict[str, Any]] | None = None


class ChatCompletionChunkChoice(ConjoinModel):
    index: int
    delta: ChatCompletionChunkDelta
    finish_reason: str | None = None


class ChatCompletionChunk(ConjoinModel):
    id: str
    object: str
    created: int
    model: str
    choices: Sequence[ChatCompletionChunkChoice]
    usage: ChatCompletionUsage | None = None
