import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listPasskeys']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPasskeys']['parameters']['query']>
type ListCountData = NonNullable<operations['listPasskeysCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPasskeysCount']['parameters']['query']>
type ReadData = NonNullable<operations['readPasskey']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deletePasskey']['responses']['200']['content']['application/json']['data']>

export function createAuthPasskeys(client: ConjoinClient) {
  return {
    list: (accountId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`auth/accounts/${encodePathParam(accountId)}/passkeys/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listCount: (accountId: string, query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>(`auth/accounts/${encodePathParam(accountId)}/passkeys/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    read: (accountId: string, passkeyId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`auth/accounts/${encodePathParam(accountId)}/passkeys/${encodePathParam(passkeyId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    delete: (accountId: string, passkeyId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`auth/accounts/${encodePathParam(accountId)}/passkeys/${encodePathParam(passkeyId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),
  }
}
