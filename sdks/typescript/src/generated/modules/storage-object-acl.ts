import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type GrantObjectAclBody = NonNullable<operations['grantStorageObjectAcl']['requestBody']>['content']['application/json']
type GrantObjectAclData = NonNullable<operations['grantStorageObjectAcl']['responses']['200']['content']['application/json']['data']>
type RevokeObjectAclBody = NonNullable<operations['revokeStorageObjectAcl']['requestBody']>['content']['application/json']
type RevokeObjectAclData = NonNullable<operations['revokeStorageObjectAcl']['responses']['200']['content']['application/json']['data']>
type SetObjectPublicBody = NonNullable<operations['setStorageObjectPublic']['requestBody']>['content']['application/json']
type SetObjectPublicData = NonNullable<operations['setStorageObjectPublic']['responses']['200']['content']['application/json']['data']>

export function createStorageObjectACLs(client: ConjoinClient) {
  return {
    grantObjectAcl: (containerNameOrId: string, objectNameOrId: string, data: GrantObjectAclBody, options?: ConjoinCallOptions) =>
      client.fetch<GrantObjectAclData>(`storage/storage-object/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}/acl/grant`, { ...options, method: 'POST', body: data }),

    revokeObjectAcl: (containerNameOrId: string, objectNameOrId: string, data: RevokeObjectAclBody, options?: ConjoinCallOptions) =>
      client.fetch<RevokeObjectAclData>(`storage/storage-object/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}/acl/revoke`, { ...options, method: 'POST', body: data }),

    setObjectPublic: (containerNameOrId: string, objectNameOrId: string, data: SetObjectPublicBody, options?: ConjoinCallOptions) =>
      client.fetch<SetObjectPublicData>(`storage/storage-object/${encodePathParam(containerNameOrId)}/${encodePathParam(objectNameOrId)}/acl/public`, { ...options, method: 'PATCH', body: data }),
  }
}
