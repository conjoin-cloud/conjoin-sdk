import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type StartSignupBody = NonNullable<operations['startAuthSignup']['requestBody']>['content']['application/json']
type StartSignupData = NonNullable<operations['startAuthSignup']['responses']['200']['content']['application/json']['data']>
type CompleteSignupBody = NonNullable<operations['completeAuthSignup']['requestBody']>['content']['application/json']
type CompleteSignupData = NonNullable<operations['completeAuthSignup']['responses']['200']['content']['application/json']['data']>
type ConfirmLinkSignupBody = NonNullable<operations['confirmLinkAuthSignup']['requestBody']>['content']['application/json']
type ConfirmLinkSignupData = NonNullable<operations['confirmLinkAuthSignup']['responses']['200']['content']['application/json']['data']>
type StartSigninBody = NonNullable<operations['startAuthSignin']['requestBody']>['content']['application/json']
type StartSigninData = NonNullable<operations['startAuthSignin']['responses']['200']['content']['application/json']['data']>
type CompleteSigninBody = NonNullable<operations['completeAuthSignin']['requestBody']>['content']['application/json']
type CompleteSigninData = NonNullable<operations['completeAuthSignin']['responses']['200']['content']['application/json']['data']>
type StartPasswordResetBody = NonNullable<operations['startAuthPasswordReset']['requestBody']>['content']['application/json']
type StartPasswordResetData = NonNullable<operations['startAuthPasswordReset']['responses']['200']['content']['application/json']['data']>
type CompletePasswordResetBody = NonNullable<operations['completeAuthPasswordReset']['requestBody']>['content']['application/json']
type CompletePasswordResetData = NonNullable<operations['completeAuthPasswordReset']['responses']['200']['content']['application/json']['data']>

export function createAuthFlows(client: ConjoinClient) {
  return {
    startSignup: (data: StartSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<StartSignupData>('auth/client/sign-ups/start', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    completeSignup: (data: CompleteSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<CompleteSignupData>('auth/client/sign-ups/complete', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    confirmLinkSignup: (data: ConfirmLinkSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<ConfirmLinkSignupData>('auth/client/sign-ups/confirm-link', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    startSignin: (data: StartSigninBody, options?: ConjoinCallOptions) =>
      client.fetch<StartSigninData>('auth/client/sign-ins/start', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    completeSignin: (data: CompleteSigninBody, options?: ConjoinCallOptions) =>
      client.fetch<CompleteSigninData>('auth/client/sign-ins/complete', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    startPasswordReset: (data: StartPasswordResetBody, options?: ConjoinCallOptions) =>
      client.fetch<StartPasswordResetData>('auth/client/password-resets/start', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    completePasswordReset: (data: CompletePasswordResetBody, options?: ConjoinCallOptions) =>
      client.fetch<CompletePasswordResetData>('auth/client/password-resets/complete', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),
  }
}
