import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateBody = NonNullable<operations['createMessagingProfile']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createMessagingProfile']['responses']['201']['content']['application/json']['data']>
type EnableData = NonNullable<operations['enableMessagingProfile']['responses']['200']['content']['application/json']['data']>
type DisableData = NonNullable<operations['disableMessagingProfile']['responses']['200']['content']['application/json']['data']>
type CloseData = NonNullable<operations['closeMessagingProfile']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateMessagingProfile']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateMessagingProfile']['responses']['200']['content']['application/json']['data']>
type ReadData = NonNullable<operations['readMessagingProfile']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteMessagingProfile']['responses']['200']['content']['application/json']['data']>
type UpdateEmailConfigBody = NonNullable<operations['updateMessagingProfileEmailConfig']['requestBody']>['content']['application/json']
type UpdateEmailConfigData = NonNullable<operations['updateMessagingProfileEmailConfig']['responses']['200']['content']['application/json']['data']>
type UpdateMultisendConfigBody = NonNullable<operations['updateMessagingProfileMultisendConfig']['requestBody']>['content']['application/json']
type UpdateMultisendConfigData = NonNullable<operations['updateMessagingProfileMultisendConfig']['responses']['200']['content']['application/json']['data']>
type UpdateVerificationsConfigBody = NonNullable<operations['updateMessagingProfileVerificationsConfig']['requestBody']>['content']['application/json']
type UpdateVerificationsConfigData = NonNullable<operations['updateMessagingProfileVerificationsConfig']['responses']['200']['content']['application/json']['data']>
type ListBody = NonNullable<operations['listMessagingProfiles']['requestBody']>['content']['application/json']
type ListData = NonNullable<operations['listMessagingProfiles']['responses']['200']['content']['application/json']['data']>[number]

export function createMessagingProfiles(client: ConjoinClient) {
  return {
    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('messaging/profiles/', { ...options, method: 'POST', body: data }),

    enable: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<EnableData>(`messaging/profiles/${encodePathParam(profileId)}/enable`, { ...options, method: 'PATCH' }),

    disable: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<DisableData>(`messaging/profiles/${encodePathParam(profileId)}/disable`, { ...options, method: 'PATCH' }),

    close: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<CloseData>(`messaging/profiles/${encodePathParam(profileId)}/close`, { ...options, method: 'PATCH' }),

    update: (profileId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`messaging/profiles/${encodePathParam(profileId)}`, { ...options, method: 'PATCH', body: data }),

    read: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`messaging/profiles/${encodePathParam(profileId)}`, { ...options, method: 'GET' }),

    delete: (profileId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`messaging/profiles/${encodePathParam(profileId)}`, { ...options, method: 'DELETE' }),

    updateEmailConfig: (profileId: string, data: UpdateEmailConfigBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateEmailConfigData>(`messaging/profiles/${encodePathParam(profileId)}/emails-config`, { ...options, method: 'PATCH', body: data }),

    updateMultisendConfig: (profileId: string, data: UpdateMultisendConfigBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateMultisendConfigData>(`messaging/profiles/${encodePathParam(profileId)}/multisend-config`, { ...options, method: 'PATCH', body: data }),

    updateVerificationsConfig: (profileId: string, data: UpdateVerificationsConfigBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateVerificationsConfigData>(`messaging/profiles/${encodePathParam(profileId)}/verifications-config`, { ...options, method: 'PATCH', body: data }),

    list: (data: ListBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('messaging/profiles/retrieve', { ...options, method: 'POST', body: data }),
  }
}
