import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listPolicies']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listPolicies']['parameters']['query']>
type CreateBody = NonNullable<operations['createPolicy']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createPolicy']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listPoliciesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listPoliciesCount']['parameters']['query']>
type ReadData = NonNullable<operations['readPolicy']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updatePolicy']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updatePolicy']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deletePolicy']['responses']['200']['content']['application/json']['data']>

export function createAuthPolicies(client: ConjoinClient) {
  return {
    list: (organizationId: string, query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>(`auth/organizations/${encodePathParam(organizationId)}/policies/`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    create: (organizationId: string, data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>(`auth/organizations/${encodePathParam(organizationId)}/policies/`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listCount: (organizationId: string, query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>(`auth/organizations/${encodePathParam(organizationId)}/policies/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    read: (organizationId: string, policyId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`auth/organizations/${encodePathParam(organizationId)}/policies/${encodePathParam(policyId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    update: (organizationId: string, policyId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`auth/organizations/${encodePathParam(organizationId)}/policies/${encodePathParam(policyId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    delete: (organizationId: string, policyId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`auth/organizations/${encodePathParam(organizationId)}/policies/${encodePathParam(policyId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),
  }
}
