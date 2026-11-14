import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listAuthOrganizationDomains']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAuthOrganizationDomains']['parameters']['query']>
type CreateBody = NonNullable<operations['createAuthOrganizationDomain']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createAuthOrganizationDomain']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listAuthOrganizationDomainsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listAuthOrganizationDomainsCount']['parameters']['query']>
type VerifyData = NonNullable<operations['verifyAuthOrganizationDomain']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteAuthOrganizationDomain']['responses']['200']['content']['application/json']['data']>

export function createAuthOrganizationDomains(client: ConjoinClient) {
  return {
    list: (organizationId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`auth/organizations/${encodePathParam(organizationId)}/domains/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    create: (organizationId: string, data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>(`auth/organizations/${encodePathParam(organizationId)}/domains/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listCount: (organizationId: string, query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>(`auth/organizations/${encodePathParam(organizationId)}/domains/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    verify: (organizationId: string, domainId: string, options?: ConjoinCallOptions) =>
      client.fetch<VerifyData>(`auth/organizations/${encodePathParam(organizationId)}/domains/${encodePathParam(domainId)}/verify`, { ...options, method: 'POST', scopes: ['authAppId'] }),

    delete: (organizationId: string, domainId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`auth/organizations/${encodePathParam(organizationId)}/domains/${encodePathParam(domainId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),
  }
}
