import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listAuthSessions']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAuthSessions']['parameters']['query']>
type ListCountData = NonNullable<operations['listAuthSessionsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listAuthSessionsCount']['parameters']['query']>
type ReadStatsData = NonNullable<operations['readAuthSessionStats']['responses']['200']['content']['application/json']['data']>
type ReadStatsQuery = NonNullable<operations['readAuthSessionStats']['parameters']['query']>
type GetAnalyticsData = NonNullable<operations['getSessionAnalytics']['responses']['200']['content']['application/json']['data']>
type GetAnalyticsQuery = NonNullable<operations['getSessionAnalytics']['parameters']['query']>
type ReadData = NonNullable<operations['readAuthSession']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateAuthSession']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateAuthSession']['responses']['200']['content']['application/json']['data']>
type ValidateBody = NonNullable<operations['validateAuthSession']['requestBody']>['content']['application/json']
type ValidateData = NonNullable<operations['validateAuthSession']['responses']['200']['content']['application/json']['data']>
type RevokeData = NonNullable<operations['revokeAuthSession']['responses']['200']['content']['application/json']['data']>
type RevokeAllForAccountData = NonNullable<operations['revokeAllAuthSessionsForAccount']['responses']['200']['content']['application/json']['data']>
type BulkRevokeAccountBody = NonNullable<operations['bulkRevokeAccountSessions']['requestBody']>['content']['application/json']
type BulkRevokeAccountData = NonNullable<operations['bulkRevokeAccountSessions']['responses']['200']['content']['application/json']['data']>
type BulkRevokeClientBody = NonNullable<operations['bulkRevokeClientSessions']['requestBody']>['content']['application/json']
type BulkRevokeClientData = NonNullable<operations['bulkRevokeClientSessions']['responses']['200']['content']['application/json']['data']>

export function createAuthSessions(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('auth/sessions', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('auth/sessions/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    readStats: (query?: ReadStatsQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadStatsData>('auth/sessions/stats', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    getAnalytics: (query: GetAnalyticsQuery, options?: ConjoinCallOptions) =>
      client.fetch<GetAnalyticsData>('auth/sessions/analytics', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    read: (sessionId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`auth/sessions/${encodePathParam(sessionId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    update: (sessionId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`auth/sessions/${encodePathParam(sessionId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    validate: (sessionId: string, data: ValidateBody, options?: ConjoinCallOptions) =>
      client.fetch<ValidateData>(`auth/sessions/${encodePathParam(sessionId)}/validate`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    revoke: (sessionId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeData>(`auth/sessions/${encodePathParam(sessionId)}/revoke`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    revokeAllForAccount: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeAllForAccountData>(`auth/accounts/${encodePathParam(accountId)}/sessions/revoke-all`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    bulkRevokeAccount: (accountId: string, data: BulkRevokeAccountBody, options?: ConjoinCallOptions) =>
      client.fetch<BulkRevokeAccountData>(`auth/accounts/${encodePathParam(accountId)}/sessions/revoke`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    bulkRevokeClient: (clientId: string, data: BulkRevokeClientBody, options?: ConjoinCallOptions) =>
      client.fetch<BulkRevokeClientData>(`auth/clients/${encodePathParam(clientId)}/sessions/revoke`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
