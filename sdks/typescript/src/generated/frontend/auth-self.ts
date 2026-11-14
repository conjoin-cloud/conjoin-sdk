import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ListOrganizationsData = NonNullable<operations['listSelfOrganizations']['responses']['200']['content']['application/json']['data']>[number]
type ListOrganizationsQuery = NonNullable<operations['listSelfOrganizations']['parameters']['query']>
type ListSessionsData = NonNullable<operations['listSelfSessions']['responses']['200']['content']['application/json']['data']>[number]
type ListSessionsQuery = NonNullable<operations['listSelfSessions']['parameters']['query']>
type ReadProfileData = NonNullable<operations['readSelfProfile']['responses']['200']['content']['application/json']['data']>
type UpdateProfileBody = NonNullable<operations['updateSelfProfile']['requestBody']>['content']['application/json']
type UpdateProfileData = NonNullable<operations['updateSelfProfile']['responses']['200']['content']['application/json']['data']>
type ListSessionsCountData = NonNullable<operations['listSelfSessionsCount']['responses']['200']['content']['application/json']['data']>
type ListSessionsCountQuery = NonNullable<operations['listSelfSessionsCount']['parameters']['query']>
type RevokeSessionData = NonNullable<operations['revokeSelfSession']['responses']['200']['content']['application/json']['data']>
type ListOrganizationsCountData = NonNullable<operations['listSelfOrganizationsCount']['responses']['200']['content']['application/json']['data']>
type ListOrganizationsCountQuery = NonNullable<operations['listSelfOrganizationsCount']['parameters']['query']>
type ReadActiveOrganizationData = NonNullable<operations['readSelfActiveOrganization']['responses']['200']['content']['application/json']['data']>
type UpdateActiveOrganizationBody = NonNullable<operations['updateSelfActiveOrganization']['requestBody']>['content']['application/json']
type UpdateActiveOrganizationData = NonNullable<operations['updateSelfActiveOrganization']['responses']['200']['content']['application/json']['data']>

export function createAuthSelves(client: ConjoinClient) {
  return {
    listOrganizations: (query?: ListOrganizationsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListOrganizationsData>('auth/self/organizations', { auth: { type: 'none' }, ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    listSessions: (query?: ListSessionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListSessionsData>('auth/self/sessions', { auth: { type: 'none' }, ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readProfile: (options?: ConjoinCallOptions) =>
      client.fetch<ReadProfileData>('auth/self/', { auth: { type: 'none' }, ...options, method: 'GET' }),

    updateProfile: (data: UpdateProfileBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateProfileData>('auth/self/', { auth: { type: 'none' }, ...options, method: 'PATCH', body: data }),

    listSessionsCount: (query?: ListSessionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListSessionsCountData>('auth/self/sessions/count', { auth: { type: 'none' }, ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    revokeSession: (sessionId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeSessionData>(`auth/self/sessions/${encodePathParam(sessionId)}`, { auth: { type: 'none' }, ...options, method: 'DELETE' }),

    listOrganizationsCount: (query?: ListOrganizationsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListOrganizationsCountData>('auth/self/organizations/count', { auth: { type: 'none' }, ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readActiveOrganization: (options?: ConjoinCallOptions) =>
      client.fetch<ReadActiveOrganizationData>('auth/self/active-organization', { auth: { type: 'none' }, ...options, method: 'GET' }),

    updateActiveOrganization: (data: UpdateActiveOrganizationBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateActiveOrganizationData>('auth/self/active-organization', { auth: { type: 'none' }, ...options, method: 'PATCH', body: data }),
  }
}
