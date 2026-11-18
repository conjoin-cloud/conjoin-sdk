import type { QueryObserverResult } from '@tanstack/query-core'
import { useCallback } from 'react'
import type { BillingSelfCalls } from '../../auth/auth-api'
import type { AuthTransport } from '../../provider/types'
import { useAuthState } from './use-auth-state'
import { useConjoinClient } from './use-conjoin-client'
import { useConjoinQuery } from './use-conjoin-query'

export const BILLING_SELF_QUERY_KEY = ['conjoin', 'billing', 'self']

type BillingSelfRead<TData> = (billing: BillingSelfCalls, transport: AuthTransport) => Promise<TData>

type BillingSelfQueryOptions<TData> = {
  name: string
  entityId: string
  keyParts?: readonly unknown[]
  isEnabled?: boolean
  read: BillingSelfRead<TData>
}

export function useBillingSelfQuery<TData>({
  name,
  entityId,
  keyParts = [],
  isEnabled = true,
  read,
}: BillingSelfQueryOptions<TData>): QueryObserverResult<TData, Error> {
  const { authApi, transport } = useConjoinClient()
  const authState = useAuthState()
  const isSignedIn = authState.isLoaded && authState.isSignedIn
  const accountId = isSignedIn ? authState.accountId : null
  const sessionId = isSignedIn ? authState.sessionId : null

  const queryFn = useCallback(async (): Promise<TData> => {
    if (authApi === null) throw new Error('Sign-in is not configured for this project')
    return read(authApi.billingSelves(entityId), transport)
  }, [authApi, transport, read, entityId])

  return useConjoinQuery<TData>({
    queryKey: [...BILLING_SELF_QUERY_KEY, name, entityId, accountId, sessionId, ...keyParts],
    queryFn,
    enabled: isEnabled && isSignedIn && authApi !== null && entityId.length > 0,
  })
}
