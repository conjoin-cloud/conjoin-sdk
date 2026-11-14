import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadClustersData = NonNullable<operations['readMemorystoreClusters']['responses']['200']['content']['application/json']['data']>[number]
type ReadClustersQuery = NonNullable<operations['readMemorystoreClusters']['parameters']['query']>
type CreateClusterBody = NonNullable<operations['createMemorystoreCluster']['requestBody']>['content']['application/json']
type CreateClusterData = NonNullable<operations['createMemorystoreCluster']['responses']['201']['content']['application/json']['data']>
type ReadClustersCountData = NonNullable<operations['readMemorystoreClustersCount']['responses']['200']['content']['application/json']['data']>
type ReadClustersCountQuery = NonNullable<operations['readMemorystoreClustersCount']['parameters']['query']>
type ReadClusterData = NonNullable<operations['readMemorystoreCluster']['responses']['200']['content']['application/json']['data']>
type UpdateClusterBody = NonNullable<operations['updateMemorystoreCluster']['requestBody']>['content']['application/json']
type UpdateClusterData = NonNullable<operations['updateMemorystoreCluster']['responses']['200']['content']['application/json']['data']>
type DeleteClusterData = NonNullable<operations['deleteMemorystoreCluster']['responses']['200']['content']['application/json']['data']>
type SuspendClusterData = NonNullable<operations['suspendMemorystoreCluster']['responses']['200']['content']['application/json']['data']>
type ExecuteCommandBody = NonNullable<operations['executeMemorystoreCommand']['requestBody']>['content']['application/json']
type ExecuteCommandData = NonNullable<operations['executeMemorystoreCommand']['responses']['200']['content']['application/json']['data']>

export function createRelayMemorystores(client: ConjoinClient) {
  return {
    readClusters: (query?: ReadClustersQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadClustersData>('relay/memorystore-clusters/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createCluster: (data: CreateClusterBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateClusterData>('relay/memorystore-clusters/', { ...options, method: 'POST', body: data }),

    readClustersCount: (query?: ReadClustersCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadClustersCountData>('relay/memorystore-clusters/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readCluster: (memorystoreClusterId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadClusterData>(`relay/memorystore-clusters/${encodePathParam(memorystoreClusterId)}`, { ...options, method: 'GET' }),

    updateCluster: (memorystoreClusterId: string, data: UpdateClusterBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateClusterData>(`relay/memorystore-clusters/${encodePathParam(memorystoreClusterId)}`, { ...options, method: 'PATCH', body: data }),

    deleteCluster: (memorystoreClusterId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteClusterData>(`relay/memorystore-clusters/${encodePathParam(memorystoreClusterId)}`, { ...options, method: 'DELETE' }),

    suspendCluster: (memorystoreClusterId: string, options?: ConjoinCallOptions) =>
      client.fetch<SuspendClusterData>(`relay/memorystore-clusters/${encodePathParam(memorystoreClusterId)}/suspend`, { ...options, method: 'POST' }),

    executeCommand: (memorystoreClusterId: string, data: ExecuteCommandBody, options?: ConjoinCallOptions) =>
      client.fetch<ExecuteCommandData>(`relay/memorystore-clusters/${encodePathParam(memorystoreClusterId)}/execute`, { ...options, method: 'POST', body: data }),
  }
}
