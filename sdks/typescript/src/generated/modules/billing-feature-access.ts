import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CheckEntitlementBody = NonNullable<operations['checkBillingEntitlement']['requestBody']>['content']['application/json']
type CheckEntitlementData = NonNullable<operations['checkBillingEntitlement']['responses']['200']['content']['application/json']['data']>
type TrackFeatureUsageBody = NonNullable<operations['trackBillingFeatureUsage']['requestBody']>['content']['application/json']
type TrackFeatureUsageData = NonNullable<operations['trackBillingFeatureUsage']['responses']['200']['content']['application/json']['data']>

export function createBillingFeatureAccesses(client: ConjoinClient) {
  return {
    checkEntitlement: (data: CheckEntitlementBody, options?: ConjoinCallOptions) =>
      client.fetch<CheckEntitlementData>('billing/entitlements/check', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    trackFeatureUsage: (data: TrackFeatureUsageBody, options?: ConjoinCallOptions) =>
      client.fetch<TrackFeatureUsageData>('billing/entitlements/track', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),
  }
}
