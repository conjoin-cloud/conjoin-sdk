import { useCallback } from 'react'
import type { ConjoinAuthApi } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { collectPages } from './internal/collect-pages'
import { useAuthState } from './internal/use-auth-state'
import { useConjoinClient } from './internal/use-conjoin-client'
import { useConjoinMutation } from './internal/use-conjoin-mutation'
import { useSignedInQuery } from './internal/use-signed-in-query'

export type ConjoinSession = Awaited<ReturnType<ConjoinAuthApi['selves']['listSessions']>>['data'][number]

const SESSION_QUERY_KEYS = [['conjoin', 'auth', 'sessions']]
const NO_SESSIONS: ConjoinSession[] = []

const readActiveSessions = (authApi: ConjoinAuthApi, transport: AuthTransport): Promise<ConjoinSession[]> =>
  collectPages(authApi.selves.listSessions({ status: 'active' }, transport.sessionCallOptions('GET')))

export function useSessions() {
  const authState = useAuthState()
  const { authApi, transport } = useConjoinClient()
  const result = useSignedInQuery('sessions', readActiveSessions)
  const currentSessionId = authState.isLoaded && authState.isSignedIn ? authState.sessionId : null

  const revokeSession = useCallback(
    async (sessionId: string): Promise<void> => {
      if (authApi === null) throw new Error('Sign-in is not configured for this project')
      if (sessionId === currentSessionId) throw new Error('Sign out to end the current session')
      await authApi.selves.revokeSession(sessionId, transport.sessionCallOptions('DELETE'))
    },
    [authApi, transport, currentSessionId],
  )

  const revocation = useConjoinMutation({ mutationFn: revokeSession, invalidateKeys: SESSION_QUERY_KEYS })

  return {
    isLoaded: result.isLoaded,
    isSignedIn: result.isSignedIn,
    currentSessionId,
    sessions: result.data ?? NO_SESSIONS,
    error: result.error,
    revoke: revocation.mutateAsync,
    isRevoking: revocation.isPending,
  }
}

export function useSession() {
  const { isLoaded, isSignedIn, sessions, currentSessionId, error } = useSessions()

  return {
    isLoaded,
    isSignedIn,
    session: sessions.find(session => session.session_id === currentSessionId) ?? null,
    error,
  }
}
