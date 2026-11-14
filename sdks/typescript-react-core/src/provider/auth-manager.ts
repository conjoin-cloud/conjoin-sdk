import type { ConjoinAuthApi } from '../auth/auth-api'
import { isSessionRejection } from '../auth/session-errors'
import type { AuthFlowState, AuthSessionGrant, AuthTransport, ConjoinAuthState } from './types'

type AuthManagerOptions = {
  api: ConjoinAuthApi | null
  transport: AuthTransport
  onStateChange: (state: ConjoinAuthState) => void
}

const REFRESH_AT_TTL_FRACTION = 0.75
const MIN_REFRESH_DELAY_MS = 5_000
const FIRST_RETRY_DELAY_MS = 1_000
const MAX_RETRY_DELAY_MS = 30_000
const SIGNED_OUT: ConjoinAuthState = { isLoaded: true, isSignedIn: false }

type ActiveOrganization = { organizationId: string | null; organizationRoles: string[] }

const NO_ORGANIZATION: ActiveOrganization = { organizationId: null, organizationRoles: [] }

function refreshDelayMs(ttlSeconds: number): number {
  if (!Number.isFinite(ttlSeconds) || ttlSeconds <= 0) return MIN_REFRESH_DELAY_MS

  return Math.max(ttlSeconds * 1000 * REFRESH_AT_TTL_FRACTION, MIN_REFRESH_DELAY_MS)
}

export function createAuthManager({ api, transport, onStateChange }: AuthManagerOptions) {
  let currentState: ConjoinAuthState = { isLoaded: false }
  let timer: ReturnType<typeof setTimeout> | null = null
  let pendingRefresh: Promise<void> | null = null
  let pendingSignOut: Promise<void> | null = null
  let sessionTail: Promise<unknown> = Promise.resolve()
  let sessionEnded = false
  let retryDelayMs = FIRST_RETRY_DELAY_MS
  let generation = 0
  let isDestroyed = false

  function setState(next: ConjoinAuthState) {
    if (isDestroyed) return
    currentState = next
    onStateChange(next)
  }

  function clearTimer() {
    if (timer !== null) clearTimeout(timer)
    timer = null
  }

  function schedule(delayMs: number, task: () => Promise<void>) {
    clearTimer()
    if (isDestroyed) return
    timer = setTimeout(() => {
      timer = null
      task().catch(() => undefined)
    }, delayMs)
  }

  function scheduleRetry(task: () => Promise<void>) {
    schedule(retryDelayMs, task)
    retryDelayMs = Math.min(retryDelayMs * 2, MAX_RETRY_DELAY_MS)
  }

  function withSessionLock<T>(task: () => Promise<T>): Promise<T> {
    const pending = sessionTail.then(() => transport.acquireRefreshLock(task))
    sessionTail = pending.catch(() => undefined)
    return pending
  }

  async function readActiveOrganization(authApi: ConjoinAuthApi): Promise<ActiveOrganization> {
    try {
      const organization = await authApi.selves.readActiveOrganization(transport.sessionCallOptions('GET'))

      return {
        organizationId: organization.active_organization_id,
        organizationRoles: organization.active_organization_roles,
      }
    } catch (error) {
      if (isSessionRejection(error)) throw error
      return NO_ORGANIZATION
    }
  }

  async function applyGrant(authApi: ConjoinAuthApi, grant: AuthSessionGrant | null, startedAt: number) {
    if (startedAt !== generation || isDestroyed) return
    if (grant === null) {
      if (startedAt === generation) {
        clearTimer()
        setState(SIGNED_OUT)
      }
      return
    }

    const organization = await readActiveOrganization(authApi)

    if (startedAt !== generation) return

    retryDelayMs = FIRST_RETRY_DELAY_MS
    setState({
      isLoaded: true,
      isSignedIn: true,
      accountId: grant.accountId,
      sessionId: grant.sessionId,
      organizationId: organization.organizationId,
      organizationRoles: organization.organizationRoles,
    })
    if (startedAt === generation) schedule(refreshDelayMs(grant.ttlSeconds), refresh)
  }

  async function runSessionStep(read: (authApi: ConjoinAuthApi) => Promise<AuthSessionGrant | null>) {
    if (api === null || isDestroyed || sessionEnded) return

    const startedAt = ++generation

    try {
      const grant = await withSessionLock(() =>
        startedAt === generation && !isDestroyed ? read(api) : Promise.resolve(null),
      )
      await applyGrant(api, grant, startedAt)
    } catch (error) {
      if (startedAt !== generation) return
      if (isSessionRejection(error)) {
        clearTimer()
        setState(SIGNED_OUT)
        return
      }
      if (!currentState.isLoaded) setState(SIGNED_OUT)
      if (startedAt !== generation) return
      scheduleRetry(currentState.isLoaded && currentState.isSignedIn ? refresh : restore)
      throw error
    }
  }

  async function restore(): Promise<void> {
    await runSessionStep(authApi => transport.restoreSession(authApi)).catch(() => undefined)
  }

  function refresh(): Promise<void> {
    if (pendingRefresh) return pendingRefresh

    pendingRefresh = runSessionStep(authApi => transport.refreshSession(authApi)).finally(() => {
      pendingRefresh = null
    })

    return pendingRefresh
  }

  function initialize() {
    if (api === null) {
      setState(SIGNED_OUT)
      return
    }
    void restore()
  }

  async function completeFlow(flow: AuthFlowState): Promise<void> {
    sessionEnded = false
    await runSessionStep(authApi => transport.finishFlow(authApi, flow))
  }

  async function switchOrganization(organizationId: string | null): Promise<void> {
    if (api === null) throw new Error('Sign-in is not configured for this project')

    await api.selves.updateActiveOrganization(
      { organization_id: organizationId },
      transport.sessionCallOptions('PATCH'),
    )
    await refresh()
  }

  function signOut(): Promise<void> {
    if (pendingSignOut !== null) return pendingSignOut
    if (isDestroyed) return Promise.resolve()
    const startedAt = ++generation
    sessionEnded = true
    clearTimer()
    const authApi = api
    const pending = withSessionLock(async () => {
      if (authApi !== null) await transport.endSession(authApi)
    }).finally(() => {
      if (pendingSignOut === pending) pendingSignOut = null
      if (startedAt === generation) setState(SIGNED_OUT)
    })
    pendingSignOut = pending
    return pending
  }

  function destroy() {
    isDestroyed = true
    generation++
    clearTimer()
    pendingRefresh = null
  }

  return {
    initialize,
    getState: () => currentState,
    getToken: () => (currentState.isLoaded && currentState.isSignedIn ? transport.readAccessToken() : null),
    completeFlow,
    switchOrganization,
    refresh,
    signOut,
    destroy,
  }
}

export type AuthManager = ReturnType<typeof createAuthManager>
