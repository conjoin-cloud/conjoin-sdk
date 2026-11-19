import type { QueryObserverResult } from '@tanstack/query-core'
import { useCallback } from 'react'
import type { ConjoinAuthApi } from '../../auth/auth-api'
import type { AuthTransport } from '../../provider/types'
import { useAuthState } from './use-auth-state'
import { useConjoinClient } from './use-conjoin-client'
import { useConjoinQuery } from './use-conjoin-query'

type SignedInRead<TData> = (authApi: ConjoinAuthApi, transport: AuthTransport) => Promise<TData>

export type SignedInQuery<TData> =
  | { isLoaded: false; isSignedIn: undefined; data: undefined; error: null }
  | { isLoaded: true; isSignedIn: false; data: null; error: null }
  | { isLoaded: boolean; isSignedIn: true; data: TData | null; error: Error | null }

type SignedInQueryOptions = {
  keyParts?: readonly unknown[]
  isEnabled?: boolean
}

export function useSignedInQuery<TData>(
  name: string,
  read: SignedInRead<TData>,
  { keyParts = [], isEnabled = true }: SignedInQueryOptions = {},
): SignedInQuery<TData> {
  const { authApi, transport } = useConjoinClient()
  const authState = useAuthState()
  const isSignedIn = authState.isLoaded && authState.isSignedIn
  const accountId = isSignedIn ? authState.accountId : null
  const sessionId = isSignedIn ? authState.sessionId : null
  const organizationId = isSignedIn ? authState.organizationId : null

  const queryFn = useCallback(async (): Promise<TData> => {
    if (authApi === null) throw new Error('Sign-in is not configured for this project')
    return read(authApi, transport)
  }, [authApi, transport, read])

  const result: QueryObserverResult<TData, Error> = useConjoinQuery<TData>({
    queryKey: ['conjoin', 'auth', name, accountId, sessionId, organizationId, ...keyParts],
    queryFn,
    enabled: isEnabled && isSignedIn && authApi !== null,
  })

  if (!authState.isLoaded) return { isLoaded: false, isSignedIn: undefined, data: undefined, error: null }
  if (!authState.isSignedIn) return { isLoaded: true, isSignedIn: false, data: null, error: null }

  return { isLoaded: !result.isLoading, isSignedIn: true, data: result.data ?? null, error: result.error ?? null }
}
