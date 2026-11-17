import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListSmsCampaignsData = NonNullable<operations['listSmsCampaigns']['responses']['200']['content']['application/json']['data']>[number]
type ListSmsCampaignsQuery = NonNullable<operations['listSmsCampaigns']['parameters']['query']>
type CreateSmsCampaignBody = NonNullable<operations['createSmsCampaign']['requestBody']>['content']['application/json']
type CreateSmsCampaignData = NonNullable<operations['createSmsCampaign']['responses']['201']['content']['application/json']['data']>
type ListSmsCampaignsCountData = NonNullable<operations['listSmsCampaignsCount']['responses']['200']['content']['application/json']['data']>
type ListSmsCampaignsCountQuery = NonNullable<operations['listSmsCampaignsCount']['parameters']['query']>
type ReadSmsCampaignData = NonNullable<operations['readSmsCampaign']['responses']['200']['content']['application/json']['data']>
type UpdateSmsCampaignBody = NonNullable<operations['updateSmsCampaign']['requestBody']>['content']['application/json']
type UpdateSmsCampaignData = NonNullable<operations['updateSmsCampaign']['responses']['200']['content']['application/json']['data']>
type DeleteSmsCampaignData = NonNullable<operations['deleteSmsCampaign']['responses']['200']['content']['application/json']['data']>

export function createMessagingSMSCampaigns(client: ConjoinClient) {
  return {
    listSmsCampaigns: (query?: ListSmsCampaignsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListSmsCampaignsData>('messaging/sms-campaigns/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    createSmsCampaign: (data: CreateSmsCampaignBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsCampaignData>('messaging/sms-campaigns/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'], acceptsIdempotencyKey: true }),

    listSmsCampaignsCount: (query?: ListSmsCampaignsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListSmsCampaignsCountData>('messaging/sms-campaigns/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['messagingProfileId'] }),

    readSmsCampaign: (smsCampaignId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSmsCampaignData>(`messaging/sms-campaigns/${encodePathParam(smsCampaignId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    updateSmsCampaign: (smsCampaignId: string, data: UpdateSmsCampaignBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSmsCampaignData>(`messaging/sms-campaigns/${encodePathParam(smsCampaignId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deleteSmsCampaign: (smsCampaignId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsCampaignData>(`messaging/sms-campaigns/${encodePathParam(smsCampaignId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),
  }
}
