import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadDefinitionsData = NonNullable<operations['readSchedulerDefinitions']['responses']['200']['content']['application/json']['data']>[number]
type ReadDefinitionsQuery = NonNullable<operations['readSchedulerDefinitions']['parameters']['query']>
type CreateDefinitionBody = NonNullable<operations['createSchedulerDefinition']['requestBody']>['content']['application/json']
type CreateDefinitionData = NonNullable<operations['createSchedulerDefinition']['responses']['201']['content']['application/json']['data']>
type ReadExecutionsData = NonNullable<operations['readSchedulerExecutions']['responses']['200']['content']['application/json']['data']>[number]
type ReadExecutionsQuery = NonNullable<operations['readSchedulerExecutions']['parameters']['query']>
type ReadDeadLetterEntriesData = NonNullable<operations['readSchedulerDeadLetterEntries']['responses']['200']['content']['application/json']['data']>[number]
type ReadDeadLetterEntriesQuery = NonNullable<operations['readSchedulerDeadLetterEntries']['parameters']['query']>
type ReadDefinitionsCountData = NonNullable<operations['readSchedulerDefinitionsCount']['responses']['200']['content']['application/json']['data']>
type ReadDefinitionsCountQuery = NonNullable<operations['readSchedulerDefinitionsCount']['parameters']['query']>
type UpdateDefinitionBody = NonNullable<operations['updateSchedulerDefinition']['requestBody']>['content']['application/json']
type UpdateDefinitionData = NonNullable<operations['updateSchedulerDefinition']['responses']['200']['content']['application/json']['data']>
type PauseData = NonNullable<operations['pauseScheduler']['responses']['200']['content']['application/json']['data']>
type ResumeData = NonNullable<operations['resumeScheduler']['responses']['200']['content']['application/json']['data']>
type CancelData = NonNullable<operations['cancelScheduler']['responses']['200']['content']['application/json']['data']>
type TriggerExecutionData = NonNullable<operations['triggerSchedulerExecution']['responses']['202']['content']['application/json']['data']>
type ReadExecutionsCountData = NonNullable<operations['readSchedulerExecutionsCount']['responses']['200']['content']['application/json']['data']>
type ReadExecutionsCountQuery = NonNullable<operations['readSchedulerExecutionsCount']['parameters']['query']>
type ReadDeadLetterEntriesCountData = NonNullable<operations['readSchedulerDeadLetterEntriesCount']['responses']['200']['content']['application/json']['data']>
type ReadDeadLetterEntriesCountQuery = NonNullable<operations['readSchedulerDeadLetterEntriesCount']['parameters']['query']>
type ReplayDeadLetterEntryData = NonNullable<operations['replaySchedulerDeadLetterEntry']['responses']['202']['content']['application/json']['data']>

export function createRelaySchedulers(client: ConjoinClient) {
  return {
    readDefinitions: (query?: ReadDefinitionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadDefinitionsData>('relay/schedules/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createDefinition: (data: CreateDefinitionBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateDefinitionData>('relay/schedules/', { ...options, method: 'POST', body: data }),

    readExecutions: (scheduleId: string, query?: ReadExecutionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadExecutionsData>(`relay/schedules/${encodePathParam(scheduleId)}/executions`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readDeadLetterEntries: (scheduleId: string, query?: ReadDeadLetterEntriesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadDeadLetterEntriesData>(`relay/schedules/${encodePathParam(scheduleId)}/dead-letters`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readDefinitionsCount: (query?: ReadDefinitionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadDefinitionsCountData>('relay/schedules/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    updateDefinition: (scheduleId: string, data: UpdateDefinitionBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateDefinitionData>(`relay/schedules/${encodePathParam(scheduleId)}`, { ...options, method: 'PATCH', body: data }),

    pause: (scheduleId: string, options?: ConjoinCallOptions) =>
      client.fetch<PauseData>(`relay/schedules/${encodePathParam(scheduleId)}/pause`, { ...options, method: 'POST' }),

    resume: (scheduleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ResumeData>(`relay/schedules/${encodePathParam(scheduleId)}/resume`, { ...options, method: 'POST' }),

    cancel: (scheduleId: string, options?: ConjoinCallOptions) =>
      client.fetch<CancelData>(`relay/schedules/${encodePathParam(scheduleId)}/cancel`, { ...options, method: 'POST' }),

    triggerExecution: (scheduleId: string, options?: ConjoinCallOptions) =>
      client.fetch<TriggerExecutionData>(`relay/schedules/${encodePathParam(scheduleId)}/trigger`, { ...options, method: 'POST' }),

    readExecutionsCount: (scheduleId: string, query?: ReadExecutionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadExecutionsCountData>(`relay/schedules/${encodePathParam(scheduleId)}/executions/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readDeadLetterEntriesCount: (scheduleId: string, query?: ReadDeadLetterEntriesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadDeadLetterEntriesCountData>(`relay/schedules/${encodePathParam(scheduleId)}/dead-letters/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    replayDeadLetterEntry: (scheduleId: string, deadLetterId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReplayDeadLetterEntryData>(`relay/schedules/${encodePathParam(scheduleId)}/dead-letters/${encodePathParam(deadLetterId)}/replay`, { ...options, method: 'POST' }),
  }
}
