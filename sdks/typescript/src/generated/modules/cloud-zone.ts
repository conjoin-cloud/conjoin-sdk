import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['readCloudZones']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['readCloudZones']['parameters']['query']>
type CreateBody = NonNullable<operations['createCloudZone']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCloudZone']['responses']['201']['content']['application/json']['data']>
type ReadCountData = NonNullable<operations['readCloudZonesCount']['responses']['200']['content']['application/json']['data']>
type ReadCountQuery = NonNullable<operations['readCloudZonesCount']['parameters']['query']>
type ReadData = NonNullable<operations['readCloudZone']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteCloudZone']['responses']['200']['content']['application/json']['data']>
type VerifyDnsData = NonNullable<operations['verifyCloudZoneDns']['responses']['200']['content']['application/json']['data']>

export function createCloudZones(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('cloud/zones/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('cloud/zones/', { ...options, method: 'POST', body: data }),

    readCount: (query?: ReadCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadCountData>('cloud/zones/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (zoneId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`cloud/zones/${encodePathParam(zoneId)}`, { ...options, method: 'GET' }),

    delete: (zoneId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`cloud/zones/${encodePathParam(zoneId)}`, { ...options, method: 'DELETE' }),

    verifyDns: (zoneId: string, options?: ConjoinCallOptions) =>
      client.fetch<VerifyDnsData>(`cloud/zones/${encodePathParam(zoneId)}/verify`, { ...options, method: 'POST' }),
  }
}
