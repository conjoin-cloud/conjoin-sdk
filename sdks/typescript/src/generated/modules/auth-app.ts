import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listAuthApps']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAuthApps']['parameters']['query']>
type CreateBody = NonNullable<operations['createAuthApp']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createAuthApp']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listAuthAppsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listAuthAppsCount']['parameters']['query']>
type ReadData = NonNullable<operations['readAuthApp']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateAuthApp']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateAuthApp']['responses']['200']['content']['application/json']['data']>
type UpdateSettingsBody = NonNullable<operations['updateAuthAppSettings']['requestBody']>['content']['application/json']
type UpdateSettingsData = NonNullable<operations['updateAuthAppSettings']['responses']['200']['content']['application/json']['data']>
type RotateSigningKeysResponse = operations['rotateAuthAppSigningKeys']['responses']['200']['content']['application/json']

export function createAuthApps(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('auth/apps/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('auth/apps/', { ...options, method: 'POST', body: data }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('auth/apps/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (appId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`auth/apps/${encodePathParam(appId)}`, { ...options, method: 'GET' }),

    update: (appId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`auth/apps/${encodePathParam(appId)}`, { ...options, method: 'PATCH', body: data }),

    updateSettings: (appId: string, data: UpdateSettingsBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSettingsData>(`auth/apps/${encodePathParam(appId)}/settings`, { ...options, method: 'PATCH', body: data }),

    rotateSigningKeys: (appId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<RotateSigningKeysResponse>(`auth/apps/${encodePathParam(appId)}/signing-keys/rotate`, { ...options, method: 'POST' }),
  }
}
