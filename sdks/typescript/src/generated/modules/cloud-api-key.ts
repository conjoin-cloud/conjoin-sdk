import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadApiKeysData = NonNullable<operations['readCloudApiKeys']['responses']['200']['content']['application/json']['data']>[number]
type ReadApiKeysQuery = NonNullable<operations['readCloudApiKeys']['parameters']['query']>
type CreateApiKeyBody = NonNullable<operations['createCloudApiKey']['requestBody']>['content']['application/json']
type CreateApiKeyData = NonNullable<operations['createCloudApiKey']['responses']['201']['content']['application/json']['data']>
type ReadApiKeysCountData = NonNullable<operations['readCloudApiKeysCount']['responses']['200']['content']['application/json']['data']>
type ReadApiKeysCountQuery = NonNullable<operations['readCloudApiKeysCount']['parameters']['query']>
type RegenerateApiKeyBody = NonNullable<operations['regenerateCloudApiKey']['requestBody']>['content']['application/json']
type RegenerateApiKeyData = NonNullable<operations['regenerateCloudApiKey']['responses']['200']['content']['application/json']['data']>
type UpdateApiKeyBody = NonNullable<operations['updateCloudApiKey']['requestBody']>['content']['application/json']
type UpdateApiKeyData = NonNullable<operations['updateCloudApiKey']['responses']['200']['content']['application/json']['data']>
type DeleteApiKeyData = NonNullable<operations['deleteCloudApiKey']['responses']['200']['content']['application/json']['data']>

export function createCloudAPIKeys(client: ConjoinClient) {
  return {
    readApiKeys: (query?: ReadApiKeysQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadApiKeysData>('cloud/api-keys/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createApiKey: (data: CreateApiKeyBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateApiKeyData>('cloud/api-keys/', { ...options, method: 'POST', body: data }),

    readApiKeysCount: (query?: ReadApiKeysCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadApiKeysCountData>('cloud/api-keys/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    regenerateApiKey: (apiKeyId: string, data: RegenerateApiKeyBody, options?: ConjoinCallOptions) =>
      client.fetch<RegenerateApiKeyData>(`cloud/api-keys/${encodePathParam(apiKeyId)}/regenerate`, { ...options, method: 'POST', body: data }),

    updateApiKey: (apiKeyId: string, data: UpdateApiKeyBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateApiKeyData>(`cloud/api-keys/${encodePathParam(apiKeyId)}`, { ...options, method: 'PATCH', body: data }),

    deleteApiKey: (apiKeyId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteApiKeyData>(`cloud/api-keys/${encodePathParam(apiKeyId)}`, { ...options, method: 'DELETE' }),
  }
}
