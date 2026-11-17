import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type UpdateApiKeyBody = NonNullable<operations['updateApiKeyCredential']['requestBody']>['content']['application/json']
type UpdateApiKeyData = NonNullable<operations['updateApiKeyCredential']['responses']['200']['content']['application/json']['data']>
type CreatePasswordBody = NonNullable<operations['createPasswordCredential']['requestBody']>['content']['application/json']
type CreatePasswordData = NonNullable<operations['createPasswordCredential']['responses']['201']['content']['application/json']['data']>
type RotatePasswordBody = NonNullable<operations['rotatePasswordCredential']['requestBody']>['content']['application/json']
type RotatePasswordData = NonNullable<operations['rotatePasswordCredential']['responses']['200']['content']['application/json']['data']>
type EnrollTotpBody = NonNullable<operations['enrollTotpCredential']['requestBody']>['content']['application/json']
type EnrollTotpData = NonNullable<operations['enrollTotpCredential']['responses']['201']['content']['application/json']['data']>
type ActivateTotpBody = NonNullable<operations['activateTotpCredential']['requestBody']>['content']['application/json']
type ActivateTotpData = NonNullable<operations['activateTotpCredential']['responses']['200']['content']['application/json']['data']>
type RotateTotpRecoveryCodesBody = NonNullable<operations['rotateTotpRecoveryCodes']['requestBody']>['content']['application/json']
type RotateTotpRecoveryCodesData = NonNullable<operations['rotateTotpRecoveryCodes']['responses']['200']['content']['application/json']['data']>
type ConsumeTotpRecoveryCodeBody = NonNullable<operations['consumeTotpRecoveryCode']['requestBody']>['content']['application/json']
type ConsumeTotpRecoveryCodeData = NonNullable<operations['consumeTotpRecoveryCode']['responses']['200']['content']['application/json']['data']>
type EnrollSmsMfaBody = NonNullable<operations['enrollSmsMfaCredential']['requestBody']>['content']['application/json']
type EnrollSmsMfaData = NonNullable<operations['enrollSmsMfaCredential']['responses']['201']['content']['application/json']['data']>
type SendSmsMfaActivationCodeData = NonNullable<operations['sendSmsMfaActivationCode']['responses']['200']['content']['application/json']['data']>
type ActivateSmsMfaBody = NonNullable<operations['activateSmsMfaCredential']['requestBody']>['content']['application/json']
type ActivateSmsMfaData = NonNullable<operations['activateSmsMfaCredential']['responses']['200']['content']['application/json']['data']>
type VerifySmsMfaBody = NonNullable<operations['verifySmsMfaCredential']['requestBody']>['content']['application/json']
type VerifySmsMfaData = NonNullable<operations['verifySmsMfaCredential']['responses']['200']['content']['application/json']['data']>
type SendSmsMfaChallengeData = NonNullable<operations['sendSmsMfaChallenge']['responses']['200']['content']['application/json']['data']>
type ReadApiKeyUsageData = NonNullable<operations['readApiKeyUsage']['responses']['200']['content']['application/json']['data']>
type IssueApiKeyBody = NonNullable<operations['issueApiKeyCredential']['requestBody']>['content']['application/json']
type IssueApiKeyData = NonNullable<operations['issueApiKeyCredential']['responses']['201']['content']['application/json']['data']>
type RotateApiKeyBody = NonNullable<operations['rotateApiKeyCredential']['requestBody']>['content']['application/json']
type RotateApiKeyData = NonNullable<operations['rotateApiKeyCredential']['responses']['200']['content']['application/json']['data']>
type RevokeApiKeyBody = NonNullable<operations['revokeApiKeyCredential']['requestBody']>['content']['application/json']
type RevokeApiKeyData = NonNullable<operations['revokeApiKeyCredential']['responses']['200']['content']['application/json']['data']>
type StartPasskeyRegistrationBody = NonNullable<operations['startPasskeyRegistration']['requestBody']>['content']['application/json']
type StartPasskeyRegistrationData = NonNullable<operations['startPasskeyRegistration']['responses']['200']['content']['application/json']['data']>
type VerifyPasskeyRegistrationBody = NonNullable<operations['verifyPasskeyRegistration']['requestBody']>['content']['application/json']
type VerifyPasskeyRegistrationData = NonNullable<operations['verifyPasskeyRegistration']['responses']['201']['content']['application/json']['data']>
type StartPasskeyenticationData = NonNullable<operations['startPasskeyAuthentication']['responses']['200']['content']['application/json']['data']>
type VerifyPasskeyenticationBody = NonNullable<operations['verifyPasskeyAuthentication']['requestBody']>['content']['application/json']
type VerifyPasskeyenticationData = NonNullable<operations['verifyPasskeyAuthentication']['responses']['200']['content']['application/json']['data']>

export function createAuthCredentials(client: ConjoinClient) {
  return {
    updateApiKey: (accountId: string, credentialId: string, data: UpdateApiKeyBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateApiKeyData>(`auth/accounts/${encodePathParam(accountId)}/credentials/${encodePathParam(credentialId)}`, { ...options, method: 'PATCH', body: data, scopes: ['authAppId'] }),

    createPassword: (accountId: string, data: CreatePasswordBody, options?: ConjoinCallOptions) =>
      client.fetch<CreatePasswordData>(`auth/accounts/${encodePathParam(accountId)}/password-credentials`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    rotatePassword: (accountId: string, data: RotatePasswordBody, options?: ConjoinCallOptions) =>
      client.fetch<RotatePasswordData>(`auth/accounts/${encodePathParam(accountId)}/password-credentials/rotate`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    enrollTotp: (accountId: string, data: EnrollTotpBody, options?: ConjoinCallOptions) =>
      client.fetch<EnrollTotpData>(`auth/accounts/${encodePathParam(accountId)}/totp-credentials/enroll`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    activateTotp: (accountId: string, data: ActivateTotpBody, options?: ConjoinCallOptions) =>
      client.fetch<ActivateTotpData>(`auth/accounts/${encodePathParam(accountId)}/totp-credentials/activate`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    rotateTotpRecoveryCodes: (accountId: string, data: RotateTotpRecoveryCodesBody, options?: ConjoinCallOptions) =>
      client.fetch<RotateTotpRecoveryCodesData>(`auth/accounts/${encodePathParam(accountId)}/totp-recovery-codes/rotate`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    consumeTotpRecoveryCode: (accountId: string, data: ConsumeTotpRecoveryCodeBody, options?: ConjoinCallOptions) =>
      client.fetch<ConsumeTotpRecoveryCodeData>(`auth/accounts/${encodePathParam(accountId)}/totp-recovery-codes/consume`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    enrollSmsMfa: (accountId: string, data: EnrollSmsMfaBody, options?: ConjoinCallOptions) =>
      client.fetch<EnrollSmsMfaData>(`auth/accounts/${encodePathParam(accountId)}/sms-credentials/enroll`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    sendSmsMfaActivationCode: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<SendSmsMfaActivationCodeData>(`auth/accounts/${encodePathParam(accountId)}/sms-credentials/send-activation-code`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    activateSmsMfa: (accountId: string, data: ActivateSmsMfaBody, options?: ConjoinCallOptions) =>
      client.fetch<ActivateSmsMfaData>(`auth/accounts/${encodePathParam(accountId)}/sms-credentials/activate`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    verifySmsMfa: (accountId: string, data: VerifySmsMfaBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifySmsMfaData>(`auth/accounts/${encodePathParam(accountId)}/sms-credentials/verify`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    sendSmsMfaChallenge: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<SendSmsMfaChallengeData>(`auth/accounts/${encodePathParam(accountId)}/sms-credentials/send-challenge`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    readApiKeyUsage: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<ReadApiKeyUsageData>(`auth/accounts/${encodePathParam(accountId)}/api-key-credentials/usage-stats`, { ...options, method: 'GET', scopes: ['authAppId'] }),

    issueApiKey: (accountId: string, data: IssueApiKeyBody, options?: ConjoinCallOptions) =>
      client.fetch<IssueApiKeyData>(`auth/accounts/${encodePathParam(accountId)}/api-key-credentials`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    rotateApiKey: (accountId: string, credentialId: string, data: RotateApiKeyBody, options?: ConjoinCallOptions) =>
      client.fetch<RotateApiKeyData>(`auth/accounts/${encodePathParam(accountId)}/credentials/${encodePathParam(credentialId)}/rotate`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    revokeApiKey: (accountId: string, credentialId: string, data: RevokeApiKeyBody, options?: ConjoinCallOptions) =>
      client.fetch<RevokeApiKeyData>(`auth/accounts/${encodePathParam(accountId)}/credentials/${encodePathParam(credentialId)}/revoke`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    startPasskeyRegistration: (accountId: string, data: StartPasskeyRegistrationBody, options?: ConjoinCallOptions) =>
      client.fetch<StartPasskeyRegistrationData>(`auth/accounts/${encodePathParam(accountId)}/passkey-registrations/start`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    verifyPasskeyRegistration: (accountId: string, data: VerifyPasskeyRegistrationBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifyPasskeyRegistrationData>(`auth/accounts/${encodePathParam(accountId)}/passkey-registrations/verify`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    startPasskeyentication: (accountId: string, options?: ConjoinCallOptions) =>
      client.fetch<StartPasskeyenticationData>(`auth/accounts/${encodePathParam(accountId)}/passkey-authentications/start`, { ...options, method: 'POST', scopes: ['authAppId'], acceptsIdempotencyKey: true }),

    verifyPasskeyentication: (accountId: string, data: VerifyPasskeyenticationBody, options?: ConjoinCallOptions) =>
      client.fetch<VerifyPasskeyenticationData>(`auth/accounts/${encodePathParam(accountId)}/passkey-authentications/verify`, { ...options, method: 'POST', body: data, scopes: ['authAppId'], acceptsIdempotencyKey: true }),
  }
}
