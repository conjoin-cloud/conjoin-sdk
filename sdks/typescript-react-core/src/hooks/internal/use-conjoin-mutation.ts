import { MutationObserver, type MutationObserverResult, type QueryKey } from '@tanstack/query-core'
import { useCallback, useEffect, useMemo, useState, useSyncExternalStore } from 'react'
import { useConjoinClient } from './use-conjoin-client'

type ConjoinMutationOptions<TData, TVariables, TError = Error> = {
  mutationFn: (variables: TVariables) => Promise<TData>
  invalidateKeys?: QueryKey[]
  onSuccess?: (data: TData, variables: TVariables) => void
  onError?: (error: TError, variables: TVariables) => void
}

type ConjoinMutationResult<TData, TVariables, TError = Error> = {
  mutate: (variables: TVariables) => void
  mutateAsync: (variables: TVariables) => Promise<TData>
  data: TData | undefined
  error: TError | null
  isIdle: boolean
  isPending: boolean
  isSuccess: boolean
  isError: boolean
  reset: () => void
}

export function useConjoinMutation<TData, TVariables, TError = Error>(
  options: ConjoinMutationOptions<TData, TVariables, TError>,
): ConjoinMutationResult<TData, TVariables, TError> {
  const { queryClient } = useConjoinClient()
  const { mutationFn, invalidateKeys, onSuccess, onError } = options

  const observerOptions = useMemo(
    () => ({
      mutationFn,
      onSuccess: async (data: TData, variables: TVariables) => {
        await Promise.all((invalidateKeys ?? []).map(key => queryClient.invalidateQueries({ queryKey: key })))
        onSuccess?.(data, variables)
      },
      onError: (error: TError, variables: TVariables) => {
        onError?.(error, variables)
      },
    }),
    [queryClient, mutationFn, invalidateKeys, onSuccess, onError],
  )

  const [observer] = useState(() => new MutationObserver<TData, TError, TVariables>(queryClient, observerOptions))

  useEffect(() => {
    observer.setOptions(observerOptions)
  }, [observer, observerOptions])

  const subscribe = useMemo(() => {
    return (onStoreChange: () => void) => {
      return observer.subscribe(() => {
        onStoreChange()
      })
    }
  }, [observer])

  const result = useSyncExternalStore(
    subscribe,
    () => observer.getCurrentResult(),
    () => observer.getCurrentResult(),
  ) as MutationObserverResult<TData, TError, TVariables>

  const mutate = useCallback(
    (variables: TVariables) => {
      observer.mutate(variables).catch(() => undefined)
    },
    [observer],
  )

  const mutateAsync = useCallback((variables: TVariables): Promise<TData> => observer.mutate(variables), [observer])

  const reset = useCallback(() => observer.reset(), [observer])

  return {
    mutate,
    mutateAsync,
    data: result.data,
    error: result.error,
    isIdle: result.status === 'idle',
    isPending: result.status === 'pending',
    isSuccess: result.status === 'success',
    isError: result.status === 'error',
    reset,
  }
}
