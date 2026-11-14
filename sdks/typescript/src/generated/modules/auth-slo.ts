import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type OidcLogoutBody = NonNullable<operations['oidcLogout']['requestBody']>['content']['application/json']
type OidcLogoutData = NonNullable<operations['oidcLogout']['responses']['200']['content']['application/json']['data']>
type SamlSpLogoutBody = NonNullable<operations['samlSpLogout']['requestBody']>['content']['application/json']
type SamlSpLogoutData = NonNullable<operations['samlSpLogout']['responses']['200']['content']['application/json']['data']>
type SamlIdpLogoutBody = NonNullable<operations['samlIdpLogout']['requestBody']>['content']['application/json']
type SamlIdpLogoutData = NonNullable<operations['samlIdpLogout']['responses']['200']['content']['application/json']['data']>

export function createAuthSLOs(client: ConjoinClient) {
  return {
    oidcLogout: (accountId: string, data: OidcLogoutBody, options?: ConjoinCallOptions) =>
      client.fetch<OidcLogoutData>(`auth/accounts/${encodePathParam(accountId)}/logout-oidc`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    samlSpLogout: (accountId: string, data: SamlSpLogoutBody, options?: ConjoinCallOptions) =>
      client.fetch<SamlSpLogoutData>(`auth/accounts/${encodePathParam(accountId)}/logout-saml`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    samlIdpLogout: (data: SamlIdpLogoutBody, options?: ConjoinCallOptions) =>
      client.fetch<SamlIdpLogoutData>('auth/saml-logout-requests', { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),
  }
}
