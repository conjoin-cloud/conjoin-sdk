import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListMembershipsData = NonNullable<operations['listMemberships']['responses']['200']['content']['application/json']['data']>[number]
type ListMembershipsQuery = NonNullable<operations['listMemberships']['parameters']['query']>
type CreateMembershipBody = NonNullable<operations['createMembership']['requestBody']>['content']['application/json']
type CreateMembershipData = NonNullable<operations['createMembership']['responses']['201']['content']['application/json']['data']>
type ListMembershipsCountData = NonNullable<operations['listMembershipsCount']['responses']['200']['content']['application/json']['data']>
type ListMembershipsCountQuery = NonNullable<operations['listMembershipsCount']['parameters']['query']>
type UpdateMembershipBody = NonNullable<operations['updateMembership']['requestBody']>['content']['application/json']
type UpdateMembershipData = NonNullable<operations['updateMembership']['responses']['200']['content']['application/json']['data']>
type DeleteMembershipData = NonNullable<operations['deleteMembership']['responses']['200']['content']['application/json']['data']>
type GrantOrgAccountRoleBody = NonNullable<operations['grantOrgAccountRole']['requestBody']>['content']['application/json']
type GrantOrgAccountRoleData = NonNullable<operations['grantOrgAccountRole']['responses']['200']['content']['application/json']['data']>
type RevokeOrgAccountRoleBody = NonNullable<operations['revokeOrgAccountRole']['requestBody']>['content']['application/json']
type RevokeOrgAccountRoleData = NonNullable<operations['revokeOrgAccountRole']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationMemberships(client: ConjoinClient) {
  return {
    listMemberships: (organizationId: string, query?: ListMembershipsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListMembershipsData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    createMembership: (organizationId: string, data: CreateMembershipBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateMembershipData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    listMembershipsCount: (organizationId: string, query?: ListMembershipsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListMembershipsCountData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    updateMembership: (organizationId: string, membershipId: string, data: UpdateMembershipBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateMembershipData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/${encodePathParam(membershipId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    deleteMembership: (organizationId: string, membershipId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteMembershipData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/${encodePathParam(membershipId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    grantOrgAccountRole: (organizationId: string, membershipId: string, data: GrantOrgAccountRoleBody, options?: ConjoinCallOptions) =>
      client.fetch<GrantOrgAccountRoleData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/${encodePathParam(membershipId)}/grant-role`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    revokeOrgAccountRole: (organizationId: string, membershipId: string, data: RevokeOrgAccountRoleBody, options?: ConjoinCallOptions) =>
      client.fetch<RevokeOrgAccountRoleData>(`auth/organizations/${encodePathParam(organizationId)}/memberships/${encodePathParam(membershipId)}/revoke-role`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
