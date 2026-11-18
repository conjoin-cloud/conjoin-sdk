import { createConjoinClient } from '../core/client'
import { ConjoinConfigurationError } from '../core/errors'
import { createCloudSDKs } from '../generated/frontend/cloud-sdk'
import { buildConjoinAuthIssuer, buildConjoinAuthJwksUrl } from '../server/tokens'
import type { NextAdapterConfig } from './types'

const AUTH_DOMAIN_PATTERN = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*(:[0-9]{1,5})?$/i
const AUTH_DOMAIN_CACHE_TTL_MS = 5 * 60 * 1000

type CachedAuthDomain = {
  domain: Promise<string>
  expiresAt: number
}

const authDomainsByPublishableKey = new Map<string, CachedAuthDomain>()

export function resolveConfig(overrides?: Partial<NextAdapterConfig>): NextAdapterConfig {
  return {
    secretKey: overrides?.secretKey ?? process.env.CONJOIN_SECRET_KEY,
    publishableKey: overrides?.publishableKey ?? process.env.CONJOIN_PUBLISHABLE_KEY,
    jwksUrl: overrides?.jwksUrl,
    authDomain: overrides?.authDomain ?? process.env.CONJOIN_AUTH_DOMAIN,
  }
}

function requireAuthDomain(domain: string): string {
  const trimmed = domain.trim()

  if (!AUTH_DOMAIN_PATTERN.test(trimmed)) {
    throw new ConjoinConfigurationError(`The auth domain is not a valid host name: ${domain}`)
  }

  return trimmed
}

async function readAuthDomainFromSettings(publishableKey: string): Promise<string> {
  const settings = await createCloudSDKs(createConjoinClient({ publishableKey })).readSdkSettings()

  if (!settings.auth?.domain) {
    throw new ConjoinConfigurationError('Sign-in is not configured for the project of this publishable key')
  }

  return requireAuthDomain(settings.auth.domain)
}

function readCachedAuthDomain(publishableKey: string): Promise<string> {
  const now = Date.now()
  const cached = authDomainsByPublishableKey.get(publishableKey)

  if (cached && cached.expiresAt > now) return cached.domain

  const domain = readAuthDomainFromSettings(publishableKey)
  authDomainsByPublishableKey.set(publishableKey, { domain, expiresAt: now + AUTH_DOMAIN_CACHE_TTL_MS })
  domain.catch(() => {
    if (authDomainsByPublishableKey.get(publishableKey)?.domain === domain) {
      authDomainsByPublishableKey.delete(publishableKey)
    }
  })

  return domain
}

export async function resolveAuthDomain(config: NextAdapterConfig): Promise<string> {
  if (config.authDomain) return requireAuthDomain(config.authDomain)

  if (!config.publishableKey) {
    throw new ConjoinConfigurationError(
      'The Conjoin Next.js adapter needs a publishableKey or an authDomain to reach the auth domain',
    )
  }

  return readCachedAuthDomain(config.publishableKey)
}

export type TokenVerificationTarget = {
  jwksUrl: string
  issuer: string | undefined
}

export async function resolveTokenVerificationTarget(config: NextAdapterConfig): Promise<TokenVerificationTarget> {
  if (config.jwksUrl && !config.authDomain && !config.publishableKey) {
    return { jwksUrl: config.jwksUrl, issuer: undefined }
  }

  const issuer = buildConjoinAuthIssuer(await resolveAuthDomain(config))

  return { jwksUrl: config.jwksUrl ?? buildConjoinAuthJwksUrl(issuer), issuer }
}
