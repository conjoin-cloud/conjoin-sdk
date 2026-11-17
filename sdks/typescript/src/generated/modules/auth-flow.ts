import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type StartSignupBody = NonNullable<operations['startSignup']['requestBody']>['content']['application/json']
type StartSignupData = NonNullable<operations['startSignup']['responses']['200']['content']['application/json']['data']>
type CompleteSignupBody = NonNullable<operations['completeSignup']['requestBody']>['content']['application/json']
type CompleteSignupData = NonNullable<operations['completeSignup']['responses']['200']['content']['application/json']['data']>
type ConfirmLinkSignupBody = NonNullable<operations['confirmLinkSignup']['requestBody']>['content']['application/json']
type ConfirmLinkSignupData = NonNullable<operations['confirmLinkSignup']['responses']['200']['content']['application/json']['data']>
type StartSigninBody = NonNullable<operations['startSignin']['requestBody']>['content']['application/json']
type StartSigninData = NonNullable<operations['startSignin']['responses']['200']['content']['application/json']['data']>
type CompleteSigninBody = NonNullable<operations['completeSignin']['requestBody']>['content']['application/json']
type CompleteSigninData = NonNullable<operations['completeSignin']['responses']['200']['content']['application/json']['data']>
type StartPasswordResetBody = NonNullable<operations['startPasswordReset']['requestBody']>['content']['application/json']
type StartPasswordResetData = NonNullable<operations['startPasswordReset']['responses']['200']['content']['application/json']['data']>
type CompletePasswordResetBody = NonNullable<operations['completePasswordReset']['requestBody']>['content']['application/json']
type CompletePasswordResetData = NonNullable<operations['completePasswordReset']['responses']['200']['content']['application/json']['data']>

export function createAuthFlows(client: ConjoinClient) {
  return {
    startSignup: (clientId: string, data: StartSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<StartSignupData>(`auth/clients/${encodePathParam(clientId)}/sign-ups/start`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    completeSignup: (clientId: string, data: CompleteSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<CompleteSignupData>(`auth/clients/${encodePathParam(clientId)}/sign-ups/complete`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    confirmLinkSignup: (clientId: string, data: ConfirmLinkSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<ConfirmLinkSignupData>(`auth/clients/${encodePathParam(clientId)}/sign-ups/confirm-link`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    startSignin: (clientId: string, data: StartSigninBody, options?: ConjoinCallOptions) =>
      client.fetch<StartSigninData>(`auth/clients/${encodePathParam(clientId)}/sign-ins/start`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    completeSignin: (clientId: string, data: CompleteSigninBody, options?: ConjoinCallOptions) =>
      client.fetch<CompleteSigninData>(`auth/clients/${encodePathParam(clientId)}/sign-ins/complete`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    startPasswordReset: (clientId: string, data: StartPasswordResetBody, options?: ConjoinCallOptions) =>
      client.fetch<StartPasswordResetData>(`auth/clients/${encodePathParam(clientId)}/password-resets/start`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    completePasswordReset: (clientId: string, data: CompletePasswordResetBody, options?: ConjoinCallOptions) =>
      client.fetch<CompletePasswordResetData>(`auth/clients/${encodePathParam(clientId)}/password-resets/complete`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
