import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../frontend-api-types'

type ReadPublicProjectData = NonNullable<operations['readPublicProjectBranding']['responses']['200']['content']['application/json']['data']>
type ReadPublicProjectQuery = NonNullable<operations['readPublicProjectBranding']['parameters']['query']>

export function createCloudBrandings(client: ConjoinClient) {
  return {
    readPublicProject: (query?: ReadPublicProjectQuery, options?: ConjoinCallOptions) =>
      client.fetch<ReadPublicProjectData>('cloud/client/branding/', { auth: { type: 'none' }, ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
