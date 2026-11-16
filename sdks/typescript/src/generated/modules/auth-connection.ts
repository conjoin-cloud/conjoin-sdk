import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListFirstPartyData = NonNullable<operations['listFirstPartyConnections']['responses']['200']['content']['application/json']['data']>
type ListFirstPartyQuery = NonNullable<operations['listFirstPartyConnections']['parameters']['query']>
type UpsertFirstPartyBody = NonNullable<operations['upsertFirstPartyConnection']['requestBody']>['content']['application/json']
type UpsertFirstPartyData = NonNullable<operations['upsertFirstPartyConnection']['responses']['201']['content']['application/json']['data']>

export function createAuthConnections(client: ConjoinClient) {
  return {
    listFirstParty: (query?: ListFirstPartyQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListFirstPartyData>('auth/connection-configs/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    upsertFirstParty: (data: UpsertFirstPartyBody, options?: ConjoinCallOptions) =>
      client.fetch<UpsertFirstPartyData>('auth/connection-configs/', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
