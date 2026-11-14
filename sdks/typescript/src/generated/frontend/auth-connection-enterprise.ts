import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ConfigureSsoPortalConnectionBody = NonNullable<operations['configureSsoPortalConnection']['requestBody']>['content']['application/json']
type ConfigureSsoPortalConnectionData = NonNullable<operations['configureSsoPortalConnection']['responses']['201']['content']['application/json']['data']>
type UpdateSsoPortalConnectionBody = NonNullable<operations['updateSsoPortalConnection']['requestBody']>['content']['application/json']
type UpdateSsoPortalConnectionData = NonNullable<operations['updateSsoPortalConnection']['responses']['200']['content']['application/json']['data']>
type ImportSsoPortalMetadataBody = NonNullable<operations['importSsoPortalMetadata']['requestBody']>['content']['multipart/form-data']
type ImportSsoPortalMetadataData = NonNullable<operations['importSsoPortalMetadata']['responses']['200']['content']['application/json']['data']>
type ReadSsoPortalProviderConfigData = NonNullable<operations['readSsoPortalProviderConfig']['responses']['200']['content']['application/json']['data']>

export function createAuthConnectionEnterprises(client: ConjoinClient) {
  return {
    configureSsoPortalConnection: (data: ConfigureSsoPortalConnectionBody, options?: ConjoinCallOptions) =>
      client.fetch<ConfigureSsoPortalConnectionData>('auth/portal/connections', { auth: { type: 'none' }, ...options, method: 'POST', body: data }),

    updateSsoPortalConnection: (connectionId: string, data: UpdateSsoPortalConnectionBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSsoPortalConnectionData>(`auth/portal/connections/${encodePathParam(connectionId)}`, { auth: { type: 'none' }, ...options, method: 'PATCH', body: data }),

    importSsoPortalMetadata: (connectionId: string, data: ImportSsoPortalMetadataBody, options?: ConjoinCallOptions) =>
      client.fetch<ImportSsoPortalMetadataData>(`auth/portal/connections/${encodePathParam(connectionId)}/import-metadata`, { auth: { type: 'none' }, ...options, method: 'POST', body: data, contentType: 'multipart/form-data' }),

    readSsoPortalProviderConfig: (connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSsoPortalProviderConfigData>(`auth/portal/connections/${encodePathParam(connectionId)}/service-provider-settings`, { auth: { type: 'none' }, ...options, method: 'GET' }),
  }
}
