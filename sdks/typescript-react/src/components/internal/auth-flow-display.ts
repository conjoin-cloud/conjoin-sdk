import type { AuthFlowResult, SignInStartBody } from '@conjoin-cloud/react-core'
import { ConjoinApiError, ConjoinNetworkError, ConjoinTimeoutError } from '@conjoin-cloud/sdk'

export type OAuthProvider = NonNullable<SignInStartBody['provider_key']>

const FIRST_PARTY_METHODS: ReadonlySet<string> = new Set([
  'email',
  'email_password',
  'password',
  'phone',
  'passkey',
  'totp',
  'magic_link',
  'saml',
])

export const PASSWORD_METHODS: ReadonlySet<string> = new Set(['email_password', 'password'])

export function readOAuthProviders(signInMethods: readonly string[]): OAuthProvider[] {
  return signInMethods.filter(method => !FIRST_PARTY_METHODS.has(method)) as OAuthProvider[]
}

export function readSafeRedirectUrl(result: AuthFlowResult): string | null {
  const redirectUrl = result.redirect_url
  if (!redirectUrl) return null

  try {
    return new URL(redirectUrl).protocol === 'https:' ? redirectUrl : null
  } catch {
    return null
  }
}

export function readFlowErrorMessage(error: unknown, fallback: string): string {
  if (error instanceof ConjoinNetworkError || error instanceof ConjoinTimeoutError) {
    return 'A network error occurred. Please check your connection and try again.'
  }
  return error instanceof ConjoinApiError && error.message ? error.message : fallback
}

export type MfaMethod = 'totp' | 'phone_verification_code'

export const readMfaMethod = (result: AuthFlowResult): MfaMethod =>
  result.mfa?.method === 'phone_verification_code' ? 'phone_verification_code' : 'totp'
