import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type StartRecoveryData = NonNullable<operations['startRecovery']['responses']['200']['content']['application/json']['data']>
type VerifyRecoveryBody = NonNullable<operations['verifyRecovery']['requestBody']>['content']['application/json']
type VerifyRecoveryData = NonNullable<operations['verifyRecovery']['responses']['200']['content']['application/json']['data']>
type CompleteRecoveryBody = NonNullable<operations['completeRecovery']['requestBody']>['content']['application/json']
type CompleteRecoveryData = NonNullable<operations['completeRecovery']['responses']['200']['content']['application/json']['data']>
type AdminResetAccountData = NonNullable<operations['adminResetAccount']['responses']['200']['content']['application/json']['data']>

export function createAuthAccountRecoveries(client: ConjoinClient) {
  return {
    startRecovery: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<StartRecoveryData>(`auth/accounts/${encodePathParam(accountId)}/recoveries/start`, { ...options, method: 'POST', scopes: ['authAppId'] }),

    verifyRecovery: (accountId: string, data: VerifyRecoveryBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifyRecoveryData>(`auth/accounts/${encodePathParam(accountId)}/recoveries/verify`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    completeRecovery: (accountId: string, data: CompleteRecoveryBody, options?: ConjoinCallOptions) =>
      client.fetch<CompleteRecoveryData>(`auth/accounts/${encodePathParam(accountId)}/recoveries/complete`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    adminResetAccount: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<AdminResetAccountData>(`auth/accounts/${encodePathParam(accountId)}/reset-mfa`, { ...options, method: 'POST', scopes: ['authAppId'] }),
  }
}
