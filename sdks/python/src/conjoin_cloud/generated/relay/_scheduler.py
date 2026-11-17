from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    RelaySchedulerCancelResponse,
    RelaySchedulerCreateDefinitionRequest,
    RelaySchedulerCreateDefinitionResponse,
    RelaySchedulerPauseResponse,
    RelaySchedulerReadDeadLetterEntriesCountQuery,
    RelaySchedulerReadDeadLetterEntriesCountResponse,
    RelaySchedulerReadDeadLetterEntriesItem,
    RelaySchedulerReadDeadLetterEntriesQuery,
    RelaySchedulerReadDefinitionsCountQuery,
    RelaySchedulerReadDefinitionsCountResponse,
    RelaySchedulerReadDefinitionsItem,
    RelaySchedulerReadDefinitionsQuery,
    RelaySchedulerReadExecutionsCountQuery,
    RelaySchedulerReadExecutionsCountResponse,
    RelaySchedulerReadExecutionsItem,
    RelaySchedulerReadExecutionsQuery,
    RelaySchedulerReplayDeadLetterEntryResponse,
    RelaySchedulerResumeResponse,
    RelaySchedulerTriggerExecutionResponse,
    RelaySchedulerUpdateDefinitionRequest,
    RelaySchedulerUpdateDefinitionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelaySchedulersResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_definitions(
        self,
        query: RelaySchedulerReadDefinitionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelaySchedulerReadDefinitionsItem]:
        return self._client.request(
            'GET',
            'relay/schedules/',
            query=query,
            cast_to=Page[RelaySchedulerReadDefinitionsItem],
            request_options=request_options,
        )

    def create_definition(
        self,
        data: RelaySchedulerCreateDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerCreateDefinitionResponse:
        return self._client.request(
            'POST',
            'relay/schedules/',
            body=data,
            cast_to=RelaySchedulerCreateDefinitionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_executions(
        self,
        schedule_id: str,
        query: RelaySchedulerReadExecutionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelaySchedulerReadExecutionsItem]:
        return self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/executions',
            query=query,
            cast_to=Page[RelaySchedulerReadExecutionsItem],
            request_options=request_options,
        )

    def read_dead_letter_entries(
        self,
        schedule_id: str,
        query: RelaySchedulerReadDeadLetterEntriesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelaySchedulerReadDeadLetterEntriesItem]:
        return self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/dead-letters',
            query=query,
            cast_to=Page[RelaySchedulerReadDeadLetterEntriesItem],
            request_options=request_options,
        )

    def read_definitions_count(
        self,
        query: RelaySchedulerReadDefinitionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReadDefinitionsCountResponse:
        return self._client.request(
            'GET',
            'relay/schedules/count',
            query=query,
            cast_to=RelaySchedulerReadDefinitionsCountResponse,
            request_options=request_options,
        )

    def update_definition(
        self,
        schedule_id: str,
        data: RelaySchedulerUpdateDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerUpdateDefinitionResponse:
        return self._client.request(
            'PATCH',
            f'relay/schedules/{encode_path_param(schedule_id)}',
            body=data,
            cast_to=RelaySchedulerUpdateDefinitionResponse,
            request_options=request_options,
        )

    def pause(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerPauseResponse:
        return self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/pause',
            cast_to=RelaySchedulerPauseResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def resume(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerResumeResponse:
        return self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/resume',
            cast_to=RelaySchedulerResumeResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def cancel(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerCancelResponse:
        return self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/cancel',
            cast_to=RelaySchedulerCancelResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def trigger_execution(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerTriggerExecutionResponse:
        return self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/trigger',
            cast_to=RelaySchedulerTriggerExecutionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_executions_count(
        self,
        schedule_id: str,
        query: RelaySchedulerReadExecutionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReadExecutionsCountResponse:
        return self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/executions/count',
            query=query,
            cast_to=RelaySchedulerReadExecutionsCountResponse,
            request_options=request_options,
        )

    def read_dead_letter_entries_count(
        self,
        schedule_id: str,
        query: RelaySchedulerReadDeadLetterEntriesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReadDeadLetterEntriesCountResponse:
        return self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/dead-letters/count',
            query=query,
            cast_to=RelaySchedulerReadDeadLetterEntriesCountResponse,
            request_options=request_options,
        )

    def replay_dead_letter_entry(
        self,
        schedule_id: str,
        dead_letter_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReplayDeadLetterEntryResponse:
        return self._client.request(
            'POST',
            (
                f'relay/schedules/{encode_path_param(schedule_id)}/dead-letters'
                f'/{encode_path_param(dead_letter_id)}/replay'
            ),
            cast_to=RelaySchedulerReplayDeadLetterEntryResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )


class AsyncRelaySchedulersResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_definitions(
        self,
        query: RelaySchedulerReadDefinitionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelaySchedulerReadDefinitionsItem]:
        return await self._client.request(
            'GET',
            'relay/schedules/',
            query=query,
            cast_to=AsyncPage[RelaySchedulerReadDefinitionsItem],
            request_options=request_options,
        )

    async def create_definition(
        self,
        data: RelaySchedulerCreateDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerCreateDefinitionResponse:
        return await self._client.request(
            'POST',
            'relay/schedules/',
            body=data,
            cast_to=RelaySchedulerCreateDefinitionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_executions(
        self,
        schedule_id: str,
        query: RelaySchedulerReadExecutionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelaySchedulerReadExecutionsItem]:
        return await self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/executions',
            query=query,
            cast_to=AsyncPage[RelaySchedulerReadExecutionsItem],
            request_options=request_options,
        )

    async def read_dead_letter_entries(
        self,
        schedule_id: str,
        query: RelaySchedulerReadDeadLetterEntriesQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelaySchedulerReadDeadLetterEntriesItem]:
        return await self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/dead-letters',
            query=query,
            cast_to=AsyncPage[RelaySchedulerReadDeadLetterEntriesItem],
            request_options=request_options,
        )

    async def read_definitions_count(
        self,
        query: RelaySchedulerReadDefinitionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReadDefinitionsCountResponse:
        return await self._client.request(
            'GET',
            'relay/schedules/count',
            query=query,
            cast_to=RelaySchedulerReadDefinitionsCountResponse,
            request_options=request_options,
        )

    async def update_definition(
        self,
        schedule_id: str,
        data: RelaySchedulerUpdateDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerUpdateDefinitionResponse:
        return await self._client.request(
            'PATCH',
            f'relay/schedules/{encode_path_param(schedule_id)}',
            body=data,
            cast_to=RelaySchedulerUpdateDefinitionResponse,
            request_options=request_options,
        )

    async def pause(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerPauseResponse:
        return await self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/pause',
            cast_to=RelaySchedulerPauseResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def resume(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerResumeResponse:
        return await self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/resume',
            cast_to=RelaySchedulerResumeResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def cancel(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerCancelResponse:
        return await self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/cancel',
            cast_to=RelaySchedulerCancelResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def trigger_execution(
        self,
        schedule_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerTriggerExecutionResponse:
        return await self._client.request(
            'POST',
            f'relay/schedules/{encode_path_param(schedule_id)}/trigger',
            cast_to=RelaySchedulerTriggerExecutionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_executions_count(
        self,
        schedule_id: str,
        query: RelaySchedulerReadExecutionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReadExecutionsCountResponse:
        return await self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/executions/count',
            query=query,
            cast_to=RelaySchedulerReadExecutionsCountResponse,
            request_options=request_options,
        )

    async def read_dead_letter_entries_count(
        self,
        schedule_id: str,
        query: RelaySchedulerReadDeadLetterEntriesCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReadDeadLetterEntriesCountResponse:
        return await self._client.request(
            'GET',
            f'relay/schedules/{encode_path_param(schedule_id)}/dead-letters/count',
            query=query,
            cast_to=RelaySchedulerReadDeadLetterEntriesCountResponse,
            request_options=request_options,
        )

    async def replay_dead_letter_entry(
        self,
        schedule_id: str,
        dead_letter_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelaySchedulerReplayDeadLetterEntryResponse:
        return await self._client.request(
            'POST',
            (
                f'relay/schedules/{encode_path_param(schedule_id)}/dead-letters'
                f'/{encode_path_param(dead_letter_id)}/replay'
            ),
            cast_to=RelaySchedulerReplayDeadLetterEntryResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )
