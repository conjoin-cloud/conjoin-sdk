import { createRemoteJWKSet, type JWTPayload, jwtVerify } from 'jose'

export const CONJOIN_AUTH_ISSUER_PATH = '/v1/auth/client'
export const CONJOIN_SESSION_TOKEN_AUDIENCE = 'conjoin-auth-session'

const CONJOIN_AUTH_JWKS_PATH = '/.well-known/jwks.json'

export type VerifyTokenOptions = {
  jwksUrl: string
  audience?: string
  issuer?: string
}

export type VerifiedToken = {
  payload: JWTPayload
  accountId: string
  sessionId: string
  organizationId: string | null
  organizationRoles: string[]
}

const jwksSets = new Map<string, ReturnType<typeof createRemoteJWKSet>>()

export function buildConjoinAuthIssuer(authDomain: string): string {
  return `https://${authDomain}${CONJOIN_AUTH_ISSUER_PATH}`
}

export function buildConjoinAuthJwksUrl(issuer: string): string {
  return `${issuer}${CONJOIN_AUTH_JWKS_PATH}`
}

function getJwksSet(url: string) {
  let jwks = jwksSets.get(url)
  if (!jwks) {
    jwks = createRemoteJWKSet(new URL(url))
    jwksSets.set(url, jwks)
  }
  return jwks
}

function readStringClaim(value: unknown): string | null {
  return typeof value === 'string' && value.length > 0 ? value : null
}

function readRolesClaim(value: unknown): string[] {
  return Array.isArray(value) ? value.filter((role): role is string => typeof role === 'string') : []
}

export async function verifyToken(token: string, options: VerifyTokenOptions): Promise<VerifiedToken> {
  const jwks = getJwksSet(options.jwksUrl)

  const { payload } = await jwtVerify(token, jwks, {
    audience: options.audience ?? CONJOIN_SESSION_TOKEN_AUDIENCE,
    issuer: options.issuer,
  })

  return {
    payload,
    accountId: payload.sub ?? '',
    sessionId: readStringClaim(payload.session_id) ?? '',
    organizationId: readStringClaim(payload.organization_id),
    organizationRoles: readRolesClaim(payload.organization_roles),
  }
}
