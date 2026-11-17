import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListIndexesData = NonNullable<operations['listAiContextIndexes']['responses']['200']['content']['application/json']['data']>[number]
type ListIndexesQuery = NonNullable<operations['listAiContextIndexes']['parameters']['query']>
type CreateIndexBody = NonNullable<operations['createAiContextIndex']['requestBody']>['content']['application/json']
type CreateIndexData = NonNullable<operations['createAiContextIndex']['responses']['201']['content']['application/json']['data']>
type ListIndexesCountData = NonNullable<operations['listAiContextIndexesCount']['responses']['200']['content']['application/json']['data']>
type ListIndexesCountQuery = NonNullable<operations['listAiContextIndexesCount']['parameters']['query']>
type ReadIndexData = NonNullable<operations['readAiContextIndex']['responses']['200']['content']['application/json']['data']>
type DeleteIndexData = NonNullable<operations['deleteAiContextIndex']['responses']['200']['content']['application/json']['data']>
type SyncIndexData = NonNullable<operations['syncAiContextIndex']['responses']['200']['content']['application/json']['data']>
type ListQueriesData = NonNullable<operations['listAiContextQueries']['responses']['200']['content']['application/json']['data']>[number]
type ListQueriesQuery = NonNullable<operations['listAiContextQueries']['parameters']['query']>
type CreateQueryBody = NonNullable<operations['createAiContextQuery']['requestBody']>['content']['application/json']
type CreateQueryData = NonNullable<operations['createAiContextQuery']['responses']['200']['content']['application/json']['data']>
type ListQueriesCountData = NonNullable<operations['listAiContextQueriesCount']['responses']['200']['content']['application/json']['data']>
type ListQueriesCountQuery = NonNullable<operations['listAiContextQueriesCount']['parameters']['query']>

export function createAiContexts(client: ConjoinClient) {
  return {
    listIndexes: (query?: ListIndexesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListIndexesData>('ai/context-indexes/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createIndex: (data: CreateIndexBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateIndexData>('ai/context-indexes/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listIndexesCount: (query?: ListIndexesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListIndexesCountData>('ai/context-indexes/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readIndex: (contextIndexId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadIndexData>(`ai/context-indexes/${encodePathParam(contextIndexId)}`, { ...options, method: 'GET' }),

    deleteIndex: (contextIndexId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteIndexData>(`ai/context-indexes/${encodePathParam(contextIndexId)}`, { ...options, method: 'DELETE' }),

    syncIndex: (contextIndexId: string, options?: ConjoinCallOptions) =>
      client.fetch<SyncIndexData>(`ai/context-indexes/${encodePathParam(contextIndexId)}/sync`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),

    listQueries: (query?: ListQueriesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListQueriesData>('ai/context-queries/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createQuery: (data: CreateQueryBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateQueryData>('ai/context-queries/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listQueriesCount: (query?: ListQueriesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListQueriesCountData>('ai/context-queries/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
