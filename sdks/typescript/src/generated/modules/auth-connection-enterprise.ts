import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListEnterpriseConnectionsData = NonNullable<operations['listEnterpriseConnections']['responses']['200']['content']['application/json']['data']>[number]
type ListEnterpriseConnectionsQuery = NonNullable<operations['listEnterpriseConnections']['parameters']['query']>
type CreateEnterpriseConnectionBody = NonNullable<operations['createEnterpriseConnection']['requestBody']>['content']['application/json']
type CreateEnterpriseConnectionData = NonNullable<operations['createEnterpriseConnection']['responses']['201']['content']['application/json']['data']>
type ListEnterpriseConnectionsCountData = NonNullable<operations['listEnterpriseConnectionsCount']['responses']['200']['content']['application/json']['data']>
type ListEnterpriseConnectionsCountQuery = NonNullable<operations['listEnterpriseConnectionsCount']['parameters']['query']>
type ReadEnterpriseConnectionData = NonNullable<operations['readEnterpriseConnection']['responses']['200']['content']['application/json']['data']>
type UpdateEnterpriseConnectionBody = NonNullable<operations['updateEnterpriseConnection']['requestBody']>['content']['application/json']
type UpdateEnterpriseConnectionData = NonNullable<operations['updateEnterpriseConnection']['responses']['200']['content']['application/json']['data']>
type DeleteEnterpriseConnectionData = NonNullable<operations['deleteEnterpriseConnection']['responses']['200']['content']['application/json']['data']>
type EnableEnterpriseConnectionData = NonNullable<operations['enableEnterpriseConnection']['responses']['200']['content']['application/json']['data']>
type DisableEnterpriseConnectionData = NonNullable<operations['disableEnterpriseConnection']['responses']['200']['content']['application/json']['data']>
type RotateEnterpriseConnectionSigningKeyData = NonNullable<operations['rotateEnterpriseConnectionSigningKey']['responses']['200']['content']['application/json']['data']>
type ActivateEnterpriseConnectionSigningKeyData = NonNullable<operations['activateEnterpriseConnectionSigningKey']['responses']['200']['content']['application/json']['data']>
type CancelEnterpriseConnectionSigningKeyData = NonNullable<operations['cancelEnterpriseConnectionSigningKey']['responses']['200']['content']['application/json']['data']>
type RevokeEnterpriseConnectionSigningKeyData = NonNullable<operations['revokeEnterpriseConnectionSigningKey']['responses']['200']['content']['application/json']['data']>
type ReadEnterpriseProviderSettingsData = NonNullable<operations['readEnterpriseProviderSettings']['responses']['200']['content']['application/json']['data']>
type ImportEnterpriseSamlMetadataBody = NonNullable<operations['importEnterpriseSamlMetadata']['requestBody']>['content']['multipart/form-data']
type ImportEnterpriseSamlMetadataData = NonNullable<operations['importEnterpriseSamlMetadata']['responses']['200']['content']['application/json']['data']>
type SyncEnterpriseSamlMetadataBody = NonNullable<operations['syncEnterpriseSamlMetadata']['requestBody']>['content']['application/json']
type SyncEnterpriseSamlMetadataData = NonNullable<operations['syncEnterpriseSamlMetadata']['responses']['200']['content']['application/json']['data']>

export function createAuthConnectionEnterprises(client: ConjoinClient) {
  return {
    listEnterpriseConnections: (organizationId: string, query?: ListEnterpriseConnectionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListEnterpriseConnectionsData>(`auth/organizations/${encodePathParam(organizationId)}/connections/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    createEnterpriseConnection: (organizationId: string, data: CreateEnterpriseConnectionBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateEnterpriseConnectionData>(`auth/organizations/${encodePathParam(organizationId)}/connections/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    listEnterpriseConnectionsCount: (organizationId: string, query?: ListEnterpriseConnectionsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListEnterpriseConnectionsCountData>(`auth/organizations/${encodePathParam(organizationId)}/connections/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    readEnterpriseConnection: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadEnterpriseConnectionData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    updateEnterpriseConnection: (organizationId: string, connectionId: string, data: UpdateEnterpriseConnectionBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateEnterpriseConnectionData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    deleteEnterpriseConnection: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteEnterpriseConnectionData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    enableEnterpriseConnection: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<EnableEnterpriseConnectionData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/enable`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    disableEnterpriseConnection: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<DisableEnterpriseConnectionData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/disable`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    rotateEnterpriseConnectionSigningKey: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<RotateEnterpriseConnectionSigningKeyData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/signing-keys/rotate`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    activateEnterpriseConnectionSigningKey: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ActivateEnterpriseConnectionSigningKeyData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/signing-keys/activate`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    cancelEnterpriseConnectionSigningKey: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<CancelEnterpriseConnectionSigningKeyData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/signing-keys/cancel`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    revokeEnterpriseConnectionSigningKey: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeEnterpriseConnectionSigningKeyData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/signing-keys/revoke`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    readEnterpriseProviderSettings: (organizationId: string, connectionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadEnterpriseProviderSettingsData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/provider-settings`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    importEnterpriseSamlMetadata: (organizationId: string, connectionId: string, data: ImportEnterpriseSamlMetadataBody, options?: ConjoinCallOptions) =>
      client.fetch<ImportEnterpriseSamlMetadataData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/import-metadata`, { ...options, method: 'POST', body: data, contentType: 'multipart/form-data', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    syncEnterpriseSamlMetadata: (organizationId: string, connectionId: string, data: SyncEnterpriseSamlMetadataBody, options?: ConjoinCallOptions) =>
      client.fetch<SyncEnterpriseSamlMetadataData>(`auth/organizations/${encodePathParam(organizationId)}/connections/${encodePathParam(connectionId)}/sync-metadata`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
