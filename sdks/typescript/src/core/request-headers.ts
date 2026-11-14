import { ConjoinAuthenticationError, ConjoinConfigurationError } from './errors'
import { IDEMPOTENCY_KEY_HEADER } from './idempotency'
import { CONJOIN_REQUEST_ID_HEADER } from './request-tracing'
import type { ConjoinScopeName, RequestOptions, ResolvedConfig } from './types'
import { SDK_VERSION } from './version'

export const SCOPE_HEADERS: Readonly<Record<ConjoinScopeName, string>> = {
  billingEntityId: 'Billing-Entity-ID',
  messagingProfileId: 'Messaging-Profile-ID',
  authAppId: 'Auth-App-ID',
}

const HEADER_VALUE_PATTERN = /^[\x21-\x7e]+$/

const MANAGED_HEADER_NAMES = new Set(
  [
    'authorization',
    'content-type',
    CONJOIN_REQUEST_ID_HEADER,
    IDEMPOTENCY_KEY_HEADER,
    ...Object.values(SCOPE_HEADERS),
  ].map(name => name.toLowerCase()),
)

function resolveAuthorization(config: ResolvedConfig, auth: RequestOptions['auth']): string | undefined {
  if (auth?.type === 'none') {
    return undefined
  }

  if (auth?.type === 'bearer') {
    if (!HEADER_VALUE_PATTERN.test(auth.token)) {
      throw new ConjoinAuthenticationError('Bearer token must be a non-empty value without spaces', {
        status: 0,
        code: 'invalid_bearer_token',
      })
    }

    return `Bearer ${auth.token}`
  }

  const key = config.apiKey ?? config.publishableKey

  return key ? `Bearer ${key}` : undefined
}

function resolveScopeHeaders(config: ResolvedConfig, scopes: RequestOptions['scopes']): Record<string, string> {
  const headers: Record<string, string> = {}

  for (const scope of scopes ?? []) {
    const value = config.scope[scope]

    if (value === undefined) {
      throw new ConjoinConfigurationError(`This call needs ${scope} in the client settings`)
    }

    headers[SCOPE_HEADERS[scope]] = value
  }

  return headers
}

function withoutManagedHeaders(headers: Record<string, string> | undefined): Record<string, string> {
  return Object.fromEntries(
    Object.entries(headers ?? {}).filter(([name]) => !MANAGED_HEADER_NAMES.has(name.toLowerCase())),
  )
}

export type ManagedHeaderValues = {
  requestId: string
  idempotencyKey?: string
}

export function buildRequestHeaders(
  config: ResolvedConfig,
  options: RequestOptions,
  managed: ManagedHeaderValues,
): Record<string, string> {
  const authorization = resolveAuthorization(config, options.auth)
  const contentType = options.contentType ?? 'application/json'

  return {
    ...withoutManagedHeaders(options.headers),
    ...(authorization ? { Authorization: authorization } : {}),
    ...(contentType === 'application/json' && options.body !== undefined ? { 'Content-Type': contentType } : {}),
    'X-Conjoin-SDK-Version': SDK_VERSION,
    'X-Conjoin-API-Version': config.apiVersion,
    ...resolveScopeHeaders(config, options.scopes),
    [CONJOIN_REQUEST_ID_HEADER]: managed.requestId,
    ...(managed.idempotencyKey ? { [IDEMPOTENCY_KEY_HEADER]: managed.idempotencyKey } : {}),
  }
}

export function assertValidScopeValue(name: ConjoinScopeName, value: string | undefined): string | undefined {
  if (value === undefined) {
    return undefined
  }

  if (!HEADER_VALUE_PATTERN.test(value)) {
    throw new ConjoinConfigurationError(`${name} must be a non-empty value without spaces or control characters`)
  }

  return value
}

export function readHeaderValue(headers: Record<string, string> | undefined, name: string): string | undefined {
  const lowerName = name.toLowerCase()

  for (const [headerName, value] of Object.entries(headers ?? {})) {
    if (headerName.toLowerCase() === lowerName) {
      return value
    }
  }

  return undefined
}
