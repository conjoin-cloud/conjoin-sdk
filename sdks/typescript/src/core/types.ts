import type { ConjoinListPage } from './pagination'

export type ConjoinScope = {
  billingEntityId?: string
  messagingProfileId?: string
  authAppId?: string
}

export type ConjoinScopeName = keyof ConjoinScope

export type ConjoinConfig = ConjoinScope & {
  apiKey?: string
  publishableKey?: string
  baseUrl?: string
  apiVersion?: string
  timeout?: number
  maxResponseBytes?: number
  conjoinRequestId?: string
  credentials?: RequestCredentials
  retry?: {
    maxRetries?: number
    backoffMs?: number
    maxDelayMs?: number
  }
}

export type ResolvedConfig = {
  readonly apiKey?: string
  readonly publishableKey?: string
  readonly baseUrl: string
  readonly apiVersion: string
  readonly timeout: number
  readonly maxResponseBytes: number
  readonly conjoinRequestId?: string
  readonly credentials?: RequestCredentials
  readonly scope: Readonly<ConjoinScope>
  readonly retry: {
    readonly maxRetries: number
    readonly backoffMs: number
    readonly maxDelayMs: number
  }
}

export type ConjoinRequestTraceScopeOptions = {
  requestId?: string
}

export type ConjoinResponseMetadata = {
  requestId?: string
  status: number
  headers: Headers
}

export type ConjoinFetchResult<T> = {
  data: T
  metadata: ConjoinResponseMetadata
}

export type ConjoinFetchListResult<T> = {
  data: ConjoinListPage<T>
  metadata: ConjoinResponseMetadata
}

export type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'

export type ConjoinAuthOption = { type: 'default' } | { type: 'none' } | { type: 'bearer'; token: string }

export type ConjoinCallOptions = {
  idempotencyKey?: string
  conjoinRequestId?: string
  headers?: Record<string, string>
  auth?: ConjoinAuthOption
  signal?: AbortSignal
  timeout?: number
  maxRetries?: number
}

export type ConjoinDeclaredHeaderRule = {
  readonly name: string
  readonly argumentName: string
  readonly required: boolean
  readonly minLength?: number
  readonly maxLength?: number
  readonly pattern?: string
}

export type ConjoinDeclaredHeaders = {
  rules: readonly ConjoinDeclaredHeaderRule[]
  values?: Readonly<Record<string, string | undefined>>
}

export type ConjoinRequestAuth = ConjoinAuthOption | { type: 'publishableKey' } | { type: 'session'; token?: string }

export type RequestOptions = Omit<ConjoinCallOptions, 'auth'> & {
  auth?: ConjoinRequestAuth
  method?: HttpMethod
  body?: unknown
  contentType?: 'application/json' | 'multipart/form-data'
  query?: Record<string, unknown>
  scopes?: readonly ConjoinScopeName[]
  acceptsIdempotencyKey?: boolean
  declaredHeaders?: ConjoinDeclaredHeaders
  cursorLocation?: ConjoinCursorLocation
}

export type ConjoinCursorLocation = 'query' | 'body' | 'none'

export type Cursor = {
  prev: string | null
  next: string | null
}

export type ConjoinResponseMeta = {
  type?: string
  code?: number
  message?: string
}

export type ConjoinResponse<T> = {
  response: ConjoinResponseMeta
  data: T
}

export type ConjoinListResponse<T> = {
  response: ConjoinResponseMeta
  data: T[]
  cursor: Cursor
}

export type PaginationParams = {
  limit?: number | string
  cursor?: { prev?: string; next?: string }
}

export type ConjoinClient = {
  config: ResolvedConfig
  fetch: <T>(path: string, options?: RequestOptions) => Promise<T>
  fetchJson: <T>(path: string, options?: RequestOptions) => Promise<T>
  fetchWithResponse: <T>(path: string, options?: RequestOptions) => Promise<ConjoinFetchResult<T>>
  fetchList: <T>(path: string, options?: RequestOptions) => Promise<ConjoinListPage<T>>
  fetchListWithResponse: <T>(path: string, options?: RequestOptions) => Promise<ConjoinFetchListResult<T>>
  fetchRaw: (path: string, options?: RequestOptions) => Promise<Response>
  withScope: (scope: ConjoinScope) => ConjoinClient
  withRequestTrace: <T>(
    callback: (client: ConjoinClient, requestId: string) => T | Promise<T>,
    options?: ConjoinRequestTraceScopeOptions,
  ) => Promise<T>
}
