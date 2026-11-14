export type ConjoinErrorOptions = {
  status?: number
  code: string
  param?: string | null
  details?: unknown
  requestId?: string
}

export class ConjoinError extends Error {
  readonly status: number
  readonly code: string
  readonly param: string | null
  readonly details: unknown
  readonly requestId?: string

  constructor(message: string, options: ConjoinErrorOptions) {
    super(message)
    this.name = 'ConjoinError'
    this.status = options.status ?? 0
    this.code = options.code
    this.param = options.param ?? null
    this.details = options.details ?? null
    this.requestId = options.requestId
  }
}

export type ConjoinApiErrorOptions = Omit<ConjoinErrorOptions, 'status'> & { status: number }

export class ConjoinApiError extends ConjoinError {
  constructor(message: string, options: ConjoinApiErrorOptions) {
    super(message, options)
    this.name = 'ConjoinApiError'
  }
}

export class ConjoinAuthenticationError extends ConjoinApiError {
  constructor(message: string, options: ConjoinApiErrorOptions) {
    super(message, options)
    this.name = 'ConjoinAuthenticationError'
  }
}

export class ConjoinPermissionDeniedError extends ConjoinApiError {
  constructor(message: string, options: ConjoinApiErrorOptions) {
    super(message, options)
    this.name = 'ConjoinPermissionDeniedError'
  }
}

export class ConjoinNotFoundError extends ConjoinApiError {
  constructor(message: string, options: ConjoinApiErrorOptions) {
    super(message, options)
    this.name = 'ConjoinNotFoundError'
  }
}

export class ConjoinConflictError extends ConjoinApiError {
  constructor(message: string, options: ConjoinApiErrorOptions) {
    super(message, options)
    this.name = 'ConjoinConflictError'
  }
}

export type ValidationFieldError = {
  message: string
  path: string
}

export class ConjoinValidationError extends ConjoinApiError {
  readonly errors: ValidationFieldError[]

  constructor(message: string, options: ConjoinApiErrorOptions & { errors: ValidationFieldError[] }) {
    super(message, options)
    this.name = 'ConjoinValidationError'
    this.errors = options.errors
  }
}

export class ConjoinRateLimitError extends ConjoinApiError {
  readonly retryAfterMs?: number

  constructor(message: string, options: ConjoinApiErrorOptions & { retryAfterMs?: number }) {
    super(message, options)
    this.name = 'ConjoinRateLimitError'
    this.retryAfterMs = options.retryAfterMs
  }
}

export class ConjoinInternalServerError extends ConjoinApiError {
  constructor(message: string, options: ConjoinApiErrorOptions) {
    super(message, options)
    this.name = 'ConjoinInternalServerError'
  }
}

export class ConjoinResponseError extends ConjoinError {
  constructor(message: string, options: { status: number; requestId?: string }) {
    super(message, { ...options, code: 'invalid_response' })
    this.name = 'ConjoinResponseError'
  }
}

export class ConjoinNetworkError extends ConjoinError {
  constructor(message: string, requestId?: string) {
    super(message, { code: 'network_error', requestId })
    this.name = 'ConjoinNetworkError'
  }
}

export class ConjoinTimeoutError extends ConjoinError {
  constructor(message: string, requestId?: string) {
    super(message, { code: 'timeout_error', requestId })
    this.name = 'ConjoinTimeoutError'
  }
}

export class ConjoinAbortError extends ConjoinError {
  constructor(message: string, requestId?: string) {
    super(message, { code: 'request_aborted', requestId })
    this.name = 'ConjoinAbortError'
  }
}

export class ConjoinConfigurationError extends ConjoinError {
  constructor(message: string) {
    super(message, { code: 'configuration_error' })
    this.name = 'ConjoinConfigurationError'
  }
}

export class ConjoinStorageError extends ConjoinError {
  readonly storageUrl: string
  readonly uploadMode?: 'resumable' | 'single'

  constructor(message: string, status: number, storageUrl: string, uploadMode?: 'resumable' | 'single') {
    super(message, { status, code: 'storage_error' })
    this.name = 'ConjoinStorageError'
    this.storageUrl = storageUrl
    this.uploadMode = uploadMode
  }
}
