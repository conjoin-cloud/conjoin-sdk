import type { RequestOptions } from './types'

function isFormDataBody(body: unknown): body is FormData {
  if (typeof FormData !== 'undefined' && body instanceof FormData) {
    return true
  }

  return (
    Boolean(body) &&
    typeof body === 'object' &&
    Object.prototype.toString.call(body) === '[object FormData]' &&
    typeof (body as { append?: unknown }).append === 'function'
  )
}

function isBlobBody(body: unknown): body is Blob {
  if (typeof Blob !== 'undefined' && body instanceof Blob) {
    return true
  }

  return Boolean(body) && typeof body === 'object' && Object.prototype.toString.call(body) === '[object Blob]'
}

function appendFormDataValue(formData: FormData, key: string, value: unknown): void {
  if (value === undefined || value === null) {
    return
  }

  if (isBlobBody(value)) {
    formData.append(key, value)
    return
  }

  if (Array.isArray(value)) {
    for (const item of value) {
      appendFormDataValue(formData, key, item)
    }
    return
  }

  if (typeof value === 'object') {
    formData.append(key, JSON.stringify(value))
    return
  }

  formData.append(key, String(value))
}

function buildFormData(body: unknown): FormData {
  if (isFormDataBody(body)) {
    return body
  }

  if (!body || typeof body !== 'object' || Array.isArray(body) || isBlobBody(body)) {
    throw new TypeError('multipart/form-data request body must be a FormData instance or object')
  }

  const formData = new FormData()
  for (const [key, value] of Object.entries(body)) {
    appendFormDataValue(formData, key, value)
  }
  return formData
}

export function buildRequestBody(body: unknown, contentType: RequestOptions['contentType']): BodyInit | undefined {
  if (body === undefined) {
    return undefined
  }

  if (contentType === 'multipart/form-data') {
    return buildFormData(body)
  }

  return JSON.stringify(body)
}
