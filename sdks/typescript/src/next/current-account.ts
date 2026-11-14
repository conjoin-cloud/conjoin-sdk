import { headers } from 'next/headers'
import { createConjoinClient } from '../core/client'
import { getConjoinRequestIdFromHeaders } from '../core/request-tracing'
import { createAuthSelves } from '../generated/frontend/auth-self'
import { auth } from './auth'
import { resolveConfig } from './config'
import type { NextAdapterConfig } from './types'

export type CurrentAccount = Awaited<ReturnType<ReturnType<typeof createAuthSelves>['readProfile']>>

export async function currentAccount(overrides?: Partial<NextAdapterConfig>): Promise<CurrentAccount | null> {
  const authObj = await auth(overrides)
  if (!authObj) return null

  const config = resolveConfig(overrides)
  const headerStore = await headers()
  const conjoinRequestId = getConjoinRequestIdFromHeaders(headerStore)
  const client = createConjoinClient({
    apiKey: config.secretKey,
    ...(conjoinRequestId ? { conjoinRequestId } : {}),
  })

  return createAuthSelves(client).readProfile({ auth: { type: 'bearer', token: authObj.getToken() } })
}
