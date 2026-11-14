import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listAiModels']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAiModels']['parameters']['query']>
type ReadData = NonNullable<operations['readAiModel']['responses']['200']['content']['application/json']['data']>

export function createAiModels(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('ai/model/models', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (modelId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`ai/model/models/${encodePathParam(modelId)}`, { ...options, method: 'GET' }),
  }
}
