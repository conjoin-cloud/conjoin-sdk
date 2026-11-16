import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listCoupons']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listCoupons']['parameters']['query']>
type CreateBody = NonNullable<operations['createCoupon']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createCoupon']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listCouponsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listCouponsCount']['parameters']['query']>
type UpdateBody = NonNullable<operations['updateCoupon']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateCoupon']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteCoupon']['responses']['200']['content']['application/json']['data']>

export function createBillingCoupons(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/coupons/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/coupons/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/coupons/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    update: (couponId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/coupons/${encodePathParam(couponId)}`, { ...options, method: 'PATCH', body: data }),

    delete: (couponId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`billing/coupons/${encodePathParam(couponId)}`, { ...options, method: 'DELETE' }),
  }
}
