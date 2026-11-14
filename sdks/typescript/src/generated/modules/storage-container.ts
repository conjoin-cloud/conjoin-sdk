import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createStorageContainer']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createStorageContainer']['responses']['201']['content']['application/json']['data']>
type ListData = NonNullable<operations['listStorageContainers']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listStorageContainers']['parameters']['query']>
type ReadData = NonNullable<operations['readStorageContainer']['responses']['200']['content']['application/json']['data']>
type RequestDeletionData = NonNullable<operations['requestStorageContainerDeletion']['responses']['200']['content']['application/json']['data']>
type ArchiveData = NonNullable<operations['archiveStorageContainer']['responses']['200']['content']['application/json']['data']>
type RestoreData = NonNullable<operations['restoreStorageContainer']['responses']['200']['content']['application/json']['data']>
type UpdateLifecyclePolicyBody = NonNullable<operations['updateStorageContainerLifecyclePolicy']['requestBody']>['content']['application/json']
type UpdateLifecyclePolicyData = NonNullable<operations['updateStorageContainerLifecyclePolicy']['responses']['200']['content']['application/json']['data']>
type UpdateSettingsBody = NonNullable<operations['updateStorageContainerSettings']['requestBody']>['content']['application/json']
type UpdateSettingsData = NonNullable<operations['updateStorageContainerSettings']['responses']['200']['content']['application/json']['data']>
type CancelDeletionData = NonNullable<operations['cancelStorageContainerDeletion']['responses']['200']['content']['application/json']['data']>
type ChangeClassBody = NonNullable<operations['changeStorageContainerClass']['requestBody']>['content']['application/json']
type ChangeClassData = NonNullable<operations['changeStorageContainerClass']['responses']['200']['content']['application/json']['data']>
type UpdateTransitionPolicyBody = NonNullable<operations['updateStorageContainerTransitionPolicy']['requestBody']>['content']['application/json']
type UpdateTransitionPolicyData = NonNullable<operations['updateStorageContainerTransitionPolicy']['responses']['200']['content']['application/json']['data']>

export function createStorageContainers(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('storage/storage-container/', { ...options, method: 'POST', body: data }),

    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('storage/storage-container/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (containerNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`storage/storage-container/${encodePathParam(containerNameOrId)}`, { ...options, method: 'GET' }),

    requestDeletion: (containerNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<RequestDeletionData>(`storage/storage-container/${encodePathParam(containerNameOrId)}`, { ...options, method: 'DELETE' }),

    archive: (containerNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`storage/storage-container/archive/${encodePathParam(containerNameOrId)}`, { ...options, method: 'PATCH' }),

    restore: (containerNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreData>(`storage/storage-container/restore/${encodePathParam(containerNameOrId)}`, { ...options, method: 'PATCH' }),

    updateLifecyclePolicy: (containerNameOrId: string, data: UpdateLifecyclePolicyBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateLifecyclePolicyData>(`storage/storage-container/lifecycle-policy/${encodePathParam(containerNameOrId)}`, { ...options, method: 'PATCH', body: data }),

    updateSettings: (containerNameOrId: string, data: UpdateSettingsBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSettingsData>(`storage/storage-container/settings/${encodePathParam(containerNameOrId)}`, { ...options, method: 'PATCH', body: data }),

    cancelDeletion: (containerNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<CancelDeletionData>(`storage/storage-container/cancel-deletion/${encodePathParam(containerNameOrId)}`, { ...options, method: 'PATCH' }),

    changeClass: (containerNameOrId: string, data: ChangeClassBody, options?: ConjoinCallOptions) =>
      client.fetch<ChangeClassData>(`storage/storage-container/storage-class/${encodePathParam(containerNameOrId)}`, { ...options, method: 'PATCH', body: data }),

    updateTransitionPolicy: (containerNameOrId: string, data: UpdateTransitionPolicyBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateTransitionPolicyData>(`storage/storage-container/transition-policy/${encodePathParam(containerNameOrId)}`, { ...options, method: 'PATCH', body: data }),
  }
}
