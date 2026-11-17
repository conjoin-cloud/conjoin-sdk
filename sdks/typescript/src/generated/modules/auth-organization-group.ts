import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListGroupsData = NonNullable<operations['listGroups']['responses']['200']['content']['application/json']['data']>[number]
type ListGroupsQuery = NonNullable<operations['listGroups']['parameters']['query']>
type CreateGroupBody = NonNullable<operations['createGroup']['requestBody']>['content']['application/json']
type CreateGroupData = NonNullable<operations['createGroup']['responses']['201']['content']['application/json']['data']>
type ListGroupMembersData = NonNullable<operations['listGroupMembers']['responses']['200']['content']['application/json']['data']>[number]
type ListGroupMembersQuery = NonNullable<operations['listGroupMembers']['parameters']['query']>
type ListGroupMembersCountData = NonNullable<operations['listGroupMembersCount']['responses']['200']['content']['application/json']['data']>
type ListGroupMembersCountQuery = NonNullable<operations['listGroupMembersCount']['parameters']['query']>
type ListGroupsCountData = NonNullable<operations['listGroupsCount']['responses']['200']['content']['application/json']['data']>
type ListGroupsCountQuery = NonNullable<operations['listGroupsCount']['parameters']['query']>
type UpdateGroupBody = NonNullable<operations['updateGroup']['requestBody']>['content']['application/json']
type UpdateGroupData = NonNullable<operations['updateGroup']['responses']['200']['content']['application/json']['data']>
type DeleteGroupData = NonNullable<operations['deleteGroup']['responses']['200']['content']['application/json']['data']>
type AddGroupMemberBody = NonNullable<operations['addGroupMember']['requestBody']>['content']['application/json']
type AddGroupMemberData = NonNullable<operations['addGroupMember']['responses']['200']['content']['application/json']['data']>
type RemoveGroupMemberBody = NonNullable<operations['removeGroupMember']['requestBody']>['content']['application/json']
type RemoveGroupMemberData = NonNullable<operations['removeGroupMember']['responses']['200']['content']['application/json']['data']>
type BulkSyncGroupMembersBody = NonNullable<operations['bulkSyncGroupMembers']['requestBody']>['content']['application/json']
type BulkSyncGroupMembersData = NonNullable<operations['bulkSyncGroupMembers']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationGroups(client: ConjoinClient) {
  return {
    listGroups: (organizationId: string, query?: ListGroupsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListGroupsData>(`auth/organizations/${encodePathParam(organizationId)}/groups/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    createGroup: (organizationId: string, data: CreateGroupBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateGroupData>(`auth/organizations/${encodePathParam(organizationId)}/groups/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    listGroupMembers: (groupId: string, query?: ListGroupMembersQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListGroupMembersData>(`auth/groups/${encodePathParam(groupId)}/members`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listGroupMembersCount: (groupId: string, query?: ListGroupMembersCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListGroupMembersCountData>(`auth/groups/${encodePathParam(groupId)}/members/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listGroupsCount: (organizationId: string, query?: ListGroupsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListGroupsCountData>(`auth/organizations/${encodePathParam(organizationId)}/groups/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    updateGroup: (organizationId: string, groupId: string, data: UpdateGroupBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateGroupData>(`auth/organizations/${encodePathParam(organizationId)}/groups/${encodePathParam(groupId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    deleteGroup: (organizationId: string, groupId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteGroupData>(`auth/organizations/${encodePathParam(organizationId)}/groups/${encodePathParam(groupId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    addGroupMember: (organizationId: string, groupId: string, data: AddGroupMemberBody, options?: ConjoinCallOptions) =>
      client.fetch<AddGroupMemberData>(`auth/organizations/${encodePathParam(organizationId)}/groups/${encodePathParam(groupId)}/add-members`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    removeGroupMember: (organizationId: string, groupId: string, data: RemoveGroupMemberBody, options?: ConjoinCallOptions) =>
      client.fetch<RemoveGroupMemberData>(`auth/organizations/${encodePathParam(organizationId)}/groups/${encodePathParam(groupId)}/remove-members`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    bulkSyncGroupMembers: (organizationId: string, groupId: string, data: BulkSyncGroupMembersBody, options?: ConjoinCallOptions) =>
      client.fetch<BulkSyncGroupMembersData>(`auth/organizations/${encodePathParam(organizationId)}/groups/${encodePathParam(groupId)}/sync-members`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
