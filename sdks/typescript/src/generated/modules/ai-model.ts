import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listAiModels']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAiModels']['parameters']['query']>
type ListCountData = NonNullable<operations['listAiModelsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listAiModelsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readAiModel']['responses']['200']['content']['application/json']['data']>

export function createAiModels(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('ai/models/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('ai/models/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (modelId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`ai/models/${encodePathParam(modelId)}`, { ...options, method: 'GET' }),
  }
}
