export function readSecureRandomBytes(length: number): Uint8Array {
  if (!globalThis.crypto?.getRandomValues) {
    throw new Error('The Conjoin SDK requires crypto.getRandomValues')
  }

  return globalThis.crypto.getRandomValues(new Uint8Array(length))
}
