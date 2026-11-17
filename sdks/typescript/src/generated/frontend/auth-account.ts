import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type BatchLookupBody = NonNullable<operations['batchLookupAccounts']['requestBody']>['content']['application/json']
type BatchLookupData = NonNullable<operations['batchLookupAccounts']['responses']['200']['content']['application/json']['data']>

export function createAuthAccounts(client: ConjoinClient) {
  return {
    batchLookup: (data: BatchLookupBody, options?: ConjoinCallOptions) =>
      client.fetch<BatchLookupData>('auth/client/account-lookups/', { ...options, auth: { type: 'publishableKey' }, method: 'POST', body: data }),
  }
}
