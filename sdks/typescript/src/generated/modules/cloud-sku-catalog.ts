import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ReadSkuCatalogData = NonNullable<operations['readSkuCatalog']['responses']['200']['content']['application/json']['data']>[number]
type ReadSkuCatalogQuery = NonNullable<operations['readSkuCatalog']['parameters']['query']>
type ReadSkuCatalogCountData = NonNullable<operations['readSkuCatalogCount']['responses']['200']['content']['application/json']['data']>
type ReadSkuCatalogCountQuery = NonNullable<operations['readSkuCatalogCount']['parameters']['query']>
type ReadSingleSkuCatalogData = NonNullable<operations['readSingleSkuCatalog']['responses']['200']['content']['application/json']['data']>

export function createCloudSKUCatalogs(client: ConjoinClient) {
  return {
    readSkuCatalog: (query?: ReadSkuCatalogQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ReadSkuCatalogData>('cloud/skus/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readSkuCatalogCount: (query?: ReadSkuCatalogCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadSkuCatalogCountData>('cloud/skus/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readSingleSkuCatalog: (skuId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadSingleSkuCatalogData>(`cloud/skus/${encodePathParam(skuId)}`, { ...options, method: 'GET' }),
  }
}
