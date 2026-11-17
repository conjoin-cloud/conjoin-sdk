import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadLogsData = NonNullable<operations['readAuditLogs']['responses']['200']['content']['application/json']['data']>[number]
type ReadLogsQuery = NonNullable<operations['readAuditLogs']['parameters']['query']>
type ReadLogsCountData = NonNullable<operations['readAuditLogsCount']['responses']['200']['content']['application/json']['data']>
type ReadLogsCountQuery = NonNullable<operations['readAuditLogsCount']['parameters']['query']>
type ReadStatsData = NonNullable<operations['readAuditStats']['responses']['200']['content']['application/json']['data']>
type ReadStatsQuery = NonNullable<operations['readAuditStats']['parameters']['query']>

export function createCloudAudits(client: ConjoinClient) {
  return {
    readLogs: (query?: ReadLogsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadLogsData>('cloud/audit-logs/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readLogsCount: (query?: ReadLogsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadLogsCountData>('cloud/audit-logs/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readStats: (query: ReadStatsQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadStatsData>('cloud/audit-logs/stats', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
