import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type CheckBody = NonNullable<operations['checkAiPolicy']['requestBody']>['content']['application/json']
type CheckData = NonNullable<operations['checkAiPolicy']['responses']['200']['content']['application/json']['data']>
type CreateRuleBody = NonNullable<operations['createAiPolicyRule']['requestBody']>['content']['application/json']
type CreateRuleData = NonNullable<operations['createAiPolicyRule']['responses']['201']['content']['application/json']['data']>
type ListRulesData = NonNullable<operations['listAiPolicyRules']['responses']['200']['content']['application/json']['data']>[number]
type ListRulesQuery = NonNullable<operations['listAiPolicyRules']['parameters']['query']>
type ReadRuleData = NonNullable<operations['readAiPolicyRule']['responses']['200']['content']['application/json']['data']>
type UpdateRuleBody = NonNullable<operations['updateAiPolicyRule']['requestBody']>['content']['application/json']
type UpdateRuleData = NonNullable<operations['updateAiPolicyRule']['responses']['200']['content']['application/json']['data']>
type DeleteRuleData = NonNullable<operations['deleteAiPolicyRule']['responses']['200']['content']['application/json']['data']>
type ListLogsData = NonNullable<operations['listAiPolicyLogs']['responses']['200']['content']['application/json']['data']>[number]
type ListLogsQuery = NonNullable<operations['listAiPolicyLogs']['parameters']['query']>

export function createAiPolicies(client: ConjoinClient) {
  return {
    check: (data: CheckBody, options?: ConjoinCallOptions) =>
      client.fetch<CheckData>('ai/policy/check', { ...options, method: 'POST', body: data }),

    createRule: (data: CreateRuleBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateRuleData>('ai/policy/rules', { ...options, method: 'POST', body: data }),

    listRules: (query?: ListRulesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListRulesData>('ai/policy/rules', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),

    readRule: (ruleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadRuleData>(`ai/policy/rules/${encodePathParam(ruleId)}`, { ...options, method: 'GET' }),

    updateRule: (ruleId: string, data: UpdateRuleBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateRuleData>(`ai/policy/rules/${encodePathParam(ruleId)}`, { ...options, method: 'PATCH', body: data }),

    deleteRule: (ruleId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteRuleData>(`ai/policy/rules/${encodePathParam(ruleId)}`, { ...options, method: 'DELETE' }),

    listLogs: (query?: ListLogsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListLogsData>('ai/policy/logs', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined }),
  }
}
