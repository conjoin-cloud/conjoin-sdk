import { cookies, headers } from 'next/headers'
import { cache } from 'react'
import { CONJOIN_SESSION_TOKEN_COOKIE, verifyToken } from '../server/tokens'
import { resolveConfig, resolveTokenVerificationTarget } from './config'
import type { AuthObject, NextAdapterConfig } from './types'

async function resolveAuth(overrides?: Partial<NextAdapterConfig>): Promise<AuthObject | null> {
  const config = resolveConfig(overrides)

  const headerStore = await headers()
  const cookieStore = await cookies()

  const bearerHeader = headerStore.get('authorization')
  const bearerToken = bearerHeader?.startsWith('Bearer ') ? bearerHeader.slice(7) : null

  const cookieToken = cookieStore.get(CONJOIN_SESSION_TOKEN_COOKIE)?.value

  const token = bearerToken ?? cookieToken
  if (!token) return null

  const { jwksUrl, issuer } = await resolveTokenVerificationTarget(config)

  try {
    const verified = await verifyToken(token, { jwksUrl, issuer })

    return {
      accountId: verified.accountId,
      sessionId: verified.sessionId,
      organizationId: verified.organizationId,
      organizationRoles: verified.organizationRoles,
      getToken: () => token,
    }
  } catch {
    return null
  }
}

export const auth = cache(resolveAuth)
