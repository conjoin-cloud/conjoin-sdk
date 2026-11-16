import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListRulesData = NonNullable<operations['listGuardRules']['responses']['200']['content']['application/json']['data']>[number]
type ListRulesQuery = NonNullable<operations['listGuardRules']['parameters']['query']>
type CreateRuleBody = NonNullable<operations['createGuardRule']['requestBody']>['content']['application/json']
type CreateRuleData = NonNullable<operations['createGuardRule']['responses']['201']['content']['application/json']['data']>
type ListRulesCountData = NonNullable<operations['listGuardRulesCount']['responses']['200']['content']['application/json']['data']>
type ListRulesCountQuery = NonNullable<operations['listGuardRulesCount']['parameters']['query']>
type ReadRuleData = NonNullable<operations['readGuardRule']['responses']['200']['content']['application/json']['data']>
type UpdateRuleBody = NonNullable<operations['updateGuardRule']['requestBody']>['content']['application/json']
type UpdateRuleData = NonNullable<operations['updateGuardRule']['responses']['200']['content']['application/json']['data']>
type DeleteRuleData = NonNullable<operations['deleteGuardRule']['responses']['200']['content']['application/json']['data']>
type ListEventsData = NonNullable<operations['listGuardEvents']['responses']['200']['content']['application/json']['data']>[number]
type ListEventsQuery = NonNullable<operations['listGuardEvents']['parameters']['query']>
type ListEventsCountData = NonNullable<operations['listGuardEventsCount']['responses']['200']['content']['application/json']['data']>
type ListEventsCountQuery = NonNullable<operations['listGuardEventsCount']['parameters']['query']>
type AddTrustedIpBody = NonNullable<operations['addGuardTrustedIp']['requestBody']>['content']['application/json']
type AddTrustedIpData = NonNullable<operations['addGuardTrustedIp']['responses']['200']['content']['application/json']['data']>
type RemoveTrustedIpBody = NonNullable<operations['removeGuardTrustedIp']['requestBody']>['content']['application/json']
type RemoveTrustedIpData = NonNullable<operations['removeGuardTrustedIp']['responses']['200']['content']['application/json']['data']>
type AddTrustedEmailBody = NonNullable<operations['addGuardTrustedEmail']['requestBody']>['content']['application/json']
type AddTrustedEmailData = NonNullable<operations['addGuardTrustedEmail']['responses']['200']['content']['application/json']['data']>
type RemoveTrustedEmailBody = NonNullable<operations['removeGuardTrustedEmail']['requestBody']>['content']['application/json']
type RemoveTrustedEmailData = NonNullable<operations['removeGuardTrustedEmail']['responses']['200']['content']['application/json']['data']>
type AddTrustedDomainBody = NonNullable<operations['addGuardTrustedDomain']['requestBody']>['content']['application/json']
type AddTrustedDomainData = NonNullable<operations['addGuardTrustedDomain']['responses']['200']['content']['application/json']['data']>
type RemoveTrustedDomainBody = NonNullable<operations['removeGuardTrustedDomain']['requestBody']>['content']['application/json']
type RemoveTrustedDomainData = NonNullable<operations['removeGuardTrustedDomain']['responses']['200']['content']['application/json']['data']>
type ListAnonymousIpsData = NonNullable<operations['listGuardAnonymousIps']['responses']['200']['content']['application/json']['data']>
type AddAnonymousIpsBody = NonNullable<operations['addGuardAnonymousIps']['requestBody']>['content']['application/json']
type AddAnonymousIpsData = NonNullable<operations['addGuardAnonymousIps']['responses']['200']['content']['application/json']['data']>
type RemoveAnonymousIpsBody = NonNullable<operations['removeGuardAnonymousIps']['requestBody']>['content']['application/json']
type RemoveAnonymousIpsData = NonNullable<operations['removeGuardAnonymousIps']['responses']['200']['content']['application/json']['data']>

export function createAuthGuards(client: ConjoinClient) {
  return {
    listRules: (query?: ListRulesQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListRulesData>('auth/guard-rules', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    createRule: (data: CreateRuleBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateRuleData>('auth/guard-rules', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    listRulesCount: (query?: ListRulesCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListRulesCountData>('auth/guard-rules/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    readRule: (guardRuleId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadRuleData>(`auth/guard-rules/${encodePathParam(guardRuleId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    updateRule: (guardRuleId: string, data: UpdateRuleBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateRuleData>(`auth/guard-rules/${encodePathParam(guardRuleId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    deleteRule: (guardRuleId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteRuleData>(`auth/guard-rules/${encodePathParam(guardRuleId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    listEvents: (query?: ListEventsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListEventsData>('auth/guard-events', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listEventsCount: (query?: ListEventsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListEventsCountData>('auth/guard-events/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    addTrustedIp: (data: AddTrustedIpBody, options?: ConjoinCallOptions) =>
      client.fetch<AddTrustedIpData>('auth/guard-trusted-ips', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    removeTrustedIp: (data: RemoveTrustedIpBody, options?: ConjoinCallOptions) =>
      client.fetch<RemoveTrustedIpData>('auth/guard-trusted-ips/remove', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    addTrustedEmail: (data: AddTrustedEmailBody, options?: ConjoinCallOptions) =>
      client.fetch<AddTrustedEmailData>('auth/guard-trusted-emails', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    removeTrustedEmail: (data: RemoveTrustedEmailBody, options?: ConjoinCallOptions) =>
      client.fetch<RemoveTrustedEmailData>('auth/guard-trusted-emails/remove', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    addTrustedDomain: (data: AddTrustedDomainBody, options?: ConjoinCallOptions) =>
      client.fetch<AddTrustedDomainData>('auth/guard-trusted-domains', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    removeTrustedDomain: (data: RemoveTrustedDomainBody, options?: ConjoinCallOptions) =>
      client.fetch<RemoveTrustedDomainData>('auth/guard-trusted-domains/remove', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    listAnonymousIps: (options?: ConjoinCallOptions) =>
      client.fetch<ListAnonymousIpsData>('auth/guard-anonymous-ips', { ...options, method: 'GET', scopes: ['authAppId'] }),

    addAnonymousIps: (data: AddAnonymousIpsBody, options?: ConjoinCallOptions) =>
      client.fetch<AddAnonymousIpsData>('auth/guard-anonymous-ips', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    removeAnonymousIps: (data: RemoveAnonymousIpsBody, options?: ConjoinCallOptions) =>
      client.fetch<RemoveAnonymousIpsData>('auth/guard-anonymous-ips/remove', { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
