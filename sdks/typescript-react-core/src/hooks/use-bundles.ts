import { useCallback, useMemo } from 'react'
import type { BillingSelfCalls } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { useBillingSelfQuery } from './internal/use-billing-self-query'

export type PriceBundleItem = Awaited<ReturnType<BillingSelfCalls['listPriceBundles']>>['data'][number]

const EMPTY_BUNDLES: PriceBundleItem[] = []

export function useBundles(entityId: string, referenceId?: string) {
  const read = useCallback(
    async (billing: BillingSelfCalls, transport: AuthTransport): Promise<PriceBundleItem[]> => {
      const page = await billing.listPriceBundles(
        referenceId ? { reference_id: referenceId } : undefined,
        transport.readSessionToken(),
        transport.sessionCallOptions('GET'),
      )
      return page.data
    },
    [referenceId],
  )

  const result = useBillingSelfQuery({ name: 'bundles', entityId, keyParts: [referenceId ?? null], read })

  const bundles = result.data ?? EMPTY_BUNDLES

  return useMemo(
    () => ({ bundles, isLoading: result.isLoading, error: result.error ?? null }),
    [bundles, result.isLoading, result.error],
  )
}
