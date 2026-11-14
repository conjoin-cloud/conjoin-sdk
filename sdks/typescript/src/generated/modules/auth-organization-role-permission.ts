import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListOrgRolePermissionsData = NonNullable<operations['listOrgRolePermissions']['responses']['200']['content']['application/json']['data']>[number]
type ListOrgRolePermissionsQuery = NonNullable<operations['listOrgRolePermissions']['parameters']['query']>
type ListOrgRolePermissionsCountData = NonNullable<operations['listOrgRolePermissionsCount']['responses']['200']['content']['application/json']['data']>
type ListOrgRolePermissionsCountQuery = NonNullable<operations['listOrgRolePermissionsCount']['parameters']['query']>
type AssignOrgRolePermissionBody = NonNullable<operations['assignOrgRolePermission']['requestBody']>['content']['application/json']
type AssignOrgRolePermissionData = NonNullable<operations['assignOrgRolePermission']['responses']['201']['content']['application/json']['data']>
type RemoveRolePermissionBody = NonNullable<operations['removeRolePermission']['requestBody']>['content']['application/json']
type RemoveRolePermissionData = NonNullable<operations['removeRolePermission']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationRolePermissions(client: ConjoinClient) {
  return {
    listOrgRolePermissions: (roleId: string, query?: ListOrgRolePermissionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListOrgRolePermissionsData>(`auth/roles/${encodePathParam(roleId)}/permissions`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listOrgRolePermissionsCount: (roleId: string, query?: ListOrgRolePermissionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListOrgRolePermissionsCountData>(`auth/roles/${encodePathParam(roleId)}/permissions/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    assignOrgRolePermission: (organizationId: string, roleId: string, data: AssignOrgRolePermissionBody, options?: ConjoinCallOptions) =>
      client.fetch<AssignOrgRolePermissionData>(`auth/organizations/${encodePathParam(organizationId)}/roles/${encodePathParam(roleId)}/assign-permissions`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    removeRolePermission: (organizationId: string, roleId: string, data: RemoveRolePermissionBody, options?: ConjoinCallOptions) =>
      client.fetch<RemoveRolePermissionData>(`auth/organizations/${encodePathParam(organizationId)}/roles/${encodePathParam(roleId)}/remove-permissions`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),
  }
}
