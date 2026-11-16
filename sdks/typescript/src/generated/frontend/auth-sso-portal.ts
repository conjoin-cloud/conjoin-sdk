import type { ConjoinCallOptions, ConjoinClient, ConjoinDeclaredHeaderRule } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ReadSsoPortalContextData = NonNullable<operations['readSsoPortalContext']['responses']['200']['content']['application/json']['data']>
type ReadSsoPortalContextHeaders = { portalTicket: string }
type ReadSsoPortalCatalogData = NonNullable<operations['readSsoPortalCatalog']['responses']['200']['content']['application/json']['data']>
type ReadSsoPortalCatalogHeaders = { portalTicket: string }
type StartSsoPortalTestBody = NonNullable<operations['startSsoPortalTest']['requestBody']>['content']['application/json']
type StartSsoPortalTestData = NonNullable<operations['startSsoPortalTest']['responses']['200']['content']['application/json']['data']>
type StartSsoPortalTestHeaders = { portalTicket: string }

const readSsoPortalContextHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

const readSsoPortalCatalogHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

const startSsoPortalTestHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

export function createAuthSSOPortals(client: ConjoinClient) {
  return {
    readSsoPortalContext: (headers: ReadSsoPortalContextHeaders, options?: ConjoinCallOptions) =>
      client.fetch<ReadSsoPortalContextData>('auth/portal/', { ...options, auth: { type: 'none' }, method: 'GET', declaredHeaders: { rules: readSsoPortalContextHeaderRules, values: headers } }),

    readSsoPortalCatalog: (headers: ReadSsoPortalCatalogHeaders, options?: ConjoinCallOptions) =>
      client.fetch<ReadSsoPortalCatalogData>('auth/portal/providers', { ...options, auth: { type: 'none' }, method: 'GET', declaredHeaders: { rules: readSsoPortalCatalogHeaderRules, values: headers } }),

    startSsoPortalTest: (data: StartSsoPortalTestBody, headers: StartSsoPortalTestHeaders, options?: ConjoinCallOptions) =>
      client.fetch<StartSsoPortalTestData>('auth/portal/test/start', { ...options, auth: { type: 'none' }, method: 'POST', body: data, declaredHeaders: { rules: startSsoPortalTestHeaderRules, values: headers } }),
  }
}
