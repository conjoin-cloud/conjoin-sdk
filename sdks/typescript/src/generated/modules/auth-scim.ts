import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient, RequestOptions } from '../../core/types'
import type { operations } from '../api-types'

type ScimBulkOperationsBody = NonNullable<operations['scimBulkOperations']['requestBody']>['content']['application/json']
type ScimBulkOperationsResponse = operations['scimBulkOperations']['responses']['200']['content']['application/json']
type ScimListGroupsResponse = operations['scimListGroups']['responses']['200']['content']['application/json']
type ScimCreateGroupBody = NonNullable<operations['scimCreateGroup']['requestBody']>['content']['application/json']
type ScimCreateGroupResponse = operations['scimCreateGroup']['responses']['201']['content']['application/json']
type ScimGetGroupResponse = operations['scimGetGroup']['responses']['200']['content']['application/json']
type ScimReplaceGroupBody = NonNullable<operations['scimReplaceGroup']['requestBody']>['content']['application/json']
type ScimReplaceGroupResponse = operations['scimReplaceGroup']['responses']['200']['content']['application/json']
type ScimPatchGroupMembersBody = NonNullable<operations['scimPatchGroupMembers']['requestBody']>['content']['application/json']
type ScimPatchGroupMembersResponse = operations['scimPatchGroupMembers']['responses']['200']['content']['application/json']
type ScimGetServiceProviderConfigResponse = operations['scimGetServiceProviderConfig']['responses']['200']['content']['application/json']
type ScimGetSchemasResponse = operations['scimGetSchemas']['responses']['200']['content']['application/json']
type ScimGetResourceTypesResponse = operations['scimGetResourceTypes']['responses']['200']['content']['application/json']
type ScimListUsersResponse = operations['scimListUsers']['responses']['200']['content']['application/json']
type ScimCreateUserBody = NonNullable<operations['scimCreateUser']['requestBody']>['content']['application/json']
type ScimCreateUserResponse = operations['scimCreateUser']['responses']['201']['content']['application/json']
type ScimGetUserResponse = operations['scimGetUser']['responses']['200']['content']['application/json']
type ScimReplaceUserBody = NonNullable<operations['scimReplaceUser']['requestBody']>['content']['application/json']
type ScimReplaceUserResponse = operations['scimReplaceUser']['responses']['200']['content']['application/json']
type ScimPatchUserResponse = operations['scimPatchUser']['responses']['200']['content']['application/json']

export type AuthSCIMOptions = {
  scimToken?: string
}

function scimBearerRequestOptions(scimToken: string | undefined): RequestOptions {
  if (!scimToken || scimToken.trim().length === 0) {
    throw new Error('SCIM token is required for tenant SCIM operations')
  }

  return { auth: { type: 'bearer', token: scimToken } }
}

export function createAuthSCIMs(client: ConjoinClient, scim: AuthSCIMOptions = {}) {
  return {
    scimBulkOperations: (projectId: string, appId: string, data: ScimBulkOperationsBody, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimBulkOperationsResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Bulk`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    scimListGroups: (projectId: string, appId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimListGroupsResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Groups`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'GET' }),

    scimCreateGroup: (projectId: string, appId: string, data: ScimCreateGroupBody, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimCreateGroupResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Groups`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    scimGetGroup: (projectId: string, appId: string, id: string, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimGetGroupResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Groups/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'GET' }),

    scimReplaceGroup: (projectId: string, appId: string, id: string, data: ScimReplaceGroupBody, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimReplaceGroupResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Groups/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'PUT', body: data }),

    scimPatchGroupMembers: (projectId: string, appId: string, id: string, data: ScimPatchGroupMembersBody, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimPatchGroupMembersResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Groups/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'PATCH', body: data }),

    scimDeleteGroup: (projectId: string, appId: string, id: string, options?: ConjoinCallOptions) =>
      client.fetchJson<undefined>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Groups/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'DELETE' }),

    scimGetServiceProviderConfig: (options?: ConjoinCallOptions) =>
      client.fetchJson<ScimGetServiceProviderConfigResponse>('auth/scim/v2/ServiceProviderConfig', { ...options, auth: { type: 'none' }, method: 'GET' }),

    scimGetSchemas: (options?: ConjoinCallOptions) =>
      client.fetchJson<ScimGetSchemasResponse>('auth/scim/v2/Schemas', { ...options, auth: { type: 'none' }, method: 'GET' }),

    scimGetResourceTypes: (options?: ConjoinCallOptions) =>
      client.fetchJson<ScimGetResourceTypesResponse>('auth/scim/v2/ResourceTypes', { ...options, auth: { type: 'none' }, method: 'GET' }),

    scimListUsers: (projectId: string, appId: string, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimListUsersResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Users`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'GET' }),

    scimCreateUser: (projectId: string, appId: string, data: ScimCreateUserBody, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimCreateUserResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Users`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'POST', body: data, acceptsIdempotencyKey: true }),

    scimGetUser: (projectId: string, appId: string, id: string, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimGetUserResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Users/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'GET' }),

    scimReplaceUser: (projectId: string, appId: string, id: string, data: ScimReplaceUserBody, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimReplaceUserResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Users/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'PUT', body: data }),

    scimPatchUser: (projectId: string, appId: string, id: string, options?: ConjoinCallOptions) =>
      client.fetchJson<ScimPatchUserResponse>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Users/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'PATCH' }),

    scimDeactivateUser: (projectId: string, appId: string, id: string, options?: ConjoinCallOptions) =>
      client.fetchJson<undefined>(`auth/scim/v2/${encodePathParam(projectId)}/${encodePathParam(appId)}/Users/${encodePathParam(id)}`, { ...scimBearerRequestOptions(scim.scimToken), ...options, method: 'DELETE' }),
  }
}
