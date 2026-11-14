import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['readCloudProjects']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['readCloudProjects']['parameters']['query']>
type CreateBody = NonNullable<operations['createCloudProject']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCloudProject']['responses']['201']['content']['application/json']['data']>
type ReadCountData = NonNullable<operations['readCloudProjectsCount']['responses']['200']['content']['application/json']['data']>
type ReadCountQuery = NonNullable<operations['readCloudProjectsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readCloudProject']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateCloudProject']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCloudProject']['responses']['200']['content']['application/json']['data']>

export function createCloudProjects(client: ConjoinClient) {
  return {
    list: (organizationId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`cloud/organizations/${encodePathParam(organizationId)}/projects/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (organizationId: string, data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>(`cloud/organizations/${encodePathParam(organizationId)}/projects/`, { ...options, method: 'POST', body: data }),

    readCount: (organizationId: string, query?: ReadCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadCountData>(`cloud/organizations/${encodePathParam(organizationId)}/projects/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (projectId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`cloud/projects/${encodePathParam(projectId)}`, { ...options, method: 'GET' }),

    update: (projectId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`cloud/projects/${encodePathParam(projectId)}`, { ...options, method: 'PATCH', body: data }),
  }
}
