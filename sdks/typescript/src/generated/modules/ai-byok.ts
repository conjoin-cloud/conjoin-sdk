import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListByokConfigsData = NonNullable<operations['listAiByokConfigs']['responses']['200']['content']['application/json']['data']>[number]
type ListByokConfigsQuery = NonNullable<operations['listAiByokConfigs']['parameters']['query']>
type CreateByokConfigBody = NonNullable<operations['createAiByokConfig']['requestBody']>['content']['application/json']
type CreateByokConfigData = NonNullable<operations['createAiByokConfig']['responses']['201']['content']['application/json']['data']>
type ListByokConfigsCountData = NonNullable<operations['listAiByokConfigsCount']['responses']['200']['content']['application/json']['data']>
type ListByokConfigsCountQuery = NonNullable<operations['listAiByokConfigsCount']['parameters']['query']>
type ReadByokConfigData = NonNullable<operations['readAiByokConfig']['responses']['200']['content']['application/json']['data']>
type UpdateByokConfigBody = NonNullable<operations['updateAiByokConfig']['requestBody']>['content']['application/json']
type UpdateByokConfigData = NonNullable<operations['updateAiByokConfig']['responses']['200']['content']['application/json']['data']>
type DeleteByokConfigData = NonNullable<operations['deleteAiByokConfig']['responses']['200']['content']['application/json']['data']>
type TestByokConnectionData = NonNullable<operations['testAiByokConnection']['responses']['200']['content']['application/json']['data']>

export function createAiBYOKs(client: ConjoinClient) {
  return {
    listByokConfigs: (query?: ListByokConfigsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListByokConfigsData>('ai/byok-configs/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createByokConfig: (data: CreateByokConfigBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateByokConfigData>('ai/byok-configs/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listByokConfigsCount: (query?: ListByokConfigsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListByokConfigsCountData>('ai/byok-configs/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readByokConfig: (byokConfigId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadByokConfigData>(`ai/byok-configs/${encodePathParam(byokConfigId)}`, { ...options, method: 'GET' }),

    updateByokConfig: (byokConfigId: string, data: UpdateByokConfigBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateByokConfigData>(`ai/byok-configs/${encodePathParam(byokConfigId)}`, { ...options, method: 'PATCH', body: data }),

    deleteByokConfig: (byokConfigId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteByokConfigData>(`ai/byok-configs/${encodePathParam(byokConfigId)}`, { ...options, method: 'DELETE' }),

    testByokConnection: (byokConfigId: string, options?: ConjoinCallOptions) =>
      client.fetch<TestByokConnectionData>(`ai/byok-configs/${encodePathParam(byokConfigId)}/test`, { ...options, method: 'POST', acceptsIdempotencyKey: true }),
  }
}
