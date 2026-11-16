import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type AuthorizeActionBody = NonNullable<operations['authorizeAction']['requestBody']>['content']['application/json']
type AuthorizeActionData = NonNullable<operations['authorizeAction']['responses']['200']['content']['application/json']['data']>
type CheckRoleBody = NonNullable<operations['checkRole']['requestBody']>['content']['application/json']
type CheckRoleData = NonNullable<operations['checkRole']['responses']['200']['content']['application/json']['data']>
type ReadEffectivePermissionsData = NonNullable<operations['readEffectivePermissions']['responses']['200']['content']['application/json']['data']>
type ReadEffectivePermissionsQuery = NonNullable<operations['readEffectivePermissions']['parameters']['query']>

export function createAuthAuthorizations(client: ConjoinClient) {
  return {
    authorizeAction: (organizationId: string, data: AuthorizeActionBody, options?: ConjoinCallOptions) =>
      client.fetch<AuthorizeActionData>(`auth/organizations/${encodePathParam(organizationId)}/authorize`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    checkRole: (organizationId: string, data: CheckRoleBody, options?: ConjoinCallOptions) =>
      client.fetch<CheckRoleData>(`auth/organizations/${encodePathParam(organizationId)}/check-role`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    readEffectivePermissions: (organizationId: string, query: ReadEffectivePermissionsQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadEffectivePermissionsData>(`auth/organizations/${encodePathParam(organizationId)}/effective-permissions`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),
  }
}
