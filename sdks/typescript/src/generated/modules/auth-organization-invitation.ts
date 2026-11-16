import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListInvitationsData = NonNullable<operations['listInvitations']['responses']['200']['content']['application/json']['data']>[number]
type ListInvitationsQuery = NonNullable<operations['listInvitations']['parameters']['query']>
type CreateInvitationBody = NonNullable<operations['createInvitation']['requestBody']>['content']['application/json']
type CreateInvitationData = NonNullable<operations['createInvitation']['responses']['201']['content']['application/json']['data']>
type ListInvitationsCountData = NonNullable<operations['listInvitationsCount']['responses']['200']['content']['application/json']['data']>
type ListInvitationsCountQuery = NonNullable<operations['listInvitationsCount']['parameters']['query']>
type RevokeInvitationData = NonNullable<operations['revokeInvitation']['responses']['200']['content']['application/json']['data']>
type ResendInvitationBody = NonNullable<operations['resendInvitation']['requestBody']>['content']['application/json']
type ResendInvitationData = NonNullable<operations['resendInvitation']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationInvitations(client: ConjoinClient) {
  return {
    listInvitations: (organizationId: string, query?: ListInvitationsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListInvitationsData>(`auth/organizations/${encodePathParam(organizationId)}/invitations/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    createInvitation: (organizationId: string, data: CreateInvitationBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateInvitationData>(`auth/organizations/${encodePathParam(organizationId)}/invitations/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    listInvitationsCount: (organizationId: string, query?: ListInvitationsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListInvitationsCountData>(`auth/organizations/${encodePathParam(organizationId)}/invitations/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    revokeInvitation: (organizationId: string, invitationId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeInvitationData>(`auth/organizations/${encodePathParam(organizationId)}/invitations/${encodePathParam(invitationId)}/revoke`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    resendInvitation: (organizationId: string, invitationId: string, data: ResendInvitationBody, options?: ConjoinCallOptions) =>
      client.fetch<ResendInvitationData>(`auth/organizations/${encodePathParam(organizationId)}/invitations/${encodePathParam(invitationId)}/resend`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
