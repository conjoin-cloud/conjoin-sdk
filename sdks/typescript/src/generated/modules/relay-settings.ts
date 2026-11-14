import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type GetData = NonNullable<operations['getRelaySettings']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateRelaySettings']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateRelaySettings']['responses']['200']['content']['application/json']['data']>
type RotateSigningSecretData = NonNullable<operations['rotateRelaySigningSecret']['responses']['200']['content']['application/json']['data']>
type RevealSigningSecretData = NonNullable<operations['revealRelaySigningSecret']['responses']['200']['content']['application/json']['data']>

export function createRelaySettings(client: ConjoinClient) {
  return {
    get: (options?: ConjoinCallOptions) =>
      client.fetch<GetData>('relay/settings/', { ...options, method: 'GET' }),

    update: (data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>('relay/settings/', { ...options, method: 'PATCH', body: data }),

    rotateSigningSecret: (options?: ConjoinCallOptions) =>
      client.fetch<RotateSigningSecretData>('relay/settings/signing-secret/rotate', { ...options, method: 'POST' }),

    revealSigningSecret: (options?: ConjoinCallOptions) =>
      client.fetch<RevealSigningSecretData>('relay/settings/signing-secret', { ...options, method: 'GET' }),
  }
}
