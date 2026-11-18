import type { NextRequest } from 'next/server'
import { type ConjoinClientHandle, parseClientHandle } from '../auth/client-handle'
import { CONJOIN_CLIENT_HANDLE_COOKIE, CONJOIN_SESSION_TOKEN_COOKIE } from '../server/tokens'
import { resolveConfig } from './config'
import type { AuthObject, NextAdapterConfig } from './types'
import { verifyAuthObject } from './verify-auth'

const CLIENT_HANDLE_MAX_BYTES = 2048

type ProxyResult = Response | undefined

type ProxyHandler = (auth: AuthObject | null, req: NextRequest) => ProxyResult | Promise<ProxyResult>

function readClientHandleCookie(cookieValue: string | undefined): ConjoinClientHandle | null {
  if (!cookieValue || new TextEncoder().encode(cookieValue).byteLength > CLIENT_HANDLE_MAX_BYTES) return null

  try {
    return parseClientHandle(JSON.parse(cookieValue))
  } catch {
    return null
  }
}

async function resolveProxyAuth(req: NextRequest, config: NextAdapterConfig): Promise<AuthObject | null> {
  const handle = readClientHandleCookie(req.cookies.get(CONJOIN_CLIENT_HANDLE_COOKIE)?.value)
  if (!handle) return null

  const token = req.cookies.get(CONJOIN_SESSION_TOKEN_COOKIE)?.value
  if (!token) return null

  return verifyAuthObject({
    token,
    config,
    isTokenAccepted: verified => verified.payload.client_id === handle.client_id,
  })
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
