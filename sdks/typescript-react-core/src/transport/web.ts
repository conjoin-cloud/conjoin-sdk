import type { ConjoinCallOptions, HttpMethod } from '@conjoin-cloud/sdk'
import type { ConjoinAuthApi } from '../auth/auth-api'
import {
  AUTH_CODE_CHALLENGE_HEADER,
  AUTH_CODE_VERIFIER_HEADER,
  AUTH_STATE_HEADER,
  CSRF_TOKEN_HEADER,
} from '../auth/flow-headers'
import { createAuthFlowProof } from '../auth/flow-proof'
import { createRedirectFlowRegistry } from '../auth/redirect-flows'
import { readSessionUnlessRejected } from '../auth/session-errors'
import type { AuthFlowState, AuthSessionGrant, AuthTransport } from '../provider/types'

const CSRF_COOKIE_NAME = '__conjoin_auth_csrf'
const REFRESH_LOCK_NAME = 'conjoin-session-handshake'

function readCookie(name: string): string | null {
  if (typeof document === 'undefined') return null

  const prefix = `${name}=`

  for (const cookie of document.cookie.split('; ')) {
    if (!cookie.startsWith(prefix)) continue

    try {
      return decodeURIComponent(cookie.substring(prefix.length))
    } catch {
      return null
    }
  }

  return null
}

function readCsrfHeaders(): Record<string, string> {
  const csrfToken = readCookie(CSRF_COOKIE_NAME)

  return csrfToken ? { [CSRF_TOKEN_HEADER]: csrfToken } : {}
}

async function handshake(api: ConjoinAuthApi): Promise<AuthSessionGrant | null> {
  const session = await readSessionUnlessRejected(() => api.clients.processHandshake())

  if (session === null) return null

  return { accountId: session.account_id, sessionId: session.session_id, ttlSeconds: session.access_token_ttl_seconds }
}

const browserCrypto = {
  fillRandomBytes: (bytes: Uint8Array<ArrayBuffer>) => globalThis.crypto.getRandomValues(bytes),
  digestSha256: (bytes: Uint8Array<ArrayBuffer>) => globalThis.crypto.subtle.digest('SHA-256', bytes),
}

const readSessionStorage = () => (typeof sessionStorage === 'undefined' ? null : sessionStorage)

export function createWebTransport(): AuthTransport {
  const redirectFlows = createRedirectFlowRegistry(readSessionStorage)

  return {
    platform: 'web',

    restoreSession: handshake,

    refreshSession: handshake,

    finishFlow: handshake,

    async endSession(api: ConjoinAuthApi) {
      await readSessionUnlessRejected(() => api.clients.processLogout({ headers: readCsrfHeaders() }))
    },

    sessionCallOptions(method: HttpMethod): ConjoinCallOptions {
      return method === 'GET' ? {} : { headers: readCsrfHeaders() }
    },

    readSessionToken: () => undefined,

    flowCallOptions(flow: AuthFlowState): ConjoinCallOptions {
      return {
        headers: {
          [AUTH_STATE_HEADER]: flow.proof.state,
          [AUTH_CODE_VERIFIER_HEADER]: flow.proof.codeVerifier,
          [AUTH_CODE_CHALLENGE_HEADER]: flow.proof.codeChallenge,
        },
      }
    },

    createFlowProof: () => createAuthFlowProof(browserCrypto),

    saveRedirectFlow: redirectFlows.save,

    takeRedirectFlow: redirectFlows.take,

    async acquireRefreshLock<T>(fn: () => Promise<T>): Promise<T> {
      if (typeof navigator !== 'undefined' && 'locks' in navigator) {
        return navigator.locks.request(REFRESH_LOCK_NAME, fn)
      }

      return fn()
    },

    readAccessToken: () => null,
  }
}
