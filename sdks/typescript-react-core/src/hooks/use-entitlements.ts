import { useCallback, useMemo } from 'react'
import type { BillingSelfCalls, ConjoinAuthApi } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { collectPages } from './internal/collect-pages'
import { useSignedInQuery } from './internal/use-signed-in-query'

type EntitlementOverrideItem = Awaited<ReturnType<BillingSelfCalls['listEntitlementOverrides']>>['data'][number]

type EntitlementCheckResult = {
  allowed: boolean
  limit?: number
}

const EMPTY_ENTITLEMENTS: EntitlementOverrideItem[] = []

export function useEntitlements(entityId: string) {
  const read = useCallback(
    (authApi: ConjoinAuthApi, transport: AuthTransport): Promise<EntitlementOverrideItem[]> =>
      collectPages(
        authApi
          .billingSelves(entityId)
          .listEntitlementOverrides(undefined, transport.readSessionToken(), transport.sessionCallOptions('GET')),
      ),
    [entityId],
  )

  const result = useSignedInQuery('billing-entitlements', read, {
    keyParts: [entityId],
    isEnabled: entityId.length > 0,
  })

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
    () => ({ entitlements, isLoading: !result.isLoaded, error: result.error, check }),
    [entitlements, result.isLoaded, result.error, check],
  )
}
