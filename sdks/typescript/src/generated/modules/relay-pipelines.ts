import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadPipelineDefinitionsData = NonNullable<operations['readPipelineDefinitions']['responses']['200']['content']['application/json']['data']>[number]
type ReadPipelineDefinitionsQuery = NonNullable<operations['readPipelineDefinitions']['parameters']['query']>
type CreatePipelineDefinitionBody = NonNullable<operations['createPipelineDefinition']['requestBody']>['content']['application/json']
type CreatePipelineDefinitionData = NonNullable<operations['createPipelineDefinition']['responses']['201']['content']['application/json']['data']>
type ReadPipelineDefinitionsCountData = NonNullable<operations['readPipelineDefinitionsCount']['responses']['200']['content']['application/json']['data']>
type ReadPipelineDefinitionsCountQuery = NonNullable<operations['readPipelineDefinitionsCount']['parameters']['query']>
type UpdatePipelineDefinitionBody = NonNullable<operations['updatePipelineDefinition']['requestBody']>['content']['application/json']
type UpdatePipelineDefinitionData = NonNullable<operations['updatePipelineDefinition']['responses']['200']['content']['application/json']['data']>
type DeletePipelineDefinitionData = NonNullable<operations['deletePipelineDefinition']['responses']['200']['content']['application/json']['data']>
type TriggerPipelineRunBody = NonNullable<operations['triggerPipelineRun']['requestBody']>['content']['application/json']
type TriggerPipelineRunData = NonNullable<operations['triggerPipelineRun']['responses']['201']['content']['application/json']['data']>
type ReadPipelineRunsData = NonNullable<operations['readPipelineRuns']['responses']['200']['content']['application/json']['data']>[number]
type ReadPipelineRunsQuery = NonNullable<operations['readPipelineRuns']['parameters']['query']>
type ReadPipelineRunsCountData = NonNullable<operations['readPipelineRunsCount']['responses']['200']['content']['application/json']['data']>
type ReadPipelineRunsCountQuery = NonNullable<operations['readPipelineRunsCount']['parameters']['query']>
type ReadPipelineRunData = NonNullable<operations['readPipelineRun']['responses']['200']['content']['application/json']['data']>
type CancelPipelineRunData = NonNullable<operations['cancelPipelineRun']['responses']['200']['content']['application/json']['data']>
type ApprovePipelineGateBody = NonNullable<operations['approvePipelineGate']['requestBody']>['content']['application/json']
type ApprovePipelineGateData = NonNullable<operations['approvePipelineGate']['responses']['200']['content']['application/json']['data']>
type RejectPipelineGateBody = NonNullable<operations['rejectPipelineGate']['requestBody']>['content']['application/json']
type RejectPipelineGateData = NonNullable<operations['rejectPipelineGate']['responses']['200']['content']['application/json']['data']>

export function createRelayPipelines(client: ConjoinClient) {
  return {
    readPipelineDefinitions: (query?: ReadPipelineDefinitionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadPipelineDefinitionsData>('relay/pipelines/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createPipelineDefinition: (data: CreatePipelineDefinitionBody, options?: ConjoinCallOptions) =>
      client.fetch<CreatePipelineDefinitionData>('relay/pipelines/', { ...options, method: 'POST', body: data }),

    readPipelineDefinitionsCount: (query?: ReadPipelineDefinitionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadPipelineDefinitionsCountData>('relay/pipelines/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    updatePipelineDefinition: (pipelineId: string, data: UpdatePipelineDefinitionBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdatePipelineDefinitionData>(`relay/pipelines/${encodePathParam(pipelineId)}`, { ...options, method: 'PATCH', body: data }),

    deletePipelineDefinition: (pipelineId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeletePipelineDefinitionData>(`relay/pipelines/${encodePathParam(pipelineId)}`, { ...options, method: 'DELETE' }),

    triggerPipelineRun: (pipelineId: string, data: TriggerPipelineRunBody, options?: ConjoinCallOptions) =>
      client.fetch<TriggerPipelineRunData>(`relay/pipelines/${encodePathParam(pipelineId)}/trigger`, { ...options, method: 'POST', body: data }),

    readPipelineRuns: (query?: ReadPipelineRunsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadPipelineRunsData>('relay/pipeline-runs/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readPipelineRunsCount: (query?: ReadPipelineRunsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadPipelineRunsCountData>('relay/pipeline-runs/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readPipelineRun: (pipelineRunId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadPipelineRunData>(`relay/pipeline-runs/${encodePathParam(pipelineRunId)}`, { ...options, method: 'GET' }),

    cancelPipelineRun: (pipelineRunId: string, options?: ConjoinCallOptions) =>
      client.fetch<CancelPipelineRunData>(`relay/pipeline-runs/${encodePathParam(pipelineRunId)}/cancel`, { ...options, method: 'POST' }),

    approvePipelineGate: (pipelineRunId: string, stepId: string, data: ApprovePipelineGateBody, options?: ConjoinCallOptions) =>
      client.fetch<ApprovePipelineGateData>(`relay/pipeline-runs/${encodePathParam(pipelineRunId)}/steps/${encodePathParam(stepId)}/approve`, { ...options, method: 'POST', body: data }),

    rejectPipelineGate: (pipelineRunId: string, stepId: string, data: RejectPipelineGateBody, options?: ConjoinCallOptions) =>
      client.fetch<RejectPipelineGateData>(`relay/pipeline-runs/${encodePathParam(pipelineRunId)}/steps/${encodePathParam(stepId)}/reject`, { ...options, method: 'POST', body: data }),
  }
}
