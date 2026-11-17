import { ConjoinConfigurationError } from './errors'
import { readSecureRandomBytes } from './secure-random'

export const IDEMPOTENCY_KEY_HEADER = 'Idempotency-Key'

const IDEMPOTENCY_KEY_PATTERN = /^[A-Za-z0-9\-_:.]{1,64}$/
const UUID_BYTE_LENGTH = 16
const UUID_VERSION_4_BITS = 0x40
const UUID_VARIANT_BITS = 0x80

const byteToHex = (value: number): string => value.toString(16).padStart(2, '0')

export function generateIdempotencyKey(): string {
  const bytes = readSecureRandomBytes(UUID_BYTE_LENGTH)
  bytes[6] = (bytes[6] & 0x0f) | UUID_VERSION_4_BITS
  bytes[8] = (bytes[8] & 0x3f) | UUID_VARIANT_BITS
  const hex = Array.from(bytes, byteToHex).join('')

  return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`
}

export function assertValidIdempotencyKey(key: string): string {
  if (!IDEMPOTENCY_KEY_PATTERN.test(key)) {
    throw new ConjoinConfigurationError(
      'idempotencyKey must be 1 to 64 characters of letters, digits, hyphens, underscores, colons, and dots',
    )
  }

  return key
}
