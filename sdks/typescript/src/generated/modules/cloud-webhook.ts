import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['readCloudWebhooks']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['readCloudWebhooks']['parameters']['query']>
type RegisterBody = NonNullable<operations['registerCloudWebhook']['requestBody']>['content']['application/json']
type RegisterData = NonNullable<operations['registerCloudWebhook']['responses']['201']['content']['application/json']['data']>
type ReadCountData = NonNullable<operations['readCloudWebhooksCount']['responses']['200']['content']['application/json']['data']>
type ReadCountQuery = NonNullable<operations['readCloudWebhooksCount']['parameters']['query']>
type ReadData = NonNullable<operations['readCloudWebhook']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateCloudWebhook']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCloudWebhook']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteCloudWebhook']['responses']['200']['content']['application/json']['data']>
type ReadEventsData = NonNullable<operations['readCloudWebhookEvents']['responses']['200']['content']['application/json']['data']>[number]
type ReadEventsQuery = NonNullable<operations['readCloudWebhookEvents']['parameters']['query']>
type ReadEventsCountData = NonNullable<operations['readCloudWebhookEventsCount']['responses']['200']['content']['application/json']['data']>
type ReadEventsCountQuery = NonNullable<operations['readCloudWebhookEventsCount']['parameters']['query']>

export function createCloudWebhooks(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('cloud/webhooks/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    register: (data: RegisterBody, options?: ConjoinCallOptions) =>
      client.fetch<RegisterData>('cloud/webhooks/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    readCount: (query?: ReadCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadCountData>('cloud/webhooks/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    read: (webhookId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`cloud/webhooks/${encodePathParam(webhookId)}`, { ...options, method: 'GET' }),

    update: (webhookId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`cloud/webhooks/${encodePathParam(webhookId)}`, { ...options, method: 'PATCH', body: data }),

    delete: (webhookId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`cloud/webhooks/${encodePathParam(webhookId)}`, { ...options, method: 'DELETE' }),

    readEvents: (query?: ReadEventsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadEventsData>('cloud/webhook-events/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readEventsCount: (query?: ReadEventsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadEventsCountData>('cloud/webhook-events/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
