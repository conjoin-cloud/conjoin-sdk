import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type VerifySsoPortalDomainBody = NonNullable<operations['verifySsoPortalDomain']['requestBody']>['content']['application/json']
type VerifySsoPortalDomainData = NonNullable<operations['verifySsoPortalDomain']['responses']['201']['content']['application/json']['data']>

export function createAuthOrganizationDomains(client: ConjoinClient) {
  return {
    verifySsoPortalDomain: (data: VerifySsoPortalDomainBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifySsoPortalDomainData>('auth/portal/domains', { auth: { type: 'none' }, ...options, method: 'POST', body: data }),
  }
}
