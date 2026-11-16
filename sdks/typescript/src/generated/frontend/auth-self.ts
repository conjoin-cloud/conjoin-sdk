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
    listOrganizations: (query?: ListOrganizationsQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetchList<ListOrganizationsData>('auth/self/organizations', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined }),

    listSessions: (query?: ListSessionsQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetchList<ListSessionsData>('auth/self/sessions', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readProfile: (sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadProfileData>('auth/self/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET' }),

    updateProfile: (data: UpdateProfileBody, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<UpdateProfileData>('auth/self/', { ...options, auth: { type: 'session', token: sessionToken }, method: 'PATCH', body: data }),

    listSessionsCount: (query?: ListSessionsCountQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ListSessionsCountData>('auth/self/sessions/count', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined }),

    revokeSession: (sessionId: string, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeSessionData>(`auth/self/sessions/${encodePathParam(sessionId)}`, { ...options, auth: { type: 'session', token: sessionToken }, method: 'DELETE' }),

    listOrganizationsCount: (query?: ListOrganizationsCountQuery, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ListOrganizationsCountData>('auth/self/organizations/count', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readActiveOrganization: (sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadActiveOrganizationData>('auth/self/active-organization', { ...options, auth: { type: 'session', token: sessionToken }, method: 'GET' }),

    updateActiveOrganization: (data: UpdateActiveOrganizationBody, sessionToken?: string, options?: ConjoinCallOptions) =>
      client.fetch<UpdateActiveOrganizationData>('auth/self/active-organization', { ...options, auth: { type: 'session', token: sessionToken }, method: 'PATCH', body: data }),
  }
}
