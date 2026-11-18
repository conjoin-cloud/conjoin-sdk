import { useCallback } from 'react'
import type { BillingSelfCalls } from '../auth/auth-api'
import { BILLING_SELF_QUERY_KEY } from './internal/use-billing-self-query'
import { useConjoinClient } from './internal/use-conjoin-client'
import { useConjoinMutation } from './internal/use-conjoin-mutation'

type DeactivateBody = Parameters<BillingSelfCalls['deactivatePriceBundle']>[1]
type CardSetupBody = Parameters<BillingSelfCalls['createPaymentMethod']>[0]

type ActivateParams = {
  entityId: string
  referenceId: string
  paymentMethodId: string
}

type DeactivateParams = {
  entityId: string
  activationId: string
  data?: DeactivateBody
}

type CardSetupParams = CardSetupBody & {
  entityId: string
}

const BILLING_SELF_INVALIDATE_KEYS = [BILLING_SELF_QUERY_KEY]

const SIGN_IN_NOT_CONFIGURED_ERROR = 'Sign-in is not configured for this project'

export function useCheckout() {
  const { authApi, transport } = useConjoinClient()

  const activateMutation = useConjoinMutation({
    mutationFn: useCallback(
      async ({ entityId, referenceId, paymentMethodId }: ActivateParams) => {
        if (authApi === null) throw new Error(SIGN_IN_NOT_CONFIGURED_ERROR)
        return authApi
          .billingSelves(entityId)
          .activatePriceBundles(
            { payment_method_id: paymentMethodId, bundles: [{ bundle_reference: referenceId }] },
            transport.readSessionToken(),
            transport.sessionCallOptions('POST'),
          )
      },
      [authApi, transport],
    ),
    invalidateKeys: BILLING_SELF_INVALIDATE_KEYS,
  })

  const deactivateMutation = useConjoinMutation({
    mutationFn: useCallback(
      async ({ entityId, activationId, data }: DeactivateParams) => {
        if (authApi === null) throw new Error(SIGN_IN_NOT_CONFIGURED_ERROR)
        return authApi
          .billingSelves(entityId)
          .deactivatePriceBundle(
            activationId,
            data ?? {},
            transport.readSessionToken(),
            transport.sessionCallOptions('POST'),
          )
      },
      [authApi, transport],
    ),
    invalidateKeys: BILLING_SELF_INVALIDATE_KEYS,
  })

  const cardSetupMutation = useConjoinMutation({
    mutationFn: useCallback(
      async ({ entityId, ...body }: CardSetupParams) => {
        if (authApi === null) throw new Error(SIGN_IN_NOT_CONFIGURED_ERROR)
        return authApi
          .billingSelves(entityId)
          .createPaymentMethod(body, transport.readSessionToken(), transport.sessionCallOptions('POST'))
      },
      [authApi, transport],
    ),
    invalidateKeys: BILLING_SELF_INVALIDATE_KEYS,
  })

  return {
    activate: activateMutation.mutateAsync,
    deactivate: deactivateMutation.mutateAsync,
    startCardSetup: cardSetupMutation.mutateAsync,
    isLoading: activateMutation.isPending || deactivateMutation.isPending || cardSetupMutation.isPending,
    error: activateMutation.error ?? deactivateMutation.error ?? cardSetupMutation.error ?? null,
  }
}

export type { ActivateParams, CardSetupParams, DeactivateParams }
