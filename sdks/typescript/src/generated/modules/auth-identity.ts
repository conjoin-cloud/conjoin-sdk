import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type DiscoverAccountBody = NonNullable<operations['discoverAccount']['requestBody']>['content']['application/json']
type DiscoverAccountData = NonNullable<operations['discoverAccount']['responses']['200']['content']['application/json']['data']>
type LinkBody = NonNullable<operations['linkIdentity']['requestBody']>['content']['application/json']
type LinkData = NonNullable<operations['linkIdentity']['responses']['200']['content']['application/json']['data']>
type UnlinkBody = NonNullable<operations['unlinkIdentity']['requestBody']>['content']['application/json']
type UnlinkData = NonNullable<operations['unlinkIdentity']['responses']['200']['content']['application/json']['data']>

export function createAuthIdentities(client: ConjoinClient) {
  return {
    discoverAccount: (data: DiscoverAccountBody, options?: ConjoinCallOptions) =>
      client.fetch<DiscoverAccountData>('auth/accounts/discover', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    link: (accountId: string, data: LinkBody, options?: ConjoinCallOptions) =>
      client.fetch<LinkData>(`auth/accounts/${encodePathParam(accountId)}/identities/link`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    unlink: (accountId: string, data: UnlinkBody, options?: ConjoinCallOptions) =>
      client.fetch<UnlinkData>(`auth/accounts/${encodePathParam(accountId)}/identities/unlink`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
