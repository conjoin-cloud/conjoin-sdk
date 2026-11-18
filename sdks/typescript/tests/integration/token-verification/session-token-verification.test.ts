import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { verifyToken } from '../../../src/server/tokens'
import {
  AUTH_CLIENT_ISSUER_PATH,
  CARDIOLOGY_ORGANIZATION_ID,
  PATIENT_ACCOUNT_ID,
  PATIENT_PORTAL_APP_ID,
  PATIENT_SESSION_ID,
  SESSION_TOKEN_AUDIENCE,
  type SigningKeyServer,
  startSigningKeyServer,
} from './signing-key-server'

describe('verifyToken against the keys that Conjoin Auth publishes under its issuer', () => {
  let signingKeys: SigningKeyServer
  let issuer: string

  beforeAll(async () => {
    signingKeys = await startSigningKeyServer()
    issuer = `http://${signingKeys.authDomain}${AUTH_CLIENT_ISSUER_PATH}`
  })

  afterAll(async () => {
    await signingKeys.stop()
  })

  it('reads the account, session, and active organisation from a session token', async () => {
    const sessionToken = await signingKeys.signToken({
      claims: {
        session_id: PATIENT_SESSION_ID,
        app_id: PATIENT_PORTAL_APP_ID,
        live_mode: false,
        organization_id: CARDIOLOGY_ORGANIZATION_ID,
        organization_roles: ['org:viewer', 'org:manager'],
      },
      audience: SESSION_TOKEN_AUDIENCE,
      issuer,
    })

    const verified = await verifyToken(sessionToken, { jwksUrl: signingKeys.jwksUrl, issuer })

    expect(verified).toMatchObject({
      accountId: PATIENT_ACCOUNT_ID,
      sessionId: PATIENT_SESSION_ID,
      organizationId: CARDIOLOGY_ORGANIZATION_ID,
      organizationRoles: ['org:viewer', 'org:manager'],
    })
  })

  it('refuses an OpenID Connect ID token that the same app signed for its client', async () => {
    const idToken = await signingKeys.signToken({
      claims: { sid: PATIENT_SESSION_ID },
      audience: PATIENT_PORTAL_APP_ID,
      issuer,
    })

    await expect(verifyToken(idToken, { jwksUrl: signingKeys.jwksUrl, issuer })).rejects.toThrow()
  })
})
