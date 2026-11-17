import { CONJOIN_REQUEST_ID_HEADER } from '../../../src/core/request-tracing'

export type ContractResponse = {
  status: number
  headers?: Record<string, string>
  body?: unknown
}

export type ConjoinContractResponseOptions = {
  status?: number
  message?: string
  requestId?: string
  headers?: Record<string, string>
}

export type ConjoinContractListOptions = ConjoinContractResponseOptions & {
  cursor?: {
    prev?: string | null
    next?: string | null
  }
}

export type ConjoinContractErrorOptions = ConjoinContractResponseOptions & {
  code?: string
  param?: string | null
  details?: unknown
  errors?: Array<{
    message: string
    path: string
  }>
}

const jsonHeaders = (options?: ConjoinContractResponseOptions): Record<string, string> => ({
  'content-type': 'application/json',
  ...(options?.requestId ? { [CONJOIN_REQUEST_ID_HEADER]: options.requestId } : {}),
  ...options?.headers,
})

const successMeta = (status: number, message: string | undefined) => ({
  type: 'SUCCESS',
  code: status,
  message: message ?? 'Success',
})

export const conjoinSuccess = <T>(data: T, options?: ConjoinContractResponseOptions): ContractResponse => {
  const status = options?.status ?? 200

  return { status, headers: jsonHeaders(options), body: { response: successMeta(status, options?.message), data } }
}

export const conjoinList = <T>(data: T[], options?: ConjoinContractListOptions): ContractResponse => {
  const status = options?.status ?? 200

  return {
    status,
    headers: jsonHeaders(options),
    body: {
      response: successMeta(status, options?.message),
      data,
      cursor: { prev: options?.cursor?.prev ?? null, next: options?.cursor?.next ?? null },
    },
  }
}

export const conjoinError = (message: string, options?: ConjoinContractErrorOptions): ContractResponse => {
  const status = options?.status ?? 500

  return {
    status,
    headers: jsonHeaders(options),
    body: {
      response: { type: status >= 500 ? 'SERVER_ERROR' : 'CLIENT_ERROR', code: status, message },
      data: null,
      error: {
        code: options?.code ?? 'contract_error',
        param: options?.param ?? null,
        details: options?.details ?? options?.errors ?? null,
      },
    },
  }
}
