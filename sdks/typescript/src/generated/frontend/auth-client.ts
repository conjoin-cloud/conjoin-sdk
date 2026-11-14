import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type GetOidcDiscoveryData = NonNullable<operations['getAuthOidcDiscovery']['responses']['200']['content']['application/json']['data']>
type ProcessHandshakeData = NonNullable<operations['processAuthHandshake']['responses']['200']['content']['application/json']['data']>
type ProcessLogoutData = NonNullable<operations['processAuthLogout']['responses']['200']['content']['application/json']['data']>
type GetJwksData = NonNullable<operations['getAuthJwks']['responses']['200']['content']['application/json']['data']>

export function createAuthClients(client: ConjoinClient) {
  return {
    getOidcDiscovery: (options?: ConjoinCallOptions) =>
      client.fetch<GetOidcDiscoveryData>('auth/client/.well-known/openid-configuration', { auth: { type: 'none' }, ...options, method: 'GET' }),

    processHandshake: (options?: ConjoinCallOptions) =>
      client.fetch<ProcessHandshakeData>('auth/client/handshakes', { auth: { type: 'none' }, ...options, method: 'POST' }),

    processLogout: (options?: ConjoinCallOptions) =>
      client.fetch<ProcessLogoutData>('auth/client/logout', { auth: { type: 'none' }, ...options, method: 'POST' }),

    getJwks: (options?: ConjoinCallOptions) =>
      client.fetch<GetJwksData>('auth/client/.well-known/jwks.json', { auth: { type: 'none' }, ...options, method: 'GET' }),
  }
}
