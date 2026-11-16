import { useCallback } from 'react'
import type { ConjoinAuthApi } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { useConjoinClient } from './internal/use-conjoin-client'
import { useConjoinMutation } from './internal/use-conjoin-mutation'
import { useSignedInQuery } from './internal/use-signed-in-query'

export type ConjoinAccount = Awaited<ReturnType<ConjoinAuthApi['selves']['readProfile']>>
export type ConjoinAccountUpdate = Parameters<ConjoinAuthApi['selves']['updateProfile']>[0]

const ACCOUNT_QUERY_KEYS = [['conjoin', 'auth', 'account']]

const readAccount = (authApi: ConjoinAuthApi, transport: AuthTransport): Promise<ConjoinAccount> =>
  authApi.selves.readProfile(transport.readSessionToken(), transport.sessionCallOptions('GET'))

export function useAccount() {
  const result = useSignedInQuery('account', readAccount)

  return { isLoaded: result.isLoaded, isSignedIn: result.isSignedIn, account: result.data, error: result.error }
}

export function useUpdateAccount() {
  const { authApi, transport } = useConjoinClient()

  const mutationFn = useCallback(
    (update: ConjoinAccountUpdate): Promise<ConjoinAccount> => {
      if (authApi === null) return Promise.reject(new Error('Sign-in is not configured for this project'))
      return authApi.selves.updateProfile(update, transport.readSessionToken(), transport.sessionCallOptions('PATCH'))
    },
    [authApi, transport],
  )

  const mutation = useConjoinMutation({ mutationFn, invalidateKeys: ACCOUNT_QUERY_KEYS })

  return { update: mutation.mutateAsync, isPending: mutation.isPending, error: mutation.error }
}
