import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listAuthOrganizations']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAuthOrganizations']['parameters']['query']>
type CreateBody = NonNullable<operations['createAuthOrganization']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createAuthOrganization']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listAuthOrganizationsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listAuthOrganizationsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readAuthOrganization']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateAuthOrganization']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateAuthOrganization']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteAuthOrganization']['responses']['200']['content']['application/json']['data']>
type UpdateSettingsBody = NonNullable<operations['updateAuthOrganizationSettings']['requestBody']>['content']['application/json']
type UpdateSettingsData = NonNullable<operations['updateAuthOrganizationSettings']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizations(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('auth/organizations/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('auth/organizations/', { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('auth/organizations/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    read: (organizationId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`auth/organizations/${encodePathParam(organizationId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    update: (organizationId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`auth/organizations/${encodePathParam(organizationId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    delete: (organizationId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`auth/organizations/${encodePathParam(organizationId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    updateSettings: (organizationId: string, data: UpdateSettingsBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSettingsData>(`auth/organizations/${encodePathParam(organizationId)}/settings`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),
  }
}
