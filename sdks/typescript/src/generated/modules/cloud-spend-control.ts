import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadData = NonNullable<operations['readCloudSpendControl']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateCloudSpendControl']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCloudSpendControl']['responses']['200']['content']['application/json']['data']>
type ReadUsageData = NonNullable<operations['readCloudSpendControlUsage']['responses']['200']['content']['application/json']['data']>

export function createCloudSpendControls(client: ConjoinClient) {
  return {
    read: (options?: ConjoinCallOptions) =>
      client.fetch<ReadData>('cloud/spend-control/', { ...options, method: 'GET' }),

    update: (data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>('cloud/spend-control/', { ...options, method: 'PATCH', body: data }),

    readUsage: (options?: ConjoinCallOptions) =>
      client.fetch<ReadUsageData>('cloud/spend-control/usage', { ...options, method: 'GET' }),
  }
}
