import { createBillingEntitlementOverrides } from '@conjoin-cloud/sdk/billing'
import { useCallback, useMemo } from 'react'
import { collectPages } from './internal/collect-pages'
import { useConjoinClient } from './internal/use-conjoin-client'
import { useConjoinQuery } from './internal/use-conjoin-query'

type EntitlementOverridesApi = ReturnType<typeof createBillingEntitlementOverrides>
type EntitlementOverrideItem = Awaited<ReturnType<EntitlementOverridesApi['list']>>['data'][number]

type EntitlementCheckResult = {
  allowed: boolean
  limit?: number
}

const EMPTY_ENTITLEMENTS: EntitlementOverrideItem[] = []

export function useEntitlements(entityId: string) {
  const { client } = useConjoinClient()
  const api = useMemo(
    () => (entityId ? createBillingEntitlementOverrides(client.withScope({ billingEntityId: entityId })) : null),
    [client, entityId],
  )

  const queryFn = useCallback(async () => {
    if (api === null) return EMPTY_ENTITLEMENTS
    return collectPages(api.list())
  }, [api])

  const result = useConjoinQuery<EntitlementOverrideItem[]>({
    queryKey: ['conjoin', 'billing', 'entitlements', entityId],
    queryFn,
    enabled: !!entityId,
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
    () => ({ entitlements, isLoading: result.isLoading, error: result.error ?? null, check }),
    [entitlements, result.isLoading, result.error, check],
  )
}
