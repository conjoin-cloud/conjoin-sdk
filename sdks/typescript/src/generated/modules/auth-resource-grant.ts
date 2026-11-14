import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listResourceGrants']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listResourceGrants']['parameters']['query']>
type GrantResourcePermissionBody = NonNullable<operations['grantResourcePermission']['requestBody']>['content']['application/json']
type GrantResourcePermissionData = NonNullable<operations['grantResourcePermission']['responses']['201']['content']['application/json']['data']>
type CheckResourcePermissionBody = NonNullable<operations['checkResourcePermission']['requestBody']>['content']['application/json']
type CheckResourcePermissionData = NonNullable<operations['checkResourcePermission']['responses']['200']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listResourceGrantsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listResourceGrantsCount']['parameters']['query']>
type RevokeResourcePermissionBody = NonNullable<operations['revokeResourcePermission']['requestBody']>['content']['application/json']
type RevokeResourcePermissionData = NonNullable<operations['revokeResourcePermission']['responses']['200']['content']['application/json']['data']>

export function createAuthResourceGrants(client: ConjoinClient) {
  return {
    list: (organizationId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`auth/organizations/${encodePathParam(organizationId)}/resource-grants/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    grantResourcePermission: (organizationId: string, data: GrantResourcePermissionBody, options?: ConjoinCallOptions) =>
      client.fetch<GrantResourcePermissionData>(`auth/organizations/${encodePathParam(organizationId)}/resource-grants/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    checkResourcePermission: (organizationId: string, data: CheckResourcePermissionBody, options?: ConjoinCallOptions) =>
      client.fetch<CheckResourcePermissionData>(`auth/organizations/${encodePathParam(organizationId)}/check-resource-permission`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listCount: (organizationId: string, query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>(`auth/organizations/${encodePathParam(organizationId)}/resource-grants/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    revokeResourcePermission: (organizationId: string, resourceGrantId: string, data: RevokeResourcePermissionBody, options?: ConjoinCallOptions) =>
      client.fetch<RevokeResourcePermissionData>(`auth/organizations/${encodePathParam(organizationId)}/resource-grants/${encodePathParam(resourceGrantId)}/revoke`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),
  }
}
