import type { NextRequest } from 'next/server'
import { CONJOIN_CLIENT_HANDLE_COOKIE, CONJOIN_SESSION_TOKEN_COOKIE, verifyToken } from '../server/tokens'
import { resolveConfig, resolveTokenVerificationTarget } from './config'
import type { AuthObject, NextAdapterConfig } from './types'

const CLIENT_HANDLE_MAX_BYTES = 2048
const CLIENT_HANDLE_IDENTIFIER_PATTERN = /^[\w.:-]{1,256}$/

type ClientHandle = {
  clientId: string
  referenceId: string
}

type ProxyResult = Response | undefined

type ProxyHandler = (auth: AuthObject | null, req: NextRequest) => ProxyResult | Promise<ProxyResult>

function isClientHandleIdentifier(value: unknown): value is string {
  return typeof value === 'string' && CLIENT_HANDLE_IDENTIFIER_PATTERN.test(value)
}

function parseClientHandle(cookieValue: string | undefined): ClientHandle | null {
  if (!cookieValue || new TextEncoder().encode(cookieValue).byteLength > CLIENT_HANDLE_MAX_BYTES) return null

  try {
    const parsed: unknown = JSON.parse(cookieValue)
    if (typeof parsed !== 'object' || parsed === null || Array.isArray(parsed)) return null

    const { client_id: clientId, reference_id: referenceId } = parsed as Record<string, unknown>
    if (!isClientHandleIdentifier(clientId) || !isClientHandleIdentifier(referenceId)) return null

    return { clientId, referenceId }
  } catch {
    return null
  }
}

async function resolveProxyAuth(req: NextRequest, config: NextAdapterConfig): Promise<AuthObject | null> {
  const handle = parseClientHandle(req.cookies.get(CONJOIN_CLIENT_HANDLE_COOKIE)?.value)
  if (!handle) return null

  const token = req.cookies.get(CONJOIN_SESSION_TOKEN_COOKIE)?.value
  if (!token) return null

  const { jwksUrl, issuer } = await resolveTokenVerificationTarget(config)

  try {
    const verified = await verifyToken(token, { jwksUrl, issuer })
    if (verified.payload.client_id !== handle.clientId) return null

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

export function conjoinProxy(handler?: ProxyHandler, overrides?: Partial<NextAdapterConfig>) {
  return async (req: NextRequest): Promise<ProxyResult> => {
    if (!handler) return undefined

    const authObj = await resolveProxyAuth(req, resolveConfig(overrides))

    return handler(authObj, req)
  }
}

export function createRouteMatcher(patterns: string[]): (req: NextRequest) => boolean {
  const regexes = patterns.map(pattern => {
    const segments: string[] = []
    let remaining = pattern

    while (remaining.length > 0) {
      const wildcardIndex = remaining.indexOf('(.*)')
      if (wildcardIndex === -1) {
        segments.push(remaining.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))
        break
      }

      const before = remaining.slice(0, wildcardIndex)
      segments.push(before.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))
      segments.push('(.*)')
      remaining = remaining.slice(wildcardIndex + 4)
    }

    return new RegExp(`^${segments.join('')}$`)
  })

  return (req: NextRequest) => {
    const pathname = new URL(req.url).pathname
    return regexes.some(re => re.test(pathname))
  }
}
