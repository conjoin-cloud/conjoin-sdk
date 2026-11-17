import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listAuthClients']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAuthClients']['parameters']['query']>
type CreateBody = NonNullable<operations['createAuthClient']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createAuthClient']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listAuthClientsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listAuthClientsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readAuthClient']['responses']['200']['content']['application/json']['data']>

export function createAuthClients(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('auth/clients/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('auth/clients/', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('auth/clients/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    read: (clientId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`auth/clients/${encodePathParam(clientId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),
  }
}
