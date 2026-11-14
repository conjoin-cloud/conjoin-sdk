import { ConjoinAbortError } from './errors'
import type { HttpMethod } from './types'

const RETRYABLE_STATUSES = new Set([429, 500, 502, 503, 504])
const METHODS_SAFE_TO_RETRY = new Set<HttpMethod>(['GET', 'PUT', 'PATCH', 'DELETE'])
const RETRY_AFTER_SECONDS_PATTERN = /^\d+(\.\d+)?$/
const MILLISECONDS_PER_SECOND = 1000

export type RetryTiming = {
  backoffMs: number
  maxDelayMs: number
}

export function canRetryMethod(method: HttpMethod, hasIdempotencyKey: boolean): boolean {
  return METHODS_SAFE_TO_RETRY.has(method) || (method === 'POST' && hasIdempotencyKey)
}

export function isRetryableStatus(status: number): boolean {
  return RETRYABLE_STATUSES.has(status)
}

export function parseRetryAfterMs(value: string | null, now: number = Date.now()): number | undefined {
  if (value === null) {
    return undefined
  }

  const trimmed = value.trim()

  if (trimmed.length === 0) {
    return undefined
  }

  if (RETRY_AFTER_SECONDS_PATTERN.test(trimmed)) {
    return Number(trimmed) * MILLISECONDS_PER_SECOND
  }

  const retryAt = Date.parse(trimmed)

  if (Number.isNaN(retryAt)) {
    return undefined
  }

  return Math.max(0, retryAt - now)
}

export function computeRetryDelayMs(attempt: number, timing: RetryTiming, retryAfterMs: number | undefined): number {
  if (retryAfterMs !== undefined) {
    return Math.min(retryAfterMs, timing.maxDelayMs)
  }

  const ceiling = Math.min(timing.backoffMs * 2 ** attempt, timing.maxDelayMs)

  return Math.random() * ceiling
}

export function sleepUnlessAborted(ms: number, signal: AbortSignal | undefined, requestId: string): Promise<void> {
  if (signal?.aborted) {
    return Promise.reject(new ConjoinAbortError('The caller aborted the request', requestId))
  }

  return new Promise((resolve, reject) => {
    const onAbort = () => {
      clearTimeout(timer)
      reject(new ConjoinAbortError('The caller aborted the request', requestId))
    }
    const timer = setTimeout(() => {
      signal?.removeEventListener('abort', onAbort)
      resolve()
    }, ms)

    signal?.addEventListener('abort', onAbort, { once: true })
  })
}
