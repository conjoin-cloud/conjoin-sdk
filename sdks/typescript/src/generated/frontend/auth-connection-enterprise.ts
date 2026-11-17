import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient, ConjoinDeclaredHeaderRule } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ConfigureSsoPortalConnectionBody = NonNullable<operations['configureSsoPortalConnection']['requestBody']>['content']['application/json']
type ConfigureSsoPortalConnectionData = NonNullable<operations['configureSsoPortalConnection']['responses']['201']['content']['application/json']['data']>
type ConfigureSsoPortalConnectionHeaders = { portalTicket: string }
type UpdateSsoPortalConnectionBody = NonNullable<operations['updateSsoPortalConnection']['requestBody']>['content']['application/json']
type UpdateSsoPortalConnectionData = NonNullable<operations['updateSsoPortalConnection']['responses']['200']['content']['application/json']['data']>
type UpdateSsoPortalConnectionHeaders = { portalTicket: string }
type ImportSsoPortalMetadataBody = NonNullable<operations['importSsoPortalMetadata']['requestBody']>['content']['multipart/form-data']
type ImportSsoPortalMetadataData = NonNullable<operations['importSsoPortalMetadata']['responses']['200']['content']['application/json']['data']>
type ImportSsoPortalMetadataHeaders = { portalTicket: string }
type ReadSsoPortalProviderConfigData = NonNullable<operations['readSsoPortalProviderConfig']['responses']['200']['content']['application/json']['data']>
type ReadSsoPortalProviderConfigHeaders = { portalTicket: string }

const configureSsoPortalConnectionHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

const updateSsoPortalConnectionHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

const importSsoPortalMetadataHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

const readSsoPortalProviderConfigHeaderRules: readonly ConjoinDeclaredHeaderRule[] = [
  { name: "x-portal-ticket", argumentName: "portalTicket", required: true },
]

export function createAuthConnectionEnterprises(client: ConjoinClient) {
  return {
    configureSsoPortalConnection: (data: ConfigureSsoPortalConnectionBody, headers: ConfigureSsoPortalConnectionHeaders, options?: ConjoinCallOptions) =>
      client.fetch<ConfigureSsoPortalConnectionData>('auth/portal/connections', { ...options, auth: { type: 'none' }, method: 'POST', body: data, declaredHeaders: { rules: configureSsoPortalConnectionHeaderRules, values: headers } }),

    updateSsoPortalConnection: (connectionId: string, data: UpdateSsoPortalConnectionBody, headers: UpdateSsoPortalConnectionHeaders, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSsoPortalConnectionData>(`auth/portal/connections/${encodePathParam(connectionId)}`, { ...options, auth: { type: 'none' }, method: 'PATCH', body: data, declaredHeaders: { rules: updateSsoPortalConnectionHeaderRules, values: headers } }),

    importSsoPortalMetadata: (connectionId: string, data: ImportSsoPortalMetadataBody, headers: ImportSsoPortalMetadataHeaders, options?: ConjoinCallOptions) =>
      client.fetch<ImportSsoPortalMetadataData>(`auth/portal/connections/${encodePathParam(connectionId)}/import-metadata`, { ...options, auth: { type: 'none' }, method: 'POST', body: data, contentType: 'multipart/form-data', declaredHeaders: { rules: importSsoPortalMetadataHeaderRules, values: headers } }),

    readSsoPortalProviderConfig: (connectionId: string, headers: ReadSsoPortalProviderConfigHeaders, options?: ConjoinCallOptions) =>
      client.fetch<ReadSsoPortalProviderConfigData>(`auth/portal/connections/${encodePathParam(connectionId)}/service-provider-settings`, { ...options, auth: { type: 'none' }, method: 'GET', declaredHeaders: { rules: readSsoPortalProviderConfigHeaderRules, values: headers } }),
  }
}
