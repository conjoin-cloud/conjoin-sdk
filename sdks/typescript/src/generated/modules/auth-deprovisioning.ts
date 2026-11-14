import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type DeprovisionAccountBody = NonNullable<operations['deprovisionAccount']['requestBody']>['content']['application/json']
type DeprovisionAccountData = NonNullable<operations['deprovisionAccount']['responses']['200']['content']['application/json']['data']>

export function createAuthDeprovisionings(client: ConjoinClient) {
  return {
    deprovisionAccount: (accountId: string, data: DeprovisionAccountBody, options?: ConjoinCallOptions) =>
      client.fetch<DeprovisionAccountData>(`auth/accounts/${encodePathParam(accountId)}/deprovision`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),
  }
}
