import { useMemo } from 'react'
import type { BillingSelfCalls } from '../auth/auth-api'
import type { AuthTransport } from '../provider/types'
import { collectPages } from './internal/collect-pages'
import { useBillingSelfQuery } from './internal/use-billing-self-query'

export type PaymentMethodItem = Awaited<ReturnType<BillingSelfCalls['listPaymentMethods']>>['data'][number]

const EMPTY_PAYMENT_METHODS: PaymentMethodItem[] = []

const readPaymentMethods = (billing: BillingSelfCalls, transport: AuthTransport): Promise<PaymentMethodItem[]> =>
  collectPages(billing.listPaymentMethods(undefined, transport.readSessionToken(), transport.sessionCallOptions('GET')))

export function usePaymentMethods(entityId: string) {
  const result = useBillingSelfQuery({ name: 'payment-methods', entityId, read: readPaymentMethods })

  const paymentMethods = result.data ?? EMPTY_PAYMENT_METHODS

  return useMemo(
    () => ({ paymentMethods, isLoading: result.isLoading, error: result.error ?? null }),
    [paymentMethods, result.isLoading, result.error],
  )
}
