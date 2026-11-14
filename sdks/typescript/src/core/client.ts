import { ConjoinConfigurationError } from './errors'
import {
  conjoinFetch,
  conjoinFetchJson,
  conjoinFetchList,
  conjoinFetchListWithResponse,
  conjoinFetchRaw,
  conjoinFetchWithResponse,
} from './fetch'
import { buildConjoinRegionBaseUrl, readConjoinKeyRegion } from './region'
import { assertValidScopeValue } from './request-headers'
import { resolveConjoinRequestId } from './request-tracing'
import type { ConjoinClient, ConjoinConfig, ConjoinScope, RequestOptions, ResolvedConfig } from './types'
import { DEFAULT_API_VERSION } from './version'

const DEFAULT_TIMEOUT_MS = 30_000
const DEFAULT_MAX_RETRIES = 3
const DEFAULT_BACKOFF_MS = 500
const DEFAULT_MAX_RETRY_DELAY_MS = 60_000
const MAX_TIMER_DELAY_MS = 2 ** 31 - 1
const SLASH_CHAR_CODE = 47

function requirePositive(value: number | undefined, fallback: number, name: string): number {
  const resolved = value ?? fallback

  if (!Number.isFinite(resolved) || resolved <= 0 || resolved > MAX_TIMER_DELAY_MS) {
    throw new ConjoinConfigurationError(`${name} must be greater than 0 and at most ${MAX_TIMER_DELAY_MS}`)
  }

  return resolved
}

function requireNonNegative(value: number | undefined, fallback: number, name: string): number {
  const resolved = value ?? fallback

  if (!Number.isFinite(resolved) || resolved < 0 || resolved > MAX_TIMER_DELAY_MS) {
    throw new ConjoinConfigurationError(`${name} must be from 0 to ${MAX_TIMER_DELAY_MS}`)
  }

  return resolved
}

function requireRetryCount(value: number | undefined): number {
  const resolved = value ?? DEFAULT_MAX_RETRIES

  if (!Number.isSafeInteger(resolved) || resolved < 0) {
    throw new ConjoinConfigurationError('retry.maxRetries must be a whole number of 0 or more')
  }

  return resolved
}

function resolveBaseUrl(config: ConjoinConfig, key: string): string {
  if (config.baseUrl === undefined) {
    return buildConjoinRegionBaseUrl(readConjoinKeyRegion(key))
  }

  let url: URL

  try {
    url = new URL(config.baseUrl)
  } catch {
    throw new ConjoinConfigurationError('baseUrl must be an absolute http or https URL')
  }

  if (url.protocol !== 'https:' && url.protocol !== 'http:') {
    throw new ConjoinConfigurationError('baseUrl must be an absolute http or https URL')
  }

  return withoutTrailingSlashes(config.baseUrl)
}

function withoutTrailingSlashes(value: string): string {
  let end = value.length

  while (end > 0 && value.charCodeAt(end - 1) === SLASH_CHAR_CODE) {
    end -= 1
  }

  return value.slice(0, end)
}

function resolveScope(scope: ConjoinScope): ConjoinScope {
  return Object.freeze({
    billingEntityId: assertValidScopeValue('billingEntityId', scope.billingEntityId),
    messagingProfileId: assertValidScopeValue('messagingProfileId', scope.messagingProfileId),
    authAppId: assertValidScopeValue('authAppId', scope.authAppId),
  })
}

function resolveConfig(config: ConjoinConfig): ResolvedConfig {
  const key = config.apiKey ?? config.publishableKey

  if (!key) {
    throw new ConjoinConfigurationError('Either apiKey or publishableKey must be provided')
  }

  if (config.apiKey && config.publishableKey) {
    throw new ConjoinConfigurationError('Provide exactly one of apiKey or publishableKey')
  }

  return Object.freeze({
    apiKey: config.apiKey,
    publishableKey: config.publishableKey,
    baseUrl: resolveBaseUrl(config, key),
    apiVersion: config.apiVersion ?? DEFAULT_API_VERSION,
    timeout: requirePositive(config.timeout, DEFAULT_TIMEOUT_MS, 'timeout'),
    maxResponseBytes: requirePositive(config.maxResponseBytes, 16 * 1024 * 1024, 'maxResponseBytes'),
    conjoinRequestId: config.conjoinRequestId,
    credentials: config.credentials,
    scope: resolveScope(config),
    retry: Object.freeze({
      maxRetries: requireRetryCount(config.retry?.maxRetries),
      backoffMs: requireNonNegative(config.retry?.backoffMs, DEFAULT_BACKOFF_MS, 'retry.backoffMs'),
      maxDelayMs: requireNonNegative(config.retry?.maxDelayMs, DEFAULT_MAX_RETRY_DELAY_MS, 'retry.maxDelayMs'),
    }),
  })
}

export function createConjoinClient(config: ConjoinConfig): ConjoinClient {
  const resolved = resolveConfig(config)

  return {
    config: resolved,
    fetch: <T>(path: string, options?: RequestOptions) => conjoinFetch<T>(resolved, path, options),
    fetchJson: <T>(path: string, options?: RequestOptions) => conjoinFetchJson<T>(resolved, path, options),
    fetchWithResponse: <T>(path: string, options?: RequestOptions) =>
      conjoinFetchWithResponse<T>(resolved, path, options),
    fetchList: <T>(path: string, options?: RequestOptions) => conjoinFetchList<T>(resolved, path, options),
    fetchListWithResponse: <T>(path: string, options?: RequestOptions) =>
      conjoinFetchListWithResponse<T>(resolved, path, options),
    fetchRaw: (path: string, options?: RequestOptions) => conjoinFetchRaw(resolved, path, options),
    withScope: scope => createConjoinClient({ ...config, ...scope }),
    withRequestTrace: async (callback, options) => {
      const requestId = resolveConjoinRequestId(options?.requestId ?? resolved.conjoinRequestId)

      return callback(createConjoinClient({ ...config, conjoinRequestId: requestId }), requestId)
    },
  }
}
