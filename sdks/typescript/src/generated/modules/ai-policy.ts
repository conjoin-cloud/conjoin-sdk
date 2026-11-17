import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CreateCheckBody = NonNullable<operations['createAiPolicyCheck']['requestBody']>['content']['application/json']
type CreateCheckData = NonNullable<operations['createAiPolicyCheck']['responses']['200']['content']['application/json']['data']>
type ListLogsData = NonNullable<operations['listAiPolicyLogs']['responses']['200']['content']['application/json']['data']>[number]
type ListLogsQuery = NonNullable<operations['listAiPolicyLogs']['parameters']['query']>
type ListLogsCountData = NonNullable<operations['listAiPolicyLogsCount']['responses']['200']['content']['application/json']['data']>
type ListLogsCountQuery = NonNullable<operations['listAiPolicyLogsCount']['parameters']['query']>
type ListRulesData = NonNullable<operations['listAiPolicyRules']['responses']['200']['content']['application/json']['data']>[number]
type ListRulesQuery = NonNullable<operations['listAiPolicyRules']['parameters']['query']>
type CreateRuleBody = NonNullable<operations['createAiPolicyRule']['requestBody']>['content']['application/json']
type CreateRuleData = NonNullable<operations['createAiPolicyRule']['responses']['201']['content']['application/json']['data']>
type ListRulesCountData = NonNullable<operations['listAiPolicyRulesCount']['responses']['200']['content']['application/json']['data']>
type ListRulesCountQuery = NonNullable<operations['listAiPolicyRulesCount']['parameters']['query']>
type ReadRuleData = NonNullable<operations['readAiPolicyRule']['responses']['200']['content']['application/json']['data']>
type UpdateRuleBody = NonNullable<operations['updateAiPolicyRule']['requestBody']>['content']['application/json']
type UpdateRuleData = NonNullable<operations['updateAiPolicyRule']['responses']['200']['content']['application/json']['data']>
type DeleteRuleData = NonNullable<operations['deleteAiPolicyRule']['responses']['200']['content']['application/json']['data']>

export function createAiPolicies(client: ConjoinClient) {
  return {
    createCheck: (data: CreateCheckBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateCheckData>('ai/policy-checks/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listLogs: (query?: ListLogsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListLogsData>('ai/policy-logs/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    listLogsCount: (query?: ListLogsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListLogsCountData>('ai/policy-logs/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    listRules: (query?: ListRulesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListRulesData>('ai/policy-rules/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    createRule: (data: CreateRuleBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateRuleData>('ai/policy-rules/', { ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    listRulesCount: (query?: ListRulesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListRulesCountData>('ai/policy-rules/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readRule: (policyRuleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadRuleData>(`ai/policy-rules/${encodePathParam(policyRuleId)}`, { ...options, method: 'GET' }),

    updateRule: (policyRuleId: string, data: UpdateRuleBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateRuleData>(`ai/policy-rules/${encodePathParam(policyRuleId)}`, { ...options, method: 'PATCH', body: data }),

    deleteRule: (policyRuleId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteRuleData>(`ai/policy-rules/${encodePathParam(policyRuleId)}`, { ...options, method: 'DELETE' }),
  }
}
