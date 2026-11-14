import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListCredentialsData = NonNullable<operations['listCredentials']['responses']['200']['content']['application/json']['data']>[number]
type ListCredentialsQuery = NonNullable<operations['listCredentials']['parameters']['query']>
type VerifyCredentialBody = NonNullable<operations['verifyCredential']['requestBody']>['content']['application/json']
type VerifyCredentialData = NonNullable<operations['verifyCredential']['responses']['200']['content']['application/json']['data']>
type VerifyCredentialMfaTotpBody = NonNullable<operations['verifyCredentialMfaTotp']['requestBody']>['content']['application/json']
type VerifyCredentialMfaTotpData = NonNullable<operations['verifyCredentialMfaTotp']['responses']['200']['content']['application/json']['data']>
type ListCredentialsCountData = NonNullable<operations['listCredentialsCount']['responses']['200']['content']['application/json']['data']>
type ListCredentialsCountQuery = NonNullable<operations['listCredentialsCount']['parameters']['query']>
type ReadCredentialData = NonNullable<operations['readCredential']['responses']['200']['content']['application/json']['data']>
type RemoveCredentialData = NonNullable<operations['removeCredential']['responses']['200']['content']['application/json']['data']>
type ListData = NonNullable<operations['listAuthAccounts']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listAuthAccounts']['parameters']['query']>
type CreateBody = NonNullable<operations['createAuthAccount']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createAuthAccount']['responses']['201']['content']['application/json']['data']>
type ListOrganizationMembershipsData = NonNullable<operations['listAccountOrganizationMemberships']['responses']['200']['content']['application/json']['data']>[number]
type ListOrganizationMembershipsQuery = NonNullable<operations['listAccountOrganizationMemberships']['parameters']['query']>
type ListCountData = NonNullable<operations['listAuthAccountsCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listAuthAccountsCount']['parameters']['query']>
type MergeBody = NonNullable<operations['mergeAuthAccounts']['requestBody']>['content']['application/json']
type MergeData = NonNullable<operations['mergeAuthAccounts']['responses']['200']['content']['application/json']['data']>
type ReadData = NonNullable<operations['readAuthAccount']['responses']['200']['content']['application/json']['data']>
type UpdateBody = NonNullable<operations['updateAuthAccount']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateAuthAccount']['responses']['200']['content']['application/json']['data']>
type DeleteData = NonNullable<operations['deleteAuthAccount']['responses']['200']['content']['application/json']['data']>
type AddEmailBody = NonNullable<operations['addAuthAccountEmail']['requestBody']>['content']['application/json']
type AddEmailData = NonNullable<operations['addAuthAccountEmail']['responses']['200']['content']['application/json']['data']>
type RemoveEmailBody = NonNullable<operations['removeAuthAccountEmail']['requestBody']>['content']['application/json']
type RemoveEmailData = NonNullable<operations['removeAuthAccountEmail']['responses']['200']['content']['application/json']['data']>
type AddPhoneBody = NonNullable<operations['addAuthAccountPhone']['requestBody']>['content']['application/json']
type AddPhoneData = NonNullable<operations['addAuthAccountPhone']['responses']['200']['content']['application/json']['data']>
type RemovePhoneBody = NonNullable<operations['removeAuthAccountPhone']['requestBody']>['content']['application/json']
type RemovePhoneData = NonNullable<operations['removeAuthAccountPhone']['responses']['200']['content']['application/json']['data']>
type GrantGlobalRoleBody = NonNullable<operations['grantGlobalRole']['requestBody']>['content']['application/json']
type GrantGlobalRoleData = NonNullable<operations['grantGlobalRole']['responses']['200']['content']['application/json']['data']>
type RevokeGlobalRoleBody = NonNullable<operations['revokeGlobalRole']['requestBody']>['content']['application/json']
type RevokeGlobalRoleData = NonNullable<operations['revokeGlobalRole']['responses']['200']['content']['application/json']['data']>
type ListOrganizationMembershipsCountData = NonNullable<operations['listAccountOrganizationMembershipsCount']['responses']['200']['content']['application/json']['data']>
type ListOrganizationMembershipsCountQuery = NonNullable<operations['listAccountOrganizationMembershipsCount']['parameters']['query']>
type ExportData = NonNullable<operations['exportAuthAccount']['responses']['200']['content']['application/json']['data']>
type ImportPasswordHashesBody = NonNullable<operations['importPasswordHashes']['requestBody']>['content']['application/json']
type ImportPasswordHashesData = NonNullable<operations['importPasswordHashes']['responses']['200']['content']['application/json']['data']>

export function createAuthAccounts(client: ConjoinClient) {
  return {
    listCredentials: (accountId: string, query?: ListCredentialsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListCredentialsData>(`auth/accounts/${encodePathParam(accountId)}/credentials`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    verifyCredential: (accountId: string, data: VerifyCredentialBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifyCredentialData>(`auth/accounts/${encodePathParam(accountId)}/credentials/verify`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    verifyCredentialMfaTotp: (accountId: string, data: VerifyCredentialMfaTotpBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifyCredentialMfaTotpData>(`auth/accounts/${encodePathParam(accountId)}/totp-credentials/verify`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listCredentialsCount: (accountId: string, query?: ListCredentialsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCredentialsCountData>(`auth/accounts/${encodePathParam(accountId)}/credentials/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    readCredential: (accountId: string, credentialId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadCredentialData>(`auth/accounts/${encodePathParam(accountId)}/credentials/${encodePathParam(credentialId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    removeCredential: (accountId: string, credentialId: string, options?: ConjoinCallOptions) =>
      client.fetch<RemoveCredentialData>(`auth/accounts/${encodePathParam(accountId)}/credentials/${encodePathParam(credentialId)}/remove`, { ...options, method: 'POST', scopes: ['authAppId'] }),

    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('auth/accounts/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('auth/accounts/', { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listOrganizationMemberships: (accountId: string, query?: ListOrganizationMembershipsQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListOrganizationMembershipsData>(`auth/accounts/${encodePathParam(accountId)}/organizations`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('auth/accounts/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    merge: (data: MergeBody, options?: ConjoinCallOptions) =>
      client.fetch<MergeData>('auth/accounts/merge', { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    read: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadData>(`auth/accounts/${encodePathParam(accountId)}`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    update: (accountId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`auth/accounts/${encodePathParam(accountId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    delete: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<DeleteData>(`auth/accounts/${encodePathParam(accountId)}`, { ...options, method: 'DELETE', scopes: ['authAppId'] }),

    addEmail: (accountId: string, data: AddEmailBody, options?: ConjoinCallOptions) =>
      client.fetch<AddEmailData>(`auth/accounts/${encodePathParam(accountId)}/emails/add`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    removeEmail: (accountId: string, data: RemoveEmailBody, options?: ConjoinCallOptions) =>
      client.fetch<RemoveEmailData>(`auth/accounts/${encodePathParam(accountId)}/emails/remove`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    addPhone: (accountId: string, data: AddPhoneBody, options?: ConjoinCallOptions) =>
      client.fetch<AddPhoneData>(`auth/accounts/${encodePathParam(accountId)}/phones/add`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    removePhone: (accountId: string, data: RemovePhoneBody, options?: ConjoinCallOptions) =>
      client.fetch<RemovePhoneData>(`auth/accounts/${encodePathParam(accountId)}/phones/remove`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    grantGlobalRole: (accountId: string, data: GrantGlobalRoleBody, options?: ConjoinCallOptions) =>
      client.fetch<GrantGlobalRoleData>(`auth/accounts/${encodePathParam(accountId)}/global-roles/grant`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    revokeGlobalRole: (accountId: string, data: RevokeGlobalRoleBody, options?: ConjoinCallOptions) =>
      client.fetch<RevokeGlobalRoleData>(`auth/accounts/${encodePathParam(accountId)}/global-roles/revoke`, { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),

    listOrganizationMembershipsCount: (accountId: string, query?: ListOrganizationMembershipsCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListOrganizationMembershipsCountData>(`auth/accounts/${encodePathParam(accountId)}/organizations/count`, { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['authAppId'] }),

    export: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<ExportData>(`auth/accounts/${encodePathParam(accountId)}/export`, { ...options, method: 'POST', scopes: ['authAppId'] }),

    importPasswordHashes: (data: ImportPasswordHashesBody, options?: ConjoinCallOptions) =>
      client.fetch<ImportPasswordHashesData>('auth/accounts/import-password-hashes', { ...options, method: 'POST', body: data, scopes: ['authAppId'] }),
  }
}
