import { ConjoinConfigurationError } from './errors'

const DOT_SEGMENTS = new Set(['.', '..'])

export function encodePathParam(value: string): string {
  if (typeof value !== 'string' || value.length === 0 || DOT_SEGMENTS.has(value)) {
    throw new ConjoinConfigurationError('A path parameter must be a non-empty ID')
  }

  return encodeURIComponent(value)
}
