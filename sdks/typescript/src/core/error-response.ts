import { readBoundedText } from './bounded-body'
import {
  ConjoinApiError,
  type ConjoinApiErrorOptions,
  ConjoinAuthenticationError,
  ConjoinConflictError,
  ConjoinInternalServerError,
  ConjoinNotFoundError,
  ConjoinPermissionDeniedError,
  ConjoinRateLimitError,
  ConjoinValidationError,
  type ValidationFieldError,
} from './errors'
import { parseRetryAfterMs } from './retry'

const MAX_ERROR_BODY_BYTES = 65_536

type ErrorBody = {
  message: string
  code?: string
  param: string | null
  details: unknown
}

const isRecord = (value: unknown): value is Record<string, unknown> =>
  Boolean(value) && typeof value === 'object' && !Array.isArray(value)

const readString = (value: unknown): string | undefined =>
  typeof value === 'string' && value.trim().length > 0 ? value : undefined

function parseErrorBody(text: string, fallbackMessage: string): ErrorBody {
  let payload: unknown

  try {
    payload = JSON.parse(text)
  } catch {
    return { message: fallbackMessage, param: null, details: null }
  }

  if (!isRecord(payload)) {
    return { message: fallbackMessage, param: null, details: null }
  }

  const response = isRecord(payload.response) ? payload.response : {}
  const error = isRecord(payload.error) ? payload.error : {}
  const legacyDetails = Array.isArray(payload.errors) ? payload.errors : null

  return {
    message: readString(response.message) ?? readString(payload.message) ?? fallbackMessage,
    code: readString(error.code),
    param: readString(error.param) ?? null,
    details: error.details ?? legacyDetails,
  }
}

function readFieldErrors(details: unknown): ValidationFieldError[] {
  if (!Array.isArray(details)) {
    return []
  }

  return details.flatMap(item =>
    isRecord(item) && typeof item.message === 'string' && typeof item.path === 'string'
      ? [{ message: item.message, path: item.path }]
      : [],
  )
}

const FALLBACK_CODES: Readonly<Record<number, string>> = {
  400: 'invalid_request',
  401: 'authentication_failed',
  403: 'permission_denied',
  404: 'not_found',
  409: 'conflict',
  422: 'invalid_request',
  429: 'rate_limited',
}

function fallbackCode(status: number): string {
  return FALLBACK_CODES[status] ?? (status >= 500 ? 'server_error' : 'api_error')
}

export async function buildApiError(response: Response, requestId: string | undefined): Promise<ConjoinApiError> {
  const text = await readBoundedText(response, MAX_ERROR_BODY_BYTES).catch(() => '')
  const body = parseErrorBody(text, response.statusText || `HTTP ${response.status}`)
  const status = response.status
  const options: ConjoinApiErrorOptions = {
    status,
    code: body.code ?? fallbackCode(status),
    param: body.param,
    details: body.details,
    requestId,
  }

  if (status === 400 || status === 422) {
    return new ConjoinValidationError(body.message, { ...options, errors: readFieldErrors(body.details) })
  }

  if (status === 401) return new ConjoinAuthenticationError(body.message, options)
  if (status === 403) return new ConjoinPermissionDeniedError(body.message, options)
  if (status === 404) return new ConjoinNotFoundError(body.message, options)
  if (status === 409) return new ConjoinConflictError(body.message, options)

  if (status === 429) {
    return new ConjoinRateLimitError(body.message, {
      ...options,
      retryAfterMs: parseRetryAfterMs(response.headers.get('retry-after')),
    })
  }

  if (status >= 500) return new ConjoinInternalServerError(body.message, options)

  return new ConjoinApiError(body.message, options)
}
