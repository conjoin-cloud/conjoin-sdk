import { headers } from 'next/headers'
import { createConjoinClient } from '../core/client'
import { ConjoinConfigurationError } from '../core/errors'
import { getConjoinRequestIdFromHeaders } from '../core/request-tracing'
import { createAuthSelves } from '../generated/frontend/auth-self'
import { auth } from './auth'
import { resolveAuthDomain, resolveConfig } from './config'
import type { NextAdapterConfig } from './types'

export type CurrentAccount = Awaited<ReturnType<ReturnType<typeof createAuthSelves>['readProfile']>>

function readClientKey(config: NextAdapterConfig): { publishableKey: string } | { apiKey: string } {
  if (config.publishableKey) return { publishableKey: config.publishableKey }
  if (config.secretKey) return { apiKey: config.secretKey }

  throw new ConjoinConfigurationError('currentAccount needs a publishableKey or a secretKey')
}

export async function currentAccount(overrides?: Partial<NextAdapterConfig>): Promise<CurrentAccount | null> {
  const authObj = await auth(overrides)
  if (!authObj) return null

  const config = resolveConfig(overrides)
  const authDomain = await resolveAuthDomain(config)
  const headerStore = await headers()
  const conjoinRequestId = getConjoinRequestIdFromHeaders(headerStore)
  const client = createConjoinClient({
    ...readClientKey(config),
    baseUrl: `https://${authDomain}`,
    ...(conjoinRequestId ? { conjoinRequestId } : {}),
  })

  return createAuthSelves(client).readProfile({ auth: { type: 'bearer', token: authObj.getToken() } })
}
