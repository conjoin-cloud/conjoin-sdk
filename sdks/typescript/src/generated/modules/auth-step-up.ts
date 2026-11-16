import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type RequestBody = NonNullable<operations['requestStepUp']['requestBody']>['content']['application/json']
type RequestData = NonNullable<operations['requestStepUp']['responses']['200']['content']['application/json']['data']>
type VerifyBody = NonNullable<operations['verifyStepUp']['requestBody']>['content']['application/json']
type VerifyData = NonNullable<operations['verifyStepUp']['responses']['200']['content']['application/json']['data']>
type ValidateBody = NonNullable<operations['validateStepUp']['requestBody']>['content']['application/json']
type ValidateData = NonNullable<operations['validateStepUp']['responses']['200']['content']['application/json']['data']>

export function createAuthStepUps(client: ConjoinClient) {
  return {
    request: (accountId: string, data: RequestBody, options?: ConjoinCallOptions) =>
      client.fetch<RequestData>(`auth/accounts/${encodePathParam(accountId)}/step-ups/start`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    verify: (accountId: string, data: VerifyBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifyData>(`auth/accounts/${encodePathParam(accountId)}/step-ups/verify`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    validate: (accountId: string, data: ValidateBody, options?: ConjoinCallOptions) =>
      client.fetch<ValidateData>(`auth/accounts/${encodePathParam(accountId)}/step-ups/validate`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
