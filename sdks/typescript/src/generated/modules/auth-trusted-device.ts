import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listTrustedDevices']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listTrustedDevices']['parameters']['query']>
type ListCountData = NonNullable<operations['listTrustedDevicesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listTrustedDevicesCount']['parameters']['query']>
type RevokeAllData = NonNullable<operations['revokeAllTrustedDevices']['responses']['200']['content']['application/json']['data']>
type RevokeData = NonNullable<operations['revokeTrustedDevice']['responses']['200']['content']['application/json']['data']>

export function createAuthTrustedDevices(client: ConjoinClient) {
  return {
    list: (accountId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`auth/accounts/${encodePathParam(accountId)}/trusted-devices/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listCount: (accountId: string, query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>(`auth/accounts/${encodePathParam(accountId)}/trusted-devices/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    revokeAll: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeAllData>(`auth/accounts/${encodePathParam(accountId)}/trusted-devices/revoke-all`, { ...options, method: 'POST', scopes: ['authAppId'] }),

    revoke: (accountId: string, trustedDeviceId: string, options?: ConjoinCallOptions) =>
      client.fetch<RevokeData>(`auth/accounts/${encodePathParam(accountId)}/trusted-devices/${encodePathParam(trustedDeviceId)}/revoke`, { ...options, method: 'POST', scopes: ['authAppId'] }),
  }
}
