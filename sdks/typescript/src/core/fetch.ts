import { readBoundedText } from './bounded-body'
import { buildApiError } from './error-response'
import {
  ConjoinAbortError,
  ConjoinConfigurationError,
  ConjoinNetworkError,
  ConjoinResponseError,
  ConjoinTimeoutError,
} from './errors'
import { assertValidIdempotencyKey, generateIdempotencyKey, IDEMPOTENCY_KEY_HEADER } from './idempotency'
import { type ConjoinListPage, createListPage } from './pagination'
import { serializeQuery } from './query-serializer'
import { buildRequestBody } from './request-body'
import { buildRequestHeaders, readHeaderValue } from './request-headers'
import { generateConjoinRequestId, getConjoinRequestIdFromHeaders, isValidConjoinRequestId } from './request-tracing'
import { canRetryMethod, computeRetryDelayMs, isRetryableStatus, parseRetryAfterMs, sleepUnlessAborted } from './retry'
import type { ConjoinFetchListResult, ConjoinFetchResult, HttpMethod, RequestOptions, ResolvedConfig } from './types'

const ABSOLUTE_URL_PATTERN = /^[a-z][a-z0-9+.-]*:/i

function buildUrl(config: ResolvedConfig, path: string, query?: Record<string, unknown>): string {
  if (ABSOLUTE_URL_PATTERN.test(path) || path.startsWith('//')) {
    throw new ConjoinConfigurationError('path must be relative to the Conjoin API')
  }

  const relativePath = path.replace(/^\/+/, '').replace(/^v1\//, '')
  const qs = query ? serializeQuery(query) : ''

  return `${config.baseUrl}/v1/${relativePath}${qs ? `?${qs}` : ''}`
}

function resolveRequestId(config: ResolvedConfig, options: RequestOptions): string {
  const supplied = [
    options.conjoinRequestId,
    getConjoinRequestIdFromHeaders(options.headers),
    config.conjoinRequestId,
  ].find(isValidConjoinRequestId)

  return supplied ?? generateConjoinRequestId()
}

function resolveIdempotencyKey(method: HttpMethod, options: RequestOptions): string | undefined {
  const supplied = options.idempotencyKey ?? readHeaderValue(options.headers, IDEMPOTENCY_KEY_HEADER)

  if (supplied !== undefined) {
    if (method !== 'POST') {
      throw new ConjoinConfigurationError('Only a POST takes an idempotency key')
    }

    return assertValidIdempotencyKey(supplied)
  }

  return method === 'POST' && options.acceptsIdempotencyKey ? generateIdempotencyKey() : undefined
}

function resolvePositive(value: number | undefined, fallback: number, name: string): number {
  if (value === undefined) {
    return fallback
  }

  if (!Number.isFinite(value) || value <= 0 || value > 2 ** 31 - 1) {
    throw new ConjoinConfigurationError(`${name} must be greater than 0 and at most ${2 ** 31 - 1}`)
  }

  return value
}

function resolveMaxRetries(value: number | undefined, fallback: number): number {
  if (value === undefined) {
    return fallback
  }

  if (!Number.isSafeInteger(value) || value < 0) {
    throw new ConjoinConfigurationError('maxRetries must be a whole number of 0 or more')
  }

  return value
}

type AttemptFailure = { kind: 'network'; error: unknown } | { kind: 'timeout' }

function readAttemptFailure(
  error: unknown,
  callerSignal: AbortSignal | undefined,
  timeoutSignal: AbortSignal,
  requestId: string,
): AttemptFailure {
  if (callerSignal?.aborted) {
    throw new ConjoinAbortError('The caller aborted the request', requestId)
  }

  if (timeoutSignal.aborted) {
    return { kind: 'timeout' }
  }

  return { kind: 'network', error }
}

function toFailureError(failure: AttemptFailure, timeout: number, requestId: string): Error {
  if (failure.kind === 'timeout') {
    return new ConjoinTimeoutError(`Request timed out after ${timeout}ms`, requestId)
  }

  const message = failure.error instanceof Error ? failure.error.message : 'Network request failed'

  return new ConjoinNetworkError(message, requestId)
}

function assertSendableHeaders(headers: Record<string, string>): Record<string, string> {
  try {
    new Headers(headers)
  } catch {
    throw new ConjoinConfigurationError('A request header has a name or value that HTTP does not allow')
  }

  return headers
}

async function discardBody(response: Response): Promise<void> {
  await response.body?.cancel().catch(() => undefined)
}

export type ConjoinRawResult = {
  response: Response
  bodyText?: string
  requestId: string
  readBody: <T>(read: (response: Response) => Promise<T>) => Promise<T>
}

export async function sendConjoinRequest(
  config: ResolvedConfig,
  path: string,
  options: RequestOptions = {},
  bufferResponse = false,
): Promise<ConjoinRawResult> {
  const method = options.method ?? 'GET'
  const url = buildUrl(config, path, options.query)
  const requestId = resolveRequestId(config, options)
  const idempotencyKey = resolveIdempotencyKey(method, options)
  const headers = assertSendableHeaders(buildRequestHeaders(config, options, { requestId, idempotencyKey }))
  const body = buildRequestBody(options.body, options.contentType ?? 'application/json')
  const timeout = resolvePositive(options.timeout, config.timeout, 'timeout')
  const maxRetries = resolveMaxRetries(options.maxRetries, config.retry.maxRetries)
  const retryAllowed = canRetryMethod(method, idempotencyKey !== undefined && options.acceptsIdempotencyKey === true)
  const callerSignal = options.signal

  for (let attempt = 0; ; attempt++) {
    if (callerSignal?.aborted) {
      throw new ConjoinAbortError('The caller aborted the request', requestId)
    }

    const timeoutSignal = AbortSignal.timeout(Math.ceil(timeout))
    const signal = callerSignal ? AbortSignal.any([timeoutSignal, callerSignal]) : timeoutSignal
    const canRetryAgain = retryAllowed && attempt < maxRetries
    let response: Response
    let bodyText: string | undefined

    try {
      response = await fetch(url, { method, headers, body, signal, credentials: config.credentials })
      if (bufferResponse && response.ok) {
        bodyText = await readBoundedText(response, config.maxResponseBytes, requestId)
      }
    } catch (error) {
      if (error instanceof ConjoinResponseError) throw error
      const failure = readAttemptFailure(error, callerSignal, timeoutSignal, requestId)

      if (!canRetryAgain) {
        throw toFailureError(failure, timeout, requestId)
      }

      await sleepUnlessAborted(computeRetryDelayMs(attempt, config.retry, undefined), callerSignal, requestId)
      continue
    }

    if (canRetryAgain && isRetryableStatus(response.status)) {
      const retryAfterMs = parseRetryAfterMs(response.headers.get('retry-after'))
      await discardBody(response)
      await sleepUnlessAborted(computeRetryDelayMs(attempt, config.retry, retryAfterMs), callerSignal, requestId)
      continue
    }

    const readBody = async <T>(read: (value: Response) => Promise<T>): Promise<T> => {
      try {
        const value = await read(response)
        if (callerSignal?.aborted) throw new ConjoinAbortError('The caller aborted the request', requestId)
        if (response.ok && timeoutSignal.aborted)
          throw new ConjoinTimeoutError(`Request timed out after ${timeout}ms`, requestId)
        return value
      } catch (error) {
        if (error instanceof ConjoinResponseError) {
          throw error
        }

        throw toFailureError(readAttemptFailure(error, callerSignal, timeoutSignal, requestId), timeout, requestId)
      }
    }

    return { response, bodyText, requestId, readBody }
  }
}

function readResponseRequestId(response: Response, sentRequestId: string): string {
  return getConjoinRequestIdFromHeaders(response.headers) ?? sentRequestId
}

async function readJsonBody(result: ConjoinRawResult): Promise<unknown> {
  const { response } = result
  const requestId = readResponseRequestId(response, result.requestId)

  if (!response.ok) {
    throw await result.readBody(value => buildApiError(value, requestId))
  }

  return result.readBody(async value => {
    const text = result.bodyText ?? (await value.text())

    if (text.length === 0) {
      return undefined
    }

    try {
      return JSON.parse(text) as unknown
    } catch {
      throw new ConjoinResponseError('The response body was not valid JSON', { status: value.status, requestId })
    }
  })
}

function metadataOf(result: ConjoinRawResult) {
  return {
    requestId: readResponseRequestId(result.response, result.requestId),
    status: result.response.status,
    headers: result.response.headers,
  }
}

export async function conjoinFetchJson<T>(config: ResolvedConfig, path: string, options?: RequestOptions): Promise<T> {
  const result = await sendConjoinRequest(config, path, options, true)

  return (await readJsonBody(result)) as T
}

export async function conjoinFetchWithResponse<T>(
  config: ResolvedConfig,
  path: string,
  options?: RequestOptions,
): Promise<ConjoinFetchResult<T>> {
  const result = await sendConjoinRequest(config, path, options, true)
  const json = await readJsonBody(result)
  const data = json && typeof json === 'object' && 'data' in json ? (json as { data: T }).data : (undefined as T)

  return { data, metadata: metadataOf(result) }
}

export async function conjoinFetch<T>(config: ResolvedConfig, path: string, options?: RequestOptions): Promise<T> {
  return (await conjoinFetchWithResponse<T>(config, path, options)).data
}

export async function conjoinFetchListWithResponse<T>(
  config: ResolvedConfig,
  path: string,
  options: RequestOptions = {},
  seenCursors: ReadonlySet<string> = new Set(),
): Promise<ConjoinFetchListResult<T>> {
  const result = await sendConjoinRequest(config, path, options, true)
  const json = await readJsonBody(result)
  const metadata = metadataOf(result)
  const query = options.query ?? {}
  const fetchNext = async (next: string, seen: ReadonlySet<string>): Promise<ConjoinListPage<T>> =>
    (await conjoinFetchListWithResponse<T>(config, path, { ...options, query: { ...query, cursor: { next } } }, seen))
      .data

  return { data: createListPage<T>(json, metadata.status, metadata.requestId, fetchNext, seenCursors), metadata }
}

export async function conjoinFetchList<T>(
  config: ResolvedConfig,
  path: string,
  options?: RequestOptions,
): Promise<ConjoinListPage<T>> {
  return (await conjoinFetchListWithResponse<T>(config, path, options)).data
}

export async function conjoinFetchRaw(config: ResolvedConfig, path: string, options?: RequestOptions) {
  return (await sendConjoinRequest(config, path, options)).response
}
