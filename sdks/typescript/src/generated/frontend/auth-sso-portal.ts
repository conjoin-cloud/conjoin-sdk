import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ReadSsoPortalContextData = NonNullable<operations['readSsoPortalContext']['responses']['200']['content']['application/json']['data']>
type ReadSsoPortalCatalogData = NonNullable<operations['readSsoPortalCatalog']['responses']['200']['content']['application/json']['data']>
type StartSsoPortalTestBody = NonNullable<operations['startSsoPortalTest']['requestBody']>['content']['application/json']
type StartSsoPortalTestData = NonNullable<operations['startSsoPortalTest']['responses']['200']['content']['application/json']['data']>

export function createAuthSSOPortals(client: ConjoinClient) {
  return {
    readSsoPortalContext: (options?: ConjoinCallOptions) =>
      client.fetch<ReadSsoPortalContextData>('auth/portal/', { auth: { type: 'none' }, ...options, method: 'GET' }),

    readSsoPortalCatalog: (options?: ConjoinCallOptions) =>
      client.fetch<ReadSsoPortalCatalogData>('auth/portal/providers', { auth: { type: 'none' }, ...options, method: 'GET' }),

    startSsoPortalTest: (data: StartSsoPortalTestBody, options?: ConjoinCallOptions) =>
      client.fetch<StartSsoPortalTestData>('auth/portal/test/start', { auth: { type: 'none' }, ...options, method: 'POST', body: data }),
  }
}
