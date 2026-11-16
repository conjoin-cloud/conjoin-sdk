import type { ConjoinCallOptions, ConjoinClient, ConjoinDeclaredHeaderRule } from '../../core/types'
import type { operations } from '../frontend-api-types'

type VerifySsoPortalDomainBody = NonNullable<operations['verifySsoPortalDomain']['requestBody']>['content']['application/json']
type VerifySsoPortalDomainData = NonNullable<operations['verifySsoPortalDomain']['responses']['201']['content']['application/json']['data']>
type VerifySsoPortalDomainHeaders = { portalTicket: string }

const verifySsoPortalDomainHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

export function createAuthOrganizationDomains(client: ConjoinClient) {
  return {
    verifySsoPortalDomain: (data: VerifySsoPortalDomainBody, headers: VerifySsoPortalDomainHeaders, options?: ConjoinCallOptions) =>
      client.fetch<VerifySsoPortalDomainData>('auth/portal/domains', { ...options, auth: { type: 'none' }, method: 'POST', body: data, declaredHeaders: { rules: verifySsoPortalDomainHeaderRules, values: headers } }),
  }
}
