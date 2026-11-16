import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadSsoPortalSettingsData = NonNullable<operations['readSsoPortalSettings']['responses']['200']['content']['application/json']['data']>
type UpdateSsoPortalSettingsBody = NonNullable<operations['updateSsoPortalSettings']['requestBody']>['content']['application/json']
type UpdateSsoPortalSettingsData = NonNullable<operations['updateSsoPortalSettings']['responses']['200']['content']['application/json']['data']>
type MintSsoPortalTicketBody = NonNullable<operations['mintSsoPortalTicket']['requestBody']>['content']['application/json']
type MintSsoPortalTicketData = NonNullable<operations['mintSsoPortalTicket']['responses']['201']['content']['application/json']['data']>
type RevokeSsoPortalTicketData = NonNullable<operations['revokeSsoPortalTicket']['responses']['200']['content']['application/json']['data']>

export function createAuthSSOPortals(client: ConjoinClient) {
  return {
    readSsoPortalSettings: (options?: ConjoinCallOptions) =>
      client.fetch<ReadSsoPortalSettingsData>('auth/portal/settings', { ...options, method: 'GET', scopes: ['authAppId'] }),

    updateSsoPortalSettings: (data: UpdateSsoPortalSettingsBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSsoPortalSettingsData>('auth/portal/settings', { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    mintSsoPortalTicket: (organizationId: string, data: MintSsoPortalTicketBody, options?: ConjoinCallOptions) =>
      client.fetch<MintSsoPortalTicketData>(`auth/organizations/${encodePathParam(organizationId)}/portal-tickets/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    revokeSsoPortalTicket: (organizationId: string, portalTicketId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeSsoPortalTicketData>(`auth/organizations/${encodePathParam(organizationId)}/portal-tickets/${encodePathParam(portalTicketId)}/revoke`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
