import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListOrgPermissionsData = NonNullable<operations['listOrgPermissions']['responses']['200']['content']['application/json']['data']>[number]
type ListOrgPermissionsQuery = NonNullable<operations['listOrgPermissions']['parameters']['query']>
type CreateOrgPermissionBody = NonNullable<operations['createOrgPermission']['requestBody']>['content']['application/json']
type CreateOrgPermissionData = NonNullable<operations['createOrgPermission']['responses']['201']['content']['application/json']['data']>
type ListOrgPermissionsCountData = NonNullable<operations['listOrgPermissionsCount']['responses']['200']['content']['application/json']['data']>
type ListOrgPermissionsCountQuery = NonNullable<operations['listOrgPermissionsCount']['parameters']['query']>
type ReadOrgPermissionData = NonNullable<operations['readOrgPermission']['responses']['200']['content']['application/json']['data']>
type UpdateOrgPermissionBody = NonNullable<operations['updateOrgPermission']['requestBody']>['content']['application/json']
type UpdateOrgPermissionData = NonNullable<operations['updateOrgPermission']['responses']['200']['content']['application/json']['data']>
type DeleteOrgPermissionData = NonNullable<operations['deleteOrgPermission']['responses']['200']['content']['application/json']['data']>
type ArchiveOrgPermissionData = NonNullable<operations['archiveOrgPermission']['responses']['200']['content']['application/json']['data']>
type RestoreOrgPermissionData = NonNullable<operations['restoreOrgPermission']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationPermissions(client: ConjoinClient) {
  return {
    listOrgPermissions: (organizationId: string, query?: ListOrgPermissionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListOrgPermissionsData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    createOrgPermission: (organizationId: string, data: CreateOrgPermissionBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateOrgPermissionData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listOrgPermissionsCount: (organizationId: string, query?: ListOrgPermissionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListOrgPermissionsCountData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    readOrgPermission: (organizationId: string, permissionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadOrgPermissionData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/${encodePathParam(permissionId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    updateOrgPermission: (organizationId: string, permissionId: string, data: UpdateOrgPermissionBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateOrgPermissionData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/${encodePathParam(permissionId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    deleteOrgPermission: (organizationId: string, permissionId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteOrgPermissionData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/${encodePathParam(permissionId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    archiveOrgPermission: (organizationId: string, permissionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveOrgPermissionData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/${encodePathParam(permissionId)}/archive`, { ...options, method: 'POST', scopes: ['authAppId'] }),

    restoreOrgPermission: (organizationId: string, permissionId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreOrgPermissionData>(`auth/organizations/${encodePathParam(organizationId)}/permissions/${encodePathParam(permissionId)}/restore`, { ...options, method: 'POST', scopes: ['authAppId'] }),
  }
}
