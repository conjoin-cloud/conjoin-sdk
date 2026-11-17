from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    RelayQueuesBatchEnqueueTasksRequest,
    RelayQueuesBatchEnqueueTasksResponse,
    RelayQueuesCreateQueueDefinitionRequest,
    RelayQueuesCreateQueueDefinitionResponse,
    RelayQueuesDeleteQueueDefinitionResponse,
    RelayQueuesEnqueueTaskRequest,
    RelayQueuesEnqueueTaskResponse,
    RelayQueuesPauseQueueResponse,
    RelayQueuesPurgeQueueTasksRequest,
    RelayQueuesPurgeQueueTasksResponse,
    RelayQueuesReadDeadLetterTasksCountQuery,
    RelayQueuesReadDeadLetterTasksCountResponse,
    RelayQueuesReadDeadLetterTasksItem,
    RelayQueuesReadDeadLetterTasksQuery,
    RelayQueuesReadQueueDefinitionsCountQuery,
    RelayQueuesReadQueueDefinitionsCountResponse,
    RelayQueuesReadQueueDefinitionsItem,
    RelayQueuesReadQueueDefinitionsQuery,
    RelayQueuesReadQueueTasksCountQuery,
    RelayQueuesReadQueueTasksCountResponse,
    RelayQueuesReadQueueTasksItem,
    RelayQueuesReadQueueTasksQuery,
    RelayQueuesReplayDeadLetterTaskResponse,
    RelayQueuesResumeQueueResponse,
    RelayQueuesUpdateQueueDefinitionRequest,
    RelayQueuesUpdateQueueDefinitionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelayQueuesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_queue_definitions(
        self,
        query: RelayQueuesReadQueueDefinitionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayQueuesReadQueueDefinitionsItem]:
        return self._client.request(
            'GET',
            'relay/queues/',
            query=query,
            cast_to=Page[RelayQueuesReadQueueDefinitionsItem],
            request_options=request_options,
        )

    def create_queue_definition(
        self,
        data: RelayQueuesCreateQueueDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesCreateQueueDefinitionResponse:
        return self._client.request(
            'POST',
            'relay/queues/',
            body=data,
            cast_to=RelayQueuesCreateQueueDefinitionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_queue_tasks(
        self,
        queue_id: str,
        query: RelayQueuesReadQueueTasksQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayQueuesReadQueueTasksItem]:
        return self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/tasks',
            query=query,
            cast_to=Page[RelayQueuesReadQueueTasksItem],
            request_options=request_options,
        )

    def enqueue_task(
        self,
        queue_id: str,
        data: RelayQueuesEnqueueTaskRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesEnqueueTaskResponse:
        return self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/tasks',
            body=data,
            cast_to=RelayQueuesEnqueueTaskResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_dead_letter_tasks(
        self,
        queue_id: str,
        query: RelayQueuesReadDeadLetterTasksQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayQueuesReadDeadLetterTasksItem]:
        return self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/dead-letters',
            query=query,
            cast_to=Page[RelayQueuesReadDeadLetterTasksItem],
            request_options=request_options,
        )

    def read_queue_definitions_count(
        self,
        query: RelayQueuesReadQueueDefinitionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReadQueueDefinitionsCountResponse:
        return self._client.request(
            'GET',
            'relay/queues/count',
            query=query,
            cast_to=RelayQueuesReadQueueDefinitionsCountResponse,
            request_options=request_options,
        )

    def update_queue_definition(
        self,
        queue_id: str,
        data: RelayQueuesUpdateQueueDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesUpdateQueueDefinitionResponse:
        return self._client.request(
            'PATCH',
            f'relay/queues/{encode_path_param(queue_id)}',
            body=data,
            cast_to=RelayQueuesUpdateQueueDefinitionResponse,
            request_options=request_options,
        )

    def delete_queue_definition(
        self,
        queue_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesDeleteQueueDefinitionResponse:
        return self._client.request(
            'DELETE',
            f'relay/queues/{encode_path_param(queue_id)}',
            cast_to=RelayQueuesDeleteQueueDefinitionResponse,
            request_options=request_options,
        )

    def pause_queue(
        self,
        queue_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesPauseQueueResponse:
        return self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/pause',
            cast_to=RelayQueuesPauseQueueResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def resume_queue(
        self,
        queue_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesResumeQueueResponse:
        return self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/resume',
            cast_to=RelayQueuesResumeQueueResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def batch_enqueue_tasks(
        self,
        queue_id: str,
        data: RelayQueuesBatchEnqueueTasksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesBatchEnqueueTasksResponse:
        return self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/enqueue-batch',
            body=data,
            cast_to=RelayQueuesBatchEnqueueTasksResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def read_queue_tasks_count(
        self,
        queue_id: str,
        query: RelayQueuesReadQueueTasksCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReadQueueTasksCountResponse:
        return self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/tasks/count',
            query=query,
            cast_to=RelayQueuesReadQueueTasksCountResponse,
            request_options=request_options,
        )

    def read_dead_letter_tasks_count(
        self,
        queue_id: str,
        query: RelayQueuesReadDeadLetterTasksCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReadDeadLetterTasksCountResponse:
        return self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/dead-letters/count',
            query=query,
            cast_to=RelayQueuesReadDeadLetterTasksCountResponse,
            request_options=request_options,
        )

    def replay_dead_letter_task(
        self,
        queue_id: str,
        dead_letter_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReplayDeadLetterTaskResponse:
        return self._client.request(
            'POST',
            (
                f'relay/queues/{encode_path_param(queue_id)}/dead-letters'
                f'/{encode_path_param(dead_letter_id)}/replay'
            ),
            cast_to=RelayQueuesReplayDeadLetterTaskResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    def purge_queue_tasks(
        self,
        queue_id: str,
        data: RelayQueuesPurgeQueueTasksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesPurgeQueueTasksResponse:
        return self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/purge',
            body=data,
            cast_to=RelayQueuesPurgeQueueTasksResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )


class AsyncRelayQueuesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_queue_definitions(
        self,
        query: RelayQueuesReadQueueDefinitionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayQueuesReadQueueDefinitionsItem]:
        return await self._client.request(
            'GET',
            'relay/queues/',
            query=query,
            cast_to=AsyncPage[RelayQueuesReadQueueDefinitionsItem],
            request_options=request_options,
        )

    async def create_queue_definition(
        self,
        data: RelayQueuesCreateQueueDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesCreateQueueDefinitionResponse:
        return await self._client.request(
            'POST',
            'relay/queues/',
            body=data,
            cast_to=RelayQueuesCreateQueueDefinitionResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_queue_tasks(
        self,
        queue_id: str,
        query: RelayQueuesReadQueueTasksQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayQueuesReadQueueTasksItem]:
        return await self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/tasks',
            query=query,
            cast_to=AsyncPage[RelayQueuesReadQueueTasksItem],
            request_options=request_options,
        )

    async def enqueue_task(
        self,
        queue_id: str,
        data: RelayQueuesEnqueueTaskRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesEnqueueTaskResponse:
        return await self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/tasks',
            body=data,
            cast_to=RelayQueuesEnqueueTaskResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_dead_letter_tasks(
        self,
        queue_id: str,
        query: RelayQueuesReadDeadLetterTasksQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayQueuesReadDeadLetterTasksItem]:
        return await self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/dead-letters',
            query=query,
            cast_to=AsyncPage[RelayQueuesReadDeadLetterTasksItem],
            request_options=request_options,
        )

    async def read_queue_definitions_count(
        self,
        query: RelayQueuesReadQueueDefinitionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReadQueueDefinitionsCountResponse:
        return await self._client.request(
            'GET',
            'relay/queues/count',
            query=query,
            cast_to=RelayQueuesReadQueueDefinitionsCountResponse,
            request_options=request_options,
        )

    async def update_queue_definition(
        self,
        queue_id: str,
        data: RelayQueuesUpdateQueueDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesUpdateQueueDefinitionResponse:
        return await self._client.request(
            'PATCH',
            f'relay/queues/{encode_path_param(queue_id)}',
            body=data,
            cast_to=RelayQueuesUpdateQueueDefinitionResponse,
            request_options=request_options,
        )

    async def delete_queue_definition(
        self,
        queue_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesDeleteQueueDefinitionResponse:
        return await self._client.request(
            'DELETE',
            f'relay/queues/{encode_path_param(queue_id)}',
            cast_to=RelayQueuesDeleteQueueDefinitionResponse,
            request_options=request_options,
        )

    async def pause_queue(
        self,
        queue_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesPauseQueueResponse:
        return await self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/pause',
            cast_to=RelayQueuesPauseQueueResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def resume_queue(
        self,
        queue_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesResumeQueueResponse:
        return await self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/resume',
            cast_to=RelayQueuesResumeQueueResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def batch_enqueue_tasks(
        self,
        queue_id: str,
        data: RelayQueuesBatchEnqueueTasksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesBatchEnqueueTasksResponse:
        return await self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/enqueue-batch',
            body=data,
            cast_to=RelayQueuesBatchEnqueueTasksResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def read_queue_tasks_count(
        self,
        queue_id: str,
        query: RelayQueuesReadQueueTasksCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReadQueueTasksCountResponse:
        return await self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/tasks/count',
            query=query,
            cast_to=RelayQueuesReadQueueTasksCountResponse,
            request_options=request_options,
        )

    async def read_dead_letter_tasks_count(
        self,
        queue_id: str,
        query: RelayQueuesReadDeadLetterTasksCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReadDeadLetterTasksCountResponse:
        return await self._client.request(
            'GET',
            f'relay/queues/{encode_path_param(queue_id)}/dead-letters/count',
            query=query,
            cast_to=RelayQueuesReadDeadLetterTasksCountResponse,
            request_options=request_options,
        )

    async def replay_dead_letter_task(
        self,
        queue_id: str,
        dead_letter_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesReplayDeadLetterTaskResponse:
        return await self._client.request(
            'POST',
            (
                f'relay/queues/{encode_path_param(queue_id)}/dead-letters'
                f'/{encode_path_param(dead_letter_id)}/replay'
            ),
            cast_to=RelayQueuesReplayDeadLetterTaskResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )

    async def purge_queue_tasks(
        self,
        queue_id: str,
        data: RelayQueuesPurgeQueueTasksRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayQueuesPurgeQueueTasksResponse:
        return await self._client.request(
            'POST',
            f'relay/queues/{encode_path_param(queue_id)}/purge',
            body=data,
            cast_to=RelayQueuesPurgeQueueTasksResponse,
            request_options=request_options,
            accepts_idempotency_key=True,
        )
