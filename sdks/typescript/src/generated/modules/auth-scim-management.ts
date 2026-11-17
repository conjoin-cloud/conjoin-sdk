import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadScimSettingsData = NonNullable<operations['readScimSettings']['responses']['200']['content']['application/json']['data']>
type UpdateScimSettingsBody = NonNullable<operations['updateScimSettings']['requestBody']>['content']['application/json']
type UpdateScimSettingsData = NonNullable<operations['updateScimSettings']['responses']['200']['content']['application/json']['data']>
type SyncScimRolesForMemberData = NonNullable<operations['syncScimRolesForMember']['responses']['200']['content']['application/json']['data']>
type SyncScimRolesForGroupData = NonNullable<operations['syncScimRolesForGroup']['responses']['200']['content']['application/json']['data']>
type ReconcileScimUsersBody = NonNullable<operations['reconcileScimUsers']['requestBody']>['content']['application/json']
type ReconcileScimUsersData = NonNullable<operations['reconcileScimUsers']['responses']['200']['content']['application/json']['data']>
type ReconcileScimGroupsBody = NonNullable<operations['reconcileScimGroups']['requestBody']>['content']['application/json']
type ReconcileScimGroupsData = NonNullable<operations['reconcileScimGroups']['responses']['200']['content']['application/json']['data']>
type ReconcileScimGroupMembersBody = NonNullable<operations['reconcileScimGroupMembers']['requestBody']>['content']['application/json']
type ReconcileScimGroupMembersData = NonNullable<operations['reconcileScimGroupMembers']['responses']['200']['content']['application/json']['data']>

export function createAuthSCIMManagements(client: ConjoinClient) {
  return {
    readScimSettings: (organizationId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadScimSettingsData>(`auth/organizations/${encodePathParam(organizationId)}/scim-settings`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    updateScimSettings: (organizationId: string, data: UpdateScimSettingsBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateScimSettingsData>(`auth/organizations/${encodePathParam(organizationId)}/scim-settings`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    syncScimRolesForMember: (organizationId: string, membershipId: string, options?: ConjoinCallOptions) =>
      client.fetch<SyncScimRolesForMemberData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/${encodePathParam(membershipId)}/sync-scim-roles`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    syncScimRolesForGroup: (organizationId: string, groupId: string, options?: ConjoinCallOptions) =>
      client.fetch<SyncScimRolesForGroupData>(`auth/organizations/${encodePathParam(organizationId)}/groups/${encodePathParam(groupId)}/sync-scim-roles`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    reconcileScimUsers: (organizationId: string, data: ReconcileScimUsersBody, options?: ConjoinCallOptions) =>
      client.fetch<ReconcileScimUsersData>(`auth/organizations/${encodePathParam(organizationId)}/reconcile-scim-users`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    reconcileScimGroups: (organizationId: string, data: ReconcileScimGroupsBody, options?: ConjoinCallOptions) =>
      client.fetch<ReconcileScimGroupsData>(`auth/organizations/${encodePathParam(organizationId)}/reconcile-scim-groups`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    reconcileScimGroupMembers: (organizationId: string, data: ReconcileScimGroupMembersBody, options?: ConjoinCallOptions) =>
      client.fetch<ReconcileScimGroupMembersData>(`auth/organizations/${encodePathParam(organizationId)}/reconcile-scim-group-members`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
