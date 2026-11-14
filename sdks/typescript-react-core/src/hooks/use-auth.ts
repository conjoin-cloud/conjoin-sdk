import { useCallback, useContext } from 'react'
import { ConjoinAuthActionsContext, ConjoinAuthStateContext } from '../provider/contexts'

const NO_ROLES: string[] = []

export function useAuth() {
  const authState = useContext(ConjoinAuthStateContext)
  const actions = useContext(ConjoinAuthActionsContext)
  if (!authState || !actions) {
    throw new Error('useAuth must be used within a ConjoinProvider')
  }

  const { getToken, signOut } = actions
  const isSignedIn = authState.isLoaded && authState.isSignedIn
  const organizationRoles = authState.isLoaded && authState.isSignedIn ? authState.organizationRoles : NO_ROLES

  const has = useCallback(
    (params: { role: string }) => isSignedIn && organizationRoles.includes(params.role),
    [isSignedIn, organizationRoles],
  )

  if (!authState.isLoaded) {
    return {
      isLoaded: false as const,
      isSignedIn: undefined,
      accountId: undefined,
      sessionId: undefined,
      organizationId: undefined,
      organizationRoles: undefined,
      getToken,
      signOut,
      has,
    }
  }

  if (!authState.isSignedIn) {
    return {
      isLoaded: true as const,
      isSignedIn: false as const,
      accountId: null,
      sessionId: null,
      organizationId: null,
      organizationRoles: NO_ROLES,
      getToken,
      signOut,
      has,
    }
  }

  return {
    isLoaded: true as const,
    isSignedIn: true as const,
    accountId: authState.accountId,
    sessionId: authState.sessionId,
    organizationId: authState.organizationId,
    organizationRoles: authState.organizationRoles,
    getToken,
    signOut,
    has,
  }
}
