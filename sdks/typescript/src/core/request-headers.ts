import { ConjoinAuthenticationError, ConjoinConfigurationError } from './errors'
import { IDEMPOTENCY_KEY_HEADER } from './idempotency'
import { CONJOIN_REQUEST_ID_HEADER } from './request-tracing'
import type {
  ConjoinDeclaredHeaderRule,
  ConjoinDeclaredHeaders,
  ConjoinScopeName,
  RequestOptions,
  ResolvedConfig,
} from './types'
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

const isBrowserRuntime = (): boolean => typeof globalThis.document !== 'undefined'

const usesSessionCookie = (auth: RequestOptions['auth']): boolean =>
  auth?.type === 'session' && auth.token === undefined

export function resolveFetchCredentials(
  config: ResolvedConfig,
  auth: RequestOptions['auth'],
): RequestCredentials | undefined {
  return usesSessionCookie(auth) ? 'include' : config.credentials
}

function toBearerAuthorization(token: string): string {
  if (!HEADER_VALUE_PATTERN.test(token)) {
    throw new ConjoinAuthenticationError('Bearer token must be a non-empty value without spaces', {
      status: 0,
      code: 'invalid_bearer_token',
    })
  }

  return `Bearer ${token}`
}

function resolveAuthorization(config: ResolvedConfig, auth: RequestOptions['auth']): string | undefined {
  if (auth?.type === 'none') {
    return undefined
  }

  if (auth?.type === 'bearer') {
    return toBearerAuthorization(auth.token)
  }

  if (auth?.type === 'publishableKey') {
    if (config.publishableKey === undefined) {
      throw new ConjoinConfigurationError('This call needs publishableKey in the client settings')
    }

    return toBearerAuthorization(config.publishableKey)
  }

  if (auth?.type === 'session') {
    if (auth.token !== undefined) return toBearerAuthorization(auth.token)
    if (isBrowserRuntime()) return undefined

    throw new ConjoinConfigurationError('This call needs sessionToken when it runs outside a browser')
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

function withoutManagedHeaders(
  headers: Record<string, string> | undefined,
  declaredNames: ReadonlySet<string>,
): Record<string, string> {
  return Object.fromEntries(
    Object.entries(headers ?? {}).filter(([name]) => {
      const lowerName = name.toLowerCase()

      return !MANAGED_HEADER_NAMES.has(lowerName) && !declaredNames.has(lowerName)
    }),
  )
}

function assertDeclaredHeaderValue(rule: ConjoinDeclaredHeaderRule, value: string): void {
  const isTooShort = rule.minLength !== undefined && value.length < rule.minLength
  const isTooLong = rule.maxLength !== undefined && value.length > rule.maxLength
  const breaksPattern = rule.pattern !== undefined && !new RegExp(rule.pattern, 'u').test(value)

  if (!HEADER_VALUE_PATTERN.test(value) || isTooShort || isTooLong || breaksPattern) {
    throw new ConjoinConfigurationError(`${rule.argumentName} does not meet the documented length or format`)
  }
}

function resolveDeclaredHeaders(declared: ConjoinDeclaredHeaders | undefined): Record<string, string> {
  const headers: Record<string, string> = {}

  for (const rule of declared?.rules ?? []) {
    const value = declared?.values?.[rule.argumentName]

    if (value === undefined) {
      if (rule.required) {
        throw new ConjoinConfigurationError(`This call needs ${rule.argumentName}`)
      }

      continue
    }

    assertDeclaredHeaderValue(rule, value)
    headers[rule.name] = value
  }

  return headers
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
  const declaredHeaders = resolveDeclaredHeaders(options.declaredHeaders)
  const declaredNames = new Set((options.declaredHeaders?.rules ?? []).map(rule => rule.name.toLowerCase()))

  return {
    ...withoutManagedHeaders(options.headers, declaredNames),
    ...declaredHeaders,
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
