import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listTaxJurisdictions']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listTaxJurisdictions']['parameters']['query']>
type ListCountData = NonNullable<operations['listTaxJurisdictionsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listTaxJurisdictionsCount']['parameters']['query']>
type QueryTaxRateData = NonNullable<operations['queryTaxRate']['responses']['200']['content']['application/json']['data']>
type QueryTaxRateQuery = NonNullable<operations['queryTaxRate']['parameters']['query']>

export function createBillingTaxJurisdictions(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/tax-jurisdictions/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/tax-jurisdictions/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    queryTaxRate: (query: QueryTaxRateQuery, options?: ConjoinCallOptions) =>
      client.fetch<QueryTaxRateData>('billing/tax-jurisdictions/effective-rates', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
