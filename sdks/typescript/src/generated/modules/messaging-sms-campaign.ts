import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateSmsCampaignBody = NonNullable<operations['createSmsCampaign']['requestBody']>['content']['application/json']
type CreateSmsCampaignData = NonNullable<operations['createSmsCampaign']['responses']['201']['content']['application/json']['data']>
type ReadSmsCampaignData = NonNullable<operations['readSmsCampaign']['responses']['200']['content']['application/json']['data']>
type UpdateSmsCampaignBody = NonNullable<operations['updateSmsCampaign']['requestBody']>['content']['application/json']
type UpdateSmsCampaignData = NonNullable<operations['updateSmsCampaign']['responses']['200']['content']['application/json']['data']>
type DeleteSmsCampaignData = NonNullable<operations['deleteSmsCampaign']['responses']['200']['content']['application/json']['data']>
type ListSmsCampaignsBody = NonNullable<operations['listSmsCampaigns']['requestBody']>['content']['application/json']
type ListSmsCampaignsData = NonNullable<operations['listSmsCampaigns']['responses']['200']['content']['application/json']['data']>[number]

export function createMessagingSMSCampaigns(client: ConjoinClient) {
  return {
    createSmsCampaign: (data: CreateSmsCampaignBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateSmsCampaignData>('messaging/sms/campaigns/', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),

    readSmsCampaign: (campaignId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSmsCampaignData>(`messaging/sms/campaigns/${encodePathParam(campaignId)}`, { ...options, method: 'GET', scopes: ['messagingProfileId'] }),

    updateSmsCampaign: (campaignId: string, data: UpdateSmsCampaignBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateSmsCampaignData>(`messaging/sms/campaigns/${encodePathParam(campaignId)}`, { ...options, method: 'PATCH', body: data, scopes: ['messagingProfileId'] }),

    deleteSmsCampaign: (campaignId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteSmsCampaignData>(`messaging/sms/campaigns/${encodePathParam(campaignId)}`, { ...options, method: 'DELETE', scopes: ['messagingProfileId'] }),

    listSmsCampaigns: (data: ListSmsCampaignsBody, options?: ConjoinCallOptions) =>
      client.fetchList<ListSmsCampaignsData>('messaging/sms/campaigns/retrieve', { ...options, method: 'POST', body: data, scopes: ['messagingProfileId'] }),
  }
}
