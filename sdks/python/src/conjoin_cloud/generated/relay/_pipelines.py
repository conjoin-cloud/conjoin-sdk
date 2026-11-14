from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from conjoin_cloud._models import AsyncPage, Page
from conjoin_cloud._request_options import RequestOptions
from conjoin_cloud._url import encode_path_param
from conjoin_cloud.generated._models import (
    RelayPipelinesApprovePipelineGateRequest,
    RelayPipelinesApprovePipelineGateResponse,
    RelayPipelinesCancelPipelineRunResponse,
    RelayPipelinesCreatePipelineDefinitionRequest,
    RelayPipelinesCreatePipelineDefinitionResponse,
    RelayPipelinesDeletePipelineDefinitionResponse,
    RelayPipelinesReadPipelineDefinitionsCountQuery,
    RelayPipelinesReadPipelineDefinitionsCountResponse,
    RelayPipelinesReadPipelineDefinitionsItem,
    RelayPipelinesReadPipelineDefinitionsQuery,
    RelayPipelinesReadPipelineRunResponse,
    RelayPipelinesReadPipelineRunsCountQuery,
    RelayPipelinesReadPipelineRunsCountResponse,
    RelayPipelinesReadPipelineRunsItem,
    RelayPipelinesReadPipelineRunsQuery,
    RelayPipelinesRejectPipelineGateRequest,
    RelayPipelinesRejectPipelineGateResponse,
    RelayPipelinesTriggerPipelineRunRequest,
    RelayPipelinesTriggerPipelineRunResponse,
    RelayPipelinesUpdatePipelineDefinitionRequest,
    RelayPipelinesUpdatePipelineDefinitionResponse,
)

if TYPE_CHECKING:
    from conjoin_cloud import AsyncConjoin, Conjoin


class RelayPipelinesResource:
    def __init__(self, client: Conjoin) -> None:
        self._client = client

    def read_pipeline_definitions(
        self,
        query: RelayPipelinesReadPipelineDefinitionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayPipelinesReadPipelineDefinitionsItem]:
        return self._client.request(
            'GET',
            'relay/pipelines/',
            query=query,
            cast_to=Page[RelayPipelinesReadPipelineDefinitionsItem],
            request_options=request_options,
        )

    def create_pipeline_definition(
        self,
        data: RelayPipelinesCreatePipelineDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesCreatePipelineDefinitionResponse:
        return self._client.request(
            'POST',
            'relay/pipelines/',
            body=data,
            cast_to=RelayPipelinesCreatePipelineDefinitionResponse,
            request_options=request_options,
        )

    def read_pipeline_definitions_count(
        self,
        query: RelayPipelinesReadPipelineDefinitionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesReadPipelineDefinitionsCountResponse:
        return self._client.request(
            'GET',
            'relay/pipelines/count',
            query=query,
            cast_to=RelayPipelinesReadPipelineDefinitionsCountResponse,
            request_options=request_options,
        )

    def update_pipeline_definition(
        self,
        pipeline_id: str,
        data: RelayPipelinesUpdatePipelineDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesUpdatePipelineDefinitionResponse:
        return self._client.request(
            'PATCH',
            f'relay/pipelines/{encode_path_param(pipeline_id)}',
            body=data,
            cast_to=RelayPipelinesUpdatePipelineDefinitionResponse,
            request_options=request_options,
        )

    def delete_pipeline_definition(
        self,
        pipeline_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesDeletePipelineDefinitionResponse:
        return self._client.request(
            'DELETE',
            f'relay/pipelines/{encode_path_param(pipeline_id)}',
            cast_to=RelayPipelinesDeletePipelineDefinitionResponse,
            request_options=request_options,
        )

    def trigger_pipeline_run(
        self,
        pipeline_id: str,
        data: RelayPipelinesTriggerPipelineRunRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesTriggerPipelineRunResponse:
        return self._client.request(
            'POST',
            f'relay/pipelines/{encode_path_param(pipeline_id)}/trigger',
            body=data,
            cast_to=RelayPipelinesTriggerPipelineRunResponse,
            request_options=request_options,
        )

    def read_pipeline_runs(
        self,
        query: RelayPipelinesReadPipelineRunsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> Page[RelayPipelinesReadPipelineRunsItem]:
        return self._client.request(
            'GET',
            'relay/pipeline-runs/',
            query=query,
            cast_to=Page[RelayPipelinesReadPipelineRunsItem],
            request_options=request_options,
        )

    def read_pipeline_runs_count(
        self,
        query: RelayPipelinesReadPipelineRunsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesReadPipelineRunsCountResponse:
        return self._client.request(
            'GET',
            'relay/pipeline-runs/count',
            query=query,
            cast_to=RelayPipelinesReadPipelineRunsCountResponse,
            request_options=request_options,
        )

    def read_pipeline_run(
        self,
        pipeline_run_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesReadPipelineRunResponse:
        return self._client.request(
            'GET',
            f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}',
            cast_to=RelayPipelinesReadPipelineRunResponse,
            request_options=request_options,
        )

    def cancel_pipeline_run(
        self,
        pipeline_run_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesCancelPipelineRunResponse:
        return self._client.request(
            'POST',
            f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}/cancel',
            cast_to=RelayPipelinesCancelPipelineRunResponse,
            request_options=request_options,
        )

    def approve_pipeline_gate(
        self,
        pipeline_run_id: str,
        step_id: str,
        data: RelayPipelinesApprovePipelineGateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesApprovePipelineGateResponse:
        return self._client.request(
            'POST',
            (
                f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}/steps'
                f'/{encode_path_param(step_id)}/approve'
            ),
            body=data,
            cast_to=RelayPipelinesApprovePipelineGateResponse,
            request_options=request_options,
        )

    def reject_pipeline_gate(
        self,
        pipeline_run_id: str,
        step_id: str,
        data: RelayPipelinesRejectPipelineGateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesRejectPipelineGateResponse:
        return self._client.request(
            'POST',
            (
                f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}/steps'
                f'/{encode_path_param(step_id)}/reject'
            ),
            body=data,
            cast_to=RelayPipelinesRejectPipelineGateResponse,
            request_options=request_options,
        )


class AsyncRelayPipelinesResource:
    def __init__(self, client: AsyncConjoin) -> None:
        self._client = client

    async def read_pipeline_definitions(
        self,
        query: RelayPipelinesReadPipelineDefinitionsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayPipelinesReadPipelineDefinitionsItem]:
        return await self._client.request(
            'GET',
            'relay/pipelines/',
            query=query,
            cast_to=AsyncPage[RelayPipelinesReadPipelineDefinitionsItem],
            request_options=request_options,
        )

    async def create_pipeline_definition(
        self,
        data: RelayPipelinesCreatePipelineDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesCreatePipelineDefinitionResponse:
        return await self._client.request(
            'POST',
            'relay/pipelines/',
            body=data,
            cast_to=RelayPipelinesCreatePipelineDefinitionResponse,
            request_options=request_options,
        )

    async def read_pipeline_definitions_count(
        self,
        query: RelayPipelinesReadPipelineDefinitionsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesReadPipelineDefinitionsCountResponse:
        return await self._client.request(
            'GET',
            'relay/pipelines/count',
            query=query,
            cast_to=RelayPipelinesReadPipelineDefinitionsCountResponse,
            request_options=request_options,
        )

    async def update_pipeline_definition(
        self,
        pipeline_id: str,
        data: RelayPipelinesUpdatePipelineDefinitionRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesUpdatePipelineDefinitionResponse:
        return await self._client.request(
            'PATCH',
            f'relay/pipelines/{encode_path_param(pipeline_id)}',
            body=data,
            cast_to=RelayPipelinesUpdatePipelineDefinitionResponse,
            request_options=request_options,
        )

    async def delete_pipeline_definition(
        self,
        pipeline_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesDeletePipelineDefinitionResponse:
        return await self._client.request(
            'DELETE',
            f'relay/pipelines/{encode_path_param(pipeline_id)}',
            cast_to=RelayPipelinesDeletePipelineDefinitionResponse,
            request_options=request_options,
        )

    async def trigger_pipeline_run(
        self,
        pipeline_id: str,
        data: RelayPipelinesTriggerPipelineRunRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesTriggerPipelineRunResponse:
        return await self._client.request(
            'POST',
            f'relay/pipelines/{encode_path_param(pipeline_id)}/trigger',
            body=data,
            cast_to=RelayPipelinesTriggerPipelineRunResponse,
            request_options=request_options,
        )

    async def read_pipeline_runs(
        self,
        query: RelayPipelinesReadPipelineRunsQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> AsyncPage[RelayPipelinesReadPipelineRunsItem]:
        return await self._client.request(
            'GET',
            'relay/pipeline-runs/',
            query=query,
            cast_to=AsyncPage[RelayPipelinesReadPipelineRunsItem],
            request_options=request_options,
        )

    async def read_pipeline_runs_count(
        self,
        query: RelayPipelinesReadPipelineRunsCountQuery | None = None,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesReadPipelineRunsCountResponse:
        return await self._client.request(
            'GET',
            'relay/pipeline-runs/count',
            query=query,
            cast_to=RelayPipelinesReadPipelineRunsCountResponse,
            request_options=request_options,
        )

    async def read_pipeline_run(
        self,
        pipeline_run_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesReadPipelineRunResponse:
        return await self._client.request(
            'GET',
            f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}',
            cast_to=RelayPipelinesReadPipelineRunResponse,
            request_options=request_options,
        )

    async def cancel_pipeline_run(
        self,
        pipeline_run_id: str,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesCancelPipelineRunResponse:
        return await self._client.request(
            'POST',
            f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}/cancel',
            cast_to=RelayPipelinesCancelPipelineRunResponse,
            request_options=request_options,
        )

    async def approve_pipeline_gate(
        self,
        pipeline_run_id: str,
        step_id: str,
        data: RelayPipelinesApprovePipelineGateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesApprovePipelineGateResponse:
        return await self._client.request(
            'POST',
            (
                f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}/steps'
                f'/{encode_path_param(step_id)}/approve'
            ),
            body=data,
            cast_to=RelayPipelinesApprovePipelineGateResponse,
            request_options=request_options,
        )

    async def reject_pipeline_gate(
        self,
        pipeline_run_id: str,
        step_id: str,
        data: RelayPipelinesRejectPipelineGateRequest,
        *,
        request_options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> RelayPipelinesRejectPipelineGateResponse:
        return await self._client.request(
            'POST',
            (
                f'relay/pipeline-runs/{encode_path_param(pipeline_run_id)}/steps'
                f'/{encode_path_param(step_id)}/reject'
            ),
            body=data,
            cast_to=RelayPipelinesRejectPipelineGateResponse,
            request_options=request_options,
        )
