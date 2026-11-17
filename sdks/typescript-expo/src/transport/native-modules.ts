import type { AuthFlowCrypto } from '@conjoin-cloud/react-core'

export type SecureStore = {
  getItemAsync: (key: string) => Promise<string | null>
  setItemAsync: (key: string, value: string) => Promise<void>
  deleteItemAsync: (key: string) => Promise<void>
}

let secureStore: SecureStore | null = null
let flowCrypto: AuthFlowCrypto | null = null

export async function loadSecureStore(): Promise<SecureStore> {
  if (secureStore) return secureStore

  try {
    const module = await import('expo-secure-store')
    secureStore = {
      getItemAsync: key => module.getItemAsync(key),
      setItemAsync: (key, value) => module.setItemAsync(key, value),
      deleteItemAsync: key => module.deleteItemAsync(key),
    }
    return secureStore
  } catch {
    throw new Error(
      'expo-secure-store is required for Conjoin Expo support. Install it with: npx expo install expo-secure-store',
    )
  }
}

export async function loadFlowCrypto(): Promise<AuthFlowCrypto> {
  if (flowCrypto) return flowCrypto

  const platformCrypto = globalThis.crypto

  if (typeof platformCrypto?.getRandomValues === 'function' && typeof platformCrypto.subtle?.digest === 'function') {
    flowCrypto = {
      fillRandomBytes: bytes => platformCrypto.getRandomValues(bytes),
      digestSha256: bytes => platformCrypto.subtle.digest('SHA-256', bytes),
    }
    return flowCrypto
  }

  try {
    const module = await import('expo-crypto')
    flowCrypto = {
      fillRandomBytes: bytes => module.getRandomValues(bytes),
      digestSha256: bytes => module.digest(module.CryptoDigestAlgorithm.SHA256, bytes),
    }
    return flowCrypto
  } catch {
    throw new Error('expo-crypto is required for Conjoin sign-in. Install it with: npx expo install expo-crypto')
  }
}
