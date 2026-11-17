import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadAccountData = NonNullable<operations['readAccountPlan']['responses']['200']['content']['application/json']['data']>
type ListData = NonNullable<operations['readCloudPlans']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['readCloudPlans']['parameters']['query']>
type ReadCountData = NonNullable<operations['readCloudPlansCount']['responses']['200']['content']['application/json']['data']>
type ReadCountQuery = NonNullable<operations['readCloudPlansCount']['parameters']['query']>
type ReadData = NonNullable<operations['readCloudPlan']['responses']['200']['content']['application/json']['data']>

export function createCloudPlans(client: ConjoinClient) {
  return {
    readAccount: (options?: ConjoinCallOptions) =>
      client.fetch<ReadAccountData>('cloud/account/plan', { ...options, method: 'GET' }),

    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('cloud/plans/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readCount: (query?: ReadCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadCountData>('cloud/plans/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (planId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`cloud/plans/${encodePathParam(planId)}`, { ...options, method: 'GET' }),
  }
}
