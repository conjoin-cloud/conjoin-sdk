import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type StartSignupBody = NonNullable<operations['startNativeSignup']['requestBody']>['content']['application/json']
type StartSignupData = NonNullable<operations['startNativeSignup']['responses']['200']['content']['application/json']['data']>
type CompleteSignupBody = NonNullable<operations['completeNativeSignup']['requestBody']>['content']['application/json']
type CompleteSignupData = NonNullable<operations['completeNativeSignup']['responses']['200']['content']['application/json']['data']>
type ConfirmLinkSignupBody = NonNullable<operations['confirmLinkNativeSignup']['requestBody']>['content']['application/json']
type ConfirmLinkSignupData = NonNullable<operations['confirmLinkNativeSignup']['responses']['200']['content']['application/json']['data']>
type StartSigninBody = NonNullable<operations['startNativeSignin']['requestBody']>['content']['application/json']
type StartSigninData = NonNullable<operations['startNativeSignin']['responses']['200']['content']['application/json']['data']>
type CompleteSigninBody = NonNullable<operations['completeNativeSignin']['requestBody']>['content']['application/json']
type CompleteSigninData = NonNullable<operations['completeNativeSignin']['responses']['200']['content']['application/json']['data']>
type ProcessTokenMintData = NonNullable<operations['processNativeTokenMint']['responses']['200']['content']['application/json']['data']>
type RefreshSessionBody = NonNullable<operations['refreshNativeSession']['requestBody']>['content']['application/json']
type RefreshSessionData = NonNullable<operations['refreshNativeSession']['responses']['200']['content']['application/json']['data']>
type ProcessLogoutData = NonNullable<operations['processNativeLogout']['responses']['200']['content']['application/json']['data']>

export function createAuthNatives(client: ConjoinClient) {
  return {
    startSignup: (data: StartSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<StartSignupData>('auth/client/native/sign-ups/start', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    completeSignup: (data: CompleteSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<CompleteSignupData>('auth/client/native/sign-ups/complete', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    confirmLinkSignup: (data: ConfirmLinkSignupBody, options?: ConjoinCallOptions) =>
      client.fetch<ConfirmLinkSignupData>('auth/client/native/sign-ups/confirm-link', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    startSignin: (data: StartSigninBody, options?: ConjoinCallOptions) =>
      client.fetch<StartSigninData>('auth/client/native/sign-ins/start', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    completeSignin: (data: CompleteSigninBody, options?: ConjoinCallOptions) =>
      client.fetch<CompleteSigninData>('auth/client/native/sign-ins/complete', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    processTokenMint: (options?: ConjoinCallOptions) =>
      client.fetch<ProcessTokenMintData>('auth/client/native/tokens', { ...options, auth: { type: 'none' }, method: 'POST' }),

    refreshSession: (data: RefreshSessionBody, options?: ConjoinCallOptions) =>
      client.fetch<RefreshSessionData>('auth/client/native/tokens/refresh', { ...options, auth: { type: 'none' }, method: 'POST', body: data }),

    processLogout: (options?: ConjoinCallOptions) =>
      client.fetch<ProcessLogoutData>('auth/client/native/logout', { ...options, auth: { type: 'none' }, method: 'POST' }),
  }
}
