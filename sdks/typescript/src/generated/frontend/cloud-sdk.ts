import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ReadSdkSettingsData = NonNullable<operations['readSdkSettings']['responses']['200']['content']['application/json']['data']>

export function createCloudSDKs(client: ConjoinClient) {
  return {
    readSdkSettings: (options?: ConjoinCallOptions) =>
      client.fetch<ReadSdkSettingsData>('cloud/client/settings/', { ...options, auth: { type: 'publishableKey' }, method: 'GET' }),
  }
}
