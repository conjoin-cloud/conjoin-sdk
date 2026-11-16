import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateIndexBody = NonNullable<operations['createSearchIndex']['requestBody']>['content']['application/json']
type CreateIndexData = NonNullable<operations['createSearchIndex']['responses']['201']['content']['application/json']['data']>
type ReadIndexesData = NonNullable<operations['readSearchIndexes']['responses']['200']['content']['application/json']['data']>[number]
type ReadIndexesQuery = NonNullable<operations['readSearchIndexes']['parameters']['query']>
type DeleteIndexData = NonNullable<operations['deleteSearchIndex']['responses']['200']['content']['application/json']['data']>
type IndexDocumentBody = NonNullable<operations['indexSearchDocument']['requestBody']>['content']['application/json']
type IndexDocumentData = NonNullable<operations['indexSearchDocument']['responses']['201']['content']['application/json']['data']>
type IndexDocumentBatchBody = NonNullable<operations['indexSearchDocumentBatch']['requestBody']>['content']['application/json']
type IndexDocumentBatchData = NonNullable<operations['indexSearchDocumentBatch']['responses']['201']['content']['application/json']['data']>
type RemoveDocumentData = NonNullable<operations['removeSearchDocument']['responses']['200']['content']['application/json']['data']>
type SearchQueryBody = NonNullable<operations['searchQuery']['requestBody']>['content']['application/json']
type SearchQueryData = NonNullable<operations['searchQuery']['responses']['200']['content']['application/json']['data']>
type AutoSuggestBody = NonNullable<operations['autoSuggestSearch']['requestBody']>['content']['application/json']
type AutoSuggestData = NonNullable<operations['autoSuggestSearch']['responses']['200']['content']['application/json']['data']>

export function createRelaySearches(client: ConjoinClient) {
  return {
    createIndex: (data: CreateIndexBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateIndexData>('relay/search/indexes', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readIndexes: (query?: ReadIndexesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadIndexesData>('relay/search/indexes', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    deleteIndex: (indexId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteIndexData>(`relay/search/indexes/${encodePathParam(indexId)}`, { ...options, method: 'DELETE' }),

    indexDocument: (indexId: string, data: IndexDocumentBody, options?: ConjoinCallOptions) =>
      client.fetch<IndexDocumentData>(`relay/search/indexes/${encodePathParam(indexId)}/documents`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    indexDocumentBatch: (indexId: string, data: IndexDocumentBatchBody, options?: ConjoinCallOptions) =>
      client.fetch<IndexDocumentBatchData>(`relay/search/indexes/${encodePathParam(indexId)}/documents/batch`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    removeDocument: (indexId: string, documentId: string, options?: ConjoinCallOptions) =>
      client.fetch<RemoveDocumentData>(`relay/search/indexes/${encodePathParam(indexId)}/documents/${encodePathParam(documentId)}`, { ...options, method: 'DELETE' }),

    searchQuery: (indexId: string, data: SearchQueryBody, options?: ConjoinCallOptions) =>
      client.fetch<SearchQueryData>(`relay/search/indexes/${encodePathParam(indexId)}/query`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    autoSuggest: (indexId: string, data: AutoSuggestBody, options?: ConjoinCallOptions) =>
      client.fetch<AutoSuggestData>(`relay/search/indexes/${encodePathParam(indexId)}/suggest`, { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),
  }
}
