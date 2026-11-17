export type AuthFlowProof = {
  state: string
  codeVerifier: string
  codeChallenge: string
}

export type AuthFlowCrypto = {
  fillRandomBytes: (bytes: Uint8Array<ArrayBuffer>) => Uint8Array<ArrayBuffer>
  digestSha256: (bytes: Uint8Array<ArrayBuffer>) => Promise<ArrayBuffer>
}

const CODE_VERIFIER_BYTES = 48
const STATE_BYTES = 24
const BASE64URL_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'

export function encodeBase64Url(bytes: Uint8Array): string {
  let encoded = ''

  for (let index = 0; index < bytes.length; index += 3) {
    const first = bytes[index] ?? 0
    const second = bytes[index + 1]
    const third = bytes[index + 2]
    const chunk = (first << 16) | ((second ?? 0) << 8) | (third ?? 0)

    encoded += BASE64URL_ALPHABET.charAt((chunk >> 18) & 63)
    encoded += BASE64URL_ALPHABET.charAt((chunk >> 12) & 63)
    if (second !== undefined) encoded += BASE64URL_ALPHABET.charAt((chunk >> 6) & 63)
    if (third !== undefined) encoded += BASE64URL_ALPHABET.charAt(chunk & 63)
  }

  return encoded
}

const randomBase64Url = (crypto: AuthFlowCrypto, length: number): string =>
  encodeBase64Url(crypto.fillRandomBytes(new Uint8Array(length)))

export async function createAuthFlowProof(crypto: AuthFlowCrypto): Promise<AuthFlowProof> {
  const codeVerifier = randomBase64Url(crypto, CODE_VERIFIER_BYTES)
  const digest = await crypto.digestSha256(new TextEncoder().encode(codeVerifier))

  return {
    state: randomBase64Url(crypto, STATE_BYTES),
    codeVerifier,
    codeChallenge: encodeBase64Url(new Uint8Array(digest)),
  }
}
