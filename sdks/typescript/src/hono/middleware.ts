import type { Context, MiddlewareHandler } from 'hono'
import { getCookie } from 'hono/cookie'
import { getConjoinRequestIdFromHeaders } from '../core/request-tracing'
import { CONJOIN_SESSION_TOKEN_COOKIE, verifyToken } from '../server/tokens'
import type { ConjoinEnv, ConjoinHonoOptions } from './types'

export function conjoinMiddleware(options: ConjoinHonoOptions): MiddlewareHandler<ConjoinEnv> {
  const cookieName = options.cookieName ?? CONJOIN_SESSION_TOKEN_COOKIE

  return async (c: Context<ConjoinEnv>, next) => {
    c.set('conjoinRequestId', getConjoinRequestIdFromHeaders(c.req.raw.headers))

    const authHeader = c.req.header('authorization')
    const bearerToken = authHeader?.startsWith('Bearer ') ? authHeader.slice(7) : null

    const cookieToken = getCookie(c, cookieName)

    const token = bearerToken ?? cookieToken

    if (!token) {
      c.set('auth', null)
      await next()
      return
    }

    try {
      const verified = await verifyToken(token, {
        jwksUrl: options.jwksUrl,
        audience: options.audience,
        issuer: options.issuer,
      })
      c.set('auth', verified)
    } catch {
      c.set('auth', null)
    }

    await next()
  }
}
