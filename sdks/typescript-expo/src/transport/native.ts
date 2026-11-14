import {
  AUTH_CODE_CHALLENGE_HEADER,
  AUTH_CODE_VERIFIER_HEADER,
  AUTH_STATE_HEADER,
  type AuthClientHandle,
  type AuthFlowState,
  type AuthSessionGrant,
  type AuthTransport,
  CLIENT_HANDLE_HEADER,
  type ConjoinAuthApi,
  createAuthFlowProof,
  createRedirectFlowRegistry,
  encodeClientHandle,
  isSessionRejection,
} from '@conjoin-cloud/react-core'
import type { ConjoinCallOptions } from '@conjoin-cloud/sdk'
import * as v from 'valibot'
import { loadFlowCrypto, loadSecureStore } from './native-modules'

const LEGACY_ACCESS_TOKEN_KEY = 'conjoin_access_token'
const REFRESH_TOKEN_KEY = 'conjoin_refresh_token'
const CLIENT_HANDLE_KEY = 'conjoin_client_handle'

const identifier = v.pipe(v.string(), v.minLength(1), v.maxLength(256), v.regex(/^[\w.:-]+$/))
const StoredClientHandleSchema = v.object({ client_id: identifier, reference_id: identifier })

type NativeSessionTokens = Awaited<ReturnType<ConjoinAuthApi['nativeFlows']['processTokenMint']>>

type NativeSession = {
  accessToken: string | null
  refreshToken: string | null
  clientHandle: AuthClientHandle | null
}

let refreshLockTail: Promise<unknown> = Promise.resolve()

function readStoredClientHandle(raw: string | null): AuthClientHandle | null {
  if (raw === null) return null

  try {
    const parsed = v.safeParse(StoredClientHandleSchema, JSON.parse(raw))
    return parsed.success ? parsed.output : null
  } catch {
    return null
  }
}

export function createNativeTransport(): AuthTransport {
  const session: NativeSession = { accessToken: null, refreshToken: null, clientHandle: null }
  let hasLoadedStore = false
  const redirectFlows = createRedirectFlowRegistry(() => null)

  async function loadStoredSession(): Promise<void> {
    if (hasLoadedStore) return

    const store = await loadSecureStore()
    const [refreshToken, clientHandle] = await Promise.all([
      store.getItemAsync(REFRESH_TOKEN_KEY),
      store.getItemAsync(CLIENT_HANDLE_KEY),
    ])

    session.refreshToken = session.refreshToken ?? refreshToken
    session.clientHandle = session.clientHandle ?? readStoredClientHandle(clientHandle)
    hasLoadedStore = true
  }

  async function keepTokens(
    tokens: NativeSessionTokens,
    clientHandle: AuthClientHandle | null,
  ): Promise<AuthSessionGrant> {
    session.accessToken = tokens.access_token
    session.refreshToken = tokens.refresh_token
    session.clientHandle = clientHandle ?? session.clientHandle

    const store = await loadSecureStore()
    await Promise.all([
      store.deleteItemAsync(LEGACY_ACCESS_TOKEN_KEY),
      store.setItemAsync(REFRESH_TOKEN_KEY, tokens.refresh_token),
      session.clientHandle
        ? store.setItemAsync(CLIENT_HANDLE_KEY, JSON.stringify(session.clientHandle))
        : store.deleteItemAsync(CLIENT_HANDLE_KEY),
    ])

    return { accountId: tokens.account_id, sessionId: tokens.session_id, ttlSeconds: tokens.expires_in }
  }

  async function forgetTokens(): Promise<void> {
    session.accessToken = null
    session.refreshToken = null
    session.clientHandle = null

    const store = await loadSecureStore()
    await Promise.all([
      store.deleteItemAsync(LEGACY_ACCESS_TOKEN_KEY),
      store.deleteItemAsync(REFRESH_TOKEN_KEY),
      store.deleteItemAsync(CLIENT_HANDLE_KEY),
    ])
  }

  async function rotateTokens(api: ConjoinAuthApi): Promise<AuthSessionGrant | null> {
    await loadStoredSession()

    const refreshToken = session.refreshToken
    if (refreshToken === null) return null

    try {
      const tokens = await api.nativeFlows.refreshSession({ refresh_token: refreshToken })
      return await keepTokens(tokens, null)
    } catch (error) {
      if (!isSessionRejection(error)) throw error
      await forgetTokens()
      return null
    }
  }

  return {
    platform: 'native',

    restoreSession: rotateTokens,

    refreshSession: rotateTokens,

    async finishFlow(api: ConjoinAuthApi, flow: AuthFlowState): Promise<AuthSessionGrant | null> {
      if (flow.clientHandle === null) {
        throw new Error('The sign-in finished without a client handle, so the app cannot mint a session')
      }

      const tokens = await api.nativeFlows.processTokenMint({
        headers: {
          [CLIENT_HANDLE_HEADER]: encodeClientHandle(flow.clientHandle),
          [AUTH_CODE_VERIFIER_HEADER]: flow.proof.codeVerifier,
        },
      })

      return keepTokens(tokens, flow.clientHandle)
    },

    async endSession(api: ConjoinAuthApi): Promise<void> {
      try {
        await loadStoredSession()
        const clientHandle = session.clientHandle
        if (clientHandle !== null) {
          await api.nativeFlows.processLogout({ headers: { [CLIENT_HANDLE_HEADER]: encodeClientHandle(clientHandle) } })
        }
      } catch (error) {
        if (!isSessionRejection(error)) throw error
      } finally {
        await forgetTokens()
      }
    },

    sessionCallOptions(): ConjoinCallOptions {
      return session.accessToken ? { auth: { type: 'bearer', token: session.accessToken } } : {}
    },

    flowCallOptions(flow: AuthFlowState): ConjoinCallOptions {
      return {
        headers: {
          [AUTH_STATE_HEADER]: flow.proof.state,
          [AUTH_CODE_CHALLENGE_HEADER]: flow.proof.codeChallenge,
          ...(flow.clientHandle ? { [CLIENT_HANDLE_HEADER]: encodeClientHandle(flow.clientHandle) } : {}),
        },
      }
    },

    createFlowProof: async () => createAuthFlowProof(await loadFlowCrypto()),

    saveRedirectFlow: redirectFlows.save,

    takeRedirectFlow: redirectFlows.take,

    acquireRefreshLock<T>(fn: () => Promise<T>): Promise<T> {
      const run = refreshLockTail.then(fn, fn)
      refreshLockTail = run.catch(() => undefined)
      return run
    },

    readAccessToken: () => session.accessToken,
  }
}
