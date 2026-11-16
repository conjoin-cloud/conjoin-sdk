import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateIndexBody = NonNullable<operations['createAiContextIndex']['requestBody']>['content']['application/json']
type CreateIndexData = NonNullable<operations['createAiContextIndex']['responses']['201']['content']['application/json']['data']>
type ListIndexesData = NonNullable<operations['listAiContextIndexes']['responses']['200']['content']['application/json']['data']>[number]
type ListIndexesQuery = NonNullable<operations['listAiContextIndexes']['parameters']['query']>
type ReadIndexData = NonNullable<operations['readAiContextIndex']['responses']['200']['content']['application/json']['data']>
type DeleteIndexData = NonNullable<operations['deleteAiContextIndex']['responses']['200']['content']['application/json']['data']>
type SyncIndexData = NonNullable<operations['syncAiContextIndex']['responses']['200']['content']['application/json']['data']>
type QueryBody = NonNullable<operations['queryAiContext']['requestBody']>['content']['application/json']
type QueryData = NonNullable<operations['queryAiContext']['responses']['200']['content']['application/json']['data']>
type ListQueryLogsData = NonNullable<operations['listAiContextQueryLogs']['responses']['200']['content']['application/json']['data']>[number]
type ListQueryLogsQuery = NonNullable<operations['listAiContextQueryLogs']['parameters']['query']>

export function createAiContexts(client: ConjoinClient) {
  return {
    createIndex: (data: CreateIndexBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateIndexData>('ai/context/indexes', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listIndexes: (query?: ListIndexesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListIndexesData>('ai/context/indexes', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readIndex: (indexId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadIndexData>(`ai/context/indexes/${encodePathParam(indexId)}`, { ...options, method: 'GET' }),

    deleteIndex: (indexId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteIndexData>(`ai/context/indexes/${encodePathParam(indexId)}`, { ...options, method: 'DELETE' }),

    syncIndex: (indexId: string, options?: ConjoinCallOptions) =>
      client.fetch<SyncIndexData>(`ai/context/indexes/${encodePathParam(indexId)}/sync`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    query: (data: QueryBody, options?: ConjoinCallOptions) =>
      client.fetch<QueryData>('ai/context/query', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listQueryLogs: (query?: ListQueryLogsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListQueryLogsData>('ai/context/query-logs', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
