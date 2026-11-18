import { cookies, headers } from 'next/headers'
import { cache } from 'react'
import { CONJOIN_SESSION_TOKEN_COOKIE } from '../server/tokens'
import { resolveConfig } from './config'
import type { AuthObject, NextAdapterConfig } from './types'
import { verifyAuthObject } from './verify-auth'

async function resolveAuth(overrides?: Partial<NextAdapterConfig>): Promise<AuthObject | null> {
  const config = resolveConfig(overrides)

  const headerStore = await headers()
  const cookieStore = await cookies()

  const bearerHeader = headerStore.get('authorization')
  const bearerToken = bearerHeader?.startsWith('Bearer ') ? bearerHeader.slice(7) : null

  const cookieToken = cookieStore.get(CONJOIN_SESSION_TOKEN_COOKIE)?.value

  const token = bearerToken ?? cookieToken
  if (!token) return null

  return verifyAuthObject({ token, config })
}

export const auth = cache(resolveAuth)
