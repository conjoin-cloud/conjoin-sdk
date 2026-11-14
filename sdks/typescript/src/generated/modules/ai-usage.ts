import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListRecordsData = NonNullable<operations['listAiUsageRecords']['responses']['200']['content']['application/json']['data']>[number]
type ListRecordsQuery = NonNullable<operations['listAiUsageRecords']['parameters']['query']>
type ReadSummaryData = NonNullable<operations['readAiUsageSummary']['responses']['200']['content']['application/json']['data']>
type ReadSummaryQuery = NonNullable<operations['readAiUsageSummary']['parameters']['query']>

export function createAiUsages(client: ConjoinClient) {
  return {
    listRecords: (query?: ListRecordsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListRecordsData>('ai/usage/records', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readSummary: (query?: ReadSummaryQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadSummaryData>('ai/usage/summary', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
