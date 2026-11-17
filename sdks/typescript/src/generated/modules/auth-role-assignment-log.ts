import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listRoleAssignmentLogs']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listRoleAssignmentLogs']['parameters']['query']>
type ListCountData = NonNullable<operations['listRoleAssignmentLogsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listRoleAssignmentLogsCount']['parameters']['query']>

export function createAuthRoleAssignmentLogs(client: ConjoinClient) {
  return {
    list: (organizationId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`auth/organizations/${encodePathParam(organizationId)}/role-assignment-logs/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listCount: (organizationId: string, query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>(`auth/organizations/${encodePathParam(organizationId)}/role-assignment-logs/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),
  }
}
