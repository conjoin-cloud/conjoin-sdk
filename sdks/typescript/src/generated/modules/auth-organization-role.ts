import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListOrgRolesData = NonNullable<operations['listOrgRoles']['responses']['200']['content']['application/json']['data']>[number]
type ListOrgRolesQuery = NonNullable<operations['listOrgRoles']['parameters']['query']>
type CreateOrgRoleBody = NonNullable<operations['createOrgRole']['requestBody']>['content']['application/json']
type CreateOrgRoleData = NonNullable<operations['createOrgRole']['responses']['201']['content']['application/json']['data']>
type ListOrgRolesCountData = NonNullable<operations['listOrgRolesCount']['responses']['200']['content']['application/json']['data']>
type ListOrgRolesCountQuery = NonNullable<operations['listOrgRolesCount']['parameters']['query']>
type ReadOrgRoleData = NonNullable<operations['readOrgRole']['responses']['200']['content']['application/json']['data']>
type UpdateOrgRoleBody = NonNullable<operations['updateOrgRole']['requestBody']>['content']['application/json']
type UpdateOrgRoleData = NonNullable<operations['updateOrgRole']['responses']['200']['content']['application/json']['data']>
type DeleteOrgRoleData = NonNullable<operations['deleteOrgRole']['responses']['200']['content']['application/json']['data']>
type ArchiveOrgRoleData = NonNullable<operations['archiveOrgRole']['responses']['200']['content']['application/json']['data']>
type RestoreOrgRoleData = NonNullable<operations['restoreOrgRole']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationRoles(client: ConjoinClient) {
  return {
    listOrgRoles: (organizationId: string, query?: ListOrgRolesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListOrgRolesData>(`auth/organizations/${encodePathParam(organizationId)}/roles/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    createOrgRole: (organizationId: string, data: CreateOrgRoleBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateOrgRoleData>(`auth/organizations/${encodePathParam(organizationId)}/roles/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listOrgRolesCount: (organizationId: string, query?: ListOrgRolesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListOrgRolesCountData>(`auth/organizations/${encodePathParam(organizationId)}/roles/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    readOrgRole: (organizationId: string, roleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadOrgRoleData>(`auth/organizations/${encodePathParam(organizationId)}/roles/${encodePathParam(roleId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    updateOrgRole: (organizationId: string, roleId: string, data: UpdateOrgRoleBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateOrgRoleData>(`auth/organizations/${encodePathParam(organizationId)}/roles/${encodePathParam(roleId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    deleteOrgRole: (organizationId: string, roleId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteOrgRoleData>(`auth/organizations/${encodePathParam(organizationId)}/roles/${encodePathParam(roleId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    archiveOrgRole: (organizationId: string, roleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveOrgRoleData>(`auth/organizations/${encodePathParam(organizationId)}/roles/${encodePathParam(roleId)}/archive`, { ...options, method: 'POST', scopes: ['authAppId'] }),

    restoreOrgRole: (organizationId: string, roleId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreOrgRoleData>(`auth/organizations/${encodePathParam(organizationId)}/roles/${encodePathParam(roleId)}/restore`, { ...options, method: 'POST', scopes: ['authAppId'] }),
  }
}
