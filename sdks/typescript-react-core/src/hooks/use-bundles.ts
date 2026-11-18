import { useCallback, useMemo } from 'react'
import type { BillingSelfCalls, ConjoinAuthApi } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { useSignedInQuery } from './internal/use-signed-in-query'

export type PriceBundleItem = Awaited<ReturnType<BillingSelfCalls['listPriceBundles']>>['data'][number]

const EMPTY_BUNDLES: PriceBundleItem[] = []

export function useBundles(entityId: string, referenceId?: string) {
  const read = useCallback(
    async (authApi: ConjoinAuthApi, transport: AuthTransport): Promise<PriceBundleItem[]> => {
      const page = await authApi
        .billingSelves(entityId)
        .listPriceBundles(
          referenceId ? { reference_id: referenceId } : undefined,
          transport.readSessionToken(),
          transport.sessionCallOptions('GET'),
        )
      return page.data
    },
    [entityId, referenceId],
  )

  const result = useSignedInQuery('billing-bundles', read, {
    keyParts: [entityId, referenceId ?? null],
    isEnabled: entityId.length > 0,
  })

  const bundles = result.data ?? EMPTY_BUNDLES

  return useMemo(
    () => ({ bundles, isLoading: !result.isLoaded, error: result.error }),
    [bundles, result.isLoaded, result.error],
  )
}
