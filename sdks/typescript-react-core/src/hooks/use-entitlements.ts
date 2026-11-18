import { useCallback, useMemo } from 'react'
import type { BillingSelfCalls } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { collectPages } from './internal/collect-pages'
import { useBillingSelfQuery } from './internal/use-billing-self-query'

type EntitlementOverrideItem = Awaited<ReturnType<BillingSelfCalls['listEntitlementOverrides']>>['data'][number]

type EntitlementCheckResult = {
  allowed: boolean
  limit?: number
}

const EMPTY_ENTITLEMENTS: EntitlementOverrideItem[] = []

const readEntitlements = (billing: BillingSelfCalls, transport: AuthTransport): Promise<EntitlementOverrideItem[]> =>
  collectPages(
    billing.listEntitlementOverrides(undefined, transport.readSessionToken(), transport.sessionCallOptions('GET')),
  )

export function useEntitlements(entityId: string) {
  const result = useBillingSelfQuery({ name: 'entitlements', entityId, read: readEntitlements })

  const entitlements = useMemo<EntitlementOverrideItem[]>(() => result.data ?? EMPTY_ENTITLEMENTS, [result.data])

  const check = useCallback(
    (featureId: string): EntitlementCheckResult => {
      const entry = entitlements.find(e => e.feature_id === featureId)
      if (!entry) return { allowed: false }
      const limit = entry.included_units ?? undefined
      return {
        allowed: entry.is_active === true,
        limit,
      }
    },
    [entitlements],
  )

  return useMemo(
    () => ({ entitlements, isLoading: result.isLoading, error: result.error ?? null, check }),
    [entitlements, result.isLoading, result.error, check],
  )
}
