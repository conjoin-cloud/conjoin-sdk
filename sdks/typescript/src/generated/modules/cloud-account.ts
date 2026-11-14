import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadData = NonNullable<operations['readCloudAccount']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateCloudAccount']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCloudAccount']['responses']['200']['content']['application/json']['data']>

export function createCloudAccounts(client: ConjoinClient) {
  return {
    read: (options?: ConjoinCallOptions) =>
      client.fetch<ReadData>('cloud/account/', { ...options, method: 'GET' }),

    update: (data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>('cloud/account/', { ...options, method: 'PATCH', body: data }),
  }
}
