import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadQueueDefinitionsData = NonNullable<operations['readQueueDefinitions']['responses']['200']['content']['application/json']['data']>[number]
type ReadQueueDefinitionsQuery = NonNullable<operations['readQueueDefinitions']['parameters']['query']>
type CreateQueueDefinitionBody = NonNullable<operations['createQueueDefinition']['requestBody']>['content']['application/json']
type CreateQueueDefinitionData = NonNullable<operations['createQueueDefinition']['responses']['201']['content']['application/json']['data']>
type ReadQueueTasksData = NonNullable<operations['readQueueTasks']['responses']['200']['content']['application/json']['data']>[number]
type ReadQueueTasksQuery = NonNullable<operations['readQueueTasks']['parameters']['query']>
type EnqueueTaskBody = NonNullable<operations['enqueueTask']['requestBody']>['content']['application/json']
type EnqueueTaskData = NonNullable<operations['enqueueTask']['responses']['201']['content']['application/json']['data']>
type ReadDeadLetterTasksData = NonNullable<operations['readDeadLetterTasks']['responses']['200']['content']['application/json']['data']>[number]
type ReadDeadLetterTasksQuery = NonNullable<operations['readDeadLetterTasks']['parameters']['query']>
type ReadQueueDefinitionsCountData = NonNullable<operations['readQueueDefinitionsCount']['responses']['200']['content']['application/json']['data']>
type ReadQueueDefinitionsCountQuery = NonNullable<operations['readQueueDefinitionsCount']['parameters']['query']>
type UpdateQueueDefinitionBody = NonNullable<operations['updateQueueDefinition']['requestBody']>['content']['application/json']
type UpdateQueueDefinitionData = NonNullable<operations['updateQueueDefinition']['responses']['200']['content']['application/json']['data']>
type DeleteQueueDefinitionData = NonNullable<operations['deleteQueueDefinition']['responses']['200']['content']['application/json']['data']>
type PauseQueueData = NonNullable<operations['pauseQueue']['responses']['200']['content']['application/json']['data']>
type ResumeQueueData = NonNullable<operations['resumeQueue']['responses']['200']['content']['application/json']['data']>
type BatchEnqueueTasksBody = NonNullable<operations['batchEnqueueTasks']['requestBody']>['content']['application/json']
type BatchEnqueueTasksData = NonNullable<operations['batchEnqueueTasks']['responses']['201']['content']['application/json']['data']>
type ReadQueueTasksCountData = NonNullable<operations['readQueueTasksCount']['responses']['200']['content']['application/json']['data']>
type ReadQueueTasksCountQuery = NonNullable<operations['readQueueTasksCount']['parameters']['query']>
type ReadDeadLetterTasksCountData = NonNullable<operations['readDeadLetterTasksCount']['responses']['200']['content']['application/json']['data']>
type ReadDeadLetterTasksCountQuery = NonNullable<operations['readDeadLetterTasksCount']['parameters']['query']>
type ReplayDeadLetterTaskData = NonNullable<operations['replayDeadLetterTask']['responses']['200']['content']['application/json']['data']>
type PurgeQueueTasksBody = NonNullable<operations['purgeQueueTasks']['requestBody']>['content']['application/json']
type PurgeQueueTasksData = NonNullable<operations['purgeQueueTasks']['responses']['200']['content']['application/json']['data']>

export function createRelayQueues(client: ConjoinClient) {
  return {
    readQueueDefinitions: (query?: ReadQueueDefinitionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadQueueDefinitionsData>('relay/queues/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createQueueDefinition: (data: CreateQueueDefinitionBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateQueueDefinitionData>('relay/queues/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readQueueTasks: (queueId: string, query?: ReadQueueTasksQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadQueueTasksData>(`relay/queues/${encodePathParam(queueId)}/tasks`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    enqueueTask: (queueId: string, data: EnqueueTaskBody, options?: ConjoinCallOptions) =>
      client.fetch<EnqueueTaskData>(`relay/queues/${encodePathParam(queueId)}/tasks`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readDeadLetterTasks: (queueId: string, query?: ReadDeadLetterTasksQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadDeadLetterTasksData>(`relay/queues/${encodePathParam(queueId)}/dead-letters`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readQueueDefinitionsCount: (query?: ReadQueueDefinitionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadQueueDefinitionsCountData>('relay/queues/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    updateQueueDefinition: (queueId: string, data: UpdateQueueDefinitionBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateQueueDefinitionData>(`relay/queues/${encodePathParam(queueId)}`, { ...options, method: 'PATCH', body: data }),

    deleteQueueDefinition: (queueId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteQueueDefinitionData>(`relay/queues/${encodePathParam(queueId)}`, { ...options, method: 'DELETE' }),

    pauseQueue: (queueId: string, options?: ConjoinCallOptions) =>
      client.fetch<PauseQueueData>(`relay/queues/${encodePathParam(queueId)}/pause`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    resumeQueue: (queueId: string, options?: ConjoinCallOptions) =>
      client.fetch<ResumeQueueData>(`relay/queues/${encodePathParam(queueId)}/resume`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    batchEnqueueTasks: (queueId: string, data: BatchEnqueueTasksBody, options?: ConjoinCallOptions) =>
      client.fetch<BatchEnqueueTasksData>(`relay/queues/${encodePathParam(queueId)}/enqueue-batch`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readQueueTasksCount: (queueId: string, query?: ReadQueueTasksCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadQueueTasksCountData>(`relay/queues/${encodePathParam(queueId)}/tasks/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readDeadLetterTasksCount: (queueId: string, query?: ReadDeadLetterTasksCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadDeadLetterTasksCountData>(`relay/queues/${encodePathParam(queueId)}/dead-letters/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    replayDeadLetterTask: (queueId: string, deadLetterId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReplayDeadLetterTaskData>(`relay/queues/${encodePathParam(queueId)}/dead-letters/${encodePathParam(deadLetterId)}/replay`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    purgeQueueTasks: (queueId: string, data: PurgeQueueTasksBody, options?: ConjoinCallOptions) =>
      client.fetch<PurgeQueueTasksData>(`relay/queues/${encodePathParam(queueId)}/purge`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),
  }
}
