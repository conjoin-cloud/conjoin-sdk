import { createBillingPriceBundles } from '@conjoin-cloud/sdk/billing'
import { useCallback } from 'react'
import { useConjoinClient } from './internal/use-conjoin-client'
import { useConjoinMutation } from './internal/use-conjoin-mutation'

type BillingApi = ReturnType<typeof createBillingPriceBundles>
type ActivateBody = Parameters<BillingApi['activate']>[0]
type DeactivateBody = Parameters<BillingApi['deactivate']>[1]
type ActivateData = Omit<ActivateBody, 'bundles'>

type ActivateParams = {
  entityId: string
  referenceId: string
  data?: ActivateData
}

type DeactivateParams = {
  entityId: string
  activationId: string
  data: DeactivateBody
}

export function useCheckout() {
  const { client } = useConjoinClient()

  const activateMutation = useConjoinMutation({
    mutationFn: useCallback(
      async (params: ActivateParams) => {
        const api = createBillingPriceBundles(client.withScope({ billingEntityId: params.entityId }))
        return api.activate({
          ...params.data,
          bundles: [{ bundle_reference: params.referenceId }],
        })
      },
      [client],
    ),
    invalidateKeys: [['conjoin', 'billing']],
  })

  const deactivateMutation = useConjoinMutation({
    mutationFn: useCallback(
      async (params: DeactivateParams) => {
        const api = createBillingPriceBundles(client.withScope({ billingEntityId: params.entityId }))
        return api.deactivate(params.activationId, params.data)
      },
      [client],
    ),
    invalidateKeys: [['conjoin', 'billing']],
  })

  return {
    activate: activateMutation.mutateAsync,
    deactivate: deactivateMutation.mutateAsync,
    isLoading: activateMutation.isPending || deactivateMutation.isPending,
    error: activateMutation.error ?? deactivateMutation.error ?? null,
  }
}

export type { ActivateParams, DeactivateParams }
