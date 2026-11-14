import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateUploadSignedUrlBody = NonNullable<operations['createUploadSignedUrl']['requestBody']>['content']['application/json']
type CreateUploadSignedUrlData = NonNullable<operations['createUploadSignedUrl']['responses']['200']['content']['application/json']['data']>
type CreateDownloadSignedUrlBody = NonNullable<operations['createDownloadSignedUrl']['requestBody']>['content']['application/json']
type CreateDownloadSignedUrlData = NonNullable<operations['createDownloadSignedUrl']['responses']['200']['content']['application/json']['data']>
type RenameData = NonNullable<operations['renameStorageObject']['responses']['200']['content']['application/json']['data']>
type ArchiveData = NonNullable<operations['archiveStorageObject']['responses']['200']['content']['application/json']['data']>
type RestoreData = NonNullable<operations['restoreStorageObject']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteStorageObject']['responses']['200']['content']['application/json']['data']>
type ListVersionsData = NonNullable<operations['listStorageObjectVersions']['responses']['200']['content']['application/json']['data']>[number]
type ListVersionsQuery = NonNullable<operations['listStorageObjectVersions']['parameters']['query']>
type RestoreVersionBody = NonNullable<operations['restoreStorageObjectVersion']['requestBody']>['content']['application/json']
type RestoreVersionData = NonNullable<operations['restoreStorageObjectVersion']['responses']['200']['content']['application/json']['data']>
type CheckDuplicateData = NonNullable<operations['checkStorageObjectDuplicate']['responses']['200']['content']['application/json']['data']>
type CheckDuplicateQuery = NonNullable<operations['checkStorageObjectDuplicate']['parameters']['query']>
type ReadData = NonNullable<operations['readStorageObject']['responses']['200']['content']['application/json']['data']>
type ListData = NonNullable<operations['listStorageObjects']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listStorageObjects']['parameters']['query']>

export function createStorageObjects(client: ConjoinClient) {
  return {
    createUploadSignedUrl: (containerNameOrId: string, data: CreateUploadSignedUrlBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateUploadSignedUrlData>(`storage/storage-object/${encodePathParam(containerNameOrId)}/signed-url/upload`, { ...options, method: 'POST', body: data }),

    createDownloadSignedUrl: (containerNameOrId: string, data: CreateDownloadSignedUrlBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateDownloadSignedUrlData>(`storage/storage-object/${encodePathParam(containerNameOrId)}/signed-url/download`, { ...options, method: 'POST', body: data }),

    rename: (containerNameOrId: string, oldName: string, newName: string, options?: ConjoinCallOptions) =>
      client.fetch<RenameData>(`storage/storage-object/rename/${encodePathParam(containerNameOrId)}/${encodePathParam(oldName)}/${encodePathParam(newName)}`, { ...options, method: 'PATCH' }),

    archive: (containerNameOrId: string, objectNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<ArchiveData>(`storage/storage-object/archive/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}`, { ...options, method: 'PATCH' }),

    restore: (containerNameOrId: string, objectNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<RestoreData>(`storage/storage-object/restore/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}`, { ...options, method: 'PATCH' }),

    delete: (containerNameOrId: string, prefix: string, name: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`storage/storage-object/${encodePathParam(containerNameOrId)}/${encodePathParam(prefix)}/${encodePathParam(name)}`, { ...options, method: 'DELETE' }),

    listVersions: (containerNameOrId: string, objectNameOrId: string, query?: ListVersionsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListVersionsData>(`storage/storage-object/versions/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    restoreVersion: (containerNameOrId: string, objectNameOrId: string, data: RestoreVersionBody, options?: ConjoinCallOptions) =>
      client.fetch<RestoreVersionData>(`storage/storage-object/versions/restore/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}`, { ...options, method: 'POST', body: data }),

    checkDuplicate: (containerNameOrId: string, query: CheckDuplicateQuery, options?: ConjoinCallOptions) =>
      client.fetch<CheckDuplicateData>(`storage/storage-object/check-duplicate/${encodePathParam(containerNameOrId)}`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (containerNameOrId: string, objectNameOrId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`storage/storage-object/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}`, { ...options, method: 'GET' }),

    list: (containerNameOrId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`storage/storage-object/${encodePathParam(containerNameOrId)}`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
